"""Converts EMu field and tab definitions from spreadsheet to reST for sphinx"""
import glob
import os
import re
import textwrap

import pandas as pd

from xmu import EMuSchema


def rewrap_rst(path):
    """Rewraps an reST document

    # FIXME: Use pandoc for this?
    """
    reformatted = []
    is_block = False
    with open(path, encoding="utf-8") as f:
        units = [[]]
        for line in f:
            line = line.rstrip()
            if not line.strip():
                units.append([])
            elif is_list_item(line):
                units.append([line])
            else:
                units[-1].append(line)
        for unit in units:
            if unit:
                # Tables
                if re.match(r"[+|].*?[+|]$", unit[0]):
                    unit = wrap_table("\n".join(unit)) + "\n"
                    unit = unit.replace(" ", "<NBSP>")
                # Headers
                elif not unit[-1].strip("#*=-^"):
                    unit = "\n".join(unit) + "\n"
                # Labels
                elif unit[0].startswith(".. _"):
                    unit = "\n".join(unit) + "\n"
                    is_block = False
                # Code blocks
                elif unit[0].startswith(".. "):
                    unit = "\n".join(unit) + "\n"
                    is_block = True
                # Indented blocks
                elif unit[0].startswith("  ") and (
                    is_block or not is_list_item(unit[0])
                ):
                    unit = "\n".join((wrap_text(s).rstrip() for s in unit))
                # List items
                elif is_list_item(unit[0]):
                    unit = wrap_list_item(" ".join(unit)).rstrip()
                    is_block = False
                # Everything else
                else:
                    unit = wrap_text(" ".join(unit))
                    is_block = False

                if (
                    reformatted
                    and not is_block
                    and not is_same_block(unit, reformatted[-1])
                ):
                    reformatted.append("")

                reformatted.append(clean_text(unit))

    reformatted = re.sub(r"\n{3,}", "\n\n", "\n".join(reformatted))
    with open(path, "w", encoding="utf-8") as f:
        f.write(reformatted)


def write_metadata(metadata, module):
    """Writes field matadata as a table"""

    schema_keys = [
        "ItemPrompt",
        "ColumnName",
        "DataKind",
        "DataType",
        "LookupName",
        "RefTable",
    ]

    cols = []
    for field in metadata["fields"]:
        field_info = SCHEMA.get_field_info(module, field)

        col = {}
        rows = []
        for key in schema_keys:
            try:
                col[key] = field_info[key]
            except KeyError:
                pass

        if col.get("RefTable"):
            col["DataType"] = "Reference"

        cols.append(col)

    keys = []
    for col in cols:
        keys.extend(col.keys())

    rows = []
    for key in [k for k in schema_keys if k in set(keys)]:
        row = [key]
        for col in cols:
            row.append(col.get(key, ""))
        rows.append(row)

    if len(cols) == 1:
        header = ["Field", "Value"]
    else:
        header = ["Field"] + [col["ColumnName"] for col in cols]

    return write_table(rows, header)


def write_table(rows, header):
    """Writes rows as a table"""

    def format_row(row, widths):
        return "|" + "|".join([c.ljust(w) for c, w in zip(row, widths)]) + "|"

    widths = {}
    for row in [header] + rows:
        for i, val in enumerate(row):
            widths.setdefault(i, []).append(len(val))
    widths = [max(w) for w in widths.values()]

    border = "+" + "+".join(["-" * w for w in widths]) + "+"
    header_border = "+" + "+".join(["=" * w for w in widths]) + "+"

    table = [border, format_row(header, widths), header_border]
    for row in rows:
        table.extend([format_row(row, widths), border])
    table.append("")

    return table


def h1(val):
    """Writes header level 1"""
    return ["#" * len(val), val, "#" * len(val), ""]


def h2(val):
    """Writes header level 2"""
    return ["*" * len(val), val, "*" * len(val), ""]


def h3(val):
    """Writes header level 3"""
    return [val, "=" * len(val), ""]


def h4(val):
    """Writes header level 4"""
    return [val, "-" * len(val), ""]


def img(src):
    """Writes image for reST"""
    try:
        stem, ext = os.path.splitext(src)
        open(f"img/{slug(stem) + ext}")
        return [f".. image:: ../img/{slug(stem) + ext}", ""]
    except FileNotFoundError:
        return []


