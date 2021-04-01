.. _angular-lsn1-exercise-solutions:

Exercise Solutions: Angular, Lesson 1
=====================================

Part 1: Modify the CSS
-----------------------

.. _angular-lsn1-exercise-solutionsA1:

1. Change the movie list text by adjusting the code in
   ``movie-list.component.css`` to accomplish the following:

   a. The text for the heading and list items can be any color EXCEPT black.
      (HINT: Take advantage of the ``movies`` class).
   b. The movie list should have a centered heading.
   c. The font size should be large enough to easily read.


   .. sourcecode:: css
      :linenos:

      .movies {
         color: purple;
         font-size: 1.3vw;
      }

      h3 {
         text-align: center;
      }

   :ref:`Back to the exercises <angular-exercises-1>`

.. _angular-lsn1-exercise-solutionsA3:

Add More Movies
^^^^^^^^^^^^^^^

3. Add two more items to the ``movies`` array.

   .. sourcecode:: TypeScript

      movies = ['The Manchurian Candidate', 'Oceans 8', 'The Incredibles', 'Hidden Figures'];

   :ref:`Back to the exercises <angular-exercises-1>`

.. _angular-lsn1-exercise-solutionsA5:

Complete the ``fav-photos`` Component
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

5. The ``fav-photos`` component has been generated, but it is incomplete. The
   page needs more images, which also need to be smaller in size.

   a. In the ``FavPhotosComponent`` class, assign a better section heading to
      the ``photosTitle`` variable.

      .. sourcecode:: TypeScript

         photosTitle = 'Random Images';

   c. In the ``.html`` file for this component, use placeholders in the ``img``
      tags to display your chosen images.

      .. sourcecode:: html

         <img src="{{image1}}" alt="Oops! Missing photo!">

   e. Use the ``.css`` file for this component to make all the images be the
      same size.

      .. sourcecode:: css

         img {
            width: 40%;
            height: auto;
         }

   :ref:`Back to the exercises <angular-exercises-1>`

.. _angular-lsn1-exercise-solutionsB7:

Part 2: Add More Components
---------------------------

7. The page needs a set of links to favorite websites.

   a. Generate a ``fav-links`` component. Open ``fav-links.component.ts`` and
      shorten the tag name to just ``fav-links``.

      .. sourcecode:: TypeScript

         @Component({
            selector: 'fav-links',
            templateUrl: './fav-links.component.html',
            styleUrls: ['./fav-links.component.css']
         })
   
   c. Inside each ``<a>`` tag, set the ``href`` attribute equal to a
      placeholder for an element in the ``favLinks`` array:

      .. sourcecode:: html

         <a href = "{{favLinks[0]}}">LaunchCode</a> <br>
         <a href = "{{favLinks[1]}}">WebElements</a>
   
   :ref:`Back to the exercises <angular-exercises-1>`

.. _angular-lsn1-exercise-solutionsC8:

Part 3: Rearrange the Components
--------------------------------

8. Rearrange the tags ``fav-photos``, ``fav-links``, ``page-title``, etc. to
   create a specific page layout:

   a. ``app.component.html`` has ``<div>`` tags to set up a three-column row.
      Use this to arrange the movie list, images, and chore list.
   
      .. sourcecode:: html

         <div class="col-3">
            <movie-list></movie-list>
         </div>

         <div class="col-3">
            <fav-photos></fav-photos>
         </div>

         <div class="col-3">
            <chores-list></chores-list>
         </div>

   c. Add a horizontal line below the three lists with the ``<hr>`` tag.

      .. sourcecode:: html

         <!-- three lists are here -->
         </div>
         <hr>
         <fav-links></fav-links>

   :ref:`Back to the exercises <angular-exercises-1>`
   
   