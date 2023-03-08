###########################
Guidelines for stratigraphy
###########################

This document contains guidance for managing stratigraphy data in EMu.
This workflow was originally developed for a data cleanup project in
2021.

Some goals of this workflow include:

* Standardizing names of stratigraphic units to improve recall
* Identifying and moving data that is in the wrong field
* Linking units to Macrostrat records or other authorities

**************************
Stratigraphy data standard
**************************

Stratigraphy data is stored in the Stratigraphy grid in the Catalog >
Stratigraphy tab. This standard defines how stratigraphic data should be
entered in those fields.

Authorities
===========

The best source for verifying stratigraphic names is probably
`Macrostrat <https://macrostrat.org/>`_, which is a curated database of
units that includes information from both the literature and major
geological surveys (primarily the USGS). Macrostrat does a nice job
depicting relationships between units and alternative names that
describe the same unit. It also makes data about stratigraphic units
available through an API.

Other good resources are websites for country geological surveys, like
the `U.S. Geologic Names Lexicon
<https://ngmdb.usgs.gov/Geolex/search>`_. For many units, Macrostrat has
already compiled data from these surveys, but sometimes the original
records have useful information that was omitted.

Ranks
=====

Stratigraphic units are arranged in a hierarchy. From least to most
specific, the typical ranks and abbreviations are:

* Supergroup (SGp)
* Group (Gp)
* Subgroup (SubGp)
* Formation (Fm)
* Member (Mbr)
* Bed (Bd)

There may be others. People like their subdivisions.

You will also see the term “series” in some places. This is an informal
rank but generally refers to either a formation or group. You can, for
example, safely standardize “Honolulu Volcanic Series” to “Honolulu
Volcanic Fm” since the latter is the form used by Macrostrat.

EMu includes fields for Group, Formation, and Member. Unit names should
always go in the field matching their rank and should include the
abbreviated form of the rank:

* Glen Canyon Group → Group = Glen Canyon Gp
* Navajo Formation → Formation = Navajo Fm

**Populating higher ranks:** Macrostrat and other sources may include
higher stratigraphic ranks that are missing from EMu. If you are able to
confidently identify a missing parent group or formation, you can add
the parent to EMu in the appropriate field. For example, Macrostrat
notes that the Navajo Formation is part of the Glen Canyon Group. That
group name can be added to any records that do not already include it.
If there’s any ambiguity to the match, add a note.

**Inconsistent higher ranks:** If an authority specifies a different
parent than is recorded in EMu, note that the hierarchy is inconcistent
with that authority.

