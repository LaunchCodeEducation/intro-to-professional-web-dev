Arrays Are Like Strings
=======================

In the previous chapter we learned in detail how strings are a sequence, ordered collection,
of characters that can be accessed by an index. Using String methods we can add, remove,
replace parts of the collection. What we can’t do is store anything other than characters.

.. index:: ! array

In this chapter we will learn about a more general usage collection data type called **Array**.
Like strings, arrays are ordred collections. A key difference is that strings can only contain contain
characters, arrays can store data of any type.

Figure: JavaScript array from prev chapter
Remember that a string is a sequence of strings with a length of 1

Figure: Array with multiple strings included JavaScript, Python, Java, C#
An array is a sequence of values that can vary in size and type.

Delcaring an Array
------------------
There are multiple ways to declare a new Array. The simplest way is to use **array literal** notation ``[]``.
Anything enclosed in the square brackets will be *items* in the array. Each item should be followed by a comma ``,``.
If there are no items inside the brackets, then the array is considered empty.

.. sourcecode:: js

   const emptyArray = [];

   const programmingLanguages = ["JavaScript", "Python", "Java", "C#"];

Array items can also be declared on a new line.

.. sourcecode:: js

   const javaScriptFrameworks = [
      "React",
      "Angular",
      "Ember",
      "Vue"
   ];

Dynamic Length
--------------
JavaScript array length is NOT fixed, meaning you can add or remove items dynamically.

.. note:: In other languages, such as Java and C#, arrays are of a static length requiring the
 length of the array to be declared upon creation.

To check to check the lenght of an array use the ``length`` property, just like with strings.

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
Not only can you have an array that contains multiple strings or numbers. You can have an array that contains both
strings and numbers. The standard JavaScript array can hold any combination of values of any type.

.. note:: In other languages such as Java and C# all items in an array have to be of the same type. It’s rare that you would store data of multiple types, because grouped data is usually the same type.

.. sourcecode:: js

   const grabBag = ["A string value", true, 99, 105.5];

Check Your Understanding
------------------------

.. admonition:: Question

   What is the length of these arrays?

   .. sourcecode:: js

      const classes = [“science, math, art”];

      const teachers = [“science”, “art”, “math”];

   How can you change the ``classes`` array declaration to have the same number of items as the ``teachers`` array?
