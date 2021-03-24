.. _orbit-report:

Assignment #6: Orbit Report
===========================

Sections:
---------

#. :ref:`Introduction and Background <orbit-report-intro>`
#. :ref:`Demo GIFs <orbit-report-demo>`
#. :ref:`Setup and Starter Code <orbit-report-setup>`
#. :ref:`Requirements <orbit-report-steps>`
#. :ref:`Bonus Missions <orbit-report-bonus-missions>`
#. :ref:`Submitting Your Work <orbit-report-submitting>`


.. _orbit-report-intro:

Introduction and Background
---------------------------

There are thousands of satellites orbiting the earth. You are tasked with
updating a searchable, sortable table of satellites. For the purposes of this
assignment, a **satellite** will be defined as any object purposefully placed
into orbit.

Your table will have the following features:

#. **Satellites**: Each row in the table contains data on one satellite.
#. **Search form:** Filters search results based on matches to the entered text.
   Pressing enter or clicking the button triggers the search.
#. **Sortable columns:** ``Name`` and ``Type`` column headers can be
   clicked, which will sort the table using that property.
#. **Counts:** Displays the total number of satellites in the table, as well as
   the count for each type of satellite.

Your completed assignment should look something like this:

.. figure:: figures/orbit-report-table.png
   :alt: Screenshot of orbit report table.


.. admonition:: Warning

   Please do not attempt this assignment until after your first lesson on
   Angular. It can be tempting to dive right in, but Angular is a broad topic,
   and you want to wait to have a solid understanding of the framework before you
   get started.


.. _orbit-report-setup:

Setup and Starter Code
----------------------

In `Canvas <https://learn.launchcode.org/>`__, Graded Assignment #6: Orbit Report contains a GitHub Classroom assignment invitation link.
Refer back to the GitHub Classroom instructions from Graded Assignment #0: Hello World for submission instructions.


.. admonition:: Note

	Don't forget to run ``npm install`` before trying to run the starter code.

.. _orbit-report-steps:

Requirements
------------

As you accomplish each task, commit and push your changes before
moving on to the next item.

1) Create Orbit List Component
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. TODO: add orbit-list html to app html


2) Display Table of Satellites
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. TODO: display sats using *ngFor


3) Highlight Space Debris
^^^^^^^^^^^^^^^^^^^^^^^^^

.. TODO: Use css warning class to display space debris types in red. 2 parter
.. pt a: fix space debris check on sat class
.. pt b: add style directive to orbit list html

.. use this to start:

You need to make it easier to spot dangerous space debris in the list. Add an
Angular attribute directive to accomplish this.

#. Add an ``isSpaceDebris`` method to the ``Satellite`` class.

   a. ``isSpaceDebris`` returns a boolean and has no parameters.
   b. ``isSpaceDebris`` returns ``true`` if the satellite ``type`` is
      ``'Space Debris'``, and it returns ``false`` otherwise. Note that this
      check should be case-insensitive.

#. Use ``isSpaceDebris`` to add the ``warning`` CSS class to the ``<td>``
   containing the satellite's type.

   a. For guidance refer to the section on :ref:`changing styles with attribute directives <changing-styles-with-booleans>`.

   .. figure:: figures/table-satellites-with-warning.png
      :alt: Screen shot of browser showing http://localhost:4200 with a table of 9 satellites, with Space Debris cell having a red background.

      Example of warning style adding a red background to Space Debris type.


4) Counting Satellites
^^^^^^^^^^^^^^^^^^^^^^

.. TODO: update innerHTML of orbit-count with number of sats

.. start with this:

Create a new component that shows the total number of satellites currently
displayed in the table. 

#. Create an ``orbit-counts`` component at the same level as ``orbit-list``.

.. TODO: refine this item below: can we remove the exact line to add?

#. Pass in ``displayList`` via ``[satellites]="displayList"``.
#. Add styles to ``orbit-counts.component.css`` to make your count table
   complement the list of satellites, or use the CSS provided in this
   `sample file  <https://gist.github.com/welzie/5247f5ac36e973903cd5202af50932e6>`__.
#. Use the given HTML as a template. Replace the hard-coded count with a directive 
   to display the number of satellites in the displayed table.

   .. sourcecode:: html
      :linenos:

      <h3>Satellite Counts:</h3>
      <div class="counts">
         <div>Total: <span>9</span></div>
      </div>

#. In ``app.component.html``, uncomment the line that adds this component to the page.

.. TODO: update this screenshot and caption for just the top count

#. Your completed component should look similar to:

   .. figure:: figures/orbit-counts-output.png
      :alt: Example of six satellite counts being displayed.

      Example of the seven different satellite counts being displayed.


.. _orbit-report-bonus-missions:

Bonus Missions
--------------

.. TODO: add the count component instructions that are relevant for the countByType() implementation
.. if not relevant, update starter code and solution repo to remove this method? 
.. or keep it for an added element of difficulty

A) Zebra Stripes
^^^^^^^^^^^^^^^^

Alternate the color for every other row in the table. Choose whichever pair
of colors you prefer, but the highlighting for space debris should still be
distinct.

.. figure:: figures/orbit-report-zebra.png
   :alt: Alternating row colors.

B) Update the Search Feature
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Modify the search feature to find matches using the ``orbitType`` and ``type``
properties.

If you completed the counting satellites bonus, use an ``*ngFor`` to loop over
an array of the different types, instead of explicitly writing a ``<tr>`` for
each satellite type.

.. admonition:: Note

   You may have already completed this mission, depending on how you
   accomplished counting the satellites.

.. _orbit-report-submitting:

Submitting Your Work
--------------------

In Canvas, open the Orbit Report assignment and click the "Submit" button.
An input box will appear.

Copy the URL for your Github repository and paste it into the box, then click
"Submit" again.


