Array Exercises
----------------

1. Create an array called ``arr`` with the following entry: 273.15. Use the
   ``push`` method to add the following elements to the array.  Add items a &
   b one at a time, then use a single ``push`` to add the items in part c.
   Print the array after each step to confirm the changes.

   a. 42
   b. "hello"
   c. ``false``, -4.6, "87"

Control+click (or right click) to: `Code it here <https://repl.it/@launchcode/ArrayExercises01>`__

|

2. ``push``, ``pop``, ``shift`` and ``unshift`` are used to add/remove elements
   from the beginning/end of an array.  **Bracket notation** can be used to
   modify any element within an array.  Starting with the full array from
   exercise 1, write statements to do the following:

   a. Replace ``false`` in the array with ``true``.
   b. Remove the last item from the array.  Print the element removed and the
      new array.
   c. Remove the first item from the array.  Print the element removed and the
      new array.
   d. Add the numbers 99 and 42 to the the array - one at the start and one at
      the end.
   e. Use a template literal to print the final array and its length.

`Code it here <https://repl.it/@launchcode/ArrayExercises02>`__

|

3. The ``splice`` method can be used to either add or remove items from an
   array.  It can also accomplish both tasks at the same time
   (`Reference <https://www.w3schools.com/js/js_array_methods.asp>`__). Use ``splice`` to
   make the following changes to the array ``['a', 'b', 'c', 'd', 'e', 'f']``.
   Be sure to print the array to confirm your updates.

   a. Insert the string “cat” at index 3 without replacing any other entries.
   b. Remove 'e' from the array.  (Hint: ``indexOf`` is helpful to avoid manually
      determining an index).
   c. Replace the elements at indexes 2 - 4 with the items "change", 0, and
      121.

`Code it here <https://repl.it/@launchcode/ArrayExercises03>`__

|

4. Some methods - like ``splice`` and ``push`` - alter the original array,
   while others do not. Use the arrays ``['j', 'm', 'f', 0, 1, 6.022e23]`` and
   ``['x', 'y', 'z', 233, 144, 300, 'parsnip']`` to explore the following
   methods: ``concat``, ``slice``, ``reverse``, ``sort``.

   a. Print the result of using ``concat`` on the two arrays.  Does ``concat``
      alter the original arrays?  Verify this by printing ``firstArray`` after
      using the method.
   b. Print a ``slice`` of two elements from each array.  Does ``slice`` alter the
      original arrays?
   c. ``reverse`` the first array, and ``sort`` the second.  Do these methods alter
      the original arrays?

`Code it here <https://repl.it/@launchcode/ArrayExercises04>`__

|

5. The ``split`` method converts a string into an array, while the ``join``
   method does the opposite.

   a. Try it!  Given the string ``str = 'Flowers bloom in the spring.'``, see what
      happens when you print ``str.split()`` vs. ``str.split('o')`` vs.
      ``str.split(' ')`` vs. ``str.split('')``. What is the purpose of the
      parameter inside the ``()``?
   b. Given the array ``arr = ['a', 'b', 'c', 1, 2, 3]``, see what happens when
      you print ``arr.join()`` vs. ``arr.join('0')`` vs. ``arr.join(' ')`` vs.
      ``arr.join('')``. What is the purpose of the parameter inside the ``()``?
   c. Do ``split`` or ``join`` change the original string/array?

`Code it here <https://repl.it/@launchcode/ArrayExercises05>`__

|

6. Arrays can hold different data types, even other arrays!  A
   **multi-dimensional array** is one with entries that are themselves arrays.

   a. Define and initialize the following arrays, which hold the name, chemical
      symbol and mass for different elements:

      i. ``element1 = ['hydrogen', 'H', 1.008]``
      ii. ``element2 = ['helium', 'He', 4.003]``
      iii. ``element26 = ['iron', 'Fe', 55.85]``

   b. Define the array ``table``, and use ``push`` to add each of the element arrays
      to it.  Print ``table`` to see its structure.
   c. Use bracket notation to examine the difference between printing ``table[1]`` and
      ``table[1][1]``.
   d. Using bracket notation and the ``table`` array, print the mass of element1, the
      name for element 2 and the symbol for element26.
   e. ``table`` is an example of a *2-dimensional array*.  The first "level" contains the
      element arrays, and the second level holds the name/symbol/mass values.
      **Experiment!** Create a 3-dimensional array and print out one entry from
      each level in the array.

`Code it here <https://repl.it/@launchcode/ArrayExercises06>`__
