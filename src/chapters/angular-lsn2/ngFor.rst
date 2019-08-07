``ngFor``
==========

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
-----------------

The example below shows the basic approach for using ``ngFor`` to iterate
through the contents of an array. For a more detailed guide to using ``ngFor``
and all of its variations, refer to the following resources:

#. `Angular documentation <https://angular.io/guide/template-syntax#ngFor>`__,
#. `Malcoded website <https://malcoded.com/posts/angular-ngfor/>`__.

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

By placing the ``*ngFor`` statement inside the tag, the loop generates
multiple ``<li></li>`` elements. Each iteration adds a new list item to the
HTML code, one for each title in the ``movies`` array.

.. admonition:: Warning

   The ``*ngFor`` statement generates a new HTML tag for each item in the
   array. *Be careful where you put the statement!* If we had added
   ``*ngFor = "let movie of movies"`` to the ``<h3>`` tag, then the ``Movies
   To Watch`` title would have been repeated multiple times.

In general, the syntax for ``*ngFor`` is:

::

   *ngFor = "let variableName of arrayName"

Where ``variableName`` is the loop variable, and ``arrayName`` represents the
array to iterate through.

``*ngFor`` only operates over the contents of an array. If we want to iterate
over the characters in a string or the key/value pairs in an object, then we
must first convert them into arrays.

Try It
-------

From the ``lesson2`` folder in VSCode, open the
``examples/ngfor-practice/src/app/chores`` folders and select the
``chores.component.html`` file.

.. figure:: ./figures/ngfor-menu.png
   :alt: Access ngFor practice in VSCode.

The starter code should match this:

.. sourcecode:: html
   :linenos:

   <div class='chores'>
      <h3>Chores To Do Today</h3>
      <ul>
         <li>{{chores[0]}}</li>
         <li>{{chores[1]}}</li>
         <li>{{chores[2]}}</li>
      </ul>
      <hr>
   </div>

In the VSCode terminal window, navigate to the ``ngfor-practice`` folder.

.. sourcecode:: bash

   $ pwd
      angular-lc101-projects/lesson2
   $ ls
      examples        exercises       studio
   $ cd examples
   $ ls
      ngfor-practice  ngif-practice
   $ cd ngfor-practice

Enter ``ng serve`` to launch the project, then:

#. Modify ``chores.component.html`` with ``*ngFor`` to loop over the items
   stored inside the ``chores`` array.
#. Open ``chores.component.ts``. Add or remove items to the ``chores``
   array, then save. Reload the webpage to make sure your changes appear.
#. Use ``*ngFor`` within the ``<div>`` tag to loop over the ``todoTitles``
   array. Replace "Chores To Do Today" with the elements of the array.
#. Return to ``chores.component.ts``. Add or remove items to the
   ``todoTitles`` array, then save. Check to make sure your changes appear on
   the webpage.

Properly done, your page should look something like:

.. figure:: ./figures/chore-list-solution.png
   :alt: *ngFor practice solution.

What If
^^^^^^^^

#. What if you placed the ``*ngFor`` statement inside the ``<h3>`` tag instead
   of the ``<div>`` tag? Try it and see what happens!
#. What if you placed the statement inside the ``<ul>`` tag instead? Try it!

Bonus What If
~~~~~~~~~~~~~~

What if we want to have different chores listed for Yesterday, Today, and
Tomorrow?

.. figure:: ./figures/chore-bonus-solution.png
   :alt: *ngFor bonus solution.

Accomplishing this task is OPTIONAL. If you are curious about how to make the
updates, switch to the ``bonus-solutions`` branch and check the code in the
``ngfor-practice`` folder. Explore how to use ``index`` in ``*ngFor``.

#. Line 1 in ``chores.component.html`` shows how to set a variable equal to an
   index value from the ``todoTitles`` array.
#. Line 4 in ``chores.component.html`` shows the syntax for using the index
   variable to access the content within the ``chores`` array.
#. Line 9 in ``chores.component.ts`` shows the 2-dimensional array of the chore
   list items.

Check Your Understanding
--------------------------

The following questions refer to this code sample:

.. sourcecode:: html
   :linenos:

   <div>
      <h3>My Pets</h3>
      <ul>
         <li>{{pet}}</li>
      </ul>
   </div>

Assume that we have defined a ``pets`` array that contains 4 animals.

.. admonition:: Question

   Adding ``*ngFor = 'let pet of pets'`` to the ``<li>`` tag produces:

   #. 4 headings
   #. 4 unordered lists
   #. 4 list items
   #. 4 headings each with 4 list items

.. admonition:: Question

   Moving ``*ngFor = 'let pet of pets'`` from the ``<li>`` tag to the ``<div>``
   tag produces:

   #. 1 heading and 4 unordered lists with 4 pets each
   #. 4 headings and 4 unordered lists with 4 pets each
   #. 1 heading and 4 unordered lists with 1 pet each
   #. 4 headings and 4 unordered lists with 1 pet each
