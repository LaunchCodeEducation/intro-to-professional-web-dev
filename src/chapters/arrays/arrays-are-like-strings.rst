Arrays Are Like Strings
=======================

.. index:: ! array

Arrays are similar to strings, but are a more general collection type. Like strings, **arrays** are a sequence of values that can be
accessed via an ordered index. Unlike strings, arrays can store data of any type.

The figure below demonstrates an array of named languages. The array contains four strings, each of those values has an index position.

.. figure:: figures/Arrays-are-like-strings.png
   :alt: A label, languages, pointing to an array that contains "Python" at index 0, "C#" at index 1, "Java" at index 2, and "JavaScript" at index 3.

Declaring an Array
------------------

.. index::
   single: array; literal

Programmers use multiple ways to declare a new array. The simplest way is to use **array literal** notation ``[]``. Anything enclosed in the square brackets will be *items* in the array. Each item should be followed by a comma ``,``. If there are no items inside the brackets, then the array is considered empty.

.. sourcecode:: js
   :linenos:

   let emptyArray = [];

   let programmingLanguages = ["JavaScript", "Python", "Java", "C#"];

Array items can also be declared on multiple lines.

.. sourcecode:: js
   :linenos:

   let javaScriptFrameworks = [
      "React",
      "Angular",
      "Ember",
      "Vue"
   ];

Array Length
------------
To check the length of an array, use the ``length`` property, just like with strings.
JavaScript array length is NOT fixed, meaning you can add or remove items dynamically.

.. note::

   In other languages, such as Java and C#, arrays are of a static length requiring the
   length of the array to be declared upon creation.


.. admonition:: Example

   Print out the length of two arrays.

   .. sourcecode:: js
      :linenos:

      let emptyArray = [];
      console.log(emptyArray.length);

      let programmingLanguages = ["JavaScript", "Python", "Java", "C#"];
      console.log(programmingLanguages.length);

   **Console Output**

   ::

      0
      4

Varying Data Types
------------------

JavaScript arrays can hold a mixture of values of any type. For example, you can have an array that contains strings, numbers, and booleans.

.. sourcecode:: js

   let grabBag = ["A string value", true, 99, 105.5];

.. note::
   
   It’s rare that you would store data of multiple types in the same array, because grouped data is usually the same type. In other languages, such as Java and C#, all items in an array have to be of the same type.



Check Your Understanding
------------------------

.. admonition:: Question

   What is the length of the two arrays?

   *Hint: look closely at the quotes in the classes array.*

   .. sourcecode:: js
      :linenos:

      let classes = ["science, computer, art"];

      let teachers = ["Jones", "Willoughby", "Rhodes"];

   How can you change the ``classes`` array declaration to have the same number of items as the ``teachers`` array?