def figure(src):
    """Writes figure for reST"""
    try:
        stem, ext = os.path.splitext(src)
        open(f"img/{slug(stem) + ext}")
        return [f".. figure:: ../../../img/{slug(stem) + ext}", "", "   Caption", ""]
    except FileNotFoundError:
        return []


def ol(vals):
    """Formats list as an ordered list"""
    return [wrap_list_item(val, marker="#.") for val in vals] + [""]


def ul(vals):
    """Formats list as an unordered list"""
    return [wrap_list_item(val, marker="*") for val in vals] + [""]


def label(*args):
    """Writes a reST label"""
    return [f".. _{'-'.join([slug(a).replace('_', '-') for a in args if a])}:", ""]


def fix_links(val, width):
    repl = {}
    for i, link in enumerate(re.findall("<http.*?>", val, flags=re.DOTALL)):
        clean = link.replace("   ", "")
        if len(clean) > width:
            placeholder = f"<{str(i).zfill(len(clean) - 2)}>"
            repl[placeholder] = clean
            val = val.replace(link, placeholder)
    return val, repl


def wrap_text(val, width=72):
    """Wraps text to keep text documents readable"""
    is_list = False
    lines = []
    indent = re.match(r" *", val).group()
    val, repl = fix_links(val, width)
    for line in val.splitlines():
        if is_list_item(line):
            lines.append(wrap_list_item(line, width))
            is_list = True
        else:
            if is_list:
                lines.append("")
                is_list = False
            lines.append(
                textwrap.fill(
                    line,
                    width,
                    initial_indent="",
                    subsequent_indent=indent,
                    break_long_words=False,
                )
            )
    val = "\n".join(lines)
    for placeholder, link in repl.items():
        val = val.replace(placeholder, link)
    return val + "\n"


def get_marker(val, default=None):
    """Gets the list marker from a value"""
    try:
        return re.match(r"(\*|#\.|\-|\+) ", val.lstrip()).group()
    except AttributeError:
        return default


def wrap_list_item(val, width=72, marker=None):
    """Wraps a list item to keep lists indented consistently"""
    if marker is None:
        marker = get_marker(val)
    marker = marker.rstrip() + " "
    indent = re.match(r" *", val).group()
    # Fix links
    val, repl = fix_links(val, width)
    # Normalize spaces
    val = re.sub(f"^ *{re.escape(marker)} *", "", val)
    # Enforce consistent marker on unordered lists
    if len(marker) == 2:
        marker = "* "
    val = textwrap.fill(
        val,
        width,
        initial_indent=indent + marker,
        subsequent_indent=indent + " " * len(marker),
        break_long_words=False,
    )
    for placeholder, link in repl.items():
        val = val.replace(placeholder, link)
    return val


def wrap_table(table, one_line_per_row=False, max_table_width=72, max_width="min"):
    """Wraps a table"""
    rows = []
    row = []
    for i, line in enumerate(table.splitlines()):
        if line.strip("|+-= "):
            delim = line[0]
            line = line[1:-1].strip()
            for i, cell in enumerate([s.strip() for s in line.split(delim)]):
                try:
                    row[i] += " " + cell
                except IndexError:
                    row.append(cell)
            if one_line_per_row:
                rows.append(row)
                row = []
        elif row and not one_line_per_row:
            rows.append(row)
            row = []
    if row:
        rows.append(row)

    cols = {}
    for i, row in enumerate(rows):
        for j, cell in enumerate(row):
            if max_width == "min":
                lines = textwrap.wrap(cell, 1, break_long_words=False)
                if lines:
                    width = max((len(s) for s in lines))
                    cols.setdefault(j, []).append(width)
            else:
                cols.setdefault(j, []).append(len(cell))

    widths = {k: max(v) + 2 for k, v in cols.items()}

    keys = list(widths)
    if max_width != "min":
        while sum(widths.values()) + 2 < max_table_width:
            widths[keys.pop()] += 1
            if not keys:
                keys = list(widths)

    sep = "+" + "+".join(["-" * w for w in widths.values()]) + "+"
    tab = [sep]
    for i, row in enumerate(rows):
        formatted = []
        for j, cell in enumerate(row):
            wrapped = textwrap.wrap(
                cell,
                widths[j] - 1,
                initial_indent=" ",
                subsequent_indent=" ",
                break_long_words=False,
            )
            formatted.append([f"{s.ljust(widths[j])}" for s in wrapped])
        lines = []
        while any(formatted):
            cells = [
                r.pop(0) if r else " " * widths[j] for j, r in enumerate(formatted)
            ]
            tab.append("|" + "|".join(cells) + "|")
        if i:
            tab.append(sep)
        else:
            tab.append(sep.replace("-", "="))

    return "\n".join(tab)


