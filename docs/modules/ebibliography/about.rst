##################
About Bibliography
##################

The bibliography module stores information about publications associated
with samples from the collection. A bibliography record should contain
enough information to confidently identify a resource. It is not the
definitive record and should ideally be generated from information
provided by the publisher (for example, using the BibTeX record provided
by the DOI resolver).

*************
Data standard
*************

A standard bibliography record should contain the following fields:

* Title
* Author
* Journal name
* Publication year
* Volume (if exists)
* Issue (if exists)
* Pages

To exceed standards, a record should also specify a DOI or other stable
handle in the GUID grid. Records with DOIs are easier to link to
external repositories containing publications data.

************************
Parties in ebibliography
************************

The implementation of bibliography records in Axiell EMu is overly
complex. NMNH Informatics is working with Axiell to simplify this
module, but until that happens, here are some issues that make working
with this module unpleasant:

* Each book and journal requires its own bibliography record
* Each publication type has its own set of backend fields
* Each author, editor, and publisher requires its own party record

The last point creates a significant difficulty for maintaining a clean
Parties module. Parties created solely for use in bibliographic records
are clearly less important than parties for transactors, collectors, or
staff, but are not necessarily easy to distinguish, especially for new
or occasional EMu users. All parties created solely for Bibliography
should therefore contain the following data to help users distinguish
them from legitimate party records:

* **Person/Organization > Source of Information:** Publication
* **Security > Record Status:** Unlisted

It is acceptable to use an existing party record as an author. In this
case, that record **should not** be unlisted or flagged as coming for a
publication.
