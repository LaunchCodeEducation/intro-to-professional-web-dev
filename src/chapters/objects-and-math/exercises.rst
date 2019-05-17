Exercises: Objects & Math
==========================

At our space base, it is a historic day! Five non-human animals are ready to run a space mission without our assistance!
For the exercises, you will use the same five animal objects throughout.

`Starter Code <https://repl.it/@launchcode/ObjectsExercises/>`_

1. Based on the two provided object literals and the following data about the remaining three animals, create the three remaining object literals needed for these exercises.

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

2. For each animal, add a property called ``astronautID``. Each ``astronautID`` should be a randomly selected number between 0 and 10. 
   The number can be 10, but it cannot be 0, and the numbers cannot repeat.

3. Create an array to store all of the animal objects.

4. For upper management at the space base, we need to print out all of the relevant information about the animal astronauts. 
   For each animal, print to the console the following string: ``'____ is a ____. They are ____ years old and ____ kilograms. Their ID is ____.'`` Fill in the blanks with the appropriate values for each animal.

5. Before these animal astronauts can get ready for launch, they need to take a physical fitness test. Add a ``move`` method to each animal object.
   The ``move`` method will select a random number of steps from 0 to 10 for the animal to take.
   Race the five animals together. An animal is done with the race when they reach 20 steps or greater.
   Create a new array to store how many turns it takes each animal to complete the race.
   Print the race results, ``'____ took ____ turns to take 20 steps.'`` Fill in the
   blanks with the animal's name and race result.

	`HINT`: There are a lot of different ways to approach this problem. One way that works well is to see how many iterations of the ``move`` method it will take for one animal to reach 20 steps. Once that has been done for every animal, you can compare the number of iterations to see which animal was the fastest.
