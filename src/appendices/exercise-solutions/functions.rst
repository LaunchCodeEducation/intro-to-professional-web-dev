.. _functions-exercise-solutions:

Exercise Solutions: Data and Variables
======================================

.. _functions-exercise-solutionsA:

A. **makeLine()**

   Write a function ``makeLine(size)`` that returns a line with exactly ``size`` hashes.

   .. sourcecode:: js
      :linenos:

      function makeLine(size) {
         let line = '';
         for (let i = 0; i < size; i++) {
            line += '#';
         }
         return line;
      }

   :ref:`Back to the exercises <exercises-functions>`

.. _functions-exercise-solutionsC:

C. **makeRectangle()**

   Write a function ``makeRectangle(width, height)`` that returns a rectangle with the given width and height. 

   .. sourcecode:: js
      :linenos:

      function makeRectangle(width, height) {
         let rectangle = '';
         for (let i = 0; i < height; i++) {
            rectangle += (makeLine(width) + '\n');
         }
         return rectangle.slice(0, -1);
      }

   :ref:`Back to the exercises <exercises-functions>`

.. _functions-exercise-solutionsE:

E. **makeDownwardStairs()**

   Write a function ``makeDownwardStairs(height)`` that prints the staircase pattern shown, with the given height.  

   .. sourcecode:: js
      :linenos:

      function makeDownwardStairs(height) {
         let stairs = '';
         for (let i = 0; i < height; i++) {
            stairs += (makeLine(i+1) + '\n');
         }
         return stairs.slice(0, -1);
      }


   :ref:`Back to the exercises <exercises-functions>`

.. _functions-exercise-solutionsG:

G. **makeIsoscelesTriangle()**

   Write a function ``makeIsoscelesTriangle(height)`` that returns a triangle of the given height.

   .. sourcecode:: js
      :linenos:

      function makeIsoscelesTriangle(height) {
         let triangle = '';
         for (let i = 0; i < height; i++) {
            triangle += (makeSpaceLine(height - i - 1, 2*i + 1) + '\n');
         }
         return triangle.slice(0, -1);
      }

   :ref:`Back to the exercises <exercises-functions>`
   