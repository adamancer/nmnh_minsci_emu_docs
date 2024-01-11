#######################
ecatalogue > Meteorites
#######################

This tab captures data specific to meteorites. Basic meteorite metadata,
including name, type, and find/fall, is aligned annually with the
`Meteorite Bulletin Database (MBDB)
<https://www.lpi.usra.edu/meteor/metbull.php>`_.

--------------------------------------------------------------------------------

.. _ecatalogue-meteorites-meteorite-details-meteorite-name:

**************
Meteorite Name
**************

+----------+----------------+
|Field     |Value           |
+==========+================+
|ItemPrompt|Meteorite Name  |
+----------+----------------+
|ColumnName|MetMeteoriteName|
+----------+----------------+
|DataKind  |dkAtom          |
+----------+----------------+
|DataType  |Text            |
+----------+----------------+

The official name of the meteorite

Usage
=====

Required

Format
======

For **non-Antarctic meteorites**, the name should exactly match the Name
field for the corresponding MBDB record. Most meteorites are named after
the nearest named place to where they fell, so these names are usually
simple strings.

For **Antarctic meteorites**, the name must be the meteorite number as
currently asssigned by NASA. The NASA meteorite number consists of two
components: a generic identifier identifying a mass and an optional
specific identifier (often referred to as a comma number) identifying a
subsample. The generic identifier includes:

* A three-character alphabetic prefix identifying the general area where
  the meteorite was collected
* A space
* A five- to six-digit number (YYDDD or YYDDDD, where YY is the last two
  digits of the collection year and DDD/DDDD is the number identifying a
  mass)


If a specific identifier has been assigned, append a comma followed by
that identifier to the generic identifier. A representative example is
"ALH 83101,15", where "ALH 83101" is the generic identifier and "15" is
the specific identifier.

Some notes on meteorite numbers:

* Meteorites collected early on in ANSMET used a letter to separate the
  locality prefix from the specimen number. The letter was intended to
  signify different field seasons within a year. Those additional field
  seasons never materialized, but some meteorites from the early years
  of the program were originally numbered named using an "A" instead of
  a space. MBDB retains the original identifiers, but NASA's public
  documentation has standardized all meteorites numbers to use a space.
  In other words, "ALHA76001" in MBDB is the same as "ALH 76001" in
  NASA's documentation. We use the NASA identifiers but retain the
  original numbers in the Other Numbers grid.
* MBDB includes the NASA meteorite number in the Abbrev. field. MBDB
  uses the Name field to provide the full name of the collection area.
  For example, for ALH 83101, MBDB uses "Allan Hills 83101" for the name
  and "ALH 83101" for the abbreviation.


Names are aligned with MBDB annually. Roughly 100 meteorites in the
collection could not be matched to an entry in MBDB.

--------------------------------------------------------------------------------

.. _ecatalogue-meteorites-meteorite-details-synonym:

*******
Synonym
*******

+----------+----------+
|Field     |Value     |
+==========+==========+
|ItemPrompt|Synonym   |
+----------+----------+
|ColumnName|MetSynonym|
+----------+----------+
|DataKind  |dkAtom    |
+----------+----------+
|DataType  |Text      |
+----------+----------+

The verbatim name of the meteorite if originally cataloged under a
synonym

Usage
=====

Required if meteorite was originally cataloged under a synonym

Format
======

For meteorites originally cataloged under a synonym, use this field to
record the verbatim name. This field should not be used to record every
synonym for a meteorite.

--------------------------------------------------------------------------------

.. _ecatalogue-meteorites-meteorite-details-meteorite-type:

**************
Meteorite Type
**************

+----------+----------------+
|Field     |Value           |
+==========+================+
|ItemPrompt|Meteorite Type  |
+----------+----------------+
|ColumnName|MetMeteoriteType|
+----------+----------------+
|DataKind  |dkAtom          |
+----------+----------------+
|DataType  |Text            |
+----------+----------------+
|LookupName|Meteorite Type  |
+----------+----------------+

