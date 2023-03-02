################################
ecollectionevents > Locality (1)
################################

This tab includes the political and marine geography of a collection
locality, along with fields for classifying the collection event.
Definitions below are adapted from the GeoNames Feature Codes list.

**Known issues:**

- Usage of Site Details is inconsistent. It has been used variously to
  try to distinguish generic localities from localities with detailed
  collection info; to try to mark records as canonical for a given
  locality (for example, by referencing the corresponding GeoNames
  record); and to idenitfy stations/dredges associatd with a specific
  expedition.
- It's difficult to reliably distinguish marine and terrestrial
  localities.
- Administrative divisions that do not map neatly to
  country/state/county scheme have been entered inconsistently. Many
  countries use deeper schemes, so it's not always clear how to fit all
  the information in.

--------------------------------------------------------------------------------

.. _ecollectionevents-locality-1-site-details-record-classification:

*********************
Record Classification
*********************

========== =======================================
Field      Value                                  
========== =======================================
ItemPrompt Record Classification                  
ColumnName LocRecordClassification                
DataKind   dkAtom                                 
DataType   Text                                   
LookupName Collection Events Record Classification
========== =======================================



Usage
=====

Under evaluation

--------------------------------------------------------------------------------

.. _ecollectionevents-locality-1-site-details-field-sample-numbers:

********************
Field/Sample Numbers
********************

========== =======================
Field      Value                  
========== =======================
ItemPrompt Site Visit Numbers     
ColumnName ColSiteVisitNumbers_tab
DataKind   dkTable                
DataType   Text                   
========== =======================



Usage
=====

Under evaluation

--------------------------------------------------------------------------------

.. _ecollectionevents-locality-1-site-details-site-station-number:

*******************
Site/Station Number
*******************

========== ====================
Field      Value               
========== ====================
ItemPrompt Site/Station Number 
ColumnName LocSiteStationNumber
DataKind   dkAtom              
DataType   Text                
========== ====================



Usage
=====

Under evaluation

Format
======

Marine collection events, like dredges or dives, are usually assigned an
identifier. Historically we've captured this information very generally
(for example, "Dredge 1" or "Station 1"). This is not very useful for
discriminating between records. Instead, the recommended practice is to
use the exact identifier assigned during the cruise. This is often the
cruise number followed by the dredge or station number, and samples
collected during an event often include the site/station number at the
beginning of their field number.

--------------------------------------------------------------------------------

.. _ecollectionevents-locality-1-site-details-site-number-source:

******************
Site Number Source
******************

========== ===================
Field      Value              
========== ===================
ItemPrompt Site Number Source 
ColumnName LocSiteNumberSource
DataKind   dkAtom             
DataType   Text               
LookupName Site Number Source 
========== ===================



Usage
=====

Under evaluation

Format
======

The name of the authority that provided the station number. For cruises,
this may be an oceanographic institute, like WHOI or Scripps.

--------------------------------------------------------------------------------

.. _ecollectionevents-locality-1-site-details-site-name:

*********
Site Name
*********

========== ===============
Field      Value          
========== ===============
ItemPrompt Site Name      
ColumnName LocSiteName_tab
DataKind   dkTable        
DataType   Text           
LookupName Site Name      
========== ===============



Usage
=====

Under evaluation

--------------------------------------------------------------------------------

.. _ecollectionevents-locality-1-ocean-ocean:

*****
Ocean
*****

========== ========
Field      Value   
========== ========
ItemPrompt Ocean   
ColumnName LocOcean
DataKind   dkAtom  
DataType   Text    
LookupName Ocean   
========== ========

The name of an ocean

Usage
=====

Required for marine localities and ocean islands. Omit for large
islands.

Format
======

Ocean and sea boundaries are determined by the International
Hydrographic Organization (IHO). Names can be resolved using
coordinates, for example, using the `GeoNames ocean webservice
<https://www.geonames.org/export/web-services.html#ocean>`_ or
shapefiles provided by the `Marine Regions
<https://www.marineregions.org/>`_ website run by the Flanders Marine
Institute.

