#########################
ecatalogue > Relationship
#########################

This tab documents relationships between objects, including objects held
by other organizations.

--------------------------------------------------------------------------------

.. _ecatalogue-relationship-object-details-object-id:

*********
Object ID
*********

========== ============
Field      Value       
========== ============
ItemPrompt URI         
ColumnName RelNhURI_tab
DataKind   dkTable     
DataType   Text        
========== ============

The identifier of the related object

Usage
=====

Required for each populated row

Format
======

This is the only identifier that appears in the summary grid and must be
populated manually for each row.

The museum recommends using a persistent URI to represent the related
object. We adopt that standard for objects not held by the department
but for Mineral Sciences specimens use the catalog number to make the
grid more usable.

--------------------------------------------------------------------------------

.. _ecatalogue-relationship-object-details-id-type:

*******
ID Type
*******

========== ====================
Field      Value               
========== ====================
ItemPrompt ID Type             
ColumnName RelNhIDType_tab     
DataKind   dkTable             
DataType   Text                
LookupName Relationship ID Type
========== ====================

The type of identifier used to represent the related object

Usage
=====

Required for each populated row

Examples
========

* Catalog Number
* EZID
* IGSN

--------------------------------------------------------------------------------

.. _ecatalogue-relationship-object-details-object:

******
Object
******

========== =================
Field      Value            
========== =================
ItemPrompt Object Ref       
ColumnName RelObjectsRef_tab
DataKind   dkTable          
DataType   Reference        
RefTable   ecatalogue       
========== =================

The catalog record of the related object if held in the same department

Usage
=====

Required for each populated row when the related object is held by the
department

Format
======

Reference to Catalog. The linked record will automatically be updated to
include the relationship.

--------------------------------------------------------------------------------

.. _ecatalogue-relationship-object-details-counts:

******
Counts
******

========== ==============
Field      Value         
========== ==============
ItemPrompt Count         
ColumnName RelNhCount_tab
DataKind   dkTable       
DataType   Integer       
========== ==============

Not used

--------------------------------------------------------------------------------

.. _ecatalogue-relationship-object-details-relationship:

************
Relationship
************

========== ===================
Field      Value              
========== ===================
ItemPrompt Relationship       
ColumnName RelRelationship_tab
DataKind   dkTable            
DataType   Text               
LookupName Object Relationship
========== ===================

The type of relationship

Usage
=====

Required for each populated row

Format
======

Relationships currently in use include:

- **Parent/child** designates subsampling relationships
- **Same as/Same as** designates specimens with different catalog
  records that are fragments of the same object
- **Whole/Part**: Deprecated. Use parent/child instead.


When the related object has a linked record in EMu, the value for
Relationship will be set to the unused value in the pair.

Allowed Values
==============

* Child
* Parent
* Same as

--------------------------------------------------------------------------------

.. _ecatalogue-relationship-object-details-date:

****
Date
****

========== ==========
Field      Value     
========== ==========
ItemPrompt Date      
ColumnName RelNhDate0
DataKind   dkTable   
DataType   Date      
========== ==========

Not used

--------------------------------------------------------------------------------

.. _ecatalogue-relationship-object-details-source:

******
Source
******

========== =======================
Field      Value                  
========== =======================
ItemPrompt According To Ref       
ColumnName RelNhAccordingToRef_tab
DataKind   dkTable                
DataType   Reference              
RefTable   eparties               
========== =======================

The source documenting the relationship

Usage
=====

Omit if no appropriate data is available

Format
======

Reference to Parties

--------------------------------------------------------------------------------

.. _ecatalogue-relationship-object-details-held-by:

*******
Held By
*******

========== ======================
Field      Value                 
========== ======================
ItemPrompt Repository Ref        
ColumnName RelNhRepositoryRef_tab
DataKind   dkTable               
DataType   Reference             
RefTable   eparties              
========== ======================

The repository that holds the related object

Usage
=====

Required for each populated row

Format
======

Reference to Parties

--------------------------------------------------------------------------------

.. _ecatalogue-relationship-object-details-inter:

******
Inter.
******

========== ========================
Field      Value                   
========== ========================
ItemPrompt Interaction             
ColumnName RelNhInteraction_tab    
DataKind   dkTable                 
DataType   Text                    
LookupName Relationship Interaction
========== ========================

Not used

--------------------------------------------------------------------------------

.. _ecatalogue-relationship-object-details-site:

****
Site
****

========== ===================
Field      Value              
========== ===================
ItemPrompt Site In Host       
ColumnName RelNhSiteInHost_tab
DataKind   dkTable            
DataType   Text               
LookupName Relationship Site  
========== ===================

Not used

--------------------------------------------------------------------------------

.. _ecatalogue-relationship-object-details-event-type:

**********
Event Type
**********

========== =======================
Field      Value                  
========== =======================
ItemPrompt Event Type             
ColumnName RelNhEventType_tab     
DataKind   dkTable                
DataType   Text                   
LookupName Relationship Event Type
========== =======================

Not used

--------------------------------------------------------------------------------

.. _ecatalogue-relationship-object-details-identified-by:

*************
Identified By
*************

========== ======================
Field      Value                 
========== ======================
ItemPrompt Identified By Ref     
ColumnName RelNhIdentifyByRef_tab
DataKind   dkTable               
DataType   Reference             
RefTable   eparties              
========== ======================

Not used

--------------------------------------------------------------------------------

.. _ecatalogue-relationship-object-details-notes:

*****
Notes
*****

========== ==============
Field      Value         
========== ==============
ItemPrompt Remarks       
ColumnName RelRemarks_tab
DataKind   dkTable       
DataType   Text          
========== ==============



Usage
=====

Omit if no appropriate data is available

Format
======

Free text

--------------------------------------------------------------------------------

.. _ecatalogue-relationship-taxon-identification-taxon-identification:

********************
Taxon Identification
********************

========== ==================== =================== ================== ================== =================== ================== ==================== ======================== ====================
Field      RelNhKingdom_tab     RelNhPhylum_tab     RelNhClass_tab     RelNhOrder_tab     RelNhFamily_tab     RelNhGenus_tab     RelNhSpecies_tab     RelNhSubspecies_tab      RelNhVariety_tab    
========== ==================== =================== ================== ================== =================== ================== ==================== ======================== ====================
ItemPrompt Kingdom              Phylum              Class              Order              Family              Genus              Species              Subsp.                   Variety             
ColumnName RelNhKingdom_tab     RelNhPhylum_tab     RelNhClass_tab     RelNhOrder_tab     RelNhFamily_tab     RelNhGenus_tab     RelNhSpecies_tab     RelNhSubspecies_tab      RelNhVariety_tab    
DataKind   dkTable              dkTable             dkTable            dkTable            dkTable             dkTable            dkTable              dkTable                  dkTable             
DataType   Text                 Text                Text               Text               Text                Text               Text                 Text                     Text                
LookupName Relationship Kingdom Relationship Phylum Relationship Class Relationship Order Relationship Family Relationship Genus Relationship Species Relationship Sub Species Relationship Variety
========== ==================== =================== ================== ================== =================== ================== ==================== ======================== ====================

Not used
