####################
ecatalogue > Catalog
####################

This tab summarizes basic information about specimen custody, counts,
and identifiers, including the catalog number that serves as the primary
identifier for a specimen that has been accessioned into the collection.
Most fields on this tab should be populated in every record.

--------------------------------------------------------------------------------

.. _ecatalogue-catalog-collection-custody-museum:

******
Museum
******

========== ==================
Field      Value             
========== ==================
ItemPrompt Museum            
ColumnName CatMuseum         
DataKind   dkAtom            
DataType   Text              
LookupName Collection Custody
========== ==================

The name of the museum that has custody of the specimen

Usage
=====

Required for all records

Allowed Values
==============

* NMNH

--------------------------------------------------------------------------------

.. _ecatalogue-catalog-collection-custody-museum-acronym:

**************
Museum Acronym
**************

========== ================
Field      Value           
========== ================
ItemPrompt Museum Acronym  
ColumnName CatMuseumAcronym
DataKind   dkAtom          
DataType   Text            
========== ================

The acronym used when displaying the catalog number. Most specimens at
NMNH use the acronym "USNM" (short for United States National Museum),
but both **Mineralogy** and **Petrology & Volcanology** switched to
"NMNH" decades ago, much to the consternation of various parties.

Usage
=====

Required for all records

Allowed Values
==============

* NMNH *(Mineralogy and Petrology & Volcanology)*
* USNM *(Meteorites)*

--------------------------------------------------------------------------------

.. _ecatalogue-catalog-collection-custody-department:

**********
Department
**********

========== =============
Field      Value        
========== =============
ItemPrompt Department   
ColumnName CatDepartment
DataKind   dkAtom       
DataType   Text         
========== =============

The name of the department that has custody of the specimen

Usage
=====

Required for all records

Allowed Values
==============

* Mineral Sciences

--------------------------------------------------------------------------------

.. _ecatalogue-catalog-collection-custody-division:

********
Division
********

========== ===========
Field      Value      
========== ===========
ItemPrompt Division   
ColumnName CatDivision
DataKind   dkAtom     
DataType   Text       
========== ===========

The name of the division within a department that has custody of the
specimen

Usage
=====

Required for all records

Allowed Values
==============

* Meteorites
* Mineralogy
* Petrology & Volcanology

--------------------------------------------------------------------------------

.. _ecatalogue-catalog-collection-custody-catalog:

*******
Catalog
*******

========== ==========
Field      Value     
========== ==========
ItemPrompt Catalog   
ColumnName CatCatalog
DataKind   dkAtom    
DataType   Text      
========== ==========

The name of the catalog within the division. Only **Mineralogy** has
multiple catalogs (Gems and Minerals).

Usage
=====

Required for all records

Allowed Values
==============

* Gems
* Meteorites
* Minerals
* Rock & Ore Collection

--------------------------------------------------------------------------------

.. _ecatalogue-catalog-collection-custody-collection-name:

***************
Collection Name
***************

========== =====================
Field      Value                
========== =====================
ItemPrompt Collection Name      
ColumnName CatCollectionName_tab
DataKind   dkTable              
DataType   Text                 
LookupName Collection Name      
========== =====================

The name of the collection or collections the specimen has been assigned
to. Each division divides its holdings into collections, that is,
subsets with some common feature. Collections may be named after
collectors, donors, or an aspect of the collection itself (like a
specific place, project, or specimen type).

Usage
=====

Recommended for all records

Format
======

Include the word "Collection" in each collection name. For collections
named after a person, use their full name if possible. A single specimen
may be assigned to multiple collections. For example, a type mineral
might include both the Type Minerals Collection and a collection named
after the collector.

Examples
========

* Inventory Collection
* Sea Floor Rock Collection
* Washington A. Roebling Collection

--------------------------------------------------------------------------------

.. _ecatalogue-catalog-cataloging-details-prefix:

******
Prefix
******

========== ==============
Field      Value         
========== ==============
ItemPrompt Prefix        
ColumnName CatPrefix     
DataKind   dkAtom        
DataType   Text          
LookupName Catalog Prefix
========== ==============

An alphabetic prefix added to the beginning of the catalog number to
specify a catalog number series. A series is similar to a collection.
**Mineralogy** uses prefixes to distinguish series.

Usage
=====

Omit if record is not part of a prefixed series

Format
======

A single capital letter

Allowed Values
==============

