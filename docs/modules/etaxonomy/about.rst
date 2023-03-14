Taxonomy Data Standard
======================

Draft set of standards for Mineral Sciences taxonomy records.

About
-----

The taxonomy module stores information about the classifications
assigned to individual rock and meteorite specimens. Classifications are
organized into an arbitrarily deep hierarchy (i.e., a given
classification can have as many ancestors as needed, as opposed to
Linnean classifications for biology where the number of available ranks
is limited).

The hierarchy used by Mineral Sciences is ad hoc and has been compiled
from multiple sources, including but not limited to the following:

* British Geological Survey Rock Classification Scheme
* Dana classification scheme
* Igneous Rocks: A Classification and Glossary of Terms
* IMS mineral list (for current mineral names)
* Mindat (for varieties, synonyms, and archaic mineral names)

The Mineral Sciences taxonomy module includes records for a large number
of classifications beyond rocks, minerals, and meteorites, including
fossils, chemical compounds lacking formal names, and cultural objects.

A reasonable up-to-date version the complete taxonomic hierarchy can be
browsed at
http://adamancer.pythonanywhere.com/classification/id/10591819.

Standard
--------

### Meets

A standard taxonomy record should contain the following fields:

* Parent
* Other > Other Rank
* Other > Other Value
* Scientific Name > Name
* Currently Accepted Name > Currently Accepted?
* Currently Accepted Name > Current Name

### Exceeds

To exceed standard, a taxonomy record must contain all the information
required above and link to an authoritative record for the
classification. Authoritative sources include the sources listed under
About above. Not all valid classifications can meet this criteria for
reasons discussed below.

Field definitions
-----------------

* Parent: a link to the next broadest classification
* Other Rank: the type of material. This list is in flux, but the most
  common values include:

    * Rock
    * Mineral
    * Synonym
    * Variety

* Other Value: the specific name of this classification
* Name: a human-readable name, like you'd put on a label
* Current name: a link to the currently valid name

Examples
--------

Attachments to other records are in [brackets].

### Sapphire

* Parent: [Corundum]
* Other rank: Variety
* Other value: Sapphire
* Name: Corundum (var. sapphire)
* Current name: [Corundum (var. sapphire)]

### Idocrase

*For synonyms, the parent is the same as the current name.*

* Parent: [Vesuvianite]
* Other rank: Synonym
* Other value: Idocrase
* Name: Idocrase
* Current name: [Vesuvianite]

### Biotite granite

*Rock names originally added to Paradox or SELGEM may be given as
Primary, Modifier (e.g., "Granite, Biotite" for this example). New
records should use the human-readable name instead, but the older
records do not need to be corrected.*

* Parent: [Granite]
* Other rank: Rock
* Other value: Biotite granite
* Name: Biotite granite
* Current name: [Biotite granite]

Division-specific guidelines
----------------------------

### Mineralogy

* Mineral varieties are expressed as *Mineral (var. variety)* in the
  scientific name field. This formulation is based on exhibit labels
  in GGM and works well for well for major varieties (for example,
  sapphire and emerald). It also makes it easier to perform simple
  searches for minerals (for example, a search for corundum would
  return sapphires and rubies without having to populate a synonym
  name in the identification grid). The syntax adopted here does
  present a few issues:

    * Microcrystalline forms of quartz (chalcedony, agate, etc.) do not
      play well with this scheme
    * Varieties that are not specific to a single mineral (for example,
      moonstone) must be explicitly defined for each mineral (for
      example, orthoclase (var. moonstone), albite (var.
      moonstone), etc.)
    * Varieties that contain the mineral name (e.g., titanian augite)
      should not use the *Mineral (var. variety)* syntax

### Petrology

The list of accepted igneous rock names contains around 400-500 entries,
but that list is not exhaustive. Using major mineral phases as modifiers
is a well-established practice in the field. As a result, the number of
valid rock names is essentially infinite, which poses a significant
problem for data management and the construction of a useful taxonomic
hierarchy.

Classification of many rock types is challenging because many rocks can
be placed at multiple locations within a hierarchy. There is no good
solution for this issue without adopting a scheme that allows each
record to have multiple parents.

Updating the parent
-------------------

The taxonomy module is badly over-engineered, and it is not possible to
assign a new parent to an existing record directly through the GUI. The
easiest workaround makes use of the search-replace feature:

* Open the Replace window by clicking Edit > Replace
* Delete any existing rows in the Replace window
* Click New in the bottom left corner to bring up the Substitution
  window and fill out the form as follows:

    * Set field to Parent or RanParentRef
    * Set text to find to .*
    * Set replace with using the green plus
    * Check the regular expression checkbox under Options
    * Click OK

* In the Replace window, click Replace to update the parent of the
  current record

You can modify an existing substitution using the Properties button near
the top of the Replace window. Tread carefully. Here are some common
gotchas doing replacements in EMu:

* All defined substitutions run when you click Replace or Replace All
* When clicking Replace, the substitution will run on any *highlighted*
  records even if the current record is not highlighted. If no records
  are highlighted, the substitution will only affect the current
  record.

This workaround may be patched out of future versions EMu.