The type of meteorite

Usage
=====

Required

Format
======

The type should exactly match the Type field for the corresponding MBDB
record. MBDB uses a different format for meteorite type than NASA.

A handful of specimens collected during ANSMET were determined to be
terrestrial in origin. These specimens are assigned the type
"Terrestrial rock".

Meteorite types  are aligned with MBDB annually.

--------------------------------------------------------------------------------

.. _ecatalogue-meteorites-meteorite-details-record-number:

*************
Record Number
*************

+----------+---------------+
|Field     |Value          |
+==========+===============+
|ItemPrompt|Record No      |
+----------+---------------+
|ColumnName|MetRecordNumber|
+----------+---------------+
|DataKind  |dkAtom         |
+----------+---------------+
|DataType  |Text           |
+----------+---------------+

No idea

Usage
=====

Legacy

--------------------------------------------------------------------------------

.. _ecatalogue-meteorites-meteorite-details-find-fall:

*********
Find/Fall
*********

+----------+------------------+
|Field     |Value             |
+==========+==================+
|ItemPrompt|Find Fall         |
+----------+------------------+
|ColumnName|MetFindFall       |
+----------+------------------+
|DataKind  |dkAtom            |
+----------+------------------+
|DataType  |Text              |
+----------+------------------+
|LookupName|Meteorite FindFall|
+----------+------------------+

Whether the meteorite fall was observed

Usage
=====

Required

Format
======

Usually "Find" or "Fall", but more recent meteorites sometimes included
more specific information.

Historically, meteorites are categorized as "falls" if they are
witnessed falling and "finds" otherwise. These categories elide much of
the uncertainy in assigning fall status. In Agee et al. (2015), the
Meteorite Nomenclature Committee revised fall categorization for recent
meteorite discoveries to better capture that uncertainty. The terms they
settled on are included in the Allowed Values list. We plan to implement
that vocabulary but, as of 2022, none of the meteorites in the
collection has been assigned to one of the new categories.

Fall status is aligned with MBDB annually.

Allowed Values
==============

* Fall
* Fall, confirmed
* Fall, probable
* Find
* Find, possible fall
* Find, doubtful fall

--------------------------------------------------------------------------------

.. _ecatalogue-meteorites-collection-details-locality:

********
Locality
********

+----------+-----------------+
|Field     |Value            |
+==========+=================+
|ItemPrompt|Event/Site Ref   |
+----------+-----------------+
|ColumnName|BioEventSiteRef  |
+----------+-----------------+
|DataKind  |dkAtom           |
+----------+-----------------+
|DataType  |Reference        |
+----------+-----------------+
|RefTable  |ecollectionevents|
+----------+-----------------+

The collection locality and event

Usage
=====

Required

Format
======

Reference to Collection Events

--------------------------------------------------------------------------------

.. _ecatalogue-meteorites-lot-description-lot-description:

***************
Lot Description
***************

+----------+---------------+
|Field     |Value          |
+==========+===============+
|ItemPrompt|Live Specimen  |
+----------+---------------+
|ColumnName|BioLiveSpecimen|
+----------+---------------+
|DataKind  |dkAtom         |
+----------+---------------+
|DataType  |Text           |
+----------+---------------+

A long-form description of the specimen

Usage
=====

Omit if no appropriate data is available

--------------------------------------------------------------------------------

.. _ecatalogue-meteorites-condition-determination-condition-determination:

***********************
Condition Determination
***********************

+----------+-------------------------+
|Field     |Value                    |
+==========+=========================+
|ItemPrompt|Condition Determination  |
+----------+-------------------------+
|ColumnName|MetConditionDetermination|
+----------+-------------------------+
|DataKind  |dkAtom                   |
+----------+-------------------------+
|DataType  |Text                     |
+----------+-------------------------+

A description of the condition of the specimen

Usage
=====

Omit if no appropriate data is available
