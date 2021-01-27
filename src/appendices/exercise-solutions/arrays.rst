.. _arrays-exercise-solutions:

Exercise Solutions: Arrays
==========================


.. _arrays-exercise-solutions1:

1. Create an array called ``practiceFile`` with the following entry: 273.15.
   Use the ``push`` method to add the following elements to the array. Add
   items a & b one at a time, then use a single ``push`` to add the items in
   part c. Print the array after each step to confirm the changes.

   .. sourcecode:: js

      let practiceFile = [273.15];

   a. 42

      .. sourcecode:: js
         :linenos:

         practiceFile.push(42);
         console.log(practiceFile);

   c. ``false``, -4.6, "87"

      .. sourcecode:: js
         :linenos:

         practiceFile.push(false, -4.6, "87");
         console.log(practiceFile);


:ref:`Back to the exercises <exercises-arrays>`.

.. _arrays-exercise-solutions2:

2. ``push``, ``pop``, ``shift`` and ``unshift`` are used to add/remove elements
   from the beginning/end of an array. **Bracket notation** can be used to
   modify any element within an array. Starting with the ``cargoHold`` array
   ``['oxygen tanks', 'space suits', 'parrot', 'instruction manual',
   'meal packs', 'slinky', 'security blanket']``, write statements to do the
   following:

   .. sourcecode:: js

      let cargoHold = ['oxygen tanks', 'space suits', 'parrot', 'instruction manual', 'meal packs', 'slinky', 'security blanket'];

   a. Use bracket notation to replace ``'slinky'`` in the array with ``'space
      tether'``. Print the array to confirm the change.

      .. sourcecode:: js
         :linenos:

         cargoHold[5] = 'space tether';
         console.log(cargoHold);

   c. Remove the first item from the array with ``shift``. Print the element
      removed and the updated array.

      .. sourcecode:: js
         :linenos:

         console.log(cargoHold.shift());
         console.log(cargoHold);
      

   e. Use a template literal to print the final array and its length.

      .. sourcecode:: js

         console.log(`The array ${cargoHold} has a length of ${cargoHold.length}.`);


:ref:`Back to the exercises <exercises-arrays>`.

.. _arrays-exercise-solutions3:

3. The ``splice`` method can be used to either add or remove items from an
   array. It can also accomplish both tasks at the same time. Review the
   :ref:`splice appendix <splice-examples>` if you need a syntax reminder. Use
   ``splice`` to make the following changes to the final ``cargoHold`` array
   from exercise 2. Be sure to print the array after each step to confirm your
   updates.

   a. Insert the string ``'keys'`` at index 3 without replacing any other
      entries.

      .. sourcecode:: js
         :linenos:

         cargoHold.splice(3,0,'keys');
         console.log(cargoHold);

   c. Replace the elements at indexes 2 - 4 with the items ``'cat'``,
      ``'fob'``, and ``'string cheese'``.

      .. sourcecode:: js
         :linenos:

         cargoHold.splice(2,3,'cat','fob','string cheese');
         console.log(cargoHold);


:ref:`Back to the exercises <exercises-arrays>`.


.. _arrays-exercise-solutions4:

4. Some methods---like ``splice`` and ``push``---alter the original array,
   while others do not. Use the arrays

   .. sourcecode:: js

      holdCabinet1 ['duct tape', 'gum', 3.14, false, 6.022e23]

   and

   .. sourcecode:: js

      holdCabinet2 ['orange drink', 'nerf toys', 'camera', 42, 'parsnip']

   to explore the following methods: ``concat``, ``slice``, ``reverse``, ``sort``. Refer back to the chapter if you need to review the proper syntax for any of these methods.

   a. Print the result of using ``concat`` on the two arrays. Does ``concat``
      alter the original arrays? Verify this by printing ``holdCabinet1``
      after using the method.

      .. sourcecode:: js
         :linenos:

         console.log(holdCabinet1.concat(holdCabinet2));
         console.log(holdCabinet1);

   c. ``reverse`` the first array, and ``sort`` the second. What is the difference
      between these two methods? Do the methods alter the original arrays?

      .. sourcecode:: js
         :linenos:

         holdCabinet1.reverse();
         holdCabinet2.sort();
         console.log(holdCabinet1);
         console.log(holdCabinet2);


:ref:`Back to the exercises <exercises-arrays>`.

.. _arrays-exercise-solutions5:

5. The ``split`` method converts a string into an array, while the ``join``
   method does the opposite.

   a. Try it! Given the string ``str = 'In space, no one can hear you code.'``,
      see what happens when you print ``str.split()`` vs. ``str.split('e')``
      vs. ``str.split(' ')`` vs. ``str.split('')``. What is the purpose of the
      parameter inside the ``()``?

      .. sourcecode:: js
         :linenos:

         console.log(str.split());
         console.log(str.split('e'));
         console.log(str.split(' '));
         console.log(str.split(''));

   c. Do ``split`` or ``join`` change the original string/array?

      .. sourcecode:: js

         console.log(cargoHold.split(',').sort().join(','));


:ref:`Back to the exercises <exercises-arrays>`.

.. _arrays-exercise-solutions6:

6. Arrays can hold different data types, even other arrays! A
   **multi-dimensional array** is one with entries that are themselves arrays.

   a. Define and initialize the following arrays, which hold the name, chemical
      symbol and mass for different elements:

      i. ``element1 = ['hydrogen', 'H', 1.008]``
      ii. ``element2 = ['helium', 'He', 4.003]``
      iii. ``element26 = ['iron', 'Fe', 55.85]``

      .. sourcecode:: js
         :linenos:

         let element1 = ['hydrogen', 'H', 1.008];
         let element2 = ['helium', 'He', 4.003];
         let element26 = ['iron', 'Fe', 55.85];

   c. Use bracket notation to examine the difference between printing
      ``table[1]`` and ``table[1][1]``. Don't just nod your head! I want to
      HEAR you describe this difference. Go ahead, talk to your screen.

      .. sourcecode:: js

         console.log(table[1], table[1][1]);


:ref:`Back to the exercises <exercises-arrays>`.
