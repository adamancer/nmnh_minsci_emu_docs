#######
General
#######

*******************************
Documenting significant changes
*******************************

When making significant changes to the content of a record (for example,
changing the rock/mineral type or updating the collection locality based
on new information), make sure to provide a note explaining the change.
It is common for inexperienced users to make errors when entering data
into EMu, some of which can modify other records without the user
realizing it. Changes are automatically documented in EMu via the Audit
Log module, but audit records have no narrative component, making it
difficult to find mistakes. *Deliberate but unannotated changes are
indistinguishable from errors.*

The descriptive statement should be brief while still conveying the info
a future user would need to understand the change. The recommended note
format, below, is based on a Markdown change log.

.. code-block:: Markdown

   Aligned meteorite data to the Meteorite Bulletin Database
   * MetMeteoriteName: Changed "Puerto Lapice" to "Puerto Lápice"
   * MetMeteoriteType: Changed "Eucrite" to "Eucrite-br"
   * BibBibliographyRef_tab: Added "Met Bull 93"

A narrative note is also acceptable:

.. code-block:: Markdown

   Updated meteorite name to "Puerto Lápice" and type to "Eucrite-br" to
   match Meteorite Bulletin.

**The most important thing is to make it clear when changes were
intentional.**

Minor changes (like correcting a spelling error or moving data to a
different field within the same record) do not need to be documented.

**********************
Using structured notes
**********************

Collection documentation often includes information with no obvious home
in EMu. It is often useful to retain that information, including both
its source and structure. As in the previous section, the best place to
include this information is as a note in the record being modified.

The recommended format for structured notes is YAML, a human-readable
markup language. Notes should include a topline comment describing the
source of the data and the data itself as a series of key-value pairs.

.. code-block:: YAML

   # NASA metadata for ALH 83101
   Weathering: A
   Fracturing: A
   Fa: 25%
   Fs: 23%
   ²⁶Al: 116 ± 8.5 dpm/kg

The primary benefit of this format is that it is legible to both people
and scripts. The primary drawback is that there are nuances to creating
properly formatted YAML that are likely to confuse less technically
savvy users.

****************************************
Standardizing place names using GeoNames
****************************************