The boundaries of the Arctic and Southern Oceans seem to vary
seasonally. The Southern Ocean is not part of the official IHO ocean
list but has been added to the IHO shapefile on the Marine Regions
website.

The generic Atlantic and Pacific Ocean names should be avoided when
possible. Map them to either North or South if coordinates or other
locality info allows. The north/south divisions generally follow the
equator, with the exception of the Galapagos and Gilbert Islands, which
cross the equator but are assigned to the South Pacific Ocean. Other
features that cross the equator but are not addressed by IHO include:

- **Halmahera** is assigned to the North Pacific Ocean because it is
  mostly north of the equator.
- **Sulawesi** is assigned to the South Pacific Ocean because it is
  mostly south of the equator.
- **Galapagos Rise** and **Galapagos Spreading Center** are assigned to
  the South Pacific Ocean by analogy to the Galapagos Islands.

Large islands at the border between oceans cannot always be assigned to
a specific ocean. For example, Sumatra sits at the border of the Indian
and Pacific Oceans *and* straddles the equator.

Allowed Values
==============

* Arctic Ocean
* Indian Ocean
* North Atlantic Ocean
* North Pacific Ocean
* South Atlantic Ocean
* South Pacific Ocean
* Southern Ocean

--------------------------------------------------------------------------------

.. _ecollectionevents-locality-1-ocean-sea-gulf:

********
Sea/Gulf
********

========== ==========
Field      Value     
========== ==========
ItemPrompt Sea/Gulf  
ColumnName LocSeaGulf
DataKind   dkAtom    
DataType   Text      
========== ==========

The name of one of the primary divisions of the oceans, like a sea,
marginal sea, or gulf

Usage
=====

Recommended for marine localities and ocean islands. Omit if locality
does not appear in a named sea or if the sea name cannot be determined.

Format
======

As with :ref:`Ocean` above, sea and gulf boundaries are determined by
the IHO. Names in this field should exactly match an IHO name. See that
entry for sources for more information about assigning ocean and sea
names.

Examples
========

* Carribean Sea
* Gulf of Mexico

--------------------------------------------------------------------------------

.. _ecollectionevents-locality-1-ocean-bay-sound:

*********
Bay/Sound
*********

========== ===========
Field      Value      
========== ===========
ItemPrompt Bay/Sound  
ColumnName LocBaySound
DataKind   dkAtom     
DataType   Text       
========== ===========

The name of any coastal body of water smaller than a sea or gulf

Usage
=====

Omit if no appropriate data is available

--------------------------------------------------------------------------------

.. _ecollectionevents-locality-1-continent-political-continent:

*********
Continent
*********

========== ============
Field      Value       
========== ============
ItemPrompt Continent   
ColumnName LocContinent
DataKind   dkAtom      
DataType   Text        
LookupName Continent   
========== ============

The name of a continent

Usage
=====

Required for records representing terrestrial specimens. Recommended for
marine localities on the continental shelf.

Format
======

Use the `GeoNames country code list
<https://www.geonames.org/countries/>`_ to map countries to continents.
Mapping this way introduces some incongruities (for example, Hawaii maps
to North America) but it beats making a series of individual decisions.

Allowed Values
==============

* Africa
* Antarctica
* Asia
* Europe
* North America
* Oceania
* South America

--------------------------------------------------------------------------------

.. _ecollectionevents-locality-1-continent-political-country:

*******
Country
*******

========== ==========
Field      Value     
========== ==========
ItemPrompt Country   
ColumnName LocCountry
DataKind   dkAtom    
DataType   Text      
========== ==========

The name of a country. Includes both independent entities and dependent
but self-governed entities.

Usage
=====

Required for all terrestrial records

Format
======