* B *(Bosch)*
* C *(Canfield)*
* G *(Gems)*
* M *(Micromount)*
* R *(Roebling)*
* S *(Synthetic)*

--------------------------------------------------------------------------------

.. _ecatalogue-catalog-cataloging-details-number:

******
Number
******

========== =========
Field      Value    
========== =========
ItemPrompt Number   
ColumnName CatNumber
DataKind   dkAtom   
DataType   Integer  
========== =========

The numeric part of a catalog number. A catalog number may represent a
single specimen or a group of related specimens.

Usage
=====

Required for all records

Format
======

The Antarctic meteorites collection in **Meteorites** uses the same
catalog number to represent all the specimens from a single field
collected during a single year. It does not assign suffixes to
individual records. Catalog numbers are essentially worthless for this
collection, and it is best to refer to individual Antarctic meteorites
by the NASA-style meteorite number.

**Petrology & Volcanology** often uses a single catalog number to
represent a group of related specimens, for example, specimens collected
at a single locality by the same collector. Individual specimens may be
distinguished by suffixes.

--------------------------------------------------------------------------------

.. _ecatalogue-catalog-cataloging-details-suffix:

******
Suffix
******

========== =========
Field      Value    
========== =========
ItemPrompt Suffix   
ColumnName CatSuffix
DataKind   dkAtom   
DataType   Text     
========== =========

An alphanumeric suffix used to distinguish specimens with the same
catalog number.

Usage
=====

Omit if no appropriate data is available

Format
======

Suffix format and meaning vary by division. When publishing the catalog
number, suffixes should be delimited with a hyphen.

**Mineralogy** typically uses a two-character alphanumeric suffix.
Numeric suffixes are zero-padded to two-characers if needed (for
example, "1" becomes "01"). The first specimen for a given catalog
number is assigned the suffix "00" (but note that this suffix is often
omitted when catalog numbers are published.)

**Petrology & Volcanology** typically uses a numeric suffix. Suffixes
are *not* zero-padded. In labels for GGM, suffixes were zero-padded to
four characters, but this is not typical.

--------------------------------------------------------------------------------

.. _ecatalogue-catalog-cataloging-details-barcode:

*******
Barcode
*******

========== ==========
Field      Value     
========== ==========
ItemPrompt Barcode   
ColumnName CatBarcode
DataKind   dkAtom    
DataType   Text      
========== ==========

Not used

--------------------------------------------------------------------------------

.. _ecatalogue-catalog-cataloging-details-part-number:

***********
Part Number
***********

========== =============
Field      Value        
========== =============
ItemPrompt Part Number  
ColumnName CatPartNumber
DataKind   dkAtom       
DataType   Integer      
========== =============

Not used

--------------------------------------------------------------------------------

.. _ecatalogue-catalog-cataloging-details-whole-part:

**********
Whole/Part
**********

========== ==================
Field      Value             
========== ==================
ItemPrompt Whole/Part        
ColumnName CatWholePart      
DataKind   dkAtom            
DataType   Text              
LookupName Catalog Whole/Part
========== ==================

Whether a record represents a specimen in its entirety or a part of a
complex specimen. For example, consider a specimen from the mineral
collection containing multiple species. In some cases, each species has
been cataloged separately, in which case using "Part" in this field
would be appropriate.

Usage
=====

Required for all specimens

Allowed Values
==============

* Part
* Whole

--------------------------------------------------------------------------------

.. _ecatalogue-catalog-cataloging-details-cataloged-by:

************
Cataloged By
************

========== =================
Field      Value            
========== =================
ItemPrompt Cataloged By     
ColumnName CatCatalogedByRef
DataKind   dkAtom           
DataType   Reference        
RefTable   eparties         
========== =================

A reference to the party record for the cataloger. For new records, the
cataloger is the person who creates the digital record, either by
creating a record in the client or submitting a record in another format
to be imported.

Usage
=====

Omit if no appropriate data is available

--------------------------------------------------------------------------------

.. _ecatalogue-catalog-cataloging-details-date-cataloged:

**************
Date Cataloged
**************

========== ================
Field      Value           
========== ================
ItemPrompt Date Cataloged  
ColumnName CatDateCataloged
DataKind   dkAtom          
DataType   Date            
========== ================

The date the specimen was cataloged. For records entered directly into
the client, the cataloged date is the date the record is created. For
imported records, the cataloged date is the date the import spreadsheet
was submitted to the data manager. For records first entered into an
earlier database, the cataloged date is the entry date in the ledger.

