Working With Arrays
===================

Bracket Notation and Index
--------------------------

.. index:: ! index

As previously discussed, arrays are an ordered collection where each item can be accessed via index. Similar to strings, an **index** in an
array is the number order given to items. Individual items can be accessed using bracket notation (``array[index]``).
Indexes are zero-based, going from ``0`` to ``array.length-1``.

.. admonition:: Example

   Use bracket notation and index to access items in an array.

   .. sourcecode:: js
      :linenos:

      let programmingLanguages = [
         "JavaScript", // index 0
         "Python",     // index 1
         "Java",       // index 2
         "C#"          // index 3
      ];
      console.log(programmingLanguages[0]);
      console.log(programmingLanguages[3]);

      // What will happen when index 4 is requested?
      console.log(programmingLanguages[4]);

   **Console Output**

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
      :linenos:

      let programmingLanguages = ["JavaScript", "Python", "Java", "C#"];
      console.log(programmingLanguages[-1]);
      console.log(programmingLanguages[100]);

   **Console Output**

   ::

      undefined
      undefined

Arrays are Mutable
------------------

.. index:: mutable

In programming, mutability refers to what happens when you attempt to change a value. Remember that strings are immutable, meaning that any change
to a string results in a new string being created. In contrast, arrays are **mutable**, meaning that individual items in
an array can be edited without a new array being created.

.. admonition:: Example

   Update an item in an array using bracket notation and index.

   .. sourcecode:: js
      :linenos:

      let javaScriptFrameworks = ["React", "Angular", "Ember"];
      console.log(javaScriptFrameworks);

      // Set the value of index 2 to be "Vue"
      javaScriptFrameworks[2] = "Vue";

      // Notice the value at index 2 is now "Vue"
      console.log(javaScriptFrameworks);

   **Console Output**

   ::

      [ 'React', 'Angular', 'Ember' ]
      [ 'React', 'Angular', 'Vue' ]
