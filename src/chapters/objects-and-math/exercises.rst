Exercises: Objects & Math
==========================

At our space base, it is a historic day! Five non-human animals are ready to run a space mission without our assistance!
For the exercises, you will use the same five animal objects throughout. 

1. Based on the two provided object literals and the following data about the remaining three animals, create the three remaining object literals needed for these exercises.

	.. list-table:: Animal Astronauts
		:header-rows: 1

		+ - Name
		  - Species
		  - Weight (lbs)
		  - Age (years)
		+ - Brad
		  - Chimpanzee
		  - 24
		  - 6
		+ - Leroy
	 	  - Beagle
		  - 30
		  - 5
		+ - Almina
		  - Tardigrade
		  - 0.0000000001
		  - 1  	

2. For each animal, add a property called ``astronautID``. Each ``astronautID`` should be a randomly selected number between 0 and 10. 
   The number can be 10, but it cannot be 0, and the numbers cannot repeat.

3. Create an array to store all of the animal objects.

4. For management at the space base, we need to print out all of the relevant information about the animal astronauts. 
   For each animal, print to the console the following string: "Name is a species. They are ________ years old and _____ lb. Their ID is astronautID.".

5. Before these animal astronauts can get ready for launch, they need to take a physical fitness test. Add a ``move`` method to each animal object.
   The ``move`` method will select a random number of steps for the animal to take.
   Race two animals together to see which one moves 20 steps forward first.
   Use this methodology to run a tournament and rank the animals from fastest to slowest.

`Starter Code <https://repl.it/@launchcode/ObjectsExercises/>`_