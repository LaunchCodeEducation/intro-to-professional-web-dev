Studio: Objects & Math
=======================

In the exercises, you created objects to store data about the candidates for
our animal astronaut corps. For this studio, we provide you with a ready-made
set of candidates.

You must create code to:

A. Select the crew,
B. Perform critical mission calculations,
C. Determine the fuel required for launch.

Select the Crew
----------------

To access the code for exercise 1, open this `repl.it link <https://repl.it/@launchcode/ObjectsStudio01>`__.

1. Each candidate was assigned an ID number, which is stored in the candidate's
   data file and in the ``idNumbers`` array.

   a. Write a function to select a random entry from the ``idNumbers`` array. Review
      the :ref:`Combining Math Methods <random-array-item>` section if you need
      a reminder on how to do this.
   b. Use the function to select three ID numbers.  Store these selections in a new
      array, making sure to avoid repeated numbers. No animal can be selected
      more than once!
   c. Use one or more loops to check which animals hold the lucky ID numbers. They
      will be going on the space mission! Store these animals in a ``crew``
      array.
   d. Use a template literal to print, "____, ____, and ____ are going to space!"
      Fill in the blanks with the names of the selected animals.

.. tip::

   ``arrayName.includes(item)`` can be used to check if the array already contains
   ``item``, and a ``while`` loop can keep the selection process going until the
   desired number of entires have been added to the array.

Orbit Calculations
-------------------

To access the code for exercises 2 - 4, open this `repl.it link <https://repl.it/@launchcode/ObjectsStudio02>`__.

2. Spacecraft orbits are not circular, but we will assume that our mission is
   special. The animals will achieve a circular orbit with an altitude of
   2000 km.

   a. Define a function that returns the circumference (C = 2πr) of the orbit.
      Round the circumference to an integer.
   b. Given an orbital speed of 28000 km/hr, calculate how long will it take our
      animals to complete 5 orbits (time = distance/speed). Round the answer to
      2 decimal places.
   c. Print, "The mission will travel ____ km around the planet, and it will
      take ____ hours to complete."

|

3. Time for an excursion!

   a. Randomly select one crew member to perform a spacewalk.
   b. The spacewalk will last for three orbits around the earth. Calculate how many
      hours the spacewalk will take. Round the answer to 2 decimal places.
   c. Use the animal's ``rate`` method to calculate how much oxygen (O :sub:`2`)
      they consume during the spacewalk. Round the answer to 1 decimal place.
   d. Print, "___ will perform the spacewalk, which will last ____ hours and
      require ___ kg of oxygen." Fill in the blanks with the animal's name, the
      spacewalk time, and the amount of O :sub:`2` used.

Bonus Missions
---------------

Conserve O :sub:`2`
^^^^^^^^^^^^^^^^^^^

4. Instead of randomly selecting a crew member for the spacewalk, have your
   program select the animal with the smallest oxygen consumption rate.

Fuel Required for Launch
^^^^^^^^^^^^^^^^^^^^^^^^^

To access the code for exercise 5, open this `repl.it link <https://repl.it/@launchcode/ObjectsStudio03>`__.

5. A general rule of thumb states that it takes about 9 - 10 kg of rocket
   fuel to lift 1 kg of mass into low-earth orbit (LEO). For our mission, we
   will assume a value of 9.5 kg to calculate how much fuel we need to launch
   our crew into space.

   a. Write a function that returns the total mass of the selected crew
      members.
   b. The mass of the uncrewed rocket plus the food and other supplies is
      75,000 kg. Combine the rocket and crew masses, then calculate and store
      the amount of fuel required to reach LEO.
   c. Our launch requires a safety margin for the fuel level, especially if the
      crew members are cute and fuzzy.  Add an extra 200 kg of fuel for each
      dog or cat on board, but only an extra 100 kg for the other species.
   d. Round the final amount of fuel UP to the nearest integer, then print "The
      mission has a launch mass of ____ kg and requires ____ kg of fuel." Fill
      in the blanks with the calculated amounts.
