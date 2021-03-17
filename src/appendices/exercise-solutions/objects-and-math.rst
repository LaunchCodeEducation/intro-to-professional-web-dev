.. _objects-and-math-exercise-solutions:

Exercises: Objects & Math
==========================

At our space base, it is a historic day! Five non-human animals are ready to
run a space mission without our assistance! For the exercises, you will use the
same five animal objects throughout.


.. _objects-and-math-exercise-solutions1:

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

Part 1 Exercise Solutions
^^^^^^^^^^^^^^^^^^^^^^^^^

.. sourcecode:: js
   :linenos:

   let superChimpOne = {
       name: "Chad",
       species: "Chimpanzee",
       mass: 9,
       age: 6,
       astronautID: 1,
       move: function () {return Math.floor(Math.random()*11)}
   };

   let salamander = {
       name: "Lacey",
       species: "Axolotl Salamander",
       mass: 0.1,
       age: 5,
       astronautID: 2,
       move: function () {return Math.floor(Math.random()*11)}
   };

   let superChimpTwo = {
       name: "Brad",
       species: "Chimpanzee",
       mass: 11,
       age: 6,
       astronautID: 3,
       move: function () {return Math.floor(Math.random()*11)}
   };

   let dog = {
       name: "Leroy",
       species: "Beagle",
       mass: 14,
       age: 5,
       astronautID: 4,
       move: function () {return Math.floor(Math.random()*11)}
   };

   let waterBear = {
       name: "Almina",
       species: "Tardigrade",
       mass: 0.0000000001,
       age: 1,
       astronautID: 5,
       move: function () {return Math.floor(Math.random()*11)}
   };

   let crew = [superChimpOne, superChimpTwo, salamander, dog, waterBear];


   let crew = [superChimpOne, superChimpTwo, salamander, dog, waterBear];


.. _objects-and-math-exercise-solutions3:

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

.. sourcecode:: js
   :linenos:

   function fitnessTest(candidates){
    let results = [], numSteps, turns;
    for (let i = 0; i < candidates.length; i++){
        numSteps = 0;
        turns = 0;
        while(numSteps < 20){
        numSteps += candidates[i].move();
        turns++;
        }
        results.push(`${candidates[i].name} took ${turns} turns to take 20 steps.`);
    }
    return results;
   }
