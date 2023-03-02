##########################
ecatalogue > Gems/Minerals
##########################

This tab captures data specific to gems and minerals.

--------------------------------------------------------------------------------

.. _ecatalogue-gems-minerals-object-data-from-time-of-collecting-event-event-site:

**********
Event/Site
**********

========== =================
Field      Value            
========== =================
ItemPrompt Event/Site Ref   
ColumnName BioEventSiteRef  
DataKind   dkAtom           
DataType   Reference        
RefTable   ecollectionevents
========== =================

The collection locality and event

Usage
=====

Required

Format
======

Reference to Collection Events

--------------------------------------------------------------------------------

.. _ecatalogue-gems-minerals-object-data-from-time-of-collecting-event-collectors:

**********
Collectors
**********

========== =====================
Field      Value                
========== =====================
ItemPrompt Collectors Ref       
ColumnName BioParticipantRef_tab
DataKind   dkTable              
DataType   Reference            
RefTable   eparties             
========== =====================

List of collector names

Usage
=====

Populated automatically from the associated Collections Event record

--------------------------------------------------------------------------------

.. _ecatalogue-gems-minerals-object-data-from-time-of-collecting-event-primary-coll-number:

*******************
Primary coll number
*******************

========== ====================
Field      Value               
========== ====================
ItemPrompt Primary Coll Number 
ColumnName BioPrimaryCollNumber
DataKind   dkAtom              
DataType   Text                
========== ====================

Not used

--------------------------------------------------------------------------------

.. _ecatalogue-gems-minerals-physical-details-jewelry-type:

************
Jewelry Type
************

========== ===============
Field      Value          
========== ===============
ItemPrompt Jewelery Type  
ColumnName MinJeweleryType
DataKind   dkAtom         
DataType   Text           
LookupName Jewelery Type  
========== ===============

The type of jewelry

Usage
=====

Omit if no appropriate data is available

Examples
========

* Bracelet
* Brooch
* Necklace
* Ring

--------------------------------------------------------------------------------

.. _ecatalogue-gems-minerals-physical-details-fashion-cut:

***********
Fashion/Cut
***********

========== ===========
Field      Value      
========== ===========
ItemPrompt Fashion/Cut
ColumnName MinCut     
DataKind   dkAtom     
DataType   Text       
LookupName Mineral Cut
========== ===========

The cut of the primary gem

Usage
=====

Omit if no appropriate data is available

Examples
========

* Cushion
* Fancy
* Step

--------------------------------------------------------------------------------

.. _ecatalogue-gems-minerals-physical-details-color:

*****
Color
*****

========== ==============
Field      Value         
========== ==============
ItemPrompt Color         
ColumnName MinColor_tab  
DataKind   dkTable       
DataType   Text          
LookupName Minerals Color
========== ==============

The color of the primary gem

Usage
=====

Omit if no appropriate data is available

Examples
========

* Blue
* Green
* Red
* Yellow

--------------------------------------------------------------------------------

.. _ecatalogue-gems-minerals-physical-details-cut-by:

******
Cut By
******

========== ===========
Field      Value      
========== ===========
ItemPrompt Cut By Ref 
ColumnName MinCutByRef
DataKind   dkAtom     
DataType   Reference  
RefTable   eparties   
========== ===========

The person who cut a gem

Usage
=====

Omit if no appropriate data is available

Format
======

Reference to Parties

--------------------------------------------------------------------------------

.. _ecatalogue-gems-minerals-physical-details-maker:

*****
Maker
*****

========== ===========
Field      Value      
========== ===========
ItemPrompt Maker      
ColumnName MinMakerRef
DataKind   dkAtom     
DataType   Reference  
RefTable   eparties   
========== ===========

The person or organization that fabricated a piece of jewelry or
synthetic specimen

Usage
=====

Omit if no appropriate data is available

Format
======

Reference to Parties

--------------------------------------------------------------------------------

.. _ecatalogue-gems-minerals-physical-details-microprobed:

***********
Microprobed
***********

