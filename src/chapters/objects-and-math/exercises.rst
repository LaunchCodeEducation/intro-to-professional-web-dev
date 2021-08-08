.. _exercises-objects-and-math:

Exercises: Objects & Math
==========================

At our space base, it is a historic day! Five non-human animals are ready to
run a space mission without our assistance! For the exercises, you will use the
same five animal objects throughout.

`Starter Code <https://repl.it/@launchcode/ObjectsExercises/>`_

Part 1: Create More Objects
----------------------------

Based on the two object literals provided in the starter code, create new
object literals for three more animals:

.. list-table:: Animal Astronauts
   :header-rows: 1

   + - Name
     - Species
     - Mass (kg)
     - Age (years)
   + - Brad
     - Chimpanzee
     - 11
     - 6
   + - Leroy
     - Beagle
     - 14
     - 5
   + - Almina
     - Tardigrade
     - 0.0000000001
     - 1

Add a New Property
^^^^^^^^^^^^^^^^^^^

For each animal, add a property called ``astronautID``. Each ``astronautID``
should be assigned a number between 1 and 10 (including 10). However, no
crew members should have the same ID.

Add a Method
^^^^^^^^^^^^^

Add a ``move`` method to each animal object. The ``move`` method will select a
random number of steps from 0 to 10 for the animal to take. The number can
be 0 as well as 10.

Store the Objects
^^^^^^^^^^^^^^^^^^

Create a ``crew`` array to store all of the animal objects.

:ref:`Check your solution <objects-and-math-exercise-solutions1>`. 

Part 2: Crew Reports
---------------------

Upper management at the space base wants us to report all of the relevant
information about the animal astronauts.

Define a ``crewReports`` function to accomplish this. When passed one of the
animal objects, the function returns a template literal with the following
string:
``'____ is a ____. They are ____ years old and ____ kilograms. Their ID is
____.'``

Fill in the blanks with the name, species, age, mass, and ID for the selected
animal.

Part 3: Crew Fitness
---------------------

Before these animal astronauts can get ready for launch, they need to take a
physical fitness test. Define a ``fitnessTest`` function that takes an array as
a parameter.

Within the function, race the five animals together by using the ``move``
method. An animal is done with the race when they reach 20 steps or greater.
Store the result as a string: ``'____ took ____ turns to take 20 steps.'``
Fill in the blanks with the animal’s name and race result. Create a new array
to store how many turns it takes each animal to complete the race.

Return the array from the function, then print the results to the console (one
animal per line).

*HINT*: There are a lot of different ways to approach this problem. One way
that works well is to see how many iterations of the ``move`` method it will
take for each animal to reach 20 steps.

:ref:`Check your solution <objects-and-math-exercise-solutions3>`.
