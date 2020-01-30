Exercises: Arrays
=================

OK, rookie. It's time to train you on how to modify the shuttle's cargo
manifest. The following actions will teach you how to add, remove, modify and
rearrange our records for the items stored in our hold.

#. Create an array called ``practiceFile`` with the following entry: 273.15.
   Use the ``push`` method to add the following elements to the array. Add
   items a & b one at a time, then use a single ``push`` to add the items in
   part c. Print the array after each step to confirm the changes.

   #. 42
   #. "hello"
   #. ``false``, -4.6, "87"

   `Code it at repl.it <https://repl.it/@launchcode/ArrayExercises01>`__

   *Congratulations, rookie. You can now add items to an array.*

#. ``push``, ``pop``, ``shift`` and ``unshift`` are used to add/remove elements
   from the beginning/end of an array. **Bracket notation** can be used to
   modify any element within an array. Starting with the ``cargoHold`` array
   ``['oxygen tanks', 'space suits', 'parrot', 'instruction manual',
   'meal packs', 'slinky', 'security blanket']``, write statements to do the
   following:

   #. Use bracket notation to replace ``'slinky'`` in the array with ``'space
      tether'``. Print the array to confirm the change.
   #. Remove the last item from the array with ``pop``. Print the element
      removed and the updated array.
   #. Remove the first item from the array with ``shift``. Print the element
      removed and the updated array.
   #. Unlike ``pop`` and ``shift``, ``push`` and ``unshift`` require arguments
      inside the ``()``. Add the items 1138 and '20 meters' to the array -
      the number at the start and the string at the end. Print the updated
      array to confirm the changes.
   #. Use a template literal to print the final array and its length.

   `Code it at repl.it <https://repl.it/@launchcode/ArrayExercises02>`__

   *Status check, rookie. Which array methods ADD items, and where are the new
   entries placed? Which methods REMOVE items, and where do the entries come
   from? Which methods require entries inside the ``()``?*

#. The ``splice`` method can be used to either add or remove items from an
   array. It can also accomplish both tasks at the same time. Review the
   :ref:`splice appendix <splice-examples>` if you need a syntax reminder. Use
   ``splice`` to make the following changes to the final ``cargoHold`` array
   from exercise 2. Be sure to print the array after each step to confirm your
   updates.

   #. Insert the string ``'keys'`` at index 3 without replacing any other
      entries.
   #. Remove 'instruction manual' from the array. (Hint: ``indexOf`` is helpful
      to avoid manually counting an index).
   #. Replace the elements at indexes 2 - 4 with the items ``'cat'``,
      ``'fob'``, and ``'string cheese'``.

   `Code it at repl.it <https://repl.it/@launchcode/ArrayExercises03>`__

   *Well done, cadet. Now let's look at some finer details about array methods.
   We've got to keep our paperwork straight, so you need to know when your
   actions change the original records.*

#. Some methods---like ``splice`` and ``push``---alter the original array,
   while others do not. Use the arrays

   .. sourcecode:: js

      holdCabinet1 ['duct tape', 'gum', 3.14, false, 6.022e23]

   and

   .. sourcecode:: js

      holdCabinet2 ['orange drink', 'nerf toys', 'camera', 42, 'parsnip']

   to explore the following methods: ``concat``, ``slice``, ``reverse``, ``sort``. Refer back to the chapter if you need to review the proper syntax for any of these methods.

   #. Print the result of using ``concat`` on the two arrays. Does ``concat``
      alter the original arrays? Verify this by printing ``holdCabinet1``
      after using the method.
   #. Print a ``slice`` of two elements from each array. Does ``slice`` alter the
      original arrays?
   #. ``reverse`` the first array, and ``sort`` the second. What is the difference
      between these two methods? Do the methods alter the original arrays?

   `Code it at repl.it <https://repl.it/@launchcode/ArrayExercises04>`__

   *Good progress, cadet. Here are two more methods for you to examine.*

#. The ``split`` method converts a string into an array, while the ``join``
   method does the opposite.

   #. Try it! Given the string ``str = 'In space, no one can hear you code.'``,
      see what happens when you print ``str.split()`` vs. ``str.split('e')``
      vs. ``str.split(' ')`` vs. ``str.split('')``. What is the purpose of the
      parameter inside the ``()``?
   #. Given the array ``arr = ['B', 'n', 'n', 5]``, see what happens when
      you print ``arr.join()`` vs. ``arr.join('a')`` vs. ``arr.join(' ')`` vs.
      ``arr.join('')``. What is the purpose of the parameter inside the ``()``?
   #. Do ``split`` or ``join`` change the original string/array?
   #. The benefit, cadet, is that we can take a string with **delimiters**
      (like commas) and convert it into a modifiable array. *Try it!*
      Alphabetize these hold contents: "water,space suits,food,plasma
      sword,batteries", and then combine them into a new string.

   `Code it at repl.it <https://repl.it/@launchcode/ArrayExercises05>`__

   *Nicely done, astronaut. Now it's time to bring you fully up to speed.*

#. Arrays can hold different data types, even other arrays! A
   **multi-dimensional array** is one with entries that are themselves arrays.

   #. Define and initialize the following arrays, which hold the name, chemical
      symbol and mass for different elements:

      i. ``element1 = ['hydrogen', 'H', 1.008]``
      ii. ``element2 = ['helium', 'He', 4.003]``
      iii. ``element26 = ['iron', 'Fe', 55.85]``

   #. Define the array ``table``, and use ``push(arrayName)`` to add each of
      the element arrays to it. Print ``table`` to see its structure.
   #. Use bracket notation to examine the difference between printing
      ``table[1]`` and ``table[1][1]``. Don't just nod your head! I want to
      HEAR you describe this difference. Go ahead, talk to your screen.
   #. Using bracket notation and the ``table`` array, print the mass of
      element1, the name for element 2 and the symbol for element26.
   #. ``table`` is an example of a *2-dimensional array*. The first "level"
      contains the element arrays, and the second level holds the
      name/symbol/mass values. **Experiment!** Create a 3-dimensional array and
      print out one entry from each level in the array.

   `Code it at repl.it <https://repl.it/@launchcode/ArrayExercises06>`__

*Excellent work, records keeper. Welcome aboard.*
