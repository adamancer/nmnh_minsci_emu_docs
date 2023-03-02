########################
Guidelines for using EMu
########################

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
   - MetMeteoriteName: Changed "Puerto Lapice" to "Puerto Lápice"
   - MetMeteoriteType: Changed "Eucrite" to "Eucrite-br"
   - BibBibliographyRef_tab: Added "Met Bull 93"

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

The recommended structured note format using YAML, a human-readable
markup language. It includes a topline comment describing the source of
the data, while the data itself is expressed as a series of key-value
pairs.

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

Place names and borders are change over time, both through
administrative reorganizations and justice-minded efforts to remove
racist or derogatory place names. It is often useful to update
collection localities to match current names. Alternatively, museum
staff may find new information about a specimen's collection locality
that requires them to update the locality. These changes can be complex
and must be handled thoughtfully.

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

Services like GeoNames allow us to fill in the administrative hierarchy
from a set of coordinates. We do not use these services to update
information, but they can be useful for identifying errors in
coordinates.

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
