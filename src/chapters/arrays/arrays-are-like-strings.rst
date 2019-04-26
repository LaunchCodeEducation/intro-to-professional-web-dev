Arrays Are Like Strings
=======================

.. index:: ! array

Arrays are similar to strings, but are a more general collection type. Like strings, **arrays** are a sequence of values that can be
accessed via an ordered index. Unlike strings, arrays can store data of any type.

Notice the values in the below figure each have an index value.

.. figure:: figures/array-example.jpg
   :alt: A label, languages, pointing to an array that contains "Python" at index 0, "C#" at index 1, "Java" at index 2, and "JavaScript" at index 3.

Declaring an Array
------------------

.. index::
   single: array; literal

There are multiple ways to declare a new array. The simplest way is to use **array literal** notation ``[]``.
Anything enclosed in the square brackets will be *items* in the array. Each item should be followed by a comma ``,``.
If there are no items inside the brackets, then the array is considered empty.

.. sourcecode:: js

   const emptyArray = [];

   const programmingLanguages = ["JavaScript", "Python", "Java", "C#"];

Array items can also be declared on multiple lines.

.. sourcecode:: js

   const javaScriptFrameworks = [
      "React",
      "Angular",
      "Ember",
      "Vue"
   ];

Array Length
------------
To check the length of an array, use the ``length`` property, just like with strings.
JavaScript array length is NOT fixed, meaning you can add or remove items dynamically.

.. admonition:: Note

   In other languages, such as Java and C#, arrays are of a static length requiring the
   length of the array to be declared upon creation.


.. admonition:: Example

   Print out the length of two arrays.

   .. sourcecode:: js

      const emptyArray = [];
      console.log(emptyArray.length);

      const programmingLanguages = ["JavaScript", "Python", "Java", "C#"];
      console.log(programmingLanguages.length);

   **Output**

   ::

      0
      4

Varying Data Types
------------------
JavaScript arrays can hold a mixture of values of any type. For example, you can have an array that contains strings, numbers, and bools.

.. sourcecode:: js

   const grabBag = ["A string value", true, 99, 105.5];

.. admonition:: Note
   
   It’s rare that you would store data of multiple types in the same array, because grouped data is usually the same type. In other languages, such as Java and C#, all items in an array have to be of the same type.



Check Your Understanding
------------------------

.. admonition:: Question

   What is the length of the two arrays?
   
   *Hint: look closely at the quotes in the classes array.*

   .. sourcecode:: js

      const classes = ["science, computer, art"];

      const teachers = ["Jones", "Willoughby", "Rhodes"];

   How can you change the ``classes`` array declaration to have the same number of items as the ``teachers`` array?