========== ==============
Field      Value         
========== ==============
ItemPrompt Microprobed   
ColumnName MinMicroprobed
DataKind   dkAtom        
DataType   Text          
LookupName Microprobed   
========== ==============

Not used

--------------------------------------------------------------------------------

.. _ecatalogue-gems-minerals-physical-details-x-rayed:

*******
X-Rayed
*******

========== =========
Field      Value    
========== =========
ItemPrompt X-Rayed  
ColumnName MinXRayed
DataKind   dkAtom   
DataType   Text     
LookupName X Rayed  
========== =========

Whether or not a specimen has been X-rayed

Usage
=====

Omit if no appropriate data is available

--------------------------------------------------------------------------------

.. _ecatalogue-gems-minerals-physical-details-synthetic:

*********
Synthetic
*********

========== ============
Field      Value       
========== ============
ItemPrompt Synthetic   
ColumnName MinSynthetic
DataKind   dkAtom      
DataType   Text        
LookupName Synthetic   
========== ============

Whether or not a specimen is synthetic

Usage
=====

Omit if no appropriate data is available

Format
======

Synthetic specimens often include information about where and how the
specimen was fabricated. This information is beyond the scope of this
field and should be recorded as follows:

- If the maker is known, record that information in Maker
- If additional details about the fabrication process are known, include
  them in the lot description

Allowed Values
==============

* Synthetic

--------------------------------------------------------------------------------

.. _ecatalogue-gems-minerals-physical-details-chemical-modifier:

*****************
Chemical Modifier
*****************

========== ===================
Field      Value              
========== ===================
ItemPrompt Chemical Modifier  
ColumnName MinChemicalModifier
DataKind   dkAtom             
DataType   Text               
LookupName Chemical Modifier  
========== ===================

A modifier applied to the primary mineral type. In practice, modifiers
are often included in Taxon instead.

Usage
=====

Omit if no appropriate data is available

Examples
========

* Ferroan
* Manganoan
* Palladian

--------------------------------------------------------------------------------

.. _ecatalogue-gems-minerals-gem-jewelry-name-gem-jewelry-name:

****************
Gem/Jewelry Name
****************

========== =======
Field      Value  
========== =======
ItemPrompt Name   
ColumnName MinName
DataKind   dkAtom 
DataType   Text   
========== =======

The name of a gem, piece of jewelry, or mineral specimen

Usage
=====

Omit if no appropriate data is available

Examples
========

* Hope Diamond
* Jolly Green Giant

--------------------------------------------------------------------------------

.. _ecatalogue-gems-minerals-lot-description-lot-description:

***************
Lot Description
***************

========== ===============
Field      Value          
========== ===============
ItemPrompt Live Specimen  
ColumnName BioLiveSpecimen
DataKind   dkAtom         
DataType   Text           
========== ===============

A long-form description of the specimen

Usage
=====

Omit if no appropriate data is available

--------------------------------------------------------------------------------

.. _ecatalogue-gems-minerals-publication-details-described-figured:

*****************
Described/Figured
*****************

========== =======================
Field      Value                  
========== =======================
ItemPrompt Described/Figured      
ColumnName MinDescribedFigured_tab
DataKind   dkTable                
DataType   Text                   
LookupName Described Figured      
========== =======================

Whether a specimen has been described or figured

Usage
=====

Omit if no appropriate data is available

Format
======

If a specimen has been described in a publication or manuscript, include
the full reference to that document in the Bibliography tab. Use
publication type "Citation" to record specific information about the
description, including page or figure numbers.

Allowed Values
==============

* Described
* Figured

--------------------------------------------------------------------------------

.. _ecatalogue-gems-minerals-composition-chemical-analysis:

*****************
Chemical Analysis
*****************

========== ==========================
Field      Value                     
========== ==========================
ItemPrompt Chemical Analysis Ref     
ColumnName PetChemicalAnalysisRef_tab
DataKind   dkTable                   
DataType   Reference                 
RefTable   enmnhanalysis             
========== ==========================

Not used
