Exercises: TypeScript
=====================

.. _TS-repo:

Part 0 - Get the Starter Code
------------------------------

#. Login to your GitHub account.
#. Fork the
   `typescript-lc101-projects repository <https://github.com/LaunchCodeEducation/typescript-lc101-projects>`__.
#. Open VSCode and use the terminal panel to clone your fork from GitHub.
#. Use the terminal to navigate into the ``typescript-lc101-projects`` folder,
   then into the ``exercises`` subfolder.

   .. sourcecode:: bash

      $ ls
         typescript-lc101-projects
      $ cd typescript-lc101-projects
      $ ls
         exercises       studio
      $ cd exercises
      $ ls
         SpaceLocation.ts        part3.ts                part5.ts
         part1-2.ts              part4.ts                tsconfig.json

Part 1 - Declare Variables With Type
------------------------------------

From the file tree in VSCode, open the ``part1-2.ts`` file.

.. figure:: ./figures/TS-exercises-file-tree.png
   :alt: VSCode file tree for the TypeScript exercises.

In the space indicated, declare and assign a variable for each of the
following:

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
In the *same* file you opened in Part 1, do the following.

#. Declare and assign these variables.

   a. Remember: variable declarations in TypeScript include the type!
   b. ``milesToMars`` is a number with the value of
      ``kilometersToMars * milesPerKilometer``.
   c. ``hoursToMars`` is a number with the value of
      ``milesToMars / speedMph``.
   d. ``daysToMars`` is a number with the value of ``hoursToMars / 24``.

#. Write a ``console.log`` statement that prints out the days to Mars.

   a. Use template literal syntax and the variables ``${spacecraftName}`` and
      ``${daysToMars}``.

#. Use the terminal in VSCode to compile your ``.ts`` file, then use the
   command ``node part1-2.js`` to run the JavaScript file created during the
   build process.

**Expected Output**

::

   $ tsc part1-2.ts
   $ node part1-2.js
      Determination would take 332.67857142857144 days to get to Mars.

Part 3 - Create a Function
---------------------------

#. From the file tree in VSCode, open the ``part3.ts`` file. Notice that a few
   variables have already been declared and assigned for you.
#. In the space indicated, define a function that calculates the days it would
   take to travel.

   a. Function name ``getDaysToLocation``
   b. Parameters

      * ``kilometersAway`` must be a number.

   c. Returns the number of days to Mars.

      * Use the same calculations as in Part 2.1.
      * Inside the function, make the variable names generic. Use ``milesAway`` and ``hours`` instead of ``milesToMars`` and ``hoursToMars``.
      * The function should declare that it returns a number.

#. Print out the days to Mars.

   a. Use a template literal, ``${getDaysToLocation(kilometersToMars)}`` and
      ``${spacecraftName}``.

#. Print out the days to the Moon.

   a. Use template literals, ``${getDaysToLocation(kilometersToTheMoon)}`` and
      ``${spacecraftName}``.

#. Use the terminal in VSCode to compile your ``.ts`` file, then run the
   ``part3.js`` file.

**Expected Output**

::

   $ tsc part3.ts
   $ node part3.js
      Determination would take 332.67857142857144 days to get to Mars.
      Determination would take 0.5683628571428571 days to get to the Moon.

Part 4 - Create a Spacecraft Class
-----------------------------------

Organize the function and variables previously defined into a class named
``Spacecraft``.

#. From the file tree in VSCode, open the ``part4.ts`` file. Notice that the
   commented-out variables and function need to be moved into a *class*.
#. Define a class named ``Spacecraft``.

   a. Properties

      * ``milesPerKilometer: number = 0.621;``
      * ``name: string;``
      * ``speedMph: number;``

   b. Constructor

      * ``name`` is the first parameter and it MUST be a string.
      * ``speedMph`` is the second parameter and it MUST be a number.
      * Sets the class properties using ``this.name`` and ``this.speedMph``.

#. Move the function ``getDaysToLocation``, defined in Part 3, into the
   ``Spacecraft`` class.

   a. Update the function to reference the class properties
      ``this.milesPerKilometer`` and ``this.speedMph``.

#. Create an instance of the ``Spacecraft`` class.

   a. ``let spaceShuttle = new Spacecraft('Determination', 17500);``

#. Print out the days to Mars.

   a. Use template literals,
      ``${spaceShuttle.getDaysToLocation(kilometersToMars)}`` and
      ``${spaceShuttle.name}``.

#. Print out the days to the Moon.

   a. Use template literals,
      ``${spaceShuttle.getDaysToLocation(kilometersToTheMoon)}`` and
      ``${spaceShuttle.name}``.

#. Use the terminal in VSCode to compile your ``.ts`` file, then run the
   ``part4.js`` file.

**Expected Output**

::

   $ tsc part4.ts
   $ node part4.js
      Determination would take 332.67857142857144 days to get to Mars.
      Determination would take 0.5683628571428571 days to get to the Moon.

Part 5 - Export and Import the SpaceLocation Class
---------------------------------------------------

#. From the file tree in VSCode, open the ``part5.ts`` file.
#. In repl.it, add a new file named ``SpaceLocation.ts``.
#. Paste in the below code to ``SpaceLocation.ts``.

   a. Notice the ``export`` keyword. That is what allows us to import it later.

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

#. Import ``SpaceLocation`` into ``index.ts``.

   * Add ``import { SpaceLocation } from './SpaceLocation';`` to the top of ``index.ts``.

#. Print out the days to Mars and the Moon.

   .. sourcecode:: js
      :linenos:

      let spaceShuttle = new Spacecraft('Determination', 17500);
      spaceShuttle.printDaysToLocation(new SpaceLocation('Mars', kilometersToMars));
      spaceShuttle.printDaysToLocation(new SpaceLocation('the Moon', kilometersToTheMoon));

#. Use the terminal in VSCode to compile your ``.ts`` file, then run the
   ``part5.js`` file.

**Expected Output**

::

   $ tsc part5.ts
   $ node part5.js
      Determination would take 332.67857142857144 days to get to Mars.
      Determination would take 0.5683628571428571 days to get to the Moon.

Sanity Check
-------------

The ``typescript-lc101-projects`` repository has two branches---``master`` and
``solutions``. 'Nuff said.
