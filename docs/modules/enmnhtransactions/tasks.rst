#########################
enmnhtransactions > Tasks
#########################

This tab is used to note tasks that need to be performed at a later date
to complete a transaction or improve the transaction record. Tasks may
include:

* Adding or modifying data to ensure that the transaction record is
  accurate and complete
* Cataloging an acquisition
* Closing a loan after a condition has been met (for example, after one
  year if specimens are reported lost)

Because tasks may not be completed for years and contacts for individual
collections may change over time, the best practice is to assign all
tasks to Position records created for this purpose. The position records
can be found by searching the Parties module using Party Type =
"Position". Records have been created for each of the four collection
managers (which will direct the task to the current collection manager)
and the registrar (which will direct the request to the NMNH-
MinSciRegistrar resource account).

--------------------------------------------------------------------------------

.. _enmnhtransactions-tasks-task-information-description:

***********
Description
***********

+------------+--------------------+
| Field      | Value              |
+============+====================+
| ItemPrompt | Task Description   |
+------------+--------------------+
| ColumnName | TasDescription_tab |
+------------+--------------------+
| DataKind   | dkTable            |
+------------+--------------------+
| DataType   | Text               |
+------------+--------------------+

A description of the task to be performed

Usage
=====

Required when task is created

Format
======

**Provisional guidance**

Description should start with an upper-case key phrase in square
brackets that describes the type of task. Additional information can
follow if needed.

Bracketed key phrases under consideration include:

* [CATALOGING PENDING] describes an acquisition that needs to be
  catalogued and reconciled. This is used to identify records
  representing the backlog.
* [DATA PENDING] describes an outgoing loan for which no data has been
  returned
* [ACTION PENDING] describes any other action that must be completed at
  a later date

Key phrases would be used for searching/reporting and must be entered
exactly.

Examples
========

* [CATALOGING PENDING] Collection of roughly 400 object stored in the NW
  corner of E433
* [DATA PENDING]
* [ACTION PENDING] Close if recipient can not locate samples within one
  year

--------------------------------------------------------------------------------

.. _enmnhtransactions-tasks-task-information-assigned-to:

***********
Assigned To
***********

+------------+--------------------------------+
| Field      | Value                          |
+============+================================+
| ItemPrompt | Person Assigned To Task        |
+------------+--------------------------------+
| ColumnName | TasPersonAssignedToRef_nesttab |
+------------+--------------------------------+
| DataKind   | dkNested                       |
+------------+--------------------------------+
| DataType   | Reference                      |
+------------+--------------------------------+
| RefTable   | eparties                       |
+------------+--------------------------------+

The position of the person responsible for completing the task

Usage
=====

Required when task is created

Format
======

Reference to Parties. Best practice is to link to the position record in
Parties for the appropriate collection manager

--------------------------------------------------------------------------------

.. _enmnhtransactions-tasks-task-information-assigned-by:

***********
Assigned By
***********

+------------+------------------------+
| Field      | Value                  |
+============+========================+
| ItemPrompt | Task Assigner          |
+------------+------------------------+
| ColumnName | TasTaskAssignerRef_tab |
+------------+------------------------+
| DataKind   | dkTable                |
+------------+------------------------+
| DataType   | Reference              |
+------------+------------------------+
| RefTable   | eparties               |
+------------+------------------------+

The person who assigned the task

Usage
=====

Required when task is created

Format
======

Reference to Parties

--------------------------------------------------------------------------------

.. _enmnhtransactions-tasks-task-information-result:

******
Result
******

+------------+----------------+
| Field      | Value          |
+============+================+
| ItemPrompt | Task Results   |
+------------+----------------+
| ColumnName | TasResults_tab |
+------------+----------------+
| DataKind   | dkTable        |
+------------+----------------+
| DataType   | Text           |
+------------+----------------+

The result of the task once completed

Usage
=====

Required when task is completed

Format
======

Provide a brief description of the result of the task, including metrics
if applicable (for example, the number of catalog records created). If
the task will not be completed (for example, if a loan recipient locates
missing specimens before a transaction is scheduled to be closed
unbalanced), note why the task was not performed.

--------------------------------------------------------------------------------

.. _enmnhtransactions-tasks-commencement-start-date:

**********
Start Date
**********

+------------+----------------------+
| Field      | Value                |
+============+======================+
| ItemPrompt | Commencement Date    |
+------------+----------------------+
| ColumnName | TasCommencementDate0 |
+------------+----------------------+
| DataKind   | dkTable              |
+------------+----------------------+
| DataType   | Date                 |
+------------+----------------------+