Usage
=====

Omit if no appropriate data is available

Format
======



--------------------------------------------------------------------------------

.. _ecatalogue-catalog-cataloging-details-kind-of-object:

**************
Kind Of Object
**************

========== =============
Field      Value        
========== =============
ItemPrompt Object Type  
ColumnName CatObjectType
DataKind   dkAtom       
DataType   Text         
LookupName Object Type  
========== =============

The type of object represented by the record

Usage
=====

Required for all records

Allowed Values
==============

* Specimen/Object

--------------------------------------------------------------------------------

.. _ecatalogue-catalog-counts-specimen-count:

**************
Specimen Count
**************

========== ================ ========================
Field      CatSpecimenCount CatSpecimenCountModifier
========== ================ ========================
ItemPrompt Specimen Count   Modifier                
ColumnName CatSpecimenCount CatSpecimenCountModifier
DataKind   dkAtom           dkAtom                  
DataType   Integer          Text                    
LookupName                  Count Modifier          
========== ================ ========================

The number of objects represented by this record.

Usage
=====

Required for all records

Format
======

Counting objects can be tricky, so here are some general guidelines:

The count is based on the primary object represented by a record. For
most records, this will be a rock or mineral, in which case the count
will be the number of rock/mineral fragments. Preparations, like thin
sections or powders, are counted separately using the preparation grid.

For some records, the primary object is itself a prepation, like vial of
powder or box of thin sections. In this case, the specimen count is the
number of preparations.

**Mineralogy** sometimes uses "10" or "100" with a modifier of "plus" to
signify that there are a large number of objects that have not been
counted exactly.

Examples
========

* Box containing three large rock fragments: 3
* Box containing a hand sample and vial of power: 1
* Box of 200 thin sections: 200

--------------------------------------------------------------------------------

.. _ecatalogue-catalog-counts-original-count:

**************
Original Count
**************

========== ================ ========================
Field      CatOriginalCount CatOriginalCountModifier
========== ================ ========================
ItemPrompt Original Count   Modifier                
ColumnName CatOriginalCount CatOriginalCountModifier
DataKind   dkAtom           dkAtom                  
DataType   Text             Text                    
LookupName                  Count Modifier          
========== ================ ========================

Not used

--------------------------------------------------------------------------------

.. _ecatalogue-catalog-counts-other-counts:

************
Other Counts
************

========== ====================== =======================
Field      CatOtherCountsType_tab CatOtherCountsValue_tab
========== ====================== =======================
ItemPrompt Type                   Value                  
ColumnName CatOtherCountsType_tab CatOtherCountsValue_tab
DataKind   dkTable                dkTable                
DataType   Text                   Integer                
LookupName Other Counts Type                             
========== ====================== =======================

Not used

--------------------------------------------------------------------------------

.. _ecatalogue-catalog-counts-other-numbers:

*************
Other Numbers
*************

========== ======================= ========================= ========================
Field      CatOtherNumbersType_tab CatOtherNumbersSource_tab CatOtherNumbersValue_tab
========== ======================= ========================= ========================
ItemPrompt Type                    Source                    Value                   
ColumnName CatOtherNumbersType_tab CatOtherNumbersSource_tab CatOtherNumbersValue_tab
DataKind   dkTable                 dkTable                   dkTable                 
DataType   Text                    Text                      Text                    
LookupName Other Numbers Type      Other Numbers Source                              
========== ======================= ========================= ========================

Additional identifiers used to refer to the specimen, like the field
number assigned by the collector.

Usage
=====

Omit if no appropriate data is available

Format
======

Each row must include both Kind and Value. Source is rarely populated
and can be omitted. Examples of typical kinds are provided below.

Identifiers should be populated verbatim. Previous collections staff
sometimes zero-padded identifiers to a common length so that they would
sort properly in a spreadsheet. Do not do this! It makes it difficult to
find occurrences of those specimens in the literature.

Each identifier should be given its own row in the grid. Do not combine
multiple identifiers into a single row, even if they are the same kind.

The first row with the Kind "Collector's field number" will appear in
the summary line at the top of the record.

The other numbers grid has been used to store information about
recataloged specimens. This information is often ambiguous. For example,
some specimens were recataloged only in part, which is not always clear
from entries in the other number grid. This information should be added
to the Relationships tab instead.

Examples
========

* Collector's field number
* IGSN
* Lab number
* Parent IGSN
* VG number
