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

      console.log(Math.max(2, 3, 100.01, 0, -5.2, 100));

   **Console Output**
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

      console.log(Math.min(2, 3, 100.01, 0, -5.2, 100));

   **Console Output**
   ::

      -5.2

.. _max-min-array:

Max and Min of an Array
------------------------

Unfortunately, the ``max`` and ``min`` methods will NOT take an array of
numbers as an argument. There are numerous workarounds. Here are TWO possible
solutions.

Sort First
^^^^^^^^^^^

This approach uses the syntax from :ref:`the sorting studio <js-sort-numbers>`
to first order the array. The maximum (or minimum) value can then be
identified with bracket notation.

.. admonition:: Examples

   .. sourcecode:: js
      :linenos:

      let numbers = [-2, 3.33, -4.44, 8.88];

      let sortedArray = numbers.sort(function(a, b){return a-b});

      console.log(sortedArray);
      console.log(`Min = ${sortedArray[0]}, Max = ${sortedArray[sortedArray.length-1]}`);

   **Console Output**
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

   **Console Output**
   ::

      [ 8.88, 3.33, -2, -4.44 ]
      Max = 8.88, Min = -4.44

.. index:: ! spread operator

Using Spread Syntax
^^^^^^^^^^^^^^^^^^^^

An alternative to the sorting approach described above is to use the
**spread operator** (``...``), also called *spread syntax*.

In cases where a set of numbers or strings (x, y, z, etc.) is expected, an
array cannot be used as-is. The spread operator expands an array into a
comma-separated set of elements, which can be passed as arguments in a
function call. ``functionName(...[x,y,z])`` is identical to
``functionName(x,y,z)``.

.. admonition:: Example

   .. sourcecode:: js
      :linenos:

      let numbers = [2, 3, 100.01, 0, -5.2, 100];

      let max = Math.max(...numbers);
      let min = Math.min(...numbers);

      console.log(...numbers);
      console.log(`Min = ${min}, Max = ${max}`);

   **Console Output**
   ::

      2 3 100.01 0 -5.2 100
      Min = -5.2, Max = 100.01

Note the absence of brackets, ``[]``, around the numbers printed by line 6.
``console.log(...numbers)`` executes as
``console.log(2, 3, 100.01, 0, -5.2, 100)``, so the output is NOT an array.

.. admonition:: Note

   The sorting approach works in all browsers. The spread operator, while
   very convenient, is NOT compatible with Internet Explorer or older versions
   of other browsers (pre-2015). For more details on the spread operator and its
   compatibility, check the
   `MDN Web Docs <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax>`__.
