.. _max-and-min-examples:

``Math.max`` and ``Math.min`` Examples
=======================================

``Math.max``
-------------

The general syntax for this method is:

::

   Math.max(x, y, z, ...)

This method finds and returns the largest value from a set of numbers (x, y, z,
...).

To find the maximum value in an array, :ref:`see below <max-min-array>`.

.. admonition:: Example

   .. sourcecode:: js
      :linenos:

      console.log(Math.max(2, 3, 100.01, 0, -5.2, 100));

   **Output**
   ::

      100.01

.. _min:

``Math.min``
-------------

The general syntax for this method is:

::

   Math.min(x, y, z, ...)

This method finds and returns the smallest value from a set of numbers
(x, y, z,...).

To find the minimum value in an array, :ref:`see below <max-min-array>`.

.. admonition:: Example

   .. sourcecode:: js
      :linenos:

      console.log(Math.min(2, 3, 100.01, 0, -5.2, 100));

   **Output**
   ::

      -5.2

.. _max-min-array:

Max and Min of an Array
------------------------

Unfortunately, the ``max`` and ``min`` methods will NOT take an array of
numbers as an argument. There are numerous workarounds. Here is ONE possible
solution.

It uses the syntax from :ref:`the sorting studio <js-sort-numbers>`
to first order the array. The maximum (or minimum) value can then be
identified with bracket notation.

.. admonition:: Example

   .. sourcecode:: js
      :linenos:

      let numbers = [-2, 3.33, -4.44, 8.88];

      let sortedArray = numbers.sort(function(a, b){return a-b});

      console.log(sortedArray);
      console.log(`Min = ${sortedArray[0]}, Max = ${sortedArray[sortedArray.length-1]}`);

   **Output**
   ::

      [ -4.44, -2, 3.33, 8.88 ]
      Min = -4.44, Max = 8.88
   
   Alternatively, we could put the array in decreasing order:

   .. sourcecode:: js
      :linenos:

      let numbers = [-2, 3.33, -4.44, 8.88];

      let sortedArray = numbers.sort(function(a, b){return b-a});

      console.log(sortedArray);
      console.log(`Max = ${sortedArray[0]}, Min = ${sortedArray[sortedArray.length-1]}`);

   **Output**
   ::

      [ 8.88, 3.33, -2, -4.44 ]
      Max = 8.88, Min = -4.44
