Array Exercises
----------------

1. Create an array called ``arr`` with the following entry: 273.15. Use the
    ``push`` method to add the following elements to the array.  Add items a &
    b one at a time, then use a single ``push`` to add the items in part c.

   a. 42
   b. ``"hello"``
   c. ``false``, -4.6, "87"

Control+click (or right click) to: **[Repl.it link]**

|

2. ``push``, ``pop``, ``shift`` and ``unshift`` are used to add or remove
   elements from the beginning or end of an array.  Bracket notation can be
   used to modify any element within an array.  Starting with the full array
   from exercise 1, write statements to do the following:

   a. Replace ``false`` in the array with ``true``.
   b. Remove the last item from the array.  Print the element removed and the
      new array.
   c. Remove the first item from the array.  Print the element removed and the
      new array.
   d. Add the values 99 and 42 to the the array - one at the start and one at
      the end.
   e. Use a template literal to print the number of 42s in the array as well as
      the length of the array.

**[Repl.it link]**

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

**[Repl.it link]**

|

4. Some methods - like ``splice`` and ``push`` - alter the original array,
   while others do not (e.g. ``indexOf``).  Use the arrays ``['a', 'b', 'c', 0,
   1, 6.022e23]`` and ``['x', 'y', 'z', 2.33, 144, 3, 'parsnip']`` to explore
   the following methods: ``concat``, ``slice``, ``reverse``, ``sort``.

   a. Does ``concat`` alter the original arrays?
   b. Print a ``slice`` of two elements from each array.  Does ``slice`` alter the
      original arrays?
   c. ``reverse`` the first array, and ``sort`` the second.  Do these methods alter
      the original arrays?

**[Repl.it link]**

|

5. The ``split`` method converts a string into an array, while the ``join``
   method does the opposite.

   a. Try it!  Given the string ``str = Flowers bloom in the spring.'``, see what
      happens when you print ``str.slice()`` vs. ``str.slice('a')`` vs.
      ``str.slice(' ')`` vs. ``str.slice('')``.
   b. Given the array ``arr = ['a', 'b', 'c', 1, 2, 3]``, see what happens when
      you print ``arr.join()`` vs. ``arr.join('0')`` vs. ``arr.join(' ')`` vs.
      ``arr.join('')``.
   c. Do ``split`` or ``join`` change the original string/array?

**[Repl.it link]**

|

6. Arrays can hold different data types, even other arrays!  A
   **multi-dimensional** array is an array with entries that are themselves
   arrays.

   a. Define and initialize the following arrays, which hold the name, chemical symbol and mass for different elements:
      i. ``element1 = ['hydrogen', 'H', 1.008]``
      ii. ``element2 = ['helium', 'He', 4.003]``
      iii. ``element26 = ['iron', 'Fe', 55.85]``
   b. Define the array ``table``, and use ``push`` to add each of the element arrays
      to it.  Print ``table`` to see its structure.
   c. Use bracket notation to examine the difference between printing ``table[1]`` and
      ``table[1][1]``.
   d. Using bracket notation and the ``table`` array, print the mass of element1, the
      name for element 2 and the symbol for element26.
   e. ``table`` is an example of a 2-dimensional array.  The first "level" contains the
      element arrays, and the second level holds the name/symbol/mass values.
      Experiment! Create a 3-dimensional array and print out one entry from
      each level in the array.

**[Repl.it link]**
