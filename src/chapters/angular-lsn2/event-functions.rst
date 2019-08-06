Events Can Call Functions
==========================

For the user input practice, we set the ``keyup`` and ``click`` events equal to
``true``. This just checks to see if these events occur. When they do, the
input is stored in ``newMovie``, and the page refreshes.

To perform more complicated tasks in response to the user's actions, we can
call a function when an event occurs. The syntax for this is:

::

   (event) = 'functionName(parameters...)'

Changing the movie list displayed on the webpage requires us to modify the
``movies`` array in the ``movie-list.component.ts`` file. We will do this by
creating an ``addMovie`` function and linking it to our event handlers.

Modify the HTML
----------------

Let's change our code in ``movie-list.component.html`` to call the function
``addMovie`` and pass the new movie title as the argument.

#. On lines 7 and 8, replace ``true`` with the function call:

   .. sourcecode:: html+ng2
      :linenos:

      <div class='movies col-4'>
         <h3>Movies to Watch</h3>
         <ol>
            <li *ngFor ="let movie of movies">{{movie}}</li>
         </ol>
         <hr>
         <input #newMovie (keyup.enter)='addMovie(newMovie.value)' type='text' placeholder="Enter Movie Title Here"/>
         <button (click)='addMovie(newMovie.value)'>Add</button>
         <p>{{newMovie.value}}</p>
      </div>

   Now when the user taps "Enter" or clicks the "Add" button after typing, the
   input ``newMovie.value`` gets sent to the function.

#. Remove the ``<p>{{newMovie.value}}</p>`` from line 9, since the new title
   should appear on the list instead of below the box.

Define the Function
--------------------

Open ``movie-list.component.ts`` and examine the code:

.. sourcecode:: TypeScript
   :linenos:

   import { Component, OnInit } from '@angular/core';

   @Component({
      selector: 'movie-list',
      templateUrl: './movie-list.component.html',
      styleUrls: ['./movie-list.component.css']
   })
   export class MovieListComponent implements OnInit {
      movies = ['Toy Story', 'The Shining', 'Sleepless in Seattle', 'The Martian'];

      constructor() { }

      ngOnInit() {
      }
   }

The ``movies`` array stores the titles displayed on the webpage, and we want to
update this when the user supplies new information.

3. Declare a function called ``addMovie`` that takes one parameter:

   .. sourcecode:: TypeScript
      :linenos:

      export class MovieListComponent implements OnInit {
         movies = ['Toy Story', 'The Shining', 'Sleepless in Seattle', 'The Martian'];

         addMovie (newTitle: string) {

         }

         constructor() { }

         ngOnInit() {
         }
      }

   Notice that we have to declare the data type for the ``newTitle`` parameter.

#. Now add code to add the new title to the ``movies`` array:

   .. sourcecode:: TypeScript
      :linenos:

      export class MovieListComponent implements OnInit {
         movies = ['Toy Story', 'The Shining', 'Sleepless in Seattle', 'The Martian'];

         addMovie (newTitle: string) {
            this.movies.push(newTitle);
            return;
         }

         constructor() { }

         ngOnInit() {
         }
      }

   The keyword ``this`` is required.

Save the changes and then refresh the page. Enter a new title to verify that it
appears in the movie list. Your page should look something like:

.. figure:: ./figures/new-movie-added.png
   :alt: Updated movie list.

Tidying Up the Display
-----------------------

Notice that after adding a new movie to the list, the text remains in the input
box. If we click "Add" multiple times in a row, we would see something like:

.. figure:: ./figures/repeated-movie.png
   :alt: Same movie added multiple times.

Let's modify the code to try to prevent this from happening.

Clear the Input Box
^^^^^^^^^^^^^^^^^^^^

5. After the user submits a new title, we can clear the input box by setting its
   value to be the empty string (``""``). Open ``movie-list.component.html``
   and modify the input statement as follows:

   .. sourcecode:: html+ng2

      <input #newMovie (keyup.enter)='addMovie(newMovie.value); newMovie.value = ""' type='text' placeholder="Enter Movie Title Here"/>

   When ``keyup.enter`` occurs, the code calls ``addMovie``. Once control
   returns from the function, ``newMovie.value`` is set equal to ``""``, which
   clears any text from the input box.

#. Since the user can also click the "Add" button to submit a title, we need to
   modify the ``<button>`` element as well:

   .. sourcecode:: html+ng2

      <button (click)='addMovie(newMovie.value); newMovie.value = ""'>Add</button>

   Now ``newMovie.value`` is set equal to ``""``, when "Enter" or "Add" are used
   to submit data.

.. admonition:: Try It

   Refresh the page and verify that the input box gets cleared after each new
   title.

Check for Duplicates
^^^^^^^^^^^^^^^^^^^^^

Even though we clear the input box, there is nothing to prevent the user from
entering the same movie multiple times. While some fans may want to watch a
film twenty times in a row, let's have our code prevent repeats.

Recall that the :ref:`includes method <includes-examples>` checks if an array
contains a particular element. The method gives us several ways to check for a
repeated title. One possibility is:

.. sourcecode:: TypeScript
   :linenos:

   addMovie (newTitle: string) {
      if(!this.movies.includes(newMovie)){
         this.movies.push(newMovie);
      }
      return;
   }

If the ``movies`` array already contains ``newMovie``, then the ``includes``
method returns ``true``. The NOT operator (``!``) flips the result to
``false``, and line 3 is skipped.

.. admonition:: Note

   If using the NOT operator bothers you, try:

   #. ``if(this.movies.includes(newMovie)===false)``,
   #. Use ``if(this.movies.includes(newMovie))``, and update lines 3 - 5 to
      respond properly when the condition is ``true``.

.. admonition:: Try It

   Refresh the page and verify that you cannot enter a duplicate title.

Bonus
------

To boost your skills, try these optional tasks to enhance your work:

#. Modify ``addMovie`` to reject the empty string as a title.
#. Use ``*ngIf`` to display an error message if the user does not enter a title
   or submits a title that is already on the list.
#. Add CSS to change the color of the error message.

Check Your Understanding
-------------------------

Lorem ipsum...
