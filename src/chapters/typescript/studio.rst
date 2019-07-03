Studio: TypeScript
==================

Let's practice TypeScript by creating classes for rocket cargo calculations.


Requirements
------------
#. Fork `the starter repl.it <https://repl.it/@launchcode/rocket-studio-starter>`_.
#. Create classes for ``Astronaut``, ``Cargo``, and ``Rocket``.  (Details below)

   * All classes should be defined in their own files.

#. Use new classes to run a simulation in ``index.ts`` file.

In the starter code, you will notice that an interface named ``Payload`` has been declared.
This interface ensures that any class that implements it will have a ``weightKg`` property.


Classes
-------
Define each of these classes in a separate files. Each class should be exported using ``export``.

.. sourcecode:: js

   export class Astronaut {
      // properties and methods
   }

As needed, the classes can be imported using ``import``.

.. sourcecode:: js

   import { Astronaut } from './Astronaut';

Astronaut Class
^^^^^^^^^^^^^^^

* Defined in ``Astronaut.ts``
* Implements the ``Payload`` interface
* Properties

  * ``weightKg`` should be a number.
  * ``name`` should be a string.

* Constructor

  * Parameter ``weightKg`` should be a number.
  * Parameter ``name`` should be string.
  * Sets value of ``this.weightKg`` and ``this.name``.

Cargo Class
^^^^^^^^^^^

* Defined in ``Cargo.ts``
* Implements the ``Payload`` interface
* Properties

  * ``weightKg`` should be a number.
  * ``material`` should be a string.

* Constructor

  * Parameter ``weightKg`` should be a number.
  * Parameter ``material`` should be a string.
  * Sets value of ``this.weightKg`` and ``this.material``

Rocket Class
^^^^^^^^^^^^

* Defined in ``Rocket.ts``
* Properties

  * ``name`` should be a string.
  * ``totalCapacityKg`` should be a number.
  * ``cargoItems`` should be an array of ``Cargo`` objects.

    * Should be initialized to an empty array ``[]``

  * ``astronauts`` should be an array of ``Astronaut`` objects.

    * Should be initialized to an empty array ``[]``

* Constructor

  * Parameter ``name`` should be a string.
  * Parameter ``totalCapacityKg`` should be a number.
  * Sets value of ``this.name`` and ``this.totalCapacityKg``

* Methods

  * ``sumWeight( items: Payload[] ): number``

    * Returns the sum of all ``items`` using each item's ``weightKg`` property

  * ``currentWeightKg(): number``

    * Uses ``this.sumWeight`` to return the combined weight of ``this.astronauts`` and ``this.cargoItems``

  * ``canAdd(item: Payload): boolean``

    * Returns ``true`` if ``this.currentWeightKg() + item.weightKg <= this.totalCapacityKg``

  * ``addCargo(cargo: Cargo)``

    * Uses ``this.canAdd(item: Payload)`` to see if it can be added

      * If ``true``, adds ``cargo`` to ``this.cargoItems`` and returns ``true``
      * If ``false``, returns ``false``

  * ``addAstronaut(astronaut: Astronaut)``

    * Uses ``this.canAdd(item: Payload)`` to see if it can be added

      * If ``true``, adds ``astronaut`` to ``this.astronauts`` and returns ``true``
      * If ``false``, returns ``false``


Simulation in ``index.ts``
--------------------------
Paste the below code into ``index.ts``.

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

   console.log('final cargo and astronaut weight:', falcon9.currentWeightKg());


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
   final cargo and astronaut weight: 5656.78


Submitting Your Work
--------------------
.. todo:: do these
