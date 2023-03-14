#####################
elocations > Location
#####################

This tab includes information about a storage location, allowing users
to locate specimens in the collection or on exhibit. Most collections
locations use the first three or four levels of the hierarchy, that is,
building, room, cabinet/case, and drawer/shelf (Mineralogy typically
omits the last level). Exhibit locations use a more flexible hierarchy,
with the first two locations identifying the building and exhibit, the
third through fifth levels describing more precise locations within the
exhibit (for example, a topic area, a group of cases, and a specific
case), and the sixth level the identifier assigned by Exhibits. The
exhibit hierarchy was derived from the exhibit script and those
locations vary widely in their specificity.

--------------------------------------------------------------------------------

.. _elocations-location-identifiers-location-code:

*************
Location Code
*************

+----------+---------------+
|Field     |Value          |
+==========+===============+
|ItemPrompt|Location Code  |
+----------+---------------+
|ColumnName|LocLocationCode|
+----------+---------------+
|DataKind  |dkAtom         |
+----------+---------------+
|DataType  |Text           |
+----------+---------------+

A code used to identify a location, usually an exhibit case

Usage
=====

Omit if no appropriate data is available

Allowed Values
==============

* NHB
* MSC
* Udvar Hazy

--------------------------------------------------------------------------------

.. _elocations-location-identifiers-barcode:

*******
Barcode
*******

+----------+----------+
|Field     |Value     |
+==========+==========+
|ItemPrompt|Barcode   |
+----------+----------+
|ColumnName|LocBarcode|
+----------+----------+
|DataKind  |dkAtom    |
+----------+----------+
|DataType  |Text      |
+----------+----------+

Not used

--------------------------------------------------------------------------------

.. _elocations-location-location-type-location-holder:

***************
Location/Holder
***************

+----------+---------------+
|Field     |Value          |
+==========+===============+
|ItemPrompt|Location Type  |
+----------+---------------+
|ColumnName|LocLocationType|
+----------+---------------+
|DataKind  |dkAtom         |
+----------+---------------+
|DataType  |Text           |
+----------+---------------+

Type of storage location

Usage
=====

Required

--------------------------------------------------------------------------------

.. _elocations-location-storage-unit-type:

*********
Unit Type
*********

+----------+--------------+
|Field     |Value         |
+==========+==============+
|ItemPrompt|Storage Type  |
+----------+--------------+
|ColumnName|LocStorageType|
+----------+--------------+
|DataKind  |dkAtom        |
+----------+--------------+
|DataType  |Text          |
+----------+--------------+
|LookupName|Storage Type  |
+----------+--------------+

Type of storage unit

Usage
=====

Required

Examples
========

* Desiccant cabinet
* Exhibit
* Quarter unit
* Shelf

--------------------------------------------------------------------------------

.. _elocations-location-location-hierarchy-level-1:

*******
Level 1
*******

+----------+------------------+
|Field     |Value             |
+==========+==================+
|ItemPrompt|Level 1           |
+----------+------------------+
|ColumnName|LocLevel1         |
+----------+------------------+
|DataKind  |dkAtom            |
+----------+------------------+
|DataType  |Text              |
+----------+------------------+
|LookupName|Location Hierarchy|
+----------+------------------+

The name or abbreviation for a building

Usage
=====

Required

Examples
========

* MSC
* NHB
* Udvar Hazy

--------------------------------------------------------------------------------

.. _elocations-location-location-hierarchy-level-2:

*******
Level 2
*******

+----------+---------+
|Field     |Value    |
+==========+=========+
|ItemPrompt|Level 2  |
+----------+---------+
|ColumnName|LocLevel2|
+----------+---------+
|DataKind  |dkAtom   |
+----------+---------+
|DataType  |Text     |
+----------+---------+

The room number or exhibit name

Usage
=====

Required

Format
======

Usually the room number. Mineralogy includes a parenthetical with a
short text description that identifies the location (like "Blue Room" or
"Reference Collection").

Examples
========

* E431C (Blue Room)
* E432A
* E433
* GGM

--------------------------------------------------------------------------------

.. _elocations-location-location-hierarchy-level-3:

*******
Level 3
*******

+----------+---------+
|Field     |Value    |
+==========+=========+
|ItemPrompt|Level 3  |
+----------+---------+
|ColumnName|LocLevel3|
+----------+---------+
|DataKind  |dkAtom   |
+----------+---------+
|DataType  |Text     |
+----------+---------+

For collections, the identifier of a cabinet, case, or other storage
unit. For exhibits, a description of where in the exhibit the case is
found.

Usage
=====

Required

Format
======

For collections locations, zero-pad the cabinet/case number to three
characters.

Examples
========

* 001
* 010
* 100

--------------------------------------------------------------------------------

.. _elocations-location-location-hierarchy-level-4:

*******
Level 4
*******

+----------+---------+
|Field     |Value    |
+==========+=========+
|ItemPrompt|Level 4  |
+----------+---------+
|ColumnName|LocLevel4|
+----------+---------+
|DataKind  |dkAtom   |
+----------+---------+
|DataType  |Text     |
+----------+---------+

For collections, the identifier of a drawer, shelf, or other storage
sub-unit.  For exhibits, a description of where in the exhibit the case
is found.

Usage
=====

Omit if no appropriate data is available

Format
======

For collections locations, zero-pad the drawer/shelf identifier to two
characters.

Examples
========

* 01
* 10

--------------------------------------------------------------------------------

.. _elocations-location-location-hierarchy-level-5:

*******
Level 5
*******

+----------+---------+
|Field     |Value    |
+==========+=========+
|ItemPrompt|Level 5  |
+----------+---------+
|ColumnName|LocLevel5|
+----------+---------+
|DataKind  |dkAtom   |
+----------+---------+
|DataType  |Text     |
+----------+---------+

For exhibits, a description of where in the exhibit the case is found.

Usage
=====

Omit if no appropriate data is available

--------------------------------------------------------------------------------

.. _elocations-location-location-hierarchy-level-6:

*******
Level 6
*******

+----------+---------+
|Field     |Value    |
+==========+=========+
|ItemPrompt|Level 6  |
+----------+---------+
|ColumnName|LocLevel6|
+----------+---------+
|DataKind  |dkAtom   |
+----------+---------+
|DataType  |Text     |
+----------+---------+

For exhibits, the case identifier

Usage
=====

Omit if no appropriate data is available

Examples
========

* MC-009
* MC-010

--------------------------------------------------------------------------------

.. _elocations-location-location-hierarchy-level-7:

*******
Level 7
*******

+----------+---------+
|Field     |Value    |
+==========+=========+
|ItemPrompt|Level 7  |
+----------+---------+
|ColumnName|LocLevel7|
+----------+---------+
|DataKind  |dkAtom   |
+----------+---------+
|DataType  |Text     |
+----------+---------+

Not used

--------------------------------------------------------------------------------

.. _elocations-location-location-hierarchy-level-8:

*******
Level 8
*******

+----------+---------+
|Field     |Value    |
+==========+=========+
|ItemPrompt|Level 8  |
+----------+---------+
|ColumnName|LocLevel8|
+----------+---------+
|DataKind  |dkAtom   |
+----------+---------+
|DataType  |Text     |
+----------+---------+

Not used
