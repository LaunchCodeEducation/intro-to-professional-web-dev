Angular Directives
===================

.. index:: ! directive

Angular manages website content through the use of *directives*, and there
are three types:

#. **Components**: These control how a set of data gets displayed within a
   template.
#. **Structural directives**: These change the layout of the DOM by adding or
   removing elements (``div``, ``ul``, ``a``, ``li``, etc.).
#. **Attribute directives**: These change the appearance of a specific element
   within the DOM.

We learned how to generate and modify components in the
:ref:`last chapter <angular-1>`. In this lesson, we will focus on how to use
structural directives to enhance our work.

``ngFor``
----------

In the :ref:`Angular lesson 1 exercises <angular-exercises-1>`, you modified
a ``movie-list`` component to display a series of titles. The final code
within ``movie-list.component.html`` probably looked something like:

.. sourcecode:: html
   :linenos:

   <div class='movies'>
      <h3>Movies to Watch</h3>
      <ol>
         <li>{{movies[0]}}</li>
         <li>{{movies[1]}}</li>
         <li>{{movies[2]}}</li>
         <li>{{movies[3]}}</li>
      </ol>
   </div>

``movies[0]`` - ``movies[3]`` reference an array assigned within the
``movie-list.component.ts`` file.

To change the number of movie titles displayed in the ordered list, we could
manually add or remove ``li`` tags, or we could use the structural directive
``ngFor`` to iterate through the movie options.

``ngFor`` Syntax
^^^^^^^^^^^^^^^^^

The example discussed below shows how use ``ngFor`` to iterate through the
contents of an array. For a complete guide to using ``ngFor`` and all of its
variations, refer to the
`Angular documentation <https://angular.io/guide/template-syntax#ngFor>`__.

Just like a ``for`` loop in JavaScript requires a specific syntax in order to
operate, loops in Angular must follow a set of rules. Let's explore these rules
by adding ``ngFor`` to our movie list code.

.. sourcecode:: html+ng2
   :linenos:

   <div class='movies'>
      <h3>Movies to Watch</h3>
      <ol>
         <li *ngFor = "let movie of movies">{{movie}}</li>
      </ol>
   </div>

Some items to note:

#. Structural directives all begin with the ``*`` symbol.
#. The string ``"let movie of movies"`` provides the instructions
   for running the loop.

   a. The ``let`` keyword declares the ``movie`` variable.
   b. ``of movies`` sets ``movie`` equal to the first element of the ``movies``
      array. Each iteration of the loop sets ``movie`` equal to the next title
      in the array.

#. The ``*ngFor`` statement is placed INSIDE the ``<li>`` tag.
#. ``{{movie}}`` is the placeholder for the current value of ``movie``.

By placing the ``*ngFor`` statement inside the list tag, the loop generates
multiple ``<li></li>`` pairs. Each iteration adds a new list item to the
HTML code, one for each title in the ``movies`` array.

In general, the syntax for ``*ngFor`` is:

::

   *ngFor = "let variableName of collection"

Where ``variableName`` is the loop variable, and ``collection`` represents the
string, array, or object to iterate through.

Try It
^^^^^^^

Fork the Angular Lesson 2 starter code and open the project in VSCode. Use the
terminal to switch to the ``ngFor-practice`` branch.

.. todo:: Add link to Angular Lesson 2 starter code.

The starter code inside ``chore-list.component.html`` should match this:

.. sourcecode:: html
   :linenos:

   <div>
      <h3>Chores To Do Today</h3>
      <ul>
         <li>{{chores[0]}}</li>
         <li>{{chores[1]}}</li>
         <li>{{chores[2]}}</li>
      </ul>
      <hr>
   </div>

Enter ``ng serve`` in the VSCode terminal window to launch the project, then:

#. Modify ``chore-list.component.html`` with ``*ngFor`` to loop over the items
   stored inside the ``chores`` array.
#. Open ``chore-list.component.ts``. Add or remove items to the ``chores``
   array, then save. Reload the webpage to make sure your changes appear.
#. Use ``*ngFor`` within the ``<div>`` tag to loop over the ``todoTitles``
   array. Replace "Chores To Do Today" with the elements of the array.
#. Return to ``chore-list.component.ts``. Add or remove items to the
   ``todoTitles`` array, then save. Check to make sure your changes appear on
   the webpage.

Properly done, your page should look something like:

.. todo:: Add screenshot of lesson 2, example 1 results.

Using ``ngFor`` With Conditions
--------------------------------

Sometimes we do not need to display every item in a collection, and for these
cases Angular allows us to modify the loop.

Check Your Understanding
--------------------------

Lorem ipsum...
