Multi-Dimensional Arrays
========================

Earlier we learned that arrays can store any type of value. If that is true, can we store arrays inside
of arrays? Well yes we can.... Get ready to venture into a multi-dimensional universe.

.. index:: ! multi-dimensional array

A **multi-dimensional array** is an array of arrays, meaning that the values inside the array are also arrays.
The *inner* arrays can store other values such as strings, numbers, or even more arrays.

.. figure:: figures/multi-dimensional-array-example.jpg
   :alt: A label, synonyms, pointing to an array that contains arrays at it's four indexes. Each inner array has a list of words that are synonyms.

Two Dimensional Arrays
----------------------
The simplest form of a multi-dimensional array is a two dimensional array. A two dimensional array is like a
spreadsheet with rows and columns. To access items in a two dimensional array, use square bracket notation and
two indexes ``array[0][0]``. The first index is for the outer array, or the "row", and second index is for the inner array,
or the "column".

.. note:: The row and column analogy is used to help visualize a two dimensional array, however it's not a perfect analogy. There are no specific JavaScript language rules forcing the inner arrays to all have the same length. The inner arrays are separate arrays that can be of different length.

.. admonition:: Example

   Use a two dimensional array to contain three different lists of space shuttle crews.

   .. sourcecode:: js

      const shuttleCrews = [
         ['Robert Gibson', 'Mark Lee', 'Mae Jemison'],
         ['Kent Rominger', 'Ellen Ochoa', 'Bernard Harris'],
         ['Eilen Collins', 'Winston Scott',  'Catherin Coleman']
      ];

      console.log(shuttleCrews[0][2]);
      console.log(shuttleCrews[1][1]);
      console.log(shuttleCrews[2][1]);

   **Output**

   ::

      Mae Jemison
      Ellen Ochoa
      Winston Scott

Multi-Dimensions and Array Methods
----------------------------------
Both the inner and outer arrays in a multi-dimensional array are still altered with array
methods.

.. admonition:: Example

   Use array methods to add an additional crew array and alter existing arrays.

   .. sourcecode:: js

      const shuttleCrews = [
         ['Robert Gibson', 'Mark Lee', 'Mae Jemison'],
         ['Kent Rominger', 'Ellen Ochoa', 'Bernard Harris'],
         ['Eilen Collins', 'Winston Scott',  'Catherin Coleman']
      ];

      const newCrew = ['Mark Polansky', 'Robert Curbeam', 'Joan Higginbotham'];

      // Add a new crew array to the end of shuttleCrews
      shuttleCrews.push(newCrew);
      console.log(shuttleCrews[3][2]);

      // Reverse the order of the crew at index 1
      shuttleCrews[1].reverse();
      console.log(shuttleCrews[1]);

   **Output**

   ::

      Joan Higginbotham
      [ 'Bernard Harris', 'Ellen Ochoa', 'Kent Rominger' ]

Beyond Two Dimensional Arrays
-----------------------------
Generally there is no limit to how many dimensions you can have when creating arrays. However it is rare that you will
use more than two dimensions. Later on in the class we will learn about more collection types that can handle complex
problems beyond the scope of two dimensional arrays.


Check Your Understanding
------------------------

.. admonition:: Question

   What are the two dimensional indexes for ``"Jones"``?

   .. sourcecode:: js

      const school = [
         ["science", "computer", "art"],
         ["Jones", "Willoughby", "Rhodes"]
      ];



   How would you add ``"dance"`` to the array at ``school[0]``?

   How would you add ``"Holmes"`` to the array at ``school[1]``?
