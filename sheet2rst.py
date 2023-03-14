"""Converts EMu field and tab definitions from spreadsheet to reST for sphinx"""
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


def wrap_text(text, width=72):
    """Wraps text to keep text documents readable"""
    is_list = False
    lines = []
    indent = re.match(r" *", text).group()
    for line in text.splitlines():
        if is_list_item(line):
            lines.append(wrap_list_item(line, width))
            is_list = True
        else:
            if is_list:
                lines.append("")
                is_list = False
            lines.append(
                textwrap.fill(line, width, initial_indent="", subsequent_indent=indent)
            )
    return "\n".join(lines) + "\n"


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
    # Normalize spaces
    val = re.sub(f"^ *{re.escape(marker)} *", "", val)
    # Enforce consistent marker on unordered lists
    if len(marker) == 2:
        marker = "* "
    return textwrap.fill(
        val,
        width,
        initial_indent=indent + marker,
        subsequent_indent=indent + " " * len(marker),
    )


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

    # Create tab lookup
    tabs = {(r["module"], r["tab"]): r["description"] for _, r in tabs.iterrows()}

    toc = {}
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

        toc.setdefault(module, []).append(tab_name)

# Create the module pages
for module, tabs in toc.items():
    content = h1(module)
    content.extend([".. toctree::", "   :maxdepth: 2", ""])
    for tab_name in tabs:
        content.append(f"   {tab_name.title()} <{slug(tab_name)}.rst>")
    with open(f"docs/modules/{module}/index.rst", "w", encoding="utf-8") as f:
        f.write("\n".join(content))

# Create the module landing page
content = h1("Modules")
content.extend([".. toctree::", "   :maxdepth: 2", ""])
for module in toc:
    content.append(f"   {module} <modules/{module}/index.rst>")
with open("docs/modules.rst", "w") as f:
    f.write("\n".join(content))

# Create the index page
content = h1("Mineral Sciences Data Guidelines")
content.extend([".. toctree::", "   :maxdepth: 2", ""])
content.append(f"    Guidelines for using EMu <guidelines.rst>")
content.append(f"    Guidelines for georeferencing <georeferencing.rst>")
content.append(f"    Guidelines for stratigraphy <stratigraphy.rst>")
content.append(f"    Field usage <modules.rst>")
with open("docs/index.rst", "w") as f:
    f.write("\n".join(content))

# Clean up manual reST files
for path in (
    "docs/guidelines.rst",
    "docs/georeferencing.rst",
    "docs/stratigraphy.rst",
):
    rewrap_rst(path)
