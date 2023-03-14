#####################
ecatalogue > Security
#####################

This tab controls who can view and modify a given record. Most fields
are grayed out and not accessible to normal users.

--------------------------------------------------------------------------------

.. _ecatalogue-security-access-record-status:

*************
Record Status
*************

+----------+----------------------+
|Field     |Value                 |
+==========+======================+
|ItemPrompt|Record Status:        |
+----------+----------------------+
|ColumnName|SecRecordStatus       |
+----------+----------------------+
|DataKind  |dkAtom                |
+----------+----------------------+
|DataType  |Text                  |
+----------+----------------------+
|LookupName|Security Record Status|
+----------+----------------------+

The status of the record

Usage
=====

Required

Format
======

The record status field is a first-order indication of whether a record:

* Corresponds to an active or retired collections object
* Is the preferred record if many similar records are available
* Conforms to minimal standards for data quality


Acceptable statuses are defined as follows:

* **Active** indicates that a record corresponds to a collections object
  or related data. By default, only Active records show up in search
  results.
* **Cancelled** indicates that a record was created in error but should
  be preserved
* **Legacy** indicates that a record was migrated from a legacy database
  and needs to be properly integrated into EMu
* **Removed** indicates that a record is ready for deletion
* **Retired** indicates that a record represents an object no longer in
  the collection
* **Unlisted** indicates that a record has valid uses but should not be
  used in normal operations (for example, author records in parties)


The following statuses may appear in EMu but should not be used:

* Depleted
* Inactive
* Not Reviewed
* Secured
* TM


By default, only Active records show up in search results. In general,
any record that is in regular use should be classified as Active.

Allowed Values
==============

* Active
* Cancelled
* Legacy
* Removed
* Retired
* Unlisted

--------------------------------------------------------------------------------

.. _ecatalogue-security-access-publish-on-internet:

*******************
Publish on Internet
*******************

+----------+-----------------------+
|Field     |Value                  |
+==========+=======================+
|ColumnName|AdmPublishWebNoPassword|
+----------+-----------------------+
|DataKind  |dkAtom                 |
+----------+-----------------------+
|DataType  |Text                   |
+----------+-----------------------+

Sets whether the record can be published to public-facing systems

Usage
=====

Required

Allowed Values
==============

* Yes
* No

--------------------------------------------------------------------------------

.. _ecatalogue-security-access-publish-on-intranet:

*******************
Publish on Intranet
*******************

+----------+-----------------------+
|Field     |Value                  |
+==========+=======================+
|ColumnName|AdmPublishWebNoPassword|
+----------+-----------------------+
|DataKind  |dkAtom                 |
+----------+-----------------------+
|DataType  |Text                   |
+----------+-----------------------+

Sets whether the record can published to intranet-only systems

Usage
=====

Required

Allowed Values
==============

* Yes
* No
