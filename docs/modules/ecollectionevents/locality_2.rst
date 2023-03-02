################################
ecollectionevents > Locality (2)
################################

This tab contains named locality features additional to what appears in
table 1.

--------------------------------------------------------------------------------

.. _ecollectionevents-locality-2-island-details-archipelago:

***********
Archipelago
***********

========== ==============
Field      Value         
========== ==============
ItemPrompt Archipelago   
ColumnName LocArchipelago
DataKind   dkAtom        
DataType   Text          
LookupName Archipelago   
========== ==============



Usage
=====

Not used. See Island Grouping instead.

--------------------------------------------------------------------------------

.. _ecollectionevents-locality-2-island-details-island-grouping:

***************
Island Grouping
***************

========== =================
Field      Value            
========== =================
ItemPrompt Island Grouping  
ColumnName LocIslandGrouping
DataKind   dkAtom           
DataType   Text             
LookupName Island Grouping  
========== =================

A group of islands

Usage
=====

Omit if no appropriate data is available

Format
======

Entries must be written out in full.
A single island may belong to more than one island group. For example,
Dominica is part of the Windward Islands, the Lesser Antilles, and the
West Indies. You may include up to two groups using the following
format: "Smaller Group (Larger Group)."

There are two island groups commonly referred to as the Windward Islands
and the Leeward Islands. One is in the Caribbean and is part of the
Lesser Antilles. The other is in the Pacific and is part of the Society
Islands. Always specify the larger group when referring to either of
these groups.

Admin divisions may correspond to island groupings (for example,
Hawaii). Include the island grouping even if it is its own admin
division.

Examples
========

* Galapagos Islands
* Windward Islands (Lesser Antilles)
* Windward Islands (Society Islands)

--------------------------------------------------------------------------------

.. _ecollectionevents-locality-2-island-details-island-name:

***********
Island Name
***********

========== =============
Field      Value        
========== =============
ItemPrompt Island Name  
ColumnName LocIslandName
DataKind   dkAtom       
DataType   Text         
========== =============

The name of an island

Usage
=====

Omit if locality is not on an island

Format
======

Entries must be written out in full.
Include the word "island" only if it is typically used when referring to
a given island. For example, enter "Fernandina," not "Fernandina
Island."

Admin divisions may correspond to a single island (for example, Puerto
Rico). Include the island name even if it is its own admin division.

Examples
========

* Fernandina
* Tahiti

--------------------------------------------------------------------------------

.. _ecollectionevents-locality-2-mine-details-mining-district:

***************
Mining District
***************

========== =================
Field      Value            
========== =================
ItemPrompt Mining District  
ColumnName LocMiningDistrict
DataKind   dkAtom           
DataType   Text             
LookupName Mining District  
========== =================

The name of an area containing a group of mines. The mines in a single
district are usually tapping the same geologic feature and extracting
related ores.

Usage
=====

Omit if no appropriate data is available

--------------------------------------------------------------------------------

.. _ecollectionevents-locality-2-mine-details-mine-name:

*********
Mine Name
*********

========== ===========
Field      Value      
========== ===========
ItemPrompt Mine Name  
ColumnName LocMineName
DataKind   dkAtom     
DataType   Text       
LookupName Mine Name  
========== ===========

The name of a mine or quarry

Usage
=====

Omit if no appropriate data is available

--------------------------------------------------------------------------------

.. _ecollectionevents-locality-2-geomorphological-location-geomorphological-location:

*************************
Geomorphological Location
*************************

========== ===========================
Field      Value                      
========== ===========================
ItemPrompt Geomorphological Location  
ColumnName LocGeomorphologicalLocation
DataKind   dkAtom                     
DataType   Text                       
========== ===========================

The name of one or more geomorphological features

Usage
=====

Omit if no appropriate data is available

Format
======

A semicolon-delimited list of feature names

Examples
========

* Rocky Mountains
* Lake Huron
* Half-Mile Beach

--------------------------------------------------------------------------------

.. _ecollectionevents-locality-2-geologic-setting-geologic-setting:

****************
Geologic Setting
****************

========== ==================
Field      Value             
========== ==================
ItemPrompt Geologic Setting  
ColumnName LocGeologicSetting
DataKind   dkAtom            
DataType   Text              
LookupName Geologic Setting  
========== ==================

The name of a geologic feature, including petrologic province, complex,
zone within a complex, or genetic association from which a specimen was
collected.

Usage
=====

Omit if no appropriate data is available

Format
======

Names of geologic settings must be writtern out in full.

- **Geologic features**, like kimberlite pipes and plutons, should be
  recorded in Geologic Setting
- **Stratigraphic units**, like groups, formations, and members, should
  be recorded in Catalog > Stratigraphy
- **Topographic features**, like ridges and cordilleras, should be
  recorded in Geomorphological Location
- **Volcanic features**, like volcanoes, volcanic fields, and calderas,
  should be recorded in the Volcano (1) > Volcano Details fields

--------------------------------------------------------------------------------

.. _ecollectionevents-locality-2-collection-event-details-collection-event-parent:

***********************
Collection Event Parent
***********************

========== =================
Field      Value            
========== =================
ItemPrompt Site Parent Ref  
ColumnName LocSiteParentRef 
DataKind   dkAtom           
DataType   Reference        
RefTable   ecollectionevents
========== =================

Not used

--------------------------------------------------------------------------------

.. _ecollectionevents-locality-2-collection-event-details-collection-event-owner:

**********************
Collection Event Owner
**********************

========== ===================
Field      Value              
========== ===================
ItemPrompt Site Owner Ref     
ColumnName LocSiteOwnerRef_tab
DataKind   dkTable            
DataType   Reference          
RefTable   eparties           
========== ===================

Not used

--------------------------------------------------------------------------------

.. _ecollectionevents-locality-2-collection-event-details-land-owner-jurisdiction:

***********************
Land Owner/Jurisdiction
***********************

========== =======================
Field      Value                  
========== =======================
ItemPrompt Jurisdiction           
ColumnName LocJurisdiction        
DataKind   dkAtom                 
DataType   Text                   
LookupName Land Owner/Jurisdiction
========== =======================

Not used
