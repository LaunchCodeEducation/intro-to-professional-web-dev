Studio: Objects & Math
======================

In the exercises, you created objects to store data about the candidates for
our animal astronaut corps. For this studio, we provide you with a ready-made
set of candidates.

You must create code to:

A. Select the crew.
B. Perform critical mission calculations.
C. Determine the fuel required for launch.


Select the Crew
---------------

To access the code for exercise 1, open this `repl.it link <https://repl.it/@launchcode/ObjectsStudio01>`__.

Randomly Select ID Numbers
^^^^^^^^^^^^^^^^^^^^^^^^^^

Each candidate was assigned an ID number, which is stored in the candidate's
data file and in the ``idNumbers`` array.

#. Write a ``selectRandomEntry`` function to select a random entry from the
   ``idNumbers`` array. Review the
   :ref:`Combining Math Methods <random-array-item>` section if you need a
   reminder on how to do this.
#. Call the function three times to select three ID numbers. Store these
   selections in a new array, making sure to avoid repeated numbers. No animal
   can be selected more than once!

.. admonition:: Tip

   ``arrayName.includes(item)`` can be used to check if the array already contains
   ``item``. A ``while`` loop can keep the selection process going until the
   desired number of entries have been added to the array.

Build a ``crew`` Array
^^^^^^^^^^^^^^^^^^^^^^

Design a function that takes two arrays as parameters. These hold the randomly
selected ID numbers and the candidate objects.

Use one or more loops to check which animals hold the lucky ID numbers. They
will be going on the space mission! Store these animals in a ``crew`` array,
and then return that array.

Use a template literal to print, ``'____, ____, and ____ are going to space!'``
Fill in the blanks with the names of the selected animals.

Orbit Calculations
------------------

To access the code for the orbit calculations and first bonus mission, go to
`repl.it <https://repl.it/@launchcode/ObjectsStudio02>`__.

#. Spacecraft orbits are not circular, but we will assume that our mission is
   special. The animals will achieve a circular orbit with an altitude of
   2000 km.

   a. Define a function that returns the circumference (C = 2πr) of the orbit.
      Round the circumference to an integer.
   b. Define the ``missionDuration`` function to take three parameters - the
      number of orbits completed, the orbit radius, and the orbital speed. Set
      the default radius to 2000 km and the default orbital speed to
      28000 km/hr.
   c. Calculate how long it will take our animals to complete 5 orbits (time =
      distance/speed). Round the answer to 2 decimal places, then return the
      result.
   d. Print, ``'The mission will travel ____ km around the planet, and it will
      take ____ hours to complete.'``

#. Time for an excursion! Code an ``oxygenExpended`` function to accomplish the
   following:

   a. The function should take a candidate object as a parameter and NOT the
      ``crew`` array.

      .. admonition:: Note

         When you call ``oxygenExpended``, feel free to use your
         ``selectRandomEntry`` to pick the crew member to pass into the
         function.

   b. The spacewalk will last for three orbits around the earth. Use
      ``missionDuration`` to calculate how many hours the spacewalk will take.
   c. Use the candidate's ``o2Used`` method to calculate how much oxygen (O :sub:`2`)
      they consume during the spacewalk. Round the answer to 3 decimal places.
   d. Return the string, ``'__ will perform the spacewalk, which will last __
      hours and require __ kg of oxygen.'`` Fill in the blanks with the
      animal's name, the spacewalk time, and the amount of O :sub:`2` used.
   e. We should not restrict our mission to the default values for orbital
      radius and orbital speed. Refactor ``oxygenExpended`` to accept values
      for these items. Remember to include the values in the
      ``missionDuration`` call.

Bonus Missions
--------------

Conserve O :sub:`2`
^^^^^^^^^^^^^^^^^^^

Instead of randomly selecting a crew member for the spacewalk, have your
program select the animal with the smallest oxygen consumption.

Fuel Required for Launch
^^^^^^^^^^^^^^^^^^^^^^^^

To access the code for this bonus mission, go to
`repl.it <https://repl.it/@launchcode/ObjectsStudio03>`__.

A general rule of thumb states that it takes about 9 - 10 kg of rocket
fuel to lift 1 kg of mass into low-earth orbit (LEO). For our mission, we
will assume a value of 9.5 kg to calculate how much fuel we need to launch
our crew into space.

#. Write a ``crewMass`` function that returns the total mass of the selected
   crew members rounded to 1 decimal place.
#. The mass of the un-crewed rocket plus the food and other supplies is
   75,000 kg. Create a ``fuelRequired`` function to combine the rocket and crew
   masses, then calculate and return the amount of fuel needed to reach LEO.
#. Our launch requires a safety margin for the fuel level, especially if the
   crew members are cute and fuzzy.  Add an extra 200 kg of fuel for each
   dog or cat on board, but only an extra 100 kg for the other species. Update
   ``fuelRequired`` to account for this, then round the final amount of fuel UP
   to the nearest integer.
#. Print ``'The mission has a launch mass of ____ kg and requires ____ kg of
   fuel.'`` Fill in the blanks with the calculated amounts.
