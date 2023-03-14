##############
Georeferencing
##############

Georeferencing is the process of converting locality information in a
catalog record (including feature names, directions, and alternative
coordinate systems like section-township-range) to a latitude and
longitude. Georeferencing provides the following benefits:

* Allows samples to be plotted on a map
* Allows users to search by coordinate ranges or polygons in a map
  interface
* Allows samples to be added to data repositories requiring coordinates

The primary drawback is that users of the database may be confused by
the addition of site info and coordinates to record summary lines, which
among other things may discourage re-use of locality records.
Additionally, coordinates determined by georeferencing are necessarily
interpretive and should never be used to update or refine the data in a
record without careful consideration. For example, you would never back-
populate the state/province and district/county names for a record
matched only a township.

Georeferencing can be done manually or via script.

**Manual georeferencing** is labor-intensive, requiring 5-10 minutes per
record even with modern tools like GEOLocate and Google Maps. However,
using this method allows access to sources that are not available in
machine-readable formats (like Mindat's locality records) and may be
necessary for complex records.

**Automatic georeferencing** can be done fairly quickly and works well
with fairly simple records, especially legacy records with limited
geographical info. It can struggle with complex records containing
multiple place names or directional info and is limited to tools and
data sources that are machine-friendly. The primary georeferencing tool
in Mineral Sciences at present is a script called situate.py that works
from the GeoNames gazetteer.

In many cases, script-based georeferencing can match some but not all
information in a record. This is common with records that include mine
names, which are highly specific but poorly represented in gazetteers.
It is often possible to match feature, town, or county names in these
records, in which case a reasonable workflow would be to georeference
the record to that level and flag it for manual review at a later date.

**********************************************
Collection-specific georeferencing information
**********************************************

Meteorites collected by the Antarctic Search for Meteorites Program (ANSMET)
============================================================================

Coordinates for meteorites collected by the Antarctic Search for
Meteorites (ANSMET) program are taken from NASA's `Complete Listing of
Antarctic Meteorites in the U.S. Collection
<https://curator.jsc.nasa.gov/antmet/excel/usantmet.xls>`_. NASA
describes their coordinate data as follows:

    Position data has been derived from a variety of surveying
    techniques (primarily GPS since the early 1990's) used by ANSMET
    field teams and reflects a typical uncertainty of around 10 m. The
    data has been truncated to avoid confusing high precision (many
    decimal places) with high accuracy (low error). These positions
    reflect a realistic “best available” accuracy, at ˜50x higher
    resolution than required by federal regulations.

All meteorites collected by ANSMET are assigned source=ANSMET, radius=10
m, and a determination date marking the year of collection. Meteorites
collected before 1993 are assigned method=Surveying and datum=Unknown.
Meteorites collected during or after 1993 are assigned method=GPS and
datum=WGS 84.
