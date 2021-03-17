.. _loops-exercise-solutions:

Exercise Solutions: Loops
======================================


.. _loops-exercise-solutions1:

``for`` Practice
-----------------

#. Construct ``for`` loops that accomplish the following tasks:

   a. Print the numbers 0 - 20, one number per line.

   .. sourcecode:: js
      :linenos:

      for (let i = 0; i <= 20; i++) {
         console.log(i);
      }

   c. Print the EVEN numbers 12 down to -14 in descending order, one number
      per line.

   .. sourcecode:: js
      :linenos:

      for (let i = 12; i >= -14; i-=2) {
         console.log(i);
      }

#. Initialize two variables to hold the string ``'LaunchCode'`` and the array
   ``[1, 5, 'LC101', 'blue', 42]``, then construct ``for`` loops to accomplish
   the following tasks:

   .. sourcecode:: js
      :linenos:

      let str = 'LaunchCode';
      let arr = [1, 5, 'LC101', 'blue', 42];

   a. Print each element of the array to a new line.

   .. sourcecode:: js
      :linenos:

      for (let i = 0; i < arr.length; i++) {
         console.log(arr[i]);
      }

#. Construct a ``for`` loop that sorts the array
   ``[2, 3, 13, 18, -5, 38, -10, 11, 0, 104]`` into two new arrays:

   a. Define an empty ``evens`` array to hold the even numbers and an ``odds``
      array for the odd numbers.

   .. sourcecode:: js
      :linenos:

      let otherArr = [2, 3, 13, 18, -5, 38, -10, 11, 0, 104];
      let evens = [], odds = [];

   c. Print the arrays to confirm the results. Print ``evens`` first. Example:
      ``console.log(evens);``

   .. sourcecode:: js
      :linenos:

      console.log(evens);
      console.log(odds);


:ref:`Back to the exercises <exercises-loops>`.

.. _loops-exercise-solutions2:

``while`` Practice
-------------------

Define three variables for the LaunchCode shuttle---one for the starting
fuel level, another for the number of astronauts aboard, and the third for
the altitude the shuttle reaches.

4. Construct ``while`` loops to do the following:

   a. Prompt the user to enter the starting fuel level. The loop should continue until
      the user enters a positive value greater than 5000 but less than 30000.

   .. sourcecode:: js
      :linenos:

      const input = require('readline-sync');
      let fuelLevel = 0, numAstronauts = 0, altitude = 0;

      while (fuelLevel <= 5000 || fuelLevel > 30000 || isNaN(fuelLevel)) {
         fuelLevel = input.question("Enter the starting fuel level: ");
      }


   c. Use a final loop to monitor the fuel status and the altitude of the
      shuttle. Each iteration, decrease the fuel level by 100 units for each
      astronaut aboard. Also, increase the altitude by 50 kilometers. (Hint:
      The loop should end when there is not enough fuel to boost the crew
      another 50 km, so the fuel level might not reach 0).


   .. sourcecode:: js
      :linenos:

      while (fuelLevel-100*numAstronauts >= 0) {
        altitude += 50;
        fuelLevel -= 100*numAstronauts;
      }

#. After the loops complete, output the result with the phrase, ``The shuttle
   gained an altitude of ___ km.``

   a. If the altitude is 2000 km or higher, add "Orbit achieved!"

   .. sourcecode:: js
      :linenos:

      let output = `The shuttle gained an altitude of ${altitude} km.`;

      if (altitude >= 2000) {
        output += " Orbit achieved!";
      }


:ref:`Back to the exercises <exercises-loops>`.