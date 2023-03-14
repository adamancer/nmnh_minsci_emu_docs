##############################
ecollectionevents > Depth/Elev
##############################

This tab is used to summarize depth and elevation information. Only
populate this tab if the collector provides this information--do not
extrapolate depths or elevations from coordinates.

This tab includes two sets of fields for depth. The **depth fields**
describe the depth in the water column at which a specimen was
collected. The **bottom depth fields** fields describe to the depth of
the sea floor. Geological specimens in the Mineral Sciences collections
always come from the sea floor. To avoid redundancy, only the Bottom
Depth columns are populated.

--------------------------------------------------------------------------------

.. _ecollectionevents-depth-elev-depth-details-depth-from:

**********
Depth From
**********

+----------+---------------+--------------+----------------+--------------------+
|Field     |AquDepthFromMet|AquDepthFromFt|AquDepthFromFath|AquDepthFromModifier|
+==========+===============+==============+================+====================+
|ItemPrompt|Depth From     |              |                |Modifier            |
+----------+---------------+--------------+----------------+--------------------+
|ColumnName|AquDepthFromMet|AquDepthFromFt|AquDepthFromFath|AquDepthFromModifier|
+----------+---------------+--------------+----------------+--------------------+
|DataKind  |dkAtom         |dkAtom        |dkAtom          |dkAtom              |
+----------+---------------+--------------+----------------+--------------------+
|DataType  |Float          |Float         |Float           |Text                |
+----------+---------------+--------------+----------------+--------------------+
|LookupName|               |              |                |Elevation Modifier  |
+----------+---------------+--------------+----------------+--------------------+

Not used

--------------------------------------------------------------------------------

.. _ecollectionevents-depth-elev-depth-details-depth-to:

********
Depth To
********

+----------+-------------+------------+--------------+------------------+
|Field     |AquDepthToMet|AquDepthToFt|AquDepthToFath|AquDepthToModifier|
+==========+=============+============+==============+==================+
|ItemPrompt|Depth To     |            |              |Modifier          |
+----------+-------------+------------+--------------+------------------+
|ColumnName|AquDepthToMet|AquDepthToFt|AquDepthToFath|AquDepthToModifier|
+----------+-------------+------------+--------------+------------------+
|DataKind  |dkAtom       |dkAtom      |dkAtom        |dkAtom            |
+----------+-------------+------------+--------------+------------------+
|DataType  |Float        |Float       |Float         |Text              |
+----------+-------------+------------+--------------+------------------+
|LookupName|             |            |              |Elevation Modifier|
+----------+-------------+------------+--------------+------------------+

Not used

--------------------------------------------------------------------------------

.. _ecollectionevents-depth-elev-depth-details-depth-determination:

*******************
Depth Determination
*******************

+----------+---------------------+
|Field     |Value                |
+==========+=====================+
|ItemPrompt|Depth Determination  |
+----------+---------------------+
|ColumnName|AquDepthDetermination|
+----------+---------------------+
|DataKind  |dkAtom               |
+----------+---------------------+
|DataType  |Text                 |
+----------+---------------------+
|LookupName|Depth Determination  |
+----------+---------------------+

Not used

--------------------------------------------------------------------------------

.. _ecollectionevents-depth-elev-depth-details-text-depth:

**********
Text Depth
**********

+----------+----------------+
|Field     |Value           |
+==========+================+
|ItemPrompt|Verbatim Depth  |
+----------+----------------+
|ColumnName|AquVerbatimDepth|
+----------+----------------+
|DataKind  |dkAtom          |
+----------+----------------+
|DataType  |Text            |
+----------+----------------+

Not used

--------------------------------------------------------------------------------

.. _ecollectionevents-depth-elev-depth-details-bottom-depth-from:

*****************
Bottom Depth From
*****************

+----------+---------------------+--------------------+----------------------+--------------------------+
|Field     |AquBottomDepthFromMet|AquBottomDepthFromFt|AquBottomDepthFromFath|AquBottomDepthFromModifier|
+==========+=====================+====================+======================+==========================+
|ItemPrompt|Bottom Depth From    |                    |                      |Modifier                  |
+----------+---------------------+--------------------+----------------------+--------------------------+
|ColumnName|AquBottomDepthFromMet|AquBottomDepthFromFt|AquBottomDepthFromFath|AquBottomDepthFromModifier|
+----------+---------------------+--------------------+----------------------+--------------------------+
|DataKind  |dkAtom               |dkAtom              |dkAtom                |dkAtom                    |
+----------+---------------------+--------------------+----------------------+--------------------------+
|DataType  |Float                |Float               |Float                 |Text                      |
+----------+---------------------+--------------------+----------------------+--------------------------+
|LookupName|                     |                    |                      |Elevation Modifier        |
+----------+---------------------+--------------------+----------------------+--------------------------+