def is_list_item(val):
    """Checks if value is a list"""
    return bool(get_marker(val))


def is_same_block(val, other):
    """Tests if two blocks have the same marker and indentation"""
    return (
        get_marker(val) == get_marker(other)
        and re.match(r" *", val).group() == re.match(" *", other).group()
    )


def slug(val):
    """Formats a value suitable for a URL"""
    return re.sub(r"[^A-Za-z0-9]+", "_", val).lower().strip("_")


def clean_text(val):
    """Collapses internal whitespace in a value"""
    clean = []
    for line in val.splitlines():
        whitespace = re.match(" *", line).group()
        marker = get_marker(line, "")
        clean.append(
            whitespace
            + marker
            + re.sub(" +", " ", line[len(whitespace) + len(marker) :])
        )
    text = "\n".join(clean) + re.search("\s*$", val).group()
    return text.replace("<NBSP>", " ")


SCHEMA = EMuSchema()
FORMATS = {"Date": "yyyy-mm-dd", "Time": "hh:mm or hh:mm:ss"}
EXCEL_PATH = "nmnh_minsci_emu_definitions.xlsx"
FIELD_PATH = "nmnh_minsci_emu_field_definitions.csv"
TAB_PATH = "nmnh_minsci_emu_tab_definitions.csv"

