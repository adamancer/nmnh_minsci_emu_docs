###################
ecatalogue > Status
###################

Documents inventory status and record quality

**Known issues:**

* The inventory grid is a mess.

--------------------------------------------------------------------------------

.. _ecatalogue-status-object-remains-status-accession-status:

****************
Accession Status
****************

+------------+--------------------+
| Field      | Value              |
+============+====================+
| ItemPrompt | Accession Status   |
+------------+--------------------+
| ColumnName | StaAccessionStatus |
+------------+--------------------+
| DataKind   | dkAtom             |
+------------+--------------------+
| DataType   | Text               |
+------------+--------------------+
| LookupName | Accession Status   |
+------------+--------------------+

The current accession status

Usage
=====

Populated automatically?

--------------------------------------------------------------------------------

.. _ecatalogue-status-object-remains-status-tm-status:

*********
TM Status
*********

+------------+-------------+
| Field      | Value       |
+============+=============+
| ItemPrompt | TM Status   |
+------------+-------------+
| ColumnName | StaTMStatus |
+------------+-------------+
| DataKind   | dkAtom      |
+------------+-------------+
| DataType   | Text        |
+------------+-------------+
| LookupName | TM Status   |
+------------+-------------+

The current transaction status. Note that incorrect transaction records
(especially partial disposals that are not entered properly) can prevent
a given record from being attached to a new transaction.

Usage
=====

Populated automatically when this record is linked to a loan or disposal
in the Transactions module if the whole specimen is part of the
transaction

Allowed Values
==============

* Deaccessioned
* Disposed
* On Loan
* Pending Deaccession
* Pending Disposal
* Pending Loan

--------------------------------------------------------------------------------

.. _ecatalogue-status-object-remains-status-record-quality:

**************
Record Quality
**************

+------------+------------------+
| Field      | Value            |
+============+==================+
| ItemPrompt | Record Quality   |
+------------+------------------+
| ColumnName | StaRecordQuality |
+------------+------------------+
| DataKind   | dkAtom           |
+------------+------------------+
| DataType   | Integer          |
+------------+------------------+
| LookupName | Record Quality   |
+------------+------------------+

The quality of the record as an integer between 2 and 4, where
increasing numbers represent increasing completeness of the record. Used
primarily to generate statistics for museum- or institution-wide
collections reports.

Usage
=====

Populated automatically based on a department-specific rubric integrated
into the EMu backend. The rubric can only be modified by contacting
Informatics.

--------------------------------------------------------------------------------

.. _ecatalogue-status-object-remains-status-primary-collection:

******************
Primary Collection
******************

+------------+----------------------+
| Field      | Value                |
+============+======================+
| ItemPrompt | Primary Collection   |
+------------+----------------------+
| ColumnName | StaPrimaryCollection |
+------------+----------------------+
| DataKind   | dkAtom               |
+------------+----------------------+
| DataType   | Text                 |
+------------+----------------------+
| LookupName | Primary Collection   |
+------------+----------------------+

The name of the collection used for reporting by the museum or
institution. Each division defined its own collections, which are based
on the collection name, storage location, or collection locality.

Primary collections are used to track the health of the collection over
time, so it's generally best to use the same ones each year. If a new
primary collection is needed, contact the Registrar and Informatics.

Usage
=====

Required for all records, but not the responsibility of the cataloger.
This field is populated annually by the data manager.

--------------------------------------------------------------------------------

.. _ecatalogue-status-inventory-status-inventory-status:

****************
Inventory Status
****************

+------------+------------------------+-------------------------------+-------------------+-------------------------+
| Field      | StaInventoryStatus_tab | StaInventoryRecordedByRef_tab | StaInventoryDate0 | StaInventoryRemarks_tab |
+============+========================+===============================+===================+=========================+
| ItemPrompt | Status                 | Recorded By                   | Date              | Remarks                 |
+------------+------------------------+-------------------------------+-------------------+-------------------------+
| ColumnName | StaInventoryStatus_tab | StaInventoryRecordedByRef_tab | StaInventoryDate0 | StaInventoryRemarks_tab |
+------------+------------------------+-------------------------------+-------------------+-------------------------+
| DataKind   | dkTable                | dkTable                       | dkTable           | dkTable                 |
+------------+------------------------+-------------------------------+-------------------+-------------------------+
| DataType   | Text                   | Reference                     | Date              | Text                    |
+------------+------------------------+-------------------------------+-------------------+-------------------------+
| LookupName | Catalog Inventory      |                               |                   |                         |
|            | Status                 |                               |                   |                         |
+------------+------------------------+-------------------------------+-------------------+-------------------------+
| RefTable   |                        | eparties                      |                   |                         |
+------------+------------------------+-------------------------------+-------------------+-------------------------+

Records an inventory event

Usage
=====

Required for documenting inventories

Format
======

Inventory status, recorded by, and data recorded must be populated in
each row. Status will ultimately be standardized to a small number of
options ("Found" and "Not found" are the only ones that spring to mind
right now). Remarks are optional and can be used to provide more detail
about the inventory.

Inventories are the only actions that should be documented in this grid.
Fields in this grid have been used to document actions like disposals,
exchanges, and transfers between divisions (i.e., recataloging). These
actions should be documented elsewhere. Actions related to transactions,
including loans, dispoals, and exchanges should be documented in the
Transactions module. Recataloged specimens should be documented using
the Relationships tab.

The grid has not been cleaned, and the lookup still contains the non-
preferred values.

Allowed Values
==============

* Found?
* Not Found?

--------------------------------------------------------------------------------

.. _ecatalogue-status-record-status-record-status:

*************
Record Status
*************

+------------+---------------------+----------------------------+----------------+----------------------+
| Field      | StaRecordStatus_tab | StaRecordRecordedByRef_tab | StaRecordDate0 | StaRecordRemarks_tab |
+============+=====================+============================+================+======================+
| ItemPrompt | Record Status       | Recorded By                | Record Date    | Remarks              |
+------------+---------------------+----------------------------+----------------+----------------------+
| ColumnName | StaRecordStatus_tab | StaRecordRecordedByRef_tab | StaRecordDate0 | StaRecordRemarks_tab |
+------------+---------------------+----------------------------+----------------+----------------------+
| DataKind   | dkTable             | dkTable                    | dkTable        | dkTable              |
+------------+---------------------+----------------------------+----------------+----------------------+
| DataType   | Text                | Reference                  | Date           | Text                 |
+------------+---------------------+----------------------------+----------------+----------------------+
| LookupName | Catalog Record      |                            |                |                      |
|            | Status              |                            |                |                      |
+------------+---------------------+----------------------------+----------------+----------------------+
| RefTable   |                     | eparties                   |                |                      |
+------------+---------------------+----------------------------+----------------+----------------------+

Records the source of the EMu record if it was loaded from a previous
database, like Paradox or SELGEM.

Usage
=====

Not used, except to document records imported from previous databases.
In the future, this field may be used to mark records that have been
validated, but the specifics for doing so have not been worked out.
