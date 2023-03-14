################
About Multimedia
################

*************
Data standard
*************

This section describes a proposed data stanadrd for multimedia in
Mineral Sciences. All categories described here can be determined based
on an EMu export file except the PDF archival format check, which
requires a copy of the document. Note that these standards are stricter
than those currently in use for annual reporting at NMNH.

Some guidelines and vocabularies used to develop this standard include:

* `Basic Guidelines for Minimal Descriptive Embedded Metadata in Digital
  Images <https://sinet.sharepoint.com/sites/NMNH-Team/Encyclopedia-of-L
  ife/Shared%20Documents/GuidelinesEmbeddedMetadata.pdf#search=NAA%20Dig
  ital%20Imaging%20Guidelines>`_ (intranet only)
* `NAA Digital Imaging Guidelines
  <https://sinet.sharepoint.com/sites/NMNH-Team/Encyclopedia-of-Life/Sha
  red%20Documents/Digital%20Imaging%20Guidelines,%20National%20Anthropol
  ogical%20Archives,%20Smithsonian%20Institution.pdf#search=NAA%20Digita
  l%20Imaging%20Guidelines>`_ (intranet only)
* `NAA Digital File Naming Guidelines
  <https://sinet.sharepoint.com/sites/NMNH-Team/Smithsonian-Marine-Stati
  on/Shared%20Documents/NAA_Digital_Filenaming_Guide.pdf#search=NAA%20Di
  gital%20Imaging%20Guidelines>`_ (intranet only)
* `RBMS Genre Terms
  <http://rbms.info/vocabularies/genre/alphabetical_list.htm>`_

File formats (images)
=====================

* **Below**: Proprietary or uncommon file type
* **Meets**: Acceptable archival file format (JPEG, PNG, non-animated
  GIF)
* **Exceeds**: Preferred archival file format (TIFF, no specific byte
  order)

The exact formats specified by the NAA Digital Imaging Guidelines are:

* **Color**: 24-bit RBG color TIFF format with an IBM PC byte order (ICC
  profile = Adobe RGB 1998)
* **Grayscale**: 8-bit Grayscale TIFF format with an IBM PC byte order
  (ICC profile = Gray Gamma 2.2)

Asset quality (images)
======================

* **Below**: The minimum dimension is < 2000 px
* **Meets**: The minimum dimension is >= 2000 px but < 3000 px
* **Exceeds**: The minimum dimension is >= 3000 px

Asset quality (documents)
=========================

* **Below**: The resolution is < 300 dpi
* **Meets**: The resolution is 300 dpi
* **Exceeds**: The resolution is > 300 dpi

PDFs
====

* **Below**: PDF is not archival and/or not searchable
* **Meets**: PDF is archival and searchable

Filenames
=========

* **Below**: Filename is > 255 characters long or contains spaces or
  non-ASCII characters
* **Meets**: Filename is <= 255 characters long and does not contain
  spaces or non-ASCII characters
* **Exceeds**: Filename is <= 64 characters long and follows a standard
  format

Embedded metadata
=================

* **Below**: One or more of the required metadata fields are missing
* **Meets**: All required metadata fields are populated
* **Exceeds**: All recommended metadata fields are populated

The lists of required and recommended IPTC metadata are based on the
Basic Guidelines for Minimal Descriptive Embedded Metadata in Digital
Images.

Required metadata
-----------------

* ObjectName
* Source
* CopyrightNotice
* By-line

Recommended metadata
--------------------

* DateCreated
* Caption-Abstract
* JobID or OriginalTransmissionReference
* Credit
* Keywords
* Headline

**********************
File naming guidelines
**********************

The basic form of the preferred format is
{subject}\_{identifier}\_{description}, where

* **subject** is the general subject of the photo
* **identifier** is the catalog number or range represented in the file
* **description** is a brief, specific description of the content of the
  file

Different subjects of media have different requirements. See the table
below for details.

* Filenames should only use alphanumeric characters, underscores, and
  hyphens. Avoid spaces, other punctuation, and diacritics.
* Filenames should not exceed 64 characters including the file
  extension. Modern OSes support longer filenames, but in practice
  these are unwieldy.
* Filenames should be lowercase. Purely aesthetic.
* Words within within filenames should be separated by underscores. This
  improves readability slightly but is also mostly an aesthetic
  preference.

Common subjects include:

