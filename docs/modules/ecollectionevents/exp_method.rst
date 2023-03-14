##############################
ecollectionevents > Exp/Method
##############################

This tab includes information about expeditions that produced samples in
the collection. Expeditions include both terrestrial and marine
programs. For the latter, this tab also includes fields for identifying
vessels and cruises.

--------------------------------------------------------------------------------

.. _ecollectionevents-exp-method-expedition-details-expedition-name:

***************
Expedition Name
***************

+----------+-----------------+
|Field     |Value            |
+==========+=================+
|ItemPrompt|Expedition Name  |
+----------+-----------------+
|ColumnName|ExpExpeditionName|
+----------+-----------------+
|DataKind  |dkAtom           |
+----------+-----------------+
|DataType  |Text             |
+----------+-----------------+
|LookupName|Expedition Name  |
+----------+-----------------+

The name of the expedition or field program during which a collecting
event took place. Names are typically assigned by the sponsor of an
expedition and should use their exact format when possible.

For cruises that are not part of a larger expedition, it can be useful
to provide a long-form cruise identifier in this field. For example, leg
2 of cruise ABCD of the Enterprise can be entered as "Enterprise Cruise
ABCD (Leg 2)". This allows the cataloger to include a more readable
version of the cruise identifier.

Usage
=====

Omit if no appropriate data is available

Examples
========

* 40th Parallel Expedition
* CERES Expedition (CERE)

--------------------------------------------------------------------------------

.. _ecollectionevents-exp-method-expedition-details-vessel-name:

***********
Vessel Name
***********

+----------+-------------+
|Field     |Value        |
+==========+=============+
|ItemPrompt|Vessel Name  |
+----------+-------------+
|ColumnName|AquVesselName|
+----------+-------------+
|DataKind  |dkAtom       |
+----------+-------------+
|DataType  |Text         |
+----------+-------------+
|LookupName|Vessel Name  |
+----------+-------------+

The name of the ship from which a sample was collected.

Usage
=====

Omit if no appropriate data is available

Format
======

If a ship-supported submersible (like Alvin) was used, include both the
ship and submersible, separated by a semicolon ("Atlantis II; Alvin").
Omit the prefix "R/V" when entering a ship name in EMu.

Examples
========

* Atlantis II
* James B. Gilliss
* Thomas Washington

--------------------------------------------------------------------------------

.. _ecollectionevents-exp-method-expedition-details-cruise-number:

*************
Cruise Number
*************

+----------+---------------+
|Field     |Value          |
+==========+===============+
|ItemPrompt|Cruise Number  |
+----------+---------------+
|ColumnName|AquCruiseNumber|
+----------+---------------+
|DataKind  |dkAtom         |
+----------+---------------+
|DataType  |Text           |
+----------+---------------+

The identifier assigned by the organization that operates a vessel to a
research cruise, that is, a continuous, port-to-port voyage conducted to
make observations or collect specimens. The terms "cruise" and "leg" are
interchangeable for the purposes of this field.

Usage
=====

Omit if no appropriate data is available

Format
======

Typically, the identifier is either a number or an alphanumeric code.
Cruise number formats vary widely between or even within organizations,
with different abbreviations, delimiters, or zero-padding conventions
being used in different documents. There are no hard rules for
formatting a cruise number, but a good practice is to search for a
vessel name to see how cruise numbers for that vessel have been recorded
previously.

Cruise numbers should include the leg if known, and legs should not be
recorded elsewhere (for example, in notes). Many organizations already
incorporate the leg into their cruise identifiers, but if not, it is
acceptable to append the leg to the cruise number. For example, leg 2 of
cruise ABCD can be entered as "ABCD-2".

--------------------------------------------------------------------------------

.. _ecollectionevents-exp-method-expedition-details-start-completion-date:

*********************
Start/Completion Date
*********************

+----------+------------+-----------------+
|Field     |ExpStartDate|ExpCompletionDate|
+==========+============+=================+
|ItemPrompt|Start Date  |Completion Date  |
+----------+------------+-----------------+
|ColumnName|ExpStartDate|ExpCompletionDate|
+----------+------------+-----------------+
|DataKind  |dkAtom      |dkAtom           |
+----------+------------+-----------------+
|DataType  |Date        |Date             |
+----------+------------+-----------------+

The start and end dates for an expedition or cruise

Usage
=====

Omit if no appropriate data is available

Format
======

EMu depicts dates using the following formats:

* Year, month, and day: 1 Jan 1970
* Year and month: Jan 1970
* Year: 1970


It accepts a variety of formats in addition to the display formats
above, including but not limited to:
* January 1, 1970
* Jan 1, 1970
* 1970-01-01
* 1970-01
* 0101970


Use the most specific date format possible.

If only a single date is available, include that date in both the start
and completion date fields. For example, if a cruise took place in Jan
1970 but the exact start and end dates are not known, enter "Jan 1970"
in both fields. If a cruise took place in 1970 and the exact dates are
not known, enter "1970" in both fields.

--------------------------------------------------------------------------------

.. _ecollectionevents-exp-method-expedition-details-project-number:

**************
Project Number
**************

+----------+----------------+
|Field     |Value           |
+==========+================+
|ItemPrompt|Project Number  |
+----------+----------------+
|ColumnName|ExpProjectNumber|
+----------+----------------+
|DataKind  |dkAtom          |
+----------+----------------+
|DataType  |Text            |
+----------+----------------+

Not used

--------------------------------------------------------------------------------

.. _ecollectionevents-exp-method-collection-method-collection-method:

*****************
Collection Method
*****************

+----------+-------------------+
|Field     |Value              |
+==========+===================+
|ItemPrompt|Collection Method  |
+----------+-------------------+
|ColumnName|ColCollectionMethod|
+----------+-------------------+
|DataKind  |dkAtom             |
+----------+-------------------+
|DataType  |Text               |
+----------+-------------------+
|LookupName|Collection Method  |
+----------+-------------------+

The device used to collect a specimen

Usage
=====

Required for marine specimens and terrestrial drill cores. Omit
otherwise. Specimens collected during routine field work do not need to
indicate a collection method.

Format
======

The format of this field is under review. Historically, we have only
captured three collection methods: core (sometimes given as drill core),
dredge, and submersible. NOAA's IMLGS includes a more detailed
vocabulary that may be worth a look.

Examples
========

* Core
* Dredge
* Submersible (HOV)
* Submersible (ROV)

--------------------------------------------------------------------------------

.. _ecollectionevents-exp-method-total-surface-area-area:

****
Area
****

+----------+------------------------+
|Field     |Value                   |
+==========+========================+
|ItemPrompt|Total Surface Area Value|
+----------+------------------------+
|ColumnName|MetTotalSurfaceAreaValue|
+----------+------------------------+
|DataKind  |dkAtom                  |
+----------+------------------------+
|DataType  |Float                   |
+----------+------------------------+

Not used

--------------------------------------------------------------------------------

.. _ecollectionevents-exp-method-total-surface-area-unit:

****
Unit
****

+----------+-----------------------+
|Field     |Value                  |
+==========+=======================+
|ItemPrompt|Total Surface Area Unit|
+----------+-----------------------+
|ColumnName|MetTotalSurfaceAreaUnit|
+----------+-----------------------+
|DataKind  |dkAtom                 |
+----------+-----------------------+
|DataType  |Text                   |
+----------+-----------------------+
|LookupName|Total Surface Area Unit|
+----------+-----------------------+

Not used