Country names should use the English short name from the `ISO 3166 list
of country codes
<https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes>`_. The
ISO list includes both sovereign states and entities, like Greenland,
that are affiliated with another country but are largely self-governed.
Puerto Rico falls into the latter category and should be given as a
country (not a territory of the United States) in EMu.

For a discussion of updating names as administrative boundaries change
over time, see TKTK.

**Known issues**

The formal ISO names have not been fully adopted in EMu. For example,
North Korea and South Korea are still in use despite not being the
preferred form in the ISO list.

--------------------------------------------------------------------------------

.. _ecollectionevents-locality-1-continent-political-province-state-terrirtory:

*************************
Province/State/Terrirtory
*************************

========== =========================
Field      Value                    
========== =========================
ItemPrompt Province/State/Territory 
ColumnName LocProvinceStateTerritory
DataKind   dkAtom                   
DataType   Text                     
========== =========================

The primary administrative division in a country, like a state in the
United States or a province in Canada

Usage
=====

Omit if no appropriate data is available

Format
======

Entities in this field must be first-order administrative divisions. The
names of administrative divisions vary from country to country,
sometimes in ways that may confuse data entry. For example, the state-
level entities in the Bahamas are called districts and the county-level
entities in the Phillipines are called provinces. GeoNames is a useful
resource for figuring out what consistutes a first-order admin division.
See :ref:`filling-in-gaps-in-the-administrative-hierarchy` for guidance
on backfilling administrative divisions from more specific locality
information.

--------------------------------------------------------------------------------

.. _ecollectionevents-locality-1-continent-political-district-county-shire:

*********************
District/County/Shire
*********************

========== ======================
Field      Value                 
========== ======================
ItemPrompt District/County/Shire 
ColumnName LocDistrictCountyShire
DataKind   dkAtom                
DataType   Text                  
========== ======================

The secondary administrative division in a country, like a county in the
United States

Usage
=====

Omit if no appropriate data is available

Format
======

Additional administrative divisions can be included in :ref:`Precise
Locality`.
See :ref:`filling-in-gaps-in-the-administrative-hierarchy` for guidance
on backfilling administrative divisions from more specific locality
information.

--------------------------------------------------------------------------------

.. _ecollectionevents-locality-1-continent-political-city-town:

*********
City/Town
*********

========== ===========
Field      Value      
========== ===========
ItemPrompt Township   
ColumnName LocTownship
DataKind   dkAtom     
DataType   Text       
LookupName Township   
========== ===========

The name of a populated place, like a city, town, or township

Usage
=====

Omit if no appropriate data is available

Format
======

The name should be given in full, without abbreviations, unless the
original documenation includes abbreviations of uncertain meaning.

If both town and township are known, include the town, then a semicolon,
then the township.

Modifiers (in parentheses) may follow the city/town/township
designation.

--------------------------------------------------------------------------------

.. _ecollectionevents-locality-1-continent-political-no-further-locality-data:

************************
No Further Locality Data
************************

========== ========================
Field      Value                   
========== ========================
ItemPrompt No Further Locality Data
ColumnName LocNoFurtherLocalityData
DataKind   dkAtom                  
DataType   Text                    
========== ========================

Identifies simple locality records that do not include information on
any tab except Locality (1) *except* georeferenced coordinates. This is
to allow simple localities to be georeferenced while still making use of
this field.

Usage
=====

Leave unchecked if locality info appears on any other tab

--------------------------------------------------------------------------------

.. _ecollectionevents-locality-1-continent-political-precise-locality:

****************
Precise Locality
****************

========== ==================
Field      Value             
========== ==================
ItemPrompt Precise Location  
ColumnName LocPreciseLocation
DataKind   dkAtom            
DataType   Text              
========== ==================

A brief description of the exact sampling location

Usage
=====

Omit if no appropriate data is available

Format
======

The precise locality is usually entered as one or more sentence
fragments. Full sentences are acceptable here, especially if quoting
from original documentation, but try to be brief. When using fragments,
separate each fragment with a semicolon, not a period, so the different
parts can be parsed if needed.