The depth of the seafloor at which a collection event began

Usage
=====

Omit for terrestrial samples and aquatic samples where the collection
depth is not known.

Format
======

For dredges and trawls, Depth From is the depth at the point where the
collecting event started. In earlier databases, this was referred to as
"on bottom".

Each of the columns in this group represents a specific unit: meters,
feet, and fathoms. When adding bottom depth, you only need to fill out
one of the three columns. The other two will be calculated automatically
by EMu. Original values display as black and calculated values as red in
the client.

If only one depth is provided, use that depth in both Depth From and
Depth To. Always provide the verbatim depth, including units, in Text
Bottom Depth.

The modifier field is used to indicate uncertainty in depth
measurements. Use "approx." to indicate uncertainty. The exact
uncertainty can be expressed in Text Bottom Depth.

--------------------------------------------------------------------------------

.. _ecollectionevents-depth-elev-depth-details-bottom-depth-to:

***************
Bottom Depth To
***************

+----------+-------------------+------------------+--------------------+------------------------+
|Field     |AquBottomDepthToMet|AquBottomDepthToFt|AquBottomDepthToFath|AquBottomDepthToModifier|
+==========+===================+==================+====================+========================+
|ItemPrompt|Bottom Depth To    |                  |                    |Modifier                |
+----------+-------------------+------------------+--------------------+------------------------+
|ColumnName|AquBottomDepthToMet|AquBottomDepthToFt|AquBottomDepthToFath|AquBottomDepthToModifier|
+----------+-------------------+------------------+--------------------+------------------------+
|DataKind  |dkAtom             |dkAtom            |dkAtom              |dkAtom                  |
+----------+-------------------+------------------+--------------------+------------------------+
|DataType  |Float              |Float             |Float               |Text                    |
+----------+-------------------+------------------+--------------------+------------------------+
|LookupName|                   |                  |                    |Elevation Modifier      |
+----------+-------------------+------------------+--------------------+------------------------+

The depth of the seafloor at which a collection event ended

Usage
=====

Omit for terrestrial samples and aquatic samples where the collection
depth is not known.

Format
======

For dredges and trawls, Depth To is the depth at the point where the
collecting event ends. In earlier databases, this was referred to as
"off bottom".

Each of the columns in this group represents a specific unit: meters,
feet, and fathoms. When adding bottom depth, you only need to fill out
one of the three columns. The other two will be calculated automatically
by EMu. Original values display as black and calculated values as red in
the client.

If only one depth is provided, use that depth in both Depth From and
Depth To. Always provide the verbatim depth, including units, in Text
Bottom Depth.

The modifier field is used to indicate uncertainty in depth
measurements. Use "approx." to indicate uncertainty. The exact
uncertainty can be expressed in Text Bottom Depth.

--------------------------------------------------------------------------------

.. _ecollectionevents-depth-elev-depth-details-bottom-depth-determination:

**************************
Bottom Depth Determination
**************************

+----------+---------------------------+
|Field     |Value                      |
+==========+===========================+
|ItemPrompt|Bottom Depth Determination |
+----------+---------------------------+
|ColumnName|AquBottomDepthDetermination|
+----------+---------------------------+
|DataKind  |dkAtom                     |
+----------+---------------------------+
|DataType  |Text                       |
+----------+---------------------------+
|LookupName|Depth Determination        |
+----------+---------------------------+

The method by which the bottom depth was measured

Usage
=====

Omit if no appropriate data is available

--------------------------------------------------------------------------------

.. _ecollectionevents-depth-elev-depth-details-text-bottom-depth:

*****************
Text Bottom Depth
*****************

+----------+----------------------+
|Field     |Value                 |
+==========+======================+
|ItemPrompt|Verbatim Bottom Depth |
+----------+----------------------+
|ColumnName|AquVerbatimBottomDepth|
+----------+----------------------+
|DataKind  |dkAtom                |
+----------+----------------------+
|DataType  |Text                  |
+----------+----------------------+

A text string with the verbatim depth information, including units and
uncertainy, if any.

Usage
=====

Required if depth info is populated

Examples
========

* 1000-1200 m
* 72 fathoms
* 125.5 Â± 0.5 ft

--------------------------------------------------------------------------------

.. _ecollectionevents-depth-elev-depth-details-source-of-sample:

****************
Source Of Sample
****************

