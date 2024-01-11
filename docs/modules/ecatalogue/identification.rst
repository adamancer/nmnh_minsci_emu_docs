###########################
ecatalogue > Identification
###########################

This tab consist of a grid identifying the types of rock or mineral
found in a specimen.

--------------------------------------------------------------------------------

.. _ecatalogue-identification-identification-details-taxon:

*****
Taxon
*****

+----------+---------------+
|Field     |Value          |
+==========+===============+
|ItemPrompt|Taxon          |
+----------+---------------+
|ColumnName|IdeTaxonRef_tab|
+----------+---------------+
|DataKind  |dkTable        |
+----------+---------------+
|DataType  |Reference      |
+----------+---------------+
|RefTable  |etaxonomy      |
+----------+---------------+

The name of the rock or mineral

Usage
=====

Required

Format
======

Reference to Taxonomy

--------------------------------------------------------------------------------

.. _ecatalogue-identification-identification-details-qualifier:

*********
Qualifier
*********

+----------+------------------------+
|Field     |Value                   |
+==========+========================+
|ItemPrompt|Qualifier               |
+----------+------------------------+
|ColumnName|IdeQualifier_tab        |
+----------+------------------------+
|DataKind  |dkTable                 |
+----------+------------------------+
|DataType  |Text                    |
+----------+------------------------+
|LookupName|Identification Qualifier|
+----------+------------------------+

Used to express uncertainty in the identification

Usage
=====

Omit if high confidence in the identification

Format
======

Must be "uncertain" if populated

--------------------------------------------------------------------------------

.. _ecatalogue-identification-identification-details-qualified-name:

**************
Qualified Name
**************

+----------+--------------------+
|Field     |Value               |
+==========+====================+
|ItemPrompt|Qualified Name      |
+----------+--------------------+
|ColumnName|IdeQualifiedName_tab|
+----------+--------------------+
|DataKind  |dkTable             |
+----------+--------------------+
|DataType  |Text                |
+----------+--------------------+

The qualified name of the rock or mineral

Usage
=====

Populated automatically by EMu

Format
======

The display name of the associated Taxon. If Qualifier is "uncertain", a
question mark will be appended to the value in this field to denote that
uncertainty.

--------------------------------------------------------------------------------

.. _ecatalogue-identification-identification-details-comments:

********
Comments
********

+----------+---------------+
|Field     |Value          |
+==========+===============+
|ItemPrompt|Comments       |
+----------+---------------+
|ColumnName|IdeComments_tab|
+----------+---------------+
|DataKind  |dkTable        |
+----------+---------------+
|DataType  |Text           |
+----------+---------------+

Comments about the identification

Usage
=====

Omit if no appropriate data is available

Format
======

Used primarily to note verbatim names when the selected Taxon does not
exactly match the name in the source material.

**Deprecated uses**

This field was previously used to store long-form descriptions of
specimens. Use Lot Description on the division-specific tabs instead.

--------------------------------------------------------------------------------

.. _ecatalogue-identification-identification-details-identified-by:

*************
Identified By
*************

+----------+----------------------+
|Field     |Value                 |
+==========+======================+
|ItemPrompt|Identified By Ref     |
+----------+----------------------+
|ColumnName|IdeIdentifiedByRef_tab|
+----------+----------------------+
|DataKind  |dkTable               |
+----------+----------------------+
|DataType  |Reference             |
+----------+----------------------+
|RefTable  |eparties              |
+----------+----------------------+

The person who identified the specimen

Usage
=====

Omit if no appropriate data is available

Format
======

Reference to Parties

--------------------------------------------------------------------------------

.. _ecatalogue-identification-identification-details-date-identified:

***************
Date Identified
***************

+----------+------------------+
|Field     |Value             |
+==========+==================+
|ItemPrompt|Date              |
+----------+------------------+
|ColumnName|IdeDateIdentified0|
+----------+------------------+
|DataKind  |dkTable           |
+----------+------------------+
|DataType  |Date              |
+----------+------------------+

The date the identification was made

Usage
=====

Omit if no appropriate data is available

Format
======



--------------------------------------------------------------------------------

.. _ecatalogue-identification-identification-details-named-part:

**********
Named Part
**********

+----------+----------------+
|Field     |Value           |
+==========+================+
|ItemPrompt|Named Part      |
+----------+----------------+
|ColumnName|IdeNamedPart_tab|
+----------+----------------+
|DataKind  |dkTable         |
+----------+----------------+
|DataType  |Text            |
+----------+----------------+
|LookupName|Named Part      |
+----------+----------------+

The part of the specimen being identified

Usage
=====

Required for each populated row

Format
======

Assign "Primary" to the primary classification (i.e., the rock name for
Petrology & Volcanology and the most important mineral phase for
Mineralogy). Assign "Associated" to additional classifications.

**Deprecated uses**

Older records use more specific terms ("Primary Rock", "Primary
Mineral", etc.) Most Taxonomy records now note whether a given species
is a rock or mineral, so this level of specificity is no longer
necessary.

Older records used "Primary Synonym" to note variety or synonym names to
a record. This term is still in use but should not be added to new
records. Most varieties and synonyms have their own records in Taxonomy.

--------------------------------------------------------------------------------

.. _ecatalogue-identification-identification-details-texture-structure:

*****************
Texture/Structure
*****************

+----------+-----------------------+
|Field     |Value                  |
+==========+=======================+
|ItemPrompt|Texture/Structure      |
+----------+-----------------------+
|ColumnName|IdeTextureStructure_tab|
+----------+-----------------------+
|DataKind  |dkTable                |
+----------+-----------------------+
|DataType  |Text                   |
+----------+-----------------------+
|LookupName|Texture Structure      |
+----------+-----------------------+

An alphabetized list of textural terms that apply to the rock/mineral

Usage
=====

Omit if no appropriate data is available

Format
======

Terms should be listed in alphabetical order in lower case. Use
semicolons to separate terms.

--------------------------------------------------------------------------------

.. _ecatalogue-identification-identification-details-color:

*****
Color
*****

+----------+--------------+
|Field     |Value         |
+==========+==============+
|ItemPrompt|Color         |
+----------+--------------+
|ColumnName|MinColor_tab  |
+----------+--------------+
|DataKind  |dkTable       |
+----------+--------------+
|DataType  |Text          |
+----------+--------------+
|LookupName|Minerals Color|
+----------+--------------+

The color of the rock/mineral

Usage
=====

Omit if no appropriate data is available
