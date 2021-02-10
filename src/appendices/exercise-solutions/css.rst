.. _css-exercise-solutions:

Exercise Solutions: CSS
=======================

.. _css-exercise-solutions1:

#. **Change the background color to yellow.**

   ``style.css``

   .. sourcecode:: css
      :linenos:

      body {
         background-color: yellow;
      }


   :ref:`Back to the exercises <exercises-css>`

.. _css-exercise-solutions3:

3. **Change all h1 to 36 px font size.**

   ``style.css``
   
   .. sourcecode:: css
      :linenos:

      h1 {
         font-size: 36px;
      }


   :ref:`Back to the exercises <exercises-css>`

.. _css-exercise-solutions5:

5. **Use a CSS class to align only the headings to the center of the page.**

   ``style.css``
   
   .. sourcecode:: css
      :linenos:

      .center {
         text-align: center;
      }

   ``index.html`` - add a ``center`` class to all header tags (``h1``, ``h2``, etc.)
   
   .. sourcecode:: html
      :linenos:

      <body>
         <h1 class="center">My Very Cool Web Page</h1>
         <h2 class="center">Why this Website is Very Cool</h2>
         <ol>
            <li>I made it!</li>
            <li>This website is colorful!</li>
         </ol>
         <h2 class="center" id="cool-text">Why I love Web Development</h2>
         <p>Web Development is a very cool skill that I love learning!</p>
         <p>I love making websites because all I have to do is reload the page to see the changes I have made!</p>
      </body>

   :ref:`Back to the exercises <exercises-css>`

.. _css-exercise-solutions7:

7. **Use a CSS id to change the elements in the ordered list to a color of your choosing.**

   ``style.css``
   
   .. sourcecode:: css
      :linenos:

      #list-color {
         color: blueviolet;
      }


   ``index.html`` - add the ``id`` attribute to the ``ol`` tag
   
   .. sourcecode:: html
      :linenos:

      <ol id="list-color">
         <li>I made it!</li>
         <li>This website is colorful!</li>
      </ol>


   :ref:`Back to the exercises <exercises-css>`