if __name__ == "__main__":
    # Read definitions
    try:
        fields = pd.read_excel(EXCEL_PATH, "fields").fillna("")
        tabs = pd.read_excel(EXCEL_PATH, "tabs").fillna("")
    except FileNotFoundError:
        fields = pd.read_csv(FIELD_PATH).fillna("")
        tabs = pd.read_csv(TAB_PATH).fillna("")
        # Generate an Excel file from the CSVs
        with pd.ExcelWriter(EXCEL_PATH) as writer:
            fields.to_excel(writer, "fields", index=False)
            tabs.to_excel(writer, "tabs", index=False)
    else:
        # Update CSV files from Excel file
        fields.to_csv(FIELD_PATH, index=False)
        tabs.to_csv(TAB_PATH, index=False)

    # Map fields that do not specify a module
    modules = sorted({m for m in fields["module"].unique() if m})
    new_rows = []
    for _, row in fields[fields["module"] == ""].iterrows():
        for mod in modules:
            new_rows.append(row.copy())
            new_rows[-1]["module"] = mod
    fields = pd.concat([fields, pd.DataFrame(new_rows)])
    fields = fields[fields["module"] != ""]

    # Create tab lookup and map tabs that do not specify a module
    tabs = {(r["module"], r["tab"]): r["description"] for _, r in tabs.iterrows()}
    for key in list(tabs):
        if not key[0]:
            for module in modules:
                tabs[(module, key[1])] = tabs[key]
            del tabs[key]

    for (module, tab_name), tab in fields.groupby(["module", "tab"], sort=False):
        output = []

        # Add page header
        # output.extend(label(module, tab_name))
        output.extend(h1(f"{module} > {tab_name}"))

        # Add image of tab
        output.extend(figure(f"{module}_{tab_name}.png"))

        # Add the description from the tabs sheet
        output.append(wrap_text(tabs[(module, tab_name)]))

        for group, fields in tab.groupby("group", sort=False):
            for _, row in fields.iterrows():
                # Convert row to dict
                row = row.to_dict()

                # Split lists
                for key, val in row.items():
                    val = val.strip()
                    if isinstance(val, str) and val.startswith("- "):
                        row[key] = [s.lstrip("-").strip() for s in val.split("\n")]
                    else:
                        row[key] = val

                if not row["usage"]:
                    raise ValueError(f"{row['field']} is missing a required key")

                # Add a horizontal line to divide sections
                output.extend(["-" * 80, ""])

                # Add basic field info
                output.extend(label(module, tab_name, row["group"], row["field"]))
                output.extend(h2(row["field"]))

                # Add field metadata from the schema file
                output.extend(write_metadata(row, module))

                # Omit additional metadta if a field is not used
                if row["usage"] == "Not used":
                    output.extend(["Not used", ""])
                    continue

                # Add definition
                output.append(wrap_text(row.get("description", "")))

                # Provide usage conditions
                output.extend(h3("Usage"))
                output.append(wrap_text(row["usage"]))

                # Provide format
                fmt = row["format"]
                if not fmt:
                    dtypes = []
                    for field in row["fields"]:
                        field_info = SCHEMA.get_field_info(module, field)
                        dtypes.append(field_info["DataType"])
                    if len(set(dtypes)) == 1:
                        fmt = FORMATS.get(dtypes[0])
                if fmt:
                    output.extend(h3("Format"))
                    output.append(wrap_text(row["format"]))

                # Provide valid or example values
                for key in ["allowed values", "examples"]:
                    vals = row[key]
                    if vals:
                        output.extend(h3(key.title()) + ul(vals))

            # Remove trailing horizontal line to silence sphinx error
            # output = output[:-2]

        try:
            os.makedirs(f"docs/modules/{module}")
        except OSError:
            pass

        with open(
            f"docs/modules/{module}/{slug(tab_name)}.rst", "w", encoding="utf-8"
        ) as f:
            f.write("\n".join(output))

    # Write index file for each module folder
    for root, dirs, files in os.walk("docs/modules"):
        pages = []
        for fn in files:
            path = os.path.join(root, fn)
            if fn == "about.rst":
                with open(path, encoding="utf-8") as f:
                    title = f.read().splitlines()[1]
                    pages.insert(0, (title, fn))
            elif fn != "index.rst" and fn.endswith(".rst"):
                with open(path, encoding="utf-8") as f:
                    title = f.read().splitlines()[1].split(">")[-1].strip()
                    pages.append((title, fn))

        if pages:
            rewrap_rst(path)
            path = f"docs/modules/{os.path.basename(root)}/index.rst"
            content = h1(os.path.basename(root))
            content.extend([".. toctree::", "   :maxdepth: 2", ""])
            content.extend([f"   {t} <{p}>" for t, p in pages])
            with open(path, "w", encoding="utf-8") as f:
                f.write("\n".join(content))

    # Create guidelines landing page and clean up manually created reST files
    content = h1("Guidelines")
    content.extend([".. toctree::", "   :maxdepth: 2", ""])
    for root, dirs, files in os.walk("docs/guidelines"):
        for fn in files:
            path = os.path.join(root, fn)
            if path.endswith(".rst"):
                rewrap_rst(path)
            if root == "docs/guidelines":
                with open(path, encoding="utf-8") as f:
                    title = f.read().splitlines()[1]
                content.append(f"   {title} <guidelines/{fn}>")
    with open("docs/guidelines.rst", "w") as f:
        f.write("\n".join(content))

    # Create module landing pages
    content = h1("Modules")
    content.extend([".. toctree::", "   :maxdepth: 2", ""])
    for root, dirs, files in os.walk("docs/modules"):
        for fn in files:
            if fn == "index.rst":
                rewrap_rst(os.path.join(root, fn))
                module = os.path.basename(root)
                content.append(f"   {module} <modules/{module}/index.rst>")

    with open("docs/modules.rst", "w") as f:
        f.write("\n".join(content))

    # Create the index page
    content = h1("Mineral Sciences Data Guide")
    content.extend([".. toctree::", "   :maxdepth: 2", ""])
    for path in glob.iglob("docs/*.rst"):
        fn = os.path.basename(path)
        if fn != "index.rst":
            content.append(f"   {os.path.splitext(fn)[0].title()} <{fn}>")
    with open("docs/index.rst", "w") as f:
        f.write("\n".join(content))
