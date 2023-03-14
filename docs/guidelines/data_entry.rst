##########
Data entry
##########

These guidelines were developed to help inexperienced catalogers better
understand how to enter data in the cataloging spreadsheet.

Information that goes into the collections database should:

* Be specific to the specimen
* Be meaningful without any context beyond what's included in the
  specimen record
* Make sense to the cataloger

**When in doubt, ask the collections staff!** Ask early, ask often.

**********************************
Getting the data entry spreadsheet
**********************************

Mineral Sciences has a data capture spreadsheet that you can customize
for the needs of your collection. Contact the data manager to obtain a
copy of the spreadsheet.

* **Using Excel instead of Google Sheets**: If you'd prefer to use Excel
  for data entry, export the spreadsheet as .xlsx by selecting File >
  Download as > Microsoft Excel (.xlsx). Some of the formatting gets a
  little messed up by the export process, but the data validation
  defined in the sheet appears to make it through unharmed.

**************************************
Customizing the data entry spreadsheet
**************************************

You can modify the data entry spreadsheet to better suit the needs of
your collection by adding columns for specific data or deleting columns
you don't need.

* **Use recommended column names**: This document and the Google sheet
  include fields and definitions for many common types of data. You
  can add any of these columns to your spreadsheet. Please stick to
  the recommended column names if possible.
* **Requesting a new column**: If you encounter data that doesn't fit
  any of these categories, ask someone from the collections staff
  where it should go.

******************
General guidelines
******************

Required metadata
=================

This is the absolute minimum information required for a specimen record
in the rock and ore collection.

* Catalog number
* Accession number
* Collector's field number
* IGSN (if exists)
* Collection name
* Storage location
* Specimen type
* Rock/mineral name
* Basic locality info (including place and feature names). Places names
  with dedicated fields in the collections database include:

    * Country
    * State/province/territory
    * District/county/shire
    * City/town
    * Mining district
    * Mine name
    * Volcano (see the [Global Volcanism Program] for volcano names)
    * Ocean
    * Sea/gulf
    * Bay/sound
    * Island grouping
    * Island name

* Specimen count
* Preparations, if any. Common preparation types include:

    * Grain mounts
    * Powders
    * Thick sections
    * Thin sections

Recommended metadata
====================

Not all specimens will have all or even some this information, but be
sure to include it if it exists.

* References mentioning the specimen

    * Include `DOIs
      <https://en.wikipedia.org/wiki/Digital_object_identifier>`_
      for each reference that has one. Otherwise include the full
      reference.
    * Use the reference tab to define citations as you would in a
      bibliography. This allows you to use shorthand citations in
      the catalog spreadsheet (like Hale et al., 2020) instead of
      writing out the full reference each time. **If using
      citations, make sure the citation string is disinct.**

* Geologic/stratigraphic unit (e.g., *Wait River Formation* or *Honolulu
  Volcanic Series*)
* Geologic setting/event (e.g. *Grenville Orogeny* or *Rainbow Basin
  Syncline*)
* A detailed locality description (e.g., *From halfway up the ridge 60-m
  N of the intersection of Ridge Rd and Cedar Ave*)
* A detailed sample description (e.g., *Coarse garnets (2-5 mm diameter)
  with kelyphite rims in a matrix of plagioclase and clinopyroxene*)
* Latitude/longitude (including the geodetic datum)
* Collection date/time (especially if sampling a recent eruption)
* Eruption date/time

Additional metadata
===================

The information here may help users discover or use this specimen, but
mostly can be reconstructed from other sources.

* **Section/township/range**: Add as its own column if required. Data
  should be formatted roughly like so: *SW1/4 NW1/4 S13 T1S R20E*.
  Some records with `PLSS
  <https://en.wikipedia.org/wiki/Public_Land_Survey_System>`_ data will
  have multiple quarter sections, some will have one or none.
* **Maps**: Include published maps as references.
* **Weight**: Add as its own column if required. Include both the weight
  and unit (e.g., *60 g*).
* **Age**: Add as its own column if required. Include the age, error,
  unit, and method (e.g., *60.1 ± 2.8 Ma based on multi-sample Sm-Nd
  isochron*).

    * Do not include ages that are not based on a measurement
      of/including the current specimen (for example,
      stratigraphic ages)
    * Describing ages can get very complex

* **Preparations**: Each different preparation should have its own
  column. The value should be the number of that preparation that we
  have for the specimen. The generic spreadsheet includes Thin
  Sections and Grain Mounts, but you can add columns for powers,
  butts, etc. A hand sample is *not* a preparation.
* **Notes**: Use notes judiciously. Most information that has
  historically gone into notes has a better home elsewhere. Never mix
  specimen and locality information in the same note.

Some things to avoid
====================

* **DO NOT** include information that you don't understand. If something
  looks important but you don't know what it means, ask the
  collections staff.
* **DO NOT** use abbreviations. Abbreviations are often ambiguous and
  it's always clearer to spell out the full word. That said, here are
  two places where it is acceptable to use abbreviations:

    * OK to abbreviate if you're quoting documentation directly (but use
      quotes!)
    * OK to abbreviate compass directions (N, S, E, W, NW, NE, NNW,
      etc.) in long-form descriptions but not in place names

