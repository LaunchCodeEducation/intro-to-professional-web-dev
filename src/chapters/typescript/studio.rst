Studio: TypeScript
==================

Let's practice TypeScript by creating classes for rocket cargo calculations.


Requirements
-------------

#. Login to your `GitHub account <https://github.com/login>`__.
#. Fork the `starter repository <https://github.com/LaunchCodeEducation/typescript-lc101-projects/>`__
   for this studio.
#. Create classes for ``Astronaut``, ``Cargo``, and ``Rocket``. (Details
   below).

   a. All classes should be defined in their own files.

#. Use new classes to run a simulation in the ``index.ts`` file.

In the starter code, you will notice that an interface named ``Payload`` has
been declared. This interface ensures that any class that implements it will
have a ``massKg`` property.


Classes
--------

Define each of these classes in a separate file. Each class should be exported
using ``export``.

.. sourcecode:: js

   export class Astronaut {
      // properties and methods
   }

As needed, the classes can be imported using ``import``.

.. sourcecode:: js

   import { Astronaut } from './Astronaut';

Astronaut Class
^^^^^^^^^^^^^^^^

#. Defined in ``Astronaut.ts``
#. Implements the ``Payload`` interface
#. Properties

   a. ``massKg`` should be a number.
   b. ``name`` should be a string.

#. Constructor

   a. Parameter ``massKg`` should be a number.
   b. Parameter ``name`` should be string.
   c. Sets value of ``this.massKg`` and ``this.name``.

Cargo Class
^^^^^^^^^^^^

#. Defined in ``Cargo.ts``
#. Implements the ``Payload`` interface
#. Properties

   a. ``massKg`` should be a number.
   b. ``material`` should be a string.

#. Constructor

   a. Parameter ``massKg`` should be a number.
   b. Parameter ``material`` should be a string.
   c. Sets value of ``this.massKg`` and ``this.material``

Rocket Class
^^^^^^^^^^^^^

#. Defined in ``Rocket.ts``.
#. Properties:

   a. ``name`` should be a string.
   b. ``totalCapacityKg`` should be a number.
   c. ``cargoItems`` should be an array of ``Cargo`` objects.

      * Should be initialized to an empty array ``[]``

   d. ``astronauts`` should be an array of ``Astronaut`` objects.

      * Should be initialized to an empty array ``[]``

#. Constructor:

   a. Parameter ``name`` should be a string.
   b. Parameter ``totalCapacityKg`` should be a number.
   c. Sets value of ``this.name`` and ``this.totalCapacityKg``

#. Methods:

   a. ``sumMass( items: Payload[] ): number``

      * Returns the sum of all ``items`` using each item's ``massKg`` property

   b. ``currentmassKg(): number``

      * Uses ``this.sumMass`` to return the combined mass of
        ``this.astronauts`` and ``this.cargoItems``

   c. ``canAdd(item: Payload): boolean``

      * Returns ``true`` if ``this.currentmassKg() + item.massKg <= this.totalCapacityKg``

   d. ``addCargo(cargo: Cargo)``.

      * Uses ``this.canAdd()`` to see if another item can be added.
      * If ``true``, adds ``cargo`` to ``this.cargoItems`` and returns
        ``true``.
      * If ``false``, returns ``false``.

   e. ``addAstronaut(astronaut: Astronaut)``.

      * Uses ``this.canAdd()`` to see if another astronaut can be added.
      * If ``true``, adds ``astronaut`` to ``this.astronauts`` and returns ``true``.
      * If ``false``, returns ``false``.

Simulation in ``index.ts``
--------------------------
Paste the code shown below into ``index.ts``.

.. sourcecode:: js
   :linenos:

   import { Astronaut } from './Astronaut';
   import { Cargo } from './Cargo';
   import { Rocket } from './Rocket';

   let falcon9: Rocket = new Rocket('Falcon 9', 7500);

   let astronauts: Astronaut[] = [
      new Astronaut(75, 'Mae'),
      new Astronaut(81, 'Sally'),
      new Astronaut(99, 'Charles')
   ];

   for (let i =0; i < astronauts.length; i++) {
      let astronaut = astronauts[i];
      console.log(astronaut.name, falcon9.addAstronaut(astronaut));
   }

   let cargo: Cargo[] = [
      new Cargo(3107.39, "Satellite"),
      new Cargo(1000.39, "Space Probe"),
      new Cargo(753, "Water"),
      new Cargo(541, "Food"),
      new Cargo(2107.39, "Tesla Roadster"),
   ];

   for (let i =0; i < cargo.length; i++) {
      let c = cargo[i];
      console.log(c.material, falcon9.addCargo(c));
   }

   console.log('final cargo and astronaut mass:', falcon9.currentmassKg());


Expected Console Output
^^^^^^^^^^^^^^^^^^^^^^^

::

   Mae true
   Sally true
   Charles true
   Satellite true
   Space Probe true
   Water true
   Food true
   Tesla Roadster false
   final cargo and astronaut mass: 5656.78


Submitting Your Work
--------------------

In Canvas, open the TypeScript studio and click the "Submit" button. An input
box will appear.

Copy the URL for your repl.it project and paste it into the box, then click
"Submit" again.
