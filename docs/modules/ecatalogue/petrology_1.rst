##########################
ecatalogue > Petrology (1)
##########################

This tab captures data specific to rocks and ores.

--------------------------------------------------------------------------------

.. _ecatalogue-petrology-1-object-data-from-time-of-collecting-event-event-site:

**********
Event/Site
**********

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

.. _ecatalogue-petrology-1-object-data-from-time-of-collecting-event-collectors:

**********
Collectors
**********

+----------+---------------------+
|Field     |Value                |
+==========+=====================+
|ItemPrompt|Collectors Ref       |
+----------+---------------------+
|ColumnName|BioParticipantRef_tab|
+----------+---------------------+
|DataKind  |dkTable              |
+----------+---------------------+
|DataType  |Reference            |
+----------+---------------------+
|RefTable  |eparties             |
+----------+---------------------+

List of collector names

Usage
=====

Populated automatically from the associated Collections Event record

--------------------------------------------------------------------------------

.. _ecatalogue-petrology-1-volcano-attributes-lava-source:

***********
Lava Source
***********

+----------+-------------+
|Field     |Value        |
+==========+=============+
|ItemPrompt|Lava Source  |
+----------+-------------+
|ColumnName|PetLavaSource|
+----------+-------------+
|DataKind  |dkAtom       |
+----------+-------------+
|DataType  |Text         |
+----------+-------------+
|LookupName|Lava Source  |
+----------+-------------+

The name of the volcanic feature

Usage
=====

Deprecated. Use the Subfeature field instead.

--------------------------------------------------------------------------------

.. _ecatalogue-petrology-1-volcano-attributes-flow-tephra:

***********
Flow/Tephra
***********

+----------+-------------+
|Field     |Value        |
+==========+=============+
|ItemPrompt|Flow/Tephra  |
+----------+-------------+
|ColumnName|PetFlowTephra|
+----------+-------------+
|DataKind  |dkAtom       |
+----------+-------------+
|DataType  |Text         |
+----------+-------------+
|LookupName|Flow Tephra  |
+----------+-------------+

The name of the flow or tephra unit

Usage
=====

Deprecate? Conceptual overlap with stratigraphy table.

--------------------------------------------------------------------------------

.. _ecatalogue-petrology-1-preparation-details-preparation:

***********
Preparation
***********

+----------+-------------------+
|Field     |Value              |
+==========+===================+
|ItemPrompt|Preparation        |
+----------+-------------------+
|ColumnName|ZooPreparation_tab |
+----------+-------------------+
|DataKind  |dkTable            |
+----------+-------------------+
|DataType  |Text               |
+----------+-------------------+
|LookupName|Zoology Preparation|
+----------+-------------------+

The type of the preparation

Usage
=====

Omit if no appropriate data is available

Format
======

The preparation grid is used to store information about preparations
dervied from and stored in the same location as the primary specimen.
Preparations stored in a different location should have their own EMu
record that links back to the primary specimen using the Relationships
tab.

Preparation type should be selected from the list of allowed values
provided here. Please contact the data manager if additional values are
required.

Historically, some collection methods (usually dredge or core) were
included in this field. This data should go in *Collection Events >
Exp/Method > Collection method* instead.

Allowed Values
==============

* Grain mount
* Powder
* Thick section
* Thin section

--------------------------------------------------------------------------------

.. _ecatalogue-petrology-1-preparation-details-prepared-by:

***********
Prepared By
***********

+----------+--------------------+
|Field     |Value               |
+==========+====================+
|ItemPrompt|Prepared By Ref     |
+----------+--------------------+
|ColumnName|ZooPreparedByRef_tab|
+----------+--------------------+
|DataKind  |dkTable             |
+----------+--------------------+
|DataType  |Reference           |
+----------+--------------------+
|RefTable  |eparties            |
+----------+--------------------+

The person who created the preparation

Usage
=====

Omit if no appropriate data is available

Format
======

Reference to Parties

--------------------------------------------------------------------------------

.. _ecatalogue-petrology-1-preparation-details-preparation-count:

*****************
Preparation Count
*****************

+----------+-----------------------+
|Field     |Value                  |
+==========+=======================+
|ItemPrompt|Preparation Count      |
+----------+-----------------------+
|ColumnName|ZooPreparationCount_tab|
+----------+-----------------------+
|DataKind  |dkTable                |
+----------+-----------------------+
|DataType  |Integer                |
+----------+-----------------------+

The number of preparations of this type

Usage
=====

Required for each row where Preparation is populated

--------------------------------------------------------------------------------

.. _ecatalogue-petrology-1-preparation-details-preparation-remarks:

*******************
Preparation Remarks
*******************

+----------+-------------------------+
|Field     |Value                    |
+==========+=========================+
|ItemPrompt|Preparation Remarks      |
+----------+-------------------------+
|ColumnName|ZooPreparationRemarks_tab|
+----------+-------------------------+
|DataKind  |dkTable                  |
+----------+-------------------------+
|DataType  |Text                     |
+----------+-------------------------+

Comments about the preparation

Usage
=====

Omit if no appropriate data is available

--------------------------------------------------------------------------------

.. _ecatalogue-petrology-1-lot-description-lot-description:

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