* **DO NOT** include references that don't mention the specific specimen

  * OK for certain older collections (especially those from the USGS)
    where the publication describes the entire collection but
    doesn't name individual samples

* **DO NOT** identify a rock specimen using a list of minerals. The
  primary identification of a rock specimen should be a rock type!
* **DO NOT** convert latitudes/longitudes given as degrees-minutes-
  seconds to decimals. Careless conversions can give a false sense of
  the precision of the original measurement, and EMu makes these
  conversions automatically.
* **DO NOT** try to map old place names to their modern equivalents.
  This process is error-prone and can be addressed once the data is in
  the collections database. Use the verbatim information instead.
* **DO NOT** wedge data with no obvious home into the notes field

*************************************
Guidelines for specific types of data
*************************************

IGSN
====

The `IGSN <http://www.geosamples.org/useigsn>`_ is a unique, persistent
identifier used to unambiguously identify a sample. **It is very
important to include the IGSN for all samples that have one.** Learn
more about IGSNs at the [System for Earth Sample Registration].

Specimen count
==============

* Each specimen tray contains one or more **primary objects** (typically
  one or more hand samples, but sometimes a bag or a vial) and may
  also contain **preparations** (distinct objects derived from the
  primary object, like thin sections or powders)
* The specimen count is the number of primary objects
* Preparations do not count toward the specimen count
* The count is never zero
* Here are some examples illustrating how to get the specimen count:

    * Tray with 3 large fragments = 3
    * Tray with one rock containing 4 distinct xenoliths = 1
    * Bag full of small fragments = 1
    * Vial of natural material (like sand or volcanic ash) = 1

        * But a vial of rock powder created in a shatterbox is a prep!

    * Tray with two large rock fragments, a thin section, and a vial of
      powder = 2

Classification
==============

* Use a pipeline to delimit|multiple|values. If including multiple
  values, list rock/mineral names in order of significance.
* When adding classifications, provide the name exactly as given

    * Use the sample description field to include more information about
      the sample (texture, grain sizes, relative proportions of
      phases, etc.)
    * It is OK to fix obvious typos

* Rock/mineral vocabularies

    * Mineral names and definitions: `Mindat <https://mindat.org/>`_
    * Rock names and definitions: `BGS Rock Classification
      <http://www.bgs.ac.uk/bgsrcs/>`_

* Pyroclastic classifications: `IUGS Pyroclastic Classification
  <http://www.geol.lsu.edu/henry/Geology3041/lectures/02IgneousClassify/IUGS-IgneousClassFlowChart.htm>`_
* Petrology specimens should almost always have a rock name as the first
  term. Major minerals are sometimes included in the rock name (e.g.,
  Olivine-basalt). List minor minerals after the primary name using a
  pipeline as the delimiter.

    * Rock/mineral name = *Olivine-basalt|Diopside|Titanite*

* Some common rock types have their own, more complex classification
  needs. If you run into any of the following rock types, use the
  following column names to distinguish the different parts.

    * **Fossils**: Use column names Rock/mineral name and Fossil

        * Rock/mineral name = *Sandstone*, Fossil = *Glossopteris*

    * **Pyroclastics**: Use column names Rock/mineral name and
      Pyroclastic Classification

        * Rock/mineral name = *Andesite*, Pyroclastic Classification =
          *Tuff*
        * Rock/mineral name = *Rhyolite*, Pyroclastic Classification =
          *Scoria*

    * **Veins**: Use column names Vein and Host Rock

        * Vein = *Andesite*, Host Rock = *Granite*

    * **Xenoliths**: Use column names Xenolith and Host Rock

        * Xenolith = *Clinopyroxenite|Dunite*, Host Rock = *Basalt*

Collection locality
===================

* When adding place and feature names, provide them exactly as given.
  Use the locality description field to include more specific
  information
* Include as much detail about the locality as possible, even if you're
  also including coordinates. Textual information may be of historical
  interest and can be used to verify and refine coordinates.
* If including latitude and longitude, you should also include the
  `geodetic datum <https://en.wikipedia.org/wiki/Geodetic_datum>`_. A
  geodetic datum is typically a short alphanumeric code. The most
  common datums are WGS 84 and NAD 83.
* **Georeferencing**: It is sometimes possible to estimate latitude and
  longitude based on the locality description using resources like
  `GEOLocate
  <http://www.museum.tulane.edu/geolocate/web/WebGeoref.aspx>`_ and
  `GeoNames <http://geonames.org/>`_. This process is called
  georeferencing and is an important tool for making natural history
  collections easier to find. When georeferencing a sample, it is
  extremely important to include a detailed description about how the
  coordinates were determined, as well as an estimated error radius
  (which can be quite large if the original description is inexact).
  This allows future users of the data to (1) distinguish between
  coordinates provided by the collector and those extrapolated later and
  (2) understand that the provided coordinates are not exact.