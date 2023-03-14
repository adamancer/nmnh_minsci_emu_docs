Parties Data Standard
=====================

Draft set of standards for Mineral Sciences parties records.

About ----- The parties module is the primary repository for information
about the people and organizations the Mineral Sciences department
transacts with.

Organizations
-------------

Organizations include universities, government agencies, and companies.
Many transactions are officially between the museum and an organization.
Organization records must therefore:

1. Be specific enough to uniquely identify the organization 2. Provide a
way to contact the organization if the original transaction contact
can't be reached

Organization records imported during the TM merge typically only include
the highest level name (i.e., the name of the university but not the
specific department). More detailed information is included in the
address field. This structures has several practical drawbacks in EMu:

* It is not possible to distinguish records from different departments
  in the same organization using the summary line

Correcting these records is difficult and remains a long-term project
for the department.

### Standard

A standard organization record should include the following information:

* Organization name
* Complete organization address
* Email address or phone number

### Guidelines

* Update the primary party record for an organization when you find
  changes
* For very large organizations, especially those with locations in
  different states or countries, each location should have its own
  record
* It is not necessary or desirable to fill out the full organizational
  hierarchy for government agencies. For example, records for the U. S.
  Geological Survey do not need to specify that the USGS is part of the
  Department of the Interior.
* **When organizations changes names:** An organization may change names
  for branding purposes or when it merges another organization. In the
  former case, we recommended updating the organization record to
  reflect the change. In the latter case, we recommended keeping the
  legacy record.

People
------

Records for individuals are used to track museum personnel (catalogers,
collection managers, etc.), collectors, authors, transaction contacts,
and a million other things. All parties records are held to the standard
required for transactions *except* records only used as authors/editors
in the bibliography module.

**The privacy implications of this policy need to be investigated. From
a privacy standpoint, maintaining address and contact info without a
compelling business interest (in NMNH's case, a recent or active
transaction) is probably not a good idea, and this kind of information
should only be maintained for parties who have open transactions or who
have transacted with the museum within the past few years. The
guidelines below assume that maintaining accurate contact info
indefinitely is sound policy.**

### Standard

A standard person record should include the following information:

* Full first and last name
* One or more affiliations
* Complete address
* Email address or phone number

### Guidelines

* Always update the primary party record for person when you find a new
  affiliation address, phone number, etc. Do not only note these changes
  in the notes field of the transaction module!
* Most parties, but especially those used as contacts for transactions,
  should specify an organizational affiliation. The specific
  affiliation (department, branch, etc.) should be included in the
  Street Address field of the Shipping/Mailing Address field groups.
* Most parties, but especially those used as contacts for transactions,
  should specify a phone number or email address
* People who change affiliations should not have a record for each
  historical affiliation. Past affiliations can be included in the
  Affiliations grid with the Current radio button set to No.
* People who have more than one current affiliation are allowed a record
  for each affiliation (provided that you expect the museum to
  transact with them in each of their various hats). This does pose a
  data management headache, and an alternative approach is to set up
  transactions through their organization while listing them as a
  contact.
* **Authors**: Parties created solely to populate a Bibliography record
  do not need to include anything beyond the short form of their name.
  They should be given a Record Status of Unlisted on the Security tab
  to distinguish them from more legitimate party records.

Record statuses
---------------

* **Active:** The party is staff, a collector, or has transacted with
  the museum. Note that the record is only active in a database sense
  --the party themself may be retired or deceased.
* **Legacy:** The party was migrated from TM but has not been harmonized
  with existing records. A given party may have more than one legacy
  record.
* **Removed:** The party is not linked anywhere in EMu and can be
  deleted, if desired.
* **Unlisted:** Reserved for authors/editors. The party only occurs in
  the Bibliography module and is hidden from the default search. It
  should not be linked to a transaction without (1) verifying that the
  name refers to the same entity and (2) filling out biographical
  details.

Roles
-----

To help identify records to exclude from upkeep (merges, etc.), we use
the Roles grid on the ---- tab. This grid is populated using an external
script and currently contains the following roles:

* Author
* Cataloger
* Gem cutter
* Gem/jewelry maker
* Transactor (Acquisition)
* Transactor (Loan/Disposal)

Records with no roles or that only list author should be checked
manually. Records that aren't attached anywhere can be deleted or marked
as Removed. Author-only records can be marked as Unlisted.
**Organizations are not currently assigned roles.**
