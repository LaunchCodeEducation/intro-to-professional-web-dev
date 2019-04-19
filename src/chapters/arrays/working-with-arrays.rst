Working With Arrays
===================

Bracket Notation
----------------
Arrays are ordered collections, meaning they will keep the order of items they contain. That order is refered to as the index.
Like with strings, use bracket notation and an index to access a specific item in an array ``array[index]``.
Also like strings, an arrays index is zero based. An array's index will go from ``0`` to ``array.length - 1``.

.. admonition:: Example

   Print out the length of two arrays.

   .. sourcecode:: js

      const programmingLanguages = ["JavaScript", "Python", "Java", "C#"];
      console.log(programmingLanguages[0]);
      console.log(programmingLanguages[3]);
      console.log(programmingLanguages[4]);

   **Output**

   ::

      JavaScript
      C#
      undefined

Notice above that ``undefined`` was printed out when index 4 was referenced. ``undefined`` is returned when you request an index
that the array does not contain.

.. note:: **undefined** is a special value in JavaScript that means no value has been assigned. We will discuss ``undefined`` more later in the class.

.. admonition:: Example

   Print out the length of two arrays.

   .. sourcecode:: js

      const programmingLanguages = ["JavaScript", "Python", "Java", "C#"];
      console.log(programmingLanguages[-1]);
      console.log(programmingLanguages[100]);

   **Output**

   ::

      undefined
      undefined

Arrays are Mutable
------------------
Mutability refers to what happens to when values are edited. Remember that Strings are immutable, meaning that any change
to a string results in a new string being created. In constrast, arrays are **mutable**, meaning that individual items in
an array can be edited without a new array being created.

.. admonition:: Example

   Print out the length of two arrays.

   .. sourcecode:: js

      const javaScriptFrameworks = ["React", "Angular", "Ember"];
      console.log(javaScriptFrameworks[2]);
      javaScriptFrameworks[2] = "Vue";
      console.log(javaScriptFrameworks[2]);

   **Output**

   ::

      Ember
      Vue
