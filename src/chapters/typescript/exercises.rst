Exercises: TypeScript
=====================

Part 1 - Declare Variables With Type
------------------------------------

#. Fork the `part 1 repl.it <https://repl.it/@launchcode/ts-exercises-part-1-and-2>`_.
#. Declare and assign a variable for each in the below table.

.. list-table::
   :widths: auto
   :header-rows: 1

   * - Variable Name
     - Type
     - Value
   * - spacecraftName
     - string
     - ``'Determination'``
   * - speedMph
     - number
     - 17500
   * - kilometersToMars
     - number
     - 225000000
   * - kilometersToTheMoon
     - number
     - 384400
   * - milesPerKilometer
     - number
     - 0.621


Part 2 - Print Days to Mars
---------------------------
In the *same* repl.it you completed Part 1, do the following.

#. Declare and assign these variables.

   * Remember: variable declarations in TypeScript include the type!
   * ``milesToMars`` is a number with the value of ``kilometersToMars * milesPerKilometer``.
   * ``hoursToMars`` is a number with the value of  ``milesToMars / speedMph``.
   * ``daysToMars`` is a number with the value of ``hoursToMars / 24``.

#. Write a ``console.log`` statement that prints out the days to Mars.

   * Use template literal syntax and the variables ``${spacecraftName}`` and ``${daysToMars}``.

Expected Output

::

   Space Shuttle would take 332.67857142857144 days to get to Mars.


Part 3 - Create a Function
--------------------------
#. Fork the `part 3 repl.it <https://repl.it/@launchcode/ts-exercises-part-3>`_.
#. Define a function that calculates the days it would take to travel.

   * Function name ``getDaysToLocation``
   * Parameters

     *   ``kilometersAway`` must be a number.

   * Returns the number of days to Mars.

     * Use the same calculations as in Part 2.1.
     * Inside the function, make the variables name generic. Use ``milesAway`` and ``hours`` instead of ``milesToMars`` and ``hoursToMars``.
     * The function should declare that it returns a number.

#. Print out the days to Mars.

   * Use template literals, ``${getDaysToLocation(kilometersToMars)}`` and ``${spacecraftName}``.

#. Print out the days to the Moon.

   * Use template literals, ``${getDaysToLocation(kilometersToTheMoon)}`` and ``${spacecraftName}``.

Expected Output

::

   Space Shuttle would take 332.67857142857144 days to get to Mars.
   Space Shuttle would take 0.5683628571428571 days to get to the Moon.


Part 4 - Create a Spacecraft Class
----------------------------------
Organize the function and variables previously defined into a class named ``Spacecraft``.

#. Fork the `part 4 repl.it <https://repl.it/@launchcode/ts-exercises-part-4>`_.
#. Define a class named ``Spacecraft``.

   * Properties

     * ``milesPerKilometer: number = 0.621;``
     * ``name: string;``
     * ``speedMph: number;``

   * Constructor

     * ``name`` is the first parameter and it MUST be a string.
     * ``speedMph`` is the second parameter and it MUST be a number.
     * Sets the class properties using ``this.name`` and ``this.speedMph``.

#. Move the function ``getDaysToLocation``, defined in Part 3, into the ``Spacecraft`` class.

   * Update the function to reference the class properties ``this.milesPerKilometer`` and ``this.speedMph``.

#. Create an instance of the ``Spacecraft`` class.

   * ``let spaceShuttle = new Spacecraft('Space Shuttle', 17500);``

#. Print out the days to Mars.

   * Use template literals, ``${spaceShuttle.getDaysToLocation(kilometersToMars)}`` and ``${spaceShuttle.name}``.

#. Print out the days to the Moon.

   * Use template literals, ``${spaceShuttle.getDaysToLocation(kilometersToTheMoon)}`` and ``${spaceShuttle.name}``.

Expected Output

::

   Space Shuttle would take 332.67857142857144 days to get to Mars.
   Space Shuttle would take 0.5683628571428571 days to get to the Moon.


Part 5 - Export and Import the SpaceLocation Class
--------------------------------------------------
1. Fork the `part 5 repl.it <https://repl.it/@launchcode/ts-exercises-part-5>`_.
2. In repl.it, add a new file named ``SpaceLocation.ts``.
3. Paste in the below code to ``SpaceLocation.ts``.

   * Notice the ``export`` keyword. That is what allows us to import it later.

.. sourcecode:: js
   :linenos:

   export class SpaceLocation {
      kilometersAway: number;
      name: string;

      constructor(name: string, kilometersAway: number) {
         this.name = name;
         this.kilometersAway = kilometersAway;
      }
   }

4. Add the function ``printDaysToLocation`` to the ``Spacecraft`` class.

   * Notice that it takes a parameter of type ``SpaceLocation``.

.. sourcecode:: js
   :linenos:

   printDaysToLocation(location: SpaceLocation) {
      console.log(`${this.name} would take ${this.getDaysToLocation(location.kilometersAway)} days to get to ${location.name}.`);
   }

5. Import ``SpaceLocation`` into ``index.ts``.

   * Add ``import { SpaceLocation } from './SpaceLocation';`` to the top of ``index.ts``.

6. Print out the days to Mars and the Moon.

.. sourcecode:: js
   :linenos:

   let spaceShuttle = new Spacecraft('Space Shuttle', 17500);
   spaceShuttle.printDaysToLocation(new SpaceLocation('Mars', kilometersToMars));
   spaceShuttle.printDaysToLocation(new SpaceLocation('the Moon', kilometersToTheMoon));

Expected Output

::

   Space Shuttle would take 332.67857142857144 days to get to Mars.
   Space Shuttle would take 0.5683628571428571 days to get to the Moon.
