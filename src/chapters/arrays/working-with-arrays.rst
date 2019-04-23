Working With Arrays
===================

Bracket Notation
----------------
Arrays are ordered collections, meaning they will keep the order of items they contain. That order is refered to as the index.
Like with strings, use bracket notation and an index to access a specific item in an array ``array[index]``.
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
Mutability refers to what happens to when values are edited. Remember that Strings are immutable, meaning that any change
to a string results in a new string being created. In constrast, arrays are **mutable**, meaning that individual items in
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