+---------------+---------------------------------------------------------------+---------------------------------------+
| Subject       | General format                                                | Example                               |
+===============+===============================================================+=======================================+
| Accession     | accession\_{accession\_num}\_{description}                    | accession\_2012345\_deed\_of\_gift    |
| documentation |                                                               |                                       |
+---------------+---------------------------------------------------------------+---------------------------------------+
| Catalog card  | catalog\_card\_{catalog\_num}                                 | catalog\_card\_123456-00              |
+---------------+---------------------------------------------------------------+---------------------------------------+
| Meteorite     | datapack\_{meteorite\_num}                                    | datapack\_eet\_83883                  |
| datapack      |                                                               |                                       |
+---------------+---------------------------------------------------------------+---------------------------------------+
| Field notes   | field\_notes\_{last\_name}\_{description}                     | field\_notes\_sorensen\_jan\_1986     |
+---------------+---------------------------------------------------------------+---------------------------------------+
| Ledger        | ledger\_{collection\_name}\_{first\_num-last\_num}            | ledger\_rock\_and\_ore\_110001-110025 |
+---------------+---------------------------------------------------------------+---------------------------------------+
| Loan          | loan\_{transaction\_num}\_{description}                       | loan\_2012346\_insurance\_part\_1     |
| documentation |                                                               |                                       |
+---------------+---------------------------------------------------------------+---------------------------------------+
| Publication   | pub\_{last\_name\_of\_first\_author}\_{year}\_{abbr\_journal} | pub\_melson\_1985\_gca                |
+---------------+---------------------------------------------------------------+---------------------------------------+
| Specimen      | specimen\_{photo\_id}\_{catalog\_num}                         | specimen\_87-45678\_g3551-00          |
| photo         |                                                               |                                       |
+---------------+---------------------------------------------------------------+---------------------------------------+

Some notes about this list:

* This list is not exhaustive, but please see the data manager for
  guidance before adding a new subject
* EMu does not care if two multimedia records share a filename
* More detailed metadata about multimedia should be always be included
  in the Title and Description fields in the EMu record
* Field notes and publications should always have a bibliography record

***********
Open access
***********

The Smithsonian seeks to make as much of its holdings as possible
available under a CC0 license, which allows the public to freely use
information and assets. At a minimum, an asset must meet the following
criteria to be eligible for open access:

* The asset was created by a Smithsonian staff member, contractor, or
  volunteer
* All objects depicted in the asset are owned by the Smithsonian
* No identifiable people are depicted in the asset
* The asset and all objects depicted are out of copyright, not subject
  to moral rights, and otherwise free of contractual restrictions
* The depicted object is not a culturally sensitive

Any of the above criteria (except possibly moral rights) can be waived
by written agreement with the relevant party (i.e., the owner of a
specimen or the holder of the copyright of a photo).

**Warning:** Watch out for incorrect usage of the creator field in EMu.
Some users will list themselves as the creator of an asset even if they
were only responsible for digitizing it.

Exceptions
==========

Meteorites
----------

All meteorite specimen photos meeting the general criteria above should
be published as open access except the following:

* Photos of certain archaeological objects from the meteorite
  collection, notably beads from near Havana, IL associated with the
  Hopewell culture and tagged with the names Brenham, Havana,
  Hopewell, or Hopewell Mounds. (Sensitive content > Native American
  and Native Hawaiian remains and objects)

Mineralogy
----------

All mineral specimen photos meeting the general criteria above should be
published as open access.

In addition to meeting the general criteria above, photos of gems and
jewelry should be approved by the Curator-in-Charge of the gem
collection before being made open access. Considerations when making the
decision about publishing a gem or jewelry photo as open access include:

* **Observing copyright.** Creative/expressive jewelry designs are
  eligible for copyright protection. Copyright protection in the
  United States lasts a long, long time, and eligible objects should
  be assumed to be in copyright unless documentation proving otherwise
  exists. Copyright protection does not extend to standalone gems.
* **Observing moral rights.** A subset of copyrightable works (including
  sculptural works and therefore jewelry) provide artists additional
  protection in the form of moral rights. Among other things, moral
  rights include a right to attribution and a right not be associated
  with distorted versions of their work. Artists typically retain
  moral rights to their work even if they sign over copyright, and
  most copyrightable objects cannot therefore be made open access
  during the lifetime of the artist. Moral rights do not apply to
  photos unless they were made specifically for exhibition.
* **Maintaining relationships with donors.** Donors are the lifeblood
  of the gem collection, and we need to make sure that they are
  comfortable with how assets from this collection are being used.

Petrology & Volcanology
-----------------------

All rock specimen photos meeting the general criteria above should be
published as open access, including photos depicting the Ontanagon
Boulder.
