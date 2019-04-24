Working With Arrays
===================

Bracket Notation and Index
--------------------------

.. index:: ! index

Arrays are ordered collections, meaning they will keep the order of items they contain. The **index** is the number order given to items
in an array. Like with strings, use bracket notation and an index to access a specific item in an array ``array[index]``.
Also like strings, an array's index is zero based. Zero based indexes start go from ``0`` to ``array.length - 1``.

.. admonition:: Example

   Use bracket notation and index to access items in an array.

   .. sourcecode:: js

      const programmingLanguages = [
         "JavaScript", // index 0
         "Python",     // index 1
         "Java",       // index 2
         "C#"          // index 3
      ];
      console.log(programmingLanguages[0]);
      console.log(programmingLanguages[3]);
      // What well happen then index 4 is requested?
      console.log(programmingLanguages[4]);

   **Output**

   ::

      JavaScript
      C#
      undefined

Notice above that ``undefined`` was printed out when index 4 was referenced. ``undefined`` is returned when you request an index
that the array does not contain.

.. index:: undefined

.. note:: **undefined** is a special value in JavaScript that means no value has been assigned. We will discuss ``undefined`` more later in the class.

.. admonition:: Example

   ``undefined`` will be returned for any index that is outside of the array's index range.

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

.. index:: mutable

In programming mutability refers to what happens when you attempt to change a value. Remember that Strings are immutable, meaning that any change
to a string results in a new string being created. In contrast, arrays are **mutable**, meaning that individual items in
an array can be edited without a new array being created.

.. admonition:: Example

   Update an item in an array using bracket notation and index.

   .. sourcecode:: js

      const javaScriptFrameworks = ["React", "Angular", "Ember"];
      console.log(javaScriptFrameworks);

      // Set the value of index 2 to be "Vue"
      javaScriptFrameworks[2] = "Vue";

      // Notice the value at index 2 is now "Vue"
      console.log(javaScriptFrameworks);

   **Output**

   ::

      [ 'React', 'Angular', 'Ember' ]
      [ 'React', 'Angular', 'Vue' ]
