.. _typescript-exercise-solutions:

Exercise Solutions: TypeScript
================================

.. _typescript-exercise-solutions1:

Part 1 - Declare Variables With Type
------------------------------------

#. Declare the variables with type based on the information given in the table.

   .. sourcecode:: js
      :linenos:

      let spacecraftName: string = 'Determination';
      let speedMph: number = 17500;
      let kilomitersToMars: number = 225000000;
      let kilometersToTheMoon: number = 384400;
      let milesPerKilometer: number = 0.621;

.. _typescript-exercise-solutions2:

Part 2 - Print Days to Mars
---------------------------

2. Use a template literal to print variables.

   .. sourcecode:: js

      console.log(`${spacecraftName} would take ${daysToMars} days to get to Mars.`);

.. _typescript-exercise-solutions3:

Part 3 - Create a Function
--------------------------

#. In the space indicated, define a function that calculates the days it would take to travel to a location.

   .. sourcecode:: js
      :linenos:

      function getDaysToLocation(kilometersAway: number): number {
         let milesAway: number = kilometersAway * milesPerKilometer;
         let hours: number = milesAway / speedMph;
         return hours / 24;
      }

.. _typescript-exercise-solutions4:

Part 4 - Create a Spacecraft Class
----------------------------------

Create a ``Spacecraft`` class.

   .. sourcecode:: js
      :linenos:

      class Spacecraft {
         milesPerKilometer: number = 0.621;
         name: string;
         speedMph: number;

         constructor(name: string, speedMph: number) {
            this.name = name;
            this.speedMph = speedMph;
         }

         getDaysToLocation(kilometersAway: number): number {
            let milesAway: number = kilometersAway * this.milesPerKilometer;
            let hoursToMars: number = milesAway / this.speedMph;
            return hoursToMars / 24;
         }
      }

.. _typescript-exercise-solutions5:

Part 5 - Export and Import the SpaceLocation Class
--------------------------------------------------

After following the steps in Part 5, your ``Spacecraft`` class should look slightly different:

.. sourcecode:: js
   :linenos:

   class Spacecraft {
      milesPerKilometer: number = 0.621;
      name: string;
      speedMph: number;

      constructor(name: string, speedMph: number) {
         this.name = name;
         this.speedMph = speedMph;
      }

      getDaysToLocation(kilometersAway: number): number {
         let milesAway: number = kilometersAway * this.milesPerKilometer;
         let hours: number = milesAway / this.speedMph;
         return hours / 24;
      }

      printDaysToLocation(location: SpaceLocation) {
         console.log(`${this.name} would take ${this.getDaysToLocation(location.kilometersAway)} days to get to ${location.name}.`);
      }
   }
