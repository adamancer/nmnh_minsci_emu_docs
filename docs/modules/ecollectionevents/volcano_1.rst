###############################
ecollectionevents > Volcano (1)
###############################

This tab contains information about the volcano that produced a given
igneous rock, including eruption dates. Information recorded on this tab
should use the identifiers, names, and events defined by the `Global
Volcanism Program (GVP) <https://volcano.si.edu>`_ .

--------------------------------------------------------------------------------

.. _ecollectionevents-volcano-1-volcano-details-volcano-number:

**************
Volcano Number
**************

+------------+------------------+
| Field      | Value            |
+============+==================+
| ItemPrompt | Volcano          |
+------------+------------------+
| ColumnName | VolVolcanoNumber |
+------------+------------------+
| DataKind   | dkAtom           |
+------------+------------------+
| DataType   | Text             |
+------------+------------------+
| LookupName | Volcano Number   |
+------------+------------------+

A numeric identifier assigned to volcanoes active in the Holocene or
Pleistocene in the GVP database

Usage
=====

Required if volcano name is populated. For volcanoes older than the
Pleistocene, use "--".

Format
======

A six-digit number corresponding to a volcano in the GVP database. Names
and numbers are checked for consistency annually by the data manager.

--------------------------------------------------------------------------------

.. _ecollectionevents-volcano-1-volcano-details-volcano-name:

************
Volcano Name
************

+------------+----------------+
| Field      | Value          |
+============+================+
| ColumnName | VolVolcanoName |
+------------+----------------+
| DataKind   | dkAtom         |
+------------+----------------+
| DataType   | Text           |
+------------+----------------+

The name of a volcano from the GVP database that produced the sampled
material

Usage
=====

Required if volcano number is populated.

Format
======

Name should exactly match the format used on the GVP website. If the
collection materials use a synonym, record the preferred name instead.

The Holocene and Pleistocene volcano lists provded by GVP use an
inverted format that omits diacritics that appear on the website. For
example, "Île de la Possession" is rendered as "Possession, Ile de la".
Use "Île de la Possession". Refer to the GVP website to verify
diacritics.

GVP omits "Mount"/"Mt" from volcano names, so use "Rainier" (not "Mt.
Rainier") and "St. Helens" (not "Mt. St. Helens"). This practice is not
consistent across languages, however. For example, Japanese volcano
names in GVP include *-san* and *-yama* suffixes that serve a similar
purpose.

GVP includes large features, like volcanic fields and calderas, that may
include named vents that are themselves referred to as volcanoes in
collection materials. Parícutin, for example, is classified by GVP as a
subfeature of Michoacán-Guanajuato. Subfeatures should be recorded in
the Subfeature field.

Examples
========

* Arenal
* Michoacán-Guanajuato
* St. Helens

--------------------------------------------------------------------------------

.. _ecollectionevents-volcano-1-volcano-details-subfeature:

**********
Subfeature
**********

+------------+---------------+
| Field      | Value         |
+============+===============+
| ItemPrompt | Subfeature:   |
+------------+---------------+
| ColumnName | VolSubfeature |
+------------+---------------+
| DataKind   | dkAtom        |
+------------+---------------+
| DataType   | Text          |
+------------+---------------+

The name of a cone, vent, or other volcanic feature from the GVP
database that produced the sampled material

Usage
=====

Omit if no appropriate data is available

Format
======

Name should exactly match a volcanic feature from the GVP database. Note
that some subfeatures defined by GVP are well-known stratovolcanoes in
their own right. For example, Sakurajima is classified as a feature of
the Aira caldera.

Examples
========

* Parícutin
* Sakurajima

--------------------------------------------------------------------------------

.. _ecollectionevents-volcano-1-volcano-details-holocene:

********
Holocene
********

+------------+-------------+
| Field      | Value       |
+============+=============+
| ItemPrompt | Holocene    |
+------------+-------------+
| ColumnName | VolHolocene |
+------------+-------------+
| DataKind   | dkAtom      |
+------------+-------------+
| DataType   | Text        |
+------------+-------------+

Whether a volcano has erupted in the Holocene

Usage
=====

Populated from GVP at least annually by data manager for records with
volcano numbers

Allowed Values
==============

* Yes
* No
* Unknown

--------------------------------------------------------------------------------

.. _ecollectionevents-volcano-1-volcano-details-tectonic-setting:

****************
Tectonic Setting
****************

+------------+------------------------+
| Field      | Value                  |
+============+========================+
| ItemPrompt | Tectonic Setting:      |
+------------+------------------------+
| ColumnName | VolTectonicSetting_tab |
+------------+------------------------+
| DataKind   | dkTable                |
+------------+------------------------+
| DataType   | Text                   |
+------------+------------------------+
| LookupName | Volcano Tectonic       |
|            | Setting                |
+------------+------------------------+

The tectonic environment in which a volcano formed, including crustal
thickness, according to GVP

Usage
=====

Populated from GVP at least annually by data manager for records with
volcano numbers

Format
======

Usually includes two values, one for the setting and one for the crustal
thickness.

Allowed Values
==============

* Oceanic crust (<15 km)
* Intermedidate crust (15-25 km)
* Continental crust (>25 km)
* Crustal thickness unknown
* Intraplate
* Rift zone
* Subduction zone
* Unknown

--------------------------------------------------------------------------------

.. _ecollectionevents-volcano-1-eruption-details-eruption-id:

***********
Eruption ID
***********

+------------+---------------+
| Field      | Value         |
+============+===============+
| ItemPrompt | Eruption ID:  |
+------------+---------------+
| ColumnName | VolEruptionID |
+------------+---------------+
| DataKind   | dkAtom        |
+------------+---------------+
| DataType   | Text          |
+------------+---------------+

A numeric identifier assigned to an eruption in the GVP database

Usage
=====

Omit if no appropriate data is available

Format
======

A five-digit number corresponding to an eruption in the GVP database

--------------------------------------------------------------------------------

.. _ecollectionevents-volcano-1-eruption-details-eruption-date-from:

******************
Eruption Date From
******************

+------------+---------------------+-------------------+
| Field      | VolEruptionDateFrom | VolEruptionDateTo |
+============+=====================+===================+
| ItemPrompt | Eruption Date From: | Eruption Date To: |
+------------+---------------------+-------------------+
| ColumnName | VolEruptionDateFrom | VolEruptionDateTo |
+------------+---------------------+-------------------+
| DataKind   | dkAtom              | dkAtom            |
+------------+---------------------+-------------------+
| DataType   | Date                | Date              |
+------------+---------------------+-------------------+

The start and end dates of the volcanic eruption as recorded by GVP

Usage
=====

Populated from GVP at least annually by data manager for records with
eruption IDs

Format
======

--------------------------------------------------------------------------------

.. _ecollectionevents-volcano-1-eruption-details-eruption-notes:

**************
Eruption Notes
**************

+------------+------------------+
| Field      | Value            |
+============+==================+
| ItemPrompt | Eruption Notes:  |
+------------+------------------+
| ColumnName | VolEruptionNotes |
+------------+------------------+
| DataKind   | dkAtom           |
+------------+------------------+
| DataType   | Text             |
+------------+------------------+

The verbatim eruption date or date range provided by the collector

Usage
=====

Required if the eruption ID or date fields are populated

Format
======

Use a structured note format for this field. Allowed keys include
"Verbatim Eruption Date", "Eruption Kind", and "Eruption Details".
