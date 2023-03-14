#######################
About Collection Events
#######################

The Collection Events module stores information about where, when, and by
whom a sample was collected. The specificity of this information varies between
samples. Old collection records may specify locality only to the level of a country
or state, while newer records may include date, time, latitude, and longitude
of sample collection.

Mineral Sciences classifies records in this module with two labels: Site and
Collection Event.

A **site** is a record that contains only place names. The place names may be very
broad (like a country or state) or quite specific (like a town, mine, or island
name). Site records are typically suitable for re-use, especially for old
records with limited geographic information. Sites can also in many cases be
matched to place names in authoritative gazetteers (like Getty or GeoNames),
which can provide useful context for records otherwise lacking specific detail.

A **collection event** includes specifics about when or by whom a sample was
collected or very precise about where a sample was collected. Event records are typically too specific to re-use outside of a
single collection or import and in many cases will be specific to a single
sample.

*************
Data standard
*************

Standard records for terrestrial collection events must include the following data:

+ Continent
+ Country
+ State/province
+ One or more of the following:
    + District/county
    + Geomorphological location
    + Island name
    + Mining district
    + Mine name
    + Precise locality
    + Quadrangle/map name
    + Township
    + Volcano name

Standard records for marine collection events must include the following data:

+ Ocean
+ Sea/Gulf
+ One or more of the following:
    + Bay/sound
    + Geomorphological location
    + Precise locality


To exceed standards, a record should include coordinates as well as all of the
data above. Coordinates may be provided by the collector or determined later
by georeferencing the sample.

In addition to coordinates, georeferenced samples must also include the
following information:

+ Source
+ Method
+ Name of geoereferencer
+ Date of georeference
+ Error radius
+ Geometry (point, polygon, or bounding box)
+ Datum
+ A description of how the sample was georeferenced. This description should
  be as detailed as possible to help end-users assess the reliability of
  coordinates.