`GeoNames <https://geonames.org>`_ (not to be confused with the National
Geospatial-Intelligence Agency's `GeoNames Search
<https://geonames.nga.mil/namesgaz/>`_) is a good source for information
about place names. It has a large database, good webservices, and for
many localities provides a list of alternate names.

******************************
Modifying locality information
******************************

Updating localities
-------------------

Place names and borders change over time, both through administrative
reorganizations and justice-minded efforts to remove racist or
derogatory place names. It is often useful to update collection
localities to match current names. Alternatively, museum staff may find
new information about a specimen's collection locality that requires
them to update the locality. These changes can be complex and must be
handled thoughtfully.

* Any change to the locality must be explicitly documented in note
  including both what changes were made and why. See :ref:`Documenting
  significant changes` for information about formatting the note.
* The original locality must be retained within the database, ideally
  in a field specific to this purpose. Deprecated place names including
  derogatory terms can be retained in a non-public field.

.. _filling-in-gaps-in-the-administrative-hierarchy:

Filling in gaps in the administrative hierarchy
-----------------------------------------------

Consider a record that includes a country, state, and town but no
county. It is often possible to uniquely identify a town within a state,
which would then allow us to determine the county as well. Should that
county be populated in the record?

In general, it is acceptable to fill in gaps like this provided that we
document the change following the rules laid out in the previous
section. The primary risk in doing so is that we make an error when
identifying the town or feature used to determine the county. For
example, some states include multiple towns with the same name, like
Springfield Township, New Jersey. If we pick the wrong one, the county
name will also be wrong. If the change is not documented, the incorrect
county name could provide support for an incorrect interpretation of the
original data.

Filling in information from coordinates
---------------------------------------

Services like `GeoNames <https://geonames.org/>`_ allow us to fill in
the administrative hierarchy from a set of coordinates. We do not use
these services to update information, but they can be useful for
identifying errors in coordinates.

*****************************************************
Adding and updating data in EMu using the import tool
*****************************************************

EMu provides tools for importing and reporting data from the client.
These tools can be used to assess and update data and allow us to
emulate common database operations that aren't supported by the EMu
client. Operations include:

* Moving data between fields or records
* Reading and making changes to specific rows in grids
* Systematically evaluating and cleaning lookups

I use a homebrewed Python package called `xmu
<https://github.com/adamancer/xmu>`_ to manage reading and importing
data in EMu using XML. See that page for information about using that
tool.

*************************
Documenting preparations
*************************

Preparations associated with specimens in the collection
--------------------------------------------------------

Preparations associated with specimens in the collection are usually
stored with the parent specimen. In this case, include them in Petrology
(1) > Preparation Details grid.

Orphaned preparations in a container
------------------------------------

Petrology accessions may include preparations that do not correspond to
specimens in the collection. For example, recent accessions often
include boxes of orphaned thin sections. Once a decision to keep these
preparations has been made, catalog the container and the associated
preparations as follows:

#. Assign the container a catalog number with no suffix
#. Create an EMu record for the container
#. For each preparation:

   #. Assign a catalog number consisting of the container number and a
      numeric suffix
   #. Create an EMu record

If the parent of a preparation is later found, it may be desirable to
relocate a preparation to be stored with its parent. TKTK

Multi-specimen preparations
---------------------------

Many preparations include samples from more than one specimen. For
example, thin sections and grain mounts may include multiple specimens
to allow comparisons or simplify analyses. Catalog a multi-specimen
preparation as follows:

#. Assign the preparation a catalog number with no suffix
#. Create an EMu record for the preparation
#. For each sample included on the preparation:

   #. Assign a catalog number consisting of the container number and a
      numeric suffix
   #. Create an EMu record for the sample
   #. In the EMu record, link each sample back to its parent specimen
      using the Relationships tab.

************************************
Filling requests for data and assets
************************************

Requests for data and assets are governed by SD609, which among other
things requires holding units to track requests received and processed,
including maintaining a record of agreements and decisions for
individual requests. Mineral Sciences uses a ticketing system to track
requests. When a request is received, the data manager creates a ticket,
which automatically generates a list of tasks that must be completed as
the request is processed and filled.

***************************
Publishing catalog numbers
***************************

Meteorites
==========

Catalog numbers
---------------

**Preferred format:** USNM {number}-{suffix}

* **Number:** Required. Strip leading zeros from the number.
* **Suffix:** Optional. Strip leading zeros from the suffix.

Examples of valid catalog numbers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* USNM 3589
* USNM 3589-1

Antarctic meteorite numbers
---------------------------

Meteorites collected by the Antarctic Meteorite Program are also tagged
with a NASA meteorite numbers. This is often more specific than the
catalog number, especially for recent acquisitions, where a large number
of distinct meteorites may be grouped under a single catalog number.

**Preferred format:** {locality_code}{number},{comma_number}

* **Locality code:** Required. A three- to four-character alpha string
  based on the general sample locality. Always capitalized. Three-
  character codes are separated from the number by a space. Four-
  character codes always end with an "A" and only appear in older
  samples.
* **Number:** Required. A five- to six-digit number consisting of a two-
  digit year and three- to four-digit sample number specifying a
  single meteorite.
* **Comma number:** Optional. An alphanumeric string specifying a
  subsample of a meteorite. Separated from the main number by a comma.

Examples of valid meteorite numbers
-----------------------------------

* ALHA76001
* ALHA76001,1
* GRO 00123,45
* GRO 001010,1

Mineralogy
==========

**Preferred format:** NMNH {prefix}{number}-{suffix}

* **Prefix:** Optional. Where present, usually consists of a single
  letter, always capitalized. There is no space between the prefix and
  the number.
* **Number:** Required. Strip any zeros from the left side of the
  number.
* **Suffix:** Optional. Numeric suffixes are zero-padded to two
  characters, excepting suffixes longer than two characters, which are
  presented verbatim. Alphanumeric suffixes are given verbatim. The
  suffix "00" is usually omitted. The suffix is delimited from the
  number by a hyphen.

Examples of valid catalog numbers
---------------------------------

* NMNH G3551
* NMNH 108683-A0
* NMNH R7138-01

Mapping from other formats
--------------------------

* G1234-00 ⇒ NMNH G1234
* G1234.00 ⇒ NMNH G1234
* G1234-1 ⇒ NMNH G1234-01
* G 1234 00 ⇒ NMNH G1234
* G 1234 A0 ⇒ NMNH G1234-A0
* G001234.A0 ⇒ NMNH G1234-A0

Petrology & Volcanology
=======================

**Preferred format:** NMNH {prefix}{number}-{suffix}

* **Prefix:** Optional, uncommon. Where present, usually consists of a
  single letter, always capitalized. There is no space between the
  prefix and the number.
* **Number:** Required. Strip leading zeros from the number.
* **Suffix:** Optional. Usually numeric. Strip leading zeros from the
  suffix.

Examples of valid catalog numbers
---------------------------------

* NMNH 123455
* NMNH 123456-78

Mapping from other formats
--------------------------

* 123455.0000 ⇒ NMNH 123455
* 123456 78 = NMNH 123456-78

**********************
Archiving scanned PDFs
**********************

This section provides instructions for setting up and using the PDF
archiving workflow for scanned documents. A properly archived document
should:

* Include a descriptive title
* Include searchable text
* Be saved as PDF/A-1b

Setup
-----

These steps import a Foxit action that OCRs each PDF and saves it as
PDF/A-1b. They only need to be performed once per computer/login.

#. Open Foxit PDF Editor
#. Click File in the upper left corner
#. Click Action Wizard in the left sidebar
#. Click Manage Actions under the Action Wizard header
#. Click the Manage Icon under the Manage Actions header
#. Click the Import button on the right side of the Manage Actions
   window
#. Navigate to the script directory
#. Click “OR PDF Finalizer.sequ”
#. Click Open

Preparing documents
-------------------

Each document requires a title. To assign a title:

#. Open Foxit PDF Editor
#. Click File in the upper left corner
#. Click Properties at the top of the left sidebar
#. Click the Title field under the Description header
#. Add a descriptive title

Run the OR PDF Finalizer action:

#. Open Foxit PDF Editor
#. Click File in the upper left corner
#. Click Action Wizard in the left sidebar
#. Click Run Action under the Action Wizard header
#. Click the OR PDF Finalizer action under the Run Action header
#. Click the Import button on the right side of the Manage Actions
   window
#. You should now be able to see a Run Action sidebar in the document
   view
#. In the Run Action sidebar, click Add Folder
#. Select the folder containing the PDFs
#. Click the blue start button

**Tip:** The action runs on all files in the selected directory,
including files nested in subdirectories. For best results, organize all
PDFs in a single directory that does not include any other files. This
will prevent Foxit from converting any images it encounter to PDF.

Accessibility considerations
----------------------------

PDFs should be made accessible to allow them to reach the broadest
possible audience and to comply with federal law. However, accessibility
remediation is labor-intensive and we are currently unable to remediate
all documents. Currently:

* Scanned documents are not remediated
* Born-digital documents must be submitted to the departmental data
  manager for review