+----------+----------------------+
|Field     |Value                 |
+==========+======================+
|ItemPrompt|Source of Sample      |
+----------+----------------------+
|ColumnName|DepSourceOfSample     |
+----------+----------------------+
|DataKind  |dkAtom                |
+----------+----------------------+
|DataType  |Text                  |
+----------+----------------------+
|LookupName|Depth Source of Sample|
+----------+----------------------+

The part of the water column from which the specimen was collected. For
geological specimens, this should always be Bottom.

Usage
=====

Required when depth info is populated

Allowed Values
==============

* Bottom

--------------------------------------------------------------------------------

.. _ecollectionevents-depth-elev-elevation-relative-elevation-from:

**************
Elevation From
**************

+----------+-------------------+------------------+------------------------+
|Field     |TerElevationFromMet|TerElevationFromFt|TerElevationFromModifier|
+==========+===================+==================+========================+
|ItemPrompt|Elevation From     |(feet)            |Modifier                |
+----------+-------------------+------------------+------------------------+
|ColumnName|TerElevationFromMet|TerElevationFromFt|TerElevationFromModifier|
+----------+-------------------+------------------+------------------------+
|DataKind  |dkAtom             |dkAtom            |dkAtom                  |
+----------+-------------------+------------------+------------------------+
|DataType  |Float              |Float             |Text                    |
+----------+-------------------+------------------+------------------------+
|LookupName|                   |                  |Elevation Modifier      |
+----------+-------------------+------------------+------------------------+

The elevation at which a collection event began

Usage
=====

Omit if no appropriate data is available

Format
======

Each of the columns in this group represents a specific unit: meters and
feet. When adding an elevation, you only need to fill out one of column.
The other unit will be calculated automatically by EMu. Original values
display as black and calculated values as red in the client.

If only one elevation is provided, use that depth in both From and To.
Always provide the verbatim elevation, including units, in Text.

The modifier field is used to indicate uncertainty in elevation
measurements. Use "approx." to indicate uncertainty. The exact
uncertainty can be expressed in Text.

--------------------------------------------------------------------------------

.. _ecollectionevents-depth-elev-elevation-relative-elevation-to:

************
Elevation To
************

+----------+-----------------+----------------+----------------------+
|Field     |TerElevationToMet|TerElevationToFt|TerElevationToModifier|
+==========+=================+================+======================+
|ItemPrompt|Elevation To     |(feet)          |Modifier              |
+----------+-----------------+----------------+----------------------+
|ColumnName|TerElevationToMet|TerElevationToFt|TerElevationToModifier|
+----------+-----------------+----------------+----------------------+
|DataKind  |dkAtom           |dkAtom          |dkAtom                |
+----------+-----------------+----------------+----------------------+
|DataType  |Float            |Float           |Text                  |
+----------+-----------------+----------------+----------------------+
|LookupName|                 |                |Elevation Modifier    |
+----------+-----------------+----------------+----------------------+

The elevation at which a collection event ended

Usage
=====

Omit if no appropriate data is available

Format
======

Each of the columns in this group represents a specific unit: meters and
feet. When adding an elevation, you only need to fill out one of column.
The other unit will be calculated automatically by EMu. Original values
display as black and calculated values as red in the client.

If only one elevation is provided, use that depth in both From and To.
Always provide the verbatim elevation, including units, in Text.

The modifier field is used to indicate uncertainty in elevation
measurements. Use "approx." to indicate uncertainty. The exact
uncertainty can be expressed in Text.

--------------------------------------------------------------------------------

.. _ecollectionevents-depth-elev-elevation-relative-elevation-determination:

***********************
Elevation Determination
***********************

+----------+-------------------------+
|Field     |Value                    |
+==========+=========================+
|ItemPrompt|Elevation Determination  |
+----------+-------------------------+
|ColumnName|TerElevationDetermination|
+----------+-------------------------+
|DataKind  |dkAtom                   |
+----------+-------------------------+
|DataType  |Text                     |
+----------+-------------------------+
|LookupName|Elevation Determination  |
+----------+-------------------------+

The method by which the elevation was measured

Usage
=====

Omit if no appropriate data is available

--------------------------------------------------------------------------------

.. _ecollectionevents-depth-elev-elevation-relative-elevation-text:

**************
Elevation Text
**************

+----------+--------------------+
|Field     |Value               |
+==========+====================+
|ItemPrompt|Verbatim Elevation  |
+----------+--------------------+
|ColumnName|TerVerbatimElevation|
+----------+--------------------+
|DataKind  |dkAtom              |
+----------+--------------------+
|DataType  |Text                |
+----------+--------------------+

A text string with the verbatim elevation information, including units
and uncertainy, if any.

Usage
=====

Required if elevation info is populated