The date on which to start the task

Usage
=====

Required for time-dependent tasks (like closing a loan after a certain
amount of time)

Format
======

--------------------------------------------------------------------------------

.. _enmnhtransactions-tasks-commencement-notify-on:

*********
Notify On
*********

+------------+---------------------+
| Field      | Value               |
+============+=====================+
| ItemPrompt | Notify Date         |
+------------+---------------------+
| ColumnName | TasStartNotifyDate0 |
+------------+---------------------+
| DataKind   | dkTable             |
+------------+---------------------+
| DataType   | Date                |
+------------+---------------------+

The date on which to notify the contacts in the associated Notify grid

Usage
=====

Required for time-dependent tasks (like closing a loan after a certain
amount of time)

Format
======

--------------------------------------------------------------------------------

.. _enmnhtransactions-tasks-commencement-notify:

******
Notify
******

+------------+------------------------------+
| Field      | Value                        |
+============+==============================+
| ItemPrompt | Commemcement                 |
+------------+------------------------------+
| ColumnName | TasCommenceNotifyRef_nesttab |
+------------+------------------------------+
| DataKind   | dkNested                     |
+------------+------------------------------+
| DataType   | Reference                    |
+------------+------------------------------+
| RefTable   | eparties                     |
+------------+------------------------------+

List of positions to notify when the task is due to start

Usage
=====

Required for time-dependent tasks (like closing a loan after a certain
amount of time)

Format
======

Reference to Parties. Include the Mineral Sciences registrar at a
minimum. Consider also including the appropriate collection manager.

--------------------------------------------------------------------------------

.. _enmnhtransactions-tasks-completion-completed:

*********
Completed
*********

+------------+------------------+
| Field      | Value            |
+============+==================+
| ItemPrompt | Completed?       |
+------------+------------------+
| ColumnName | TasCompleted_tab |
+------------+------------------+
| DataKind   | dkTable          |
+------------+------------------+
| DataType   | Text             |
+------------+------------------+

Whether the task has been completed

Usage
=====

Required when task is created

Format
======

Yes if the task has been completed, No otherwise.

Note that you should use Yes even if the assigned action did not need to
be completed after all (for example, if a loan recipient locates missing
specimens before a transaction is scheduled to be closed unbalanced).

--------------------------------------------------------------------------------

.. _enmnhtransactions-tasks-completion-hours-taken:

***********
Hours Taken
***********

+------------+------------------------+
| Field      | Value                  |
+============+========================+
| ItemPrompt | Time Taken On Task     |
+------------+------------------------+
| ColumnName | TasTimeTakenOnTask_tab |
+------------+------------------------+
| DataKind   | dkTable                |
+------------+------------------------+
| DataType   | Float                  |
+------------+------------------------+

Not used

--------------------------------------------------------------------------------

.. _enmnhtransactions-tasks-completion-end-date:

********
End Date
********

+------------+--------------------+
| Field      | Value              |
+============+====================+
| ItemPrompt | Completion Date    |
+------------+--------------------+
| ColumnName | TasCompletionDate0 |
+------------+--------------------+
| DataKind   | dkTable            |
+------------+--------------------+
| DataType   | Date               |
+------------+--------------------+

The date on which the task was completed

Usage
=====

Required when the task is completed

Format
======

--------------------------------------------------------------------------------

.. _enmnhtransactions-tasks-completion-notify-on:

*********
Notify On
*********

+------------+-------------------+
| Field      | Value             |
+============+===================+
| ItemPrompt | Notify Date       |
+------------+-------------------+
| ColumnName | TasEndNotifyDate0 |
+------------+-------------------+
| DataKind   | dkTable           |
+------------+-------------------+
| DataType   | Date              |
+------------+-------------------+

Not used

--------------------------------------------------------------------------------

.. _enmnhtransactions-tasks-completion-notify:

******
Notify
******

+------------+--------------------------------+
| Field      | Value                          |
+============+================================+
| ItemPrompt | Completion                     |
+------------+--------------------------------+
| ColumnName | TasCompletionNotifyRef_nesttab |
+------------+--------------------------------+
| DataKind   | dkNested                       |
+------------+--------------------------------+
| DataType   | Reference                      |
+------------+--------------------------------+
| RefTable   | eparties                       |
+------------+--------------------------------+

Not used
