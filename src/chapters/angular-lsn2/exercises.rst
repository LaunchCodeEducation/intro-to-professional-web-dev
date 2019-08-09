Exercises: Angular, Lesson 2
=============================

Let's build an interactive webpage that allows us to review data for our
astronaut candidates and select crew members for a space mission.

Starter Code
-------------

From the ``lesson2`` folder in VSCode, navigate into the
``exercises/src/app/candidates`` folder. Open the
``candidates.component.html`` file.

.. figure:: ./figures/lesson2-exercises-menu.png
   :alt: Access lesson 2 exercises in VSCode.

The code should look like:

   Code sample here...

In the terminal, navigate into the lesson 2 ``exercises`` folder. Enter
``npm install`` to add the Angular modules, then run ``ng serve``. The webpage
should look like this:

   Add lesson2-exercises-start.png...

Candidates Column
------------------

Examine the ``candidates`` array in ``candidates.component.ts``. It contains
one object for each animal astronaut. We want to start by listing the names of
the animals in the "Candidates" column of the webpage.

#. Find the "Candidates" section in ``candidates.component.html``. Use
   ``*ngFor`` in the ``<li>`` tag to loop over the ``candidates`` array and
   display each name in an ordered list.
#. We want each name to be interactive. Add a ``click`` event to the ``<li>``
   tag. When a user clicks on a name, set the variable ``selected`` to be equal
   to the chosen candidate.

Properly done, your output should behave something like this:

.. figure:: ./figures/lesson2-exercises-candidates.gif
   :alt: Candidate results.

Candidate Data Column
----------------------

When we click on a candidate's name, we want their information to appear in the
"Candidate Data" column. If no candidate is selected, we want the space under
the heading to remain blank.

#. In the ``<p></p>`` element underneath the "Candidate Data" heading, add
   labels for a candidate's ``Name``, ``Age``, ``Mass``, and ``Sidekick``.
#. Add placeholders to display the candidate's data next to each label.
#. Use ``*ngIf`` inside the ``<p>`` tag to check if a candidate has been
   selected. If so, display the labels and the data.
#. Next, create a way to clear the data. In the ``<button>`` tag for "Clear
   Data & Image", add a ``click`` event that sets ``selected`` to ``false``.

Properly done, your output should behave something like this:

.. figure:: ./figures/lesson2-exercises-candidate-data.gif
   :alt: Candidate Data results.

Sidekick Image Column
----------------------

Every good hero needs a loyal sidekick, and our candidates are no exception!

When we click on a candidate's name, we want an image of their sidekick to
appear under the "Sidekick" column. If no candidate is selected, we want this
area to remain blank.

#. In the ``<img>`` tag, use ``*ngIf`` to check if a candidate has been
   selected.
#. Replace the generic ``{{placeholder}}`` with the ``image`` property of the
   candidate.

Properly done, your output should behave something like this:

.. figure:: ./figures/lesson2-exercises-sidekicks.gif
   :alt: Sidekick image results.