**Multiple ranks in the authority record:** Sometimes the authority
record will include alternate names of different rank (for example,
https://macrostrat.org/sift/#/strat_name_concept/6602). For Macrostrat
records, defer to the name/rank with the higher number of citations. For
other sources, note the multiple ranks.

Supergroups, subgroups, and beds
================================

Some stratigraphic ranks do not have dedicated fields in EMu, Darwin
Core, or both. The general guidance for these ranks is to include them
only if they appear in the original EMu record. Here are the possible
cases:

* **Supergroup but no group:** Group = Supergroup SGp
* **Supergroup and group:** Group = Supergroup SGp > Group Gp
* **Group and subgroup:** Group = Group Gp > Subgroup SubGp
* **Subgroup but not group:** Group = Subgroup SubGp
* **Member and bed:** Member = Member Mbr > Bed Bd
* **Bed but no formation:** Member = Bed Bd

Only populate missing values for these ranks if there is no data in the
relevant field.

Lithologies
===========

Unit names sometimes include the name of the primary rock name that
makes up the unit. Some rock names will be familiar (limestone), some
less so (tonalite). Sometimes rock names are abbreviated. Common
abbreviations include:

* Ls: Limestone
* Ss: Sandstone or siltstone

Rock names are used inconsistently in stratigraphic units, and the same
unit may appear in the literature with or without one. For units that
grade between lithologies (for example, from sandstone to siltstone),
the rock name may add a bit of extra info that you’d lose if you omitted
it, so the best practice is to defer to the data in EMu or the original
documentation. If those records includes the rock name, keep it when
standardizing the name:

* Navajo Sandstone → Navajo Sandstone Fm

Otherwise leave it out:

* Navajo Formation → Navajo Fm

You can include the rock name even if it isn’t officially listed by
Macrostrat as an alternative name. Note also that rank (“Fm” in this
case) is included in either case.

The diversity of rock names is large and the abbreviations are less than
perfectly clear, so for clarity you should always use the full rock name
if you do decide to include it:

* Navajo Ss → Navajo Sandstone Fm

Modifiers
=========

Unit names in EMu may be modified to describe where in the unit a given
sample was collected. Common modifiers include:

* Top
* Upper
* Middle
* Lower
* Bottom

To maintain sorting in the lookup list, include modifiers as a trailing
parenthetical:

* Upper Navajo Formation → Navajo Fm (Upper)

Ranges
======

Some records include stratigraphic ranges. For ranges, each unit should
get its own line in the Stratigraphy grid, with the older unit listed
first.

****************
Cleanup workflow
****************

Use the following steps to clean stratigraphic data:

#. Verify the stratigraphic data
#. Match stratigraphic name to an authority
#. Update the EMu record

1. Verify the stratigraphic data
================================

The Stratigraphy and Geologic Setting fields contain similar data, and
as a result, a name will sometimes end up in the wrong field.

* Stratigraphy should only be used for stratigraphic units (groups,
  formations, members, etc.), that is, names that refer to horizons in
  the rock record.
* Geologic setting should only be used for geologic place names
  (batholiths, provinces, etc.) These are geographic names referring to
  geologic features.

So the basic difference is that stratigraphy refers to the rock record,
whereas setting refers to a point or area on a map.

Address problem data as follows:

* If data in the Stratigraphy grid is not a stratigraphic unit, figure
  out what kind of feature it refers to and move the data to the proper
  field. This will probably involve updating the Collections Event
  record. Be sure to search for the unit name in Macrostrat before
  making this determination.
* If data in Geologic Setting is a stratigraphic unit and the
  Stratigraphy grid is empty, move the data in setting to the
  appropriate field in Catalog.
* Stratigraphic data is often included in both the Stratigraphy grid
  and Geologic Setting. If both fields contain the same information,
  determine which one should be use and clear the other.
* If the Stratigraphy grid and Geologic Setting contain different
  stratigraphy information, use primary collection documentation to
  sort out which value is correct. Make sure to note the incorrect data
  in a note.

Terms that are likely to be units
---------------------------------

* Amphibolite
* Andesite
* Argillite
* Basalt
* Claystone
* Conglomerate
* Dacite
* Eclogite
* Gabbro
* Gneiss
* Granite
* Granulite
* Greenstone
* Greywacke
* Limestone
* Marl
* Marble
* Meta-
* Mudstone
* Porphyry
* Sandstone
* Siltstone
* Tonalite
* Trondjemite
* Tuff
* Welded Tuff
* Most other rock types, there are lots

Terms that are likely to be settings
------------------------------------

* Alnoite
* Batholith
* Diatreme
* Kimberlite
* Pipe
* Province
* Volcano

**Note:** Kimberlite, lamproite, alnoite, and a few others are rock
types, but names using these terms usually refer to a pipe (basically a
special type of volcano) where material was erupted. Macrostrat
sometimes include such pipes as units, but I think they are closer to
settings.

2. Match stratigraphic name to a Macrostrat record
==================================================

Stratigraphic names are not unique. When researching a unit, make sure
to verify that all metadata (notably geography and higher stratigraphy)
for that unit matches the record in EMu.

If you can match the stratigraphy info to an authority, record the link
in a note. Macrostrat is the preferred authority, but if no record
exists there, you can link to another resource as long as the link
resolves to a specific record for the current unit.

3. Update the EMu record
========================

#. Ensure names are in correct fields
#. Standardize names to preferred format (defined below)
#. Fill in higher stratigraphic ranks, if possilbe

********
Examples
********

Real stratigraphic data can be tricky to parse and clean. The examples
below illustrate some some common issues you're likely to run into when
working with this kind of data.

`NMNH PET 102574 <http://n2t.net/ark:/65665/37f420e08-ce86-4e7b-8c51-26400a1b8b0e>`_
====================================================================================

+-----------+----------+-----------------------------------------------------------+
| Field     | Original | Recommended                                               |
+===========+==========+===========================================================+
| Group     | Dakota   |                                                           |
|           | Ss.      |                                                           |
+-----------+----------+-----------------------------------------------------------+
| Formation |          | `Dakota Sandstone Fm                                      |
|           |          | <https://macrostrat.org/sift/#/strat_name_concept/7833>`_ |
+-----------+----------+-----------------------------------------------------------+
| Member    |          |                                                           |
+-----------+----------+-----------------------------------------------------------+

The unit is originally given as Dakota Ss. To get the final value, we
expand the rock type and append formation to the original value,
yielding Dakota Sandstone Fm. The tricky part with this one is that the
lithology and rank of this unit vary over time, space, and by author,
and there is no clear best option for a canonical name or rank. That’s
fine, really–one of the reasons we use an authority in the first place
is to help sort out complex historical usages–but since EMu uses a
hierarchy for stratigraphy we do ultimately have to pick a rank for this
unit, ideally one that can be used consistently across the database (or,
even better, across the discipline).

Macrostrat lists four names under Dakota:

* Dakota Fm
* Dakota Gp
* Dakota Sandstone Fm
* Dakota Conglomerate Fm

The `USGS Geolex entry
<https://ngmdb.usgs.gov/Geolex/Units/Dakota_7833.html>`_ gives the same
four names and includes a list of formations and members that are
associated with the Dakota unit in the literature.

When selecting a name and rank, consider:

* **Does the database include children of these units? What are the
  ranks of those children?** If the children are all formations, it
  may make sense to treat the parent unit as a group. If they’re all
  members, formation may make more sense.
* **Do database entries for the name commonly specify a rock type?**
  Groups are typically diverse and don’t include rock types, so that
  may mean that formation is a better home for this data.

There’s not really a wrong answer, and it’s worth noting that Geolex and
Macrostrat often do not specify rank on the titles of their unit pages,
in part because the rank question cannot always be resolved. The main
thing to aim for is consistency.

`NMNH PET 117710-42 <http://n2t.net/ark:/65665/3830b6202-e635-42f6-b842-48f37ced35ec>`_
=======================================================================================

+-----------+-----------+----------------------------------------------------+
| Field     | Original  | Recommended                                        |
+===========+===========+====================================================+
| Group     | Beaver    | Beaver Bay Gp                                      |
|           | Bay Group |                                                    |
+-----------+-----------+----------------------------------------------------+
| Formation | Stepovak  | `Stepovak Fm                                       |
|           | Formation | <https://macrostrat.org/sift/#/strat_name/75176>`_ |
|           | - Boulder | \> Boulder Bay-Fox Bay Section                     |
|           | Bay-Fox   |                                                    |
|           | Bay       |                                                    |
|           | Section   |                                                    |
+-----------+-----------+----------------------------------------------------+
| Member    |           |                                                    |
+-----------+-----------+----------------------------------------------------+

A section is a specific exposure of a unit. Stratigraphic units can be
horizontally extensive and are not necessarily homogenous, so it can be
useful to note where in the unit a rock was sampled from. Section names
are often project-specific and are unlikely to appear in central
authorities. If you find a section name, append it to the most specific
unit name, e.g. “Stepovak Fm > Boulder Bay-Fox Bay Section”

`NMNH PET 117247-270 <http://n2t.net/ark:/65665/32003f073-052d-4537-b764-fadf3b9f0b09>`_
========================================================================================

+-----------+-----------+-----------------------------------------------------------+
| Field     | Original  | Recommended                                               |
+===========+===========+===========================================================+
| Group     | Colorado  | `Colorado Gp                                              |
|           | Group     | <https://macrostrat.org/sift/#/strat_name_concept/7668>`_ |
+-----------+-----------+-----------------------------------------------------------+
| Formation | Basal     | `Fall River Fm                                            |
|           | Fall      | <https://macrostrat.org/sift/#/strat_name/70582>`_        |
|           | River     | (Basal)                                                   |
|           | Formation |                                                           |
+-----------+-----------+-----------------------------------------------------------+
| Member    |           |                                                           |
+-----------+-----------+-----------------------------------------------------------+

This is an example of multiple, apparently related units being assigned
different ranks over time. Colorado Group is by far the most common
variant for the Colorado Group/Shale/Formation in Macrostrat, while the
Fall River unit is variously listed as a formation or member. The
closest match to the EMu records is actually Colorado Fm > Fall River
Mbr, but given the clear preference for Colorado Group, I’d map this as
Colorado Gp > Fall River Fm (Basal) instead (with basal being a modified
of the unit name).

`NMNH PET 117230-130 <http://n2t.net/ark:/65665/3fcccd942-6873-4f93-927c-2ed0d08773ef>`_
========================================================================================

+-----------+----------+-----------------------------------------------------------+
| Field     | Original | Recommended                                               |
+===========+==========+===========================================================+
| Group     | Keres    | Keres Gp                                                  |
+-----------+----------+-----------------------------------------------------------+
| Formation | Peralta  | `Bearhead Fm                                              |
|           | Tuff     | <https://macrostrat.org/sift/#/strat_name_concept/6742>`_ |
+-----------+----------+-----------------------------------------------------------+
| Member    |          | `Peralta Tuff Mbr                                         |
|           |          | <https://macrostrat.org/sift/#/strat_name_concept/9587>`_ |
+-----------+----------+-----------------------------------------------------------+

This is an example of a unit being assigned the wrong rank in EMu.
According to Macrostrat, the Peralta Tuff is part of the Bearhead
Formation, which is itself part of the Keres Group. So the hierarchy in
EMu is consistent with Macrostrat–the Peralta Tuff is a subunit of the
Keres Group–but the Peralta Tuff is in the wrong place. The main thing
to look for in cases like this is consistency—are the parent-child
relationships generally correct, even if there are gaps?

`NMNH PET 117227-210 <http://n2t.net/ark:/65665/3514ebc69-cd8c-4592-b300-79111b849af0>`_
========================================================================================

+-----------+-----------+-----------------------------------------------------------+
| Field     | Original  | Recommended                                               |
+===========+===========+===========================================================+
| Group     | Polvadera | `Santa Fe Gp                                              |
|           |           | <https://macrostrat.org/sift/#/strat_name_concept/9963>`_ |
+-----------+-----------+-----------------------------------------------------------+
| Formation | Puye      | `Puye Fm                                                  |
|           |           | <https://macrostrat.org/sift/#/strat_name/72949>`_        |
+-----------+-----------+-----------------------------------------------------------+
| Member    |           |                                                           |
+-----------+-----------+-----------------------------------------------------------+

Samples assigned to Polvadera > Puye are mostly volcanic. The Polvadera
Group is a volcanic unit that occurs in the same general area as the
Puye Formation, but the two units do not appear to be related. The USGS
instead describes the Puye as a conglomerate or gravel consisting of a
mix of sedimentary and igneous rocks that is part of the Sante Fe Group.
At first glance, that description does not seem like a good match for
the rocks in the collection. However, some 1970s publications associated
with the Puye (viewable using the `Significant Publications
<https://ngmdb.usgs.gov/Geolex/UnitRefs/PuyeRefs_9942.html>`_ link on
the Puye page on Geolex) reference one or more pumice layers within that
formation. These seem like the most likely source for the NMNH rocks,
and that is the interpretation we went with here.

`NMNH PET 117795-7 <http://n2t.net/ark:/65665/38acf86df-d51a-40a1-a096-0449c8b35187>`_
======================================================================================

+-----------+-----------+---------------------------------------------------+
| Field     | Original  | Recommended                                       |
+===========+===========+===================================================+
| Group     |           |                                                   |
+-----------+-----------+---------------------------------------------------+
| Formation | Kalamazoo | `Kalamazoo Volcanics Fm                           |
|           | Volcanics | <https://macrostrat.org/sift/#/strat_name/4469>`_ |
+-----------+-----------+---------------------------------------------------+
| Member    | 1         | 1                                                 |
+-----------+-----------+---------------------------------------------------+

Numeric members are likely to be project-specific and are unlikely to
appear in authorities but might show up in associated publications. As
here, we leave them as is. Some numbered units, like zones, might
represent biostratigraphic layers.

`NMNH PET 117806-946 <http://n2t.net/ark:/65665/38e66b201-c745-4251-abbb-611bd78934ab>`_
========================================================================================

+-----------+----------+---------------------------------------------------+
| Field     | Original | Recommended                                       |
+===========+==========+===================================================+
| Group     |          |                                                   |
+-----------+----------+---------------------------------------------------+
| Formation | Paxton   | `Paxton Schist Fm                                 |
|           | Schist   | <https://macrostrat.org/sift/#/strat_name/1530>`_ |
|           |          | (Lower)                                           |
+-----------+----------+---------------------------------------------------+
| Member    | Lower    |                                                   |
+-----------+----------+---------------------------------------------------+

This example demonstrates two decisions we made when mapping units to
authorities:

* **What do we do with unit names that include rock types in EMu but
  not in the authority?** EMu gives the formation here as Paxton Schist,
  but Macrostrat uses Paxton Fm. We’ve chosen to keep the rock name
  and append formation. Here is the reasoning behind this decision:

   #. For some units, the variant including the rock type is by far the
      preferred way to refer to the unit. Removing the rock type hampers
      discoverability. (ex. Bishop Tuff)
   #. Units, especially groups and formations, may include multiple rock
      types, including igneous layers. Keeping the rock type may provide
      additional context when the sample is different from the parent
      rock (as in NMNH PET 117227-210 above).
   #. Including a link to an authority should resolve any ambiguity from
      using a slightly different name, so the exact name is not
      important if the link is provided and active.

* **What do we do with modifiers that appear in separate fields?** The
  original entry for this sample puts lower in a separate field. We
  reserve fields for named (or rarely numbered) units, so we appended
  lower as a parenthetical modifier to the formation name instead.
  Common modifiers include basal, lower, middle, upper, and top.