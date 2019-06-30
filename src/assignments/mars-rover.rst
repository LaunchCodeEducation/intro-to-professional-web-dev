Assignment #3: Mars Rover
=========================
This task is going to put your unit tests, modules, and exceptions knowledge to use
by writing tests and classes for the Mars rover named Curiosity.

.. figure:: figures/curiosity-rover-selfie.jpg
   :alt: Image of Curiosity rover taken by the rover on Mars.

   Selfie of the Curiosity on Mars.


Requirements
------------

#. Fork the `Mars rover starter repl.it <https://repl.it/@launchcode/mars-rover-starter>`_
#. Write a unit test for each item in the Test List shown below

   * Some tests have been created for you as examples

#. Create or update these classes: `Rover`, `Message`, `Command`

   * Details for each class are below

#. Use modules

   * Each class should be defined in it's own file and exported and imported using modules.


Detailed Requirements
---------------------
Focus on one test at a time. Write the test and *then* the code to make it pass. Only write the minimum
amount of code needed to make the test pass. There are some constraints on
how you can implement these features. A list of required classes and methods is below.

Test List
^^^^^^^^^
Use these exact phrases as the test description.

Message tests in ``spec/message.spec.js``

1. throws error if name NOT passed into constructor as first parameter

   * This test is provided in the starter code. The code to make it pass is also included.

2. constructor sets name
3. contains commands passed into constructor as 2nd argument

Command tests in ``spec/command.spec.js``

4. throws error if type is NOT passed into constructor as first parameter

Rover tests in ``spec/rover.spec.js``

5. constructor sets default values for mode and generatorWatts
6. response returned by receiveMessage contains name of message
7. response returned by receiveMessage includes two results, if two commands are sent in message
8. receiveMessage responds correctly to status check
9. status check shows correct mode after mode change
10. TODO ADD MORE...

Required Classes and Methods
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Message Class

* ``constructor(name, commands)``

  * ``name`` string name of message
  * ``commands`` is an array of ``Command`` objects
  * Example: ``let message = new Message('e1', commands);``

Command Class

* ``constructor(type, value)``

  * ``type`` is a string that represents the command type (see table below for possible values)
  * ``value`` is a value related to the type of command. Example: the mode the rover should change to.
  * Example: ``let command = new Command('MODE_CHANGE', 'LOW_POWER');``

Rover Class

* ``constructor()``
  * Sets ``this.mode`` to ``'NORMAL'``
  * Default value for generatorWatts is 110
  * Example: ``new Rover('Example Rover');``

* ``receiveMessage(message)``

  * ``message`` is a ``Message`` object
  * Example: ``let response = rover.receiveMessage(message);``

Rover Commands
^^^^^^^^^^^^^^
.. list-table::
   :widths: auto
   :header-rows: 1

   * - Command
     - Value(s) sent with command
     - Result
   * - MOVE
     - TBD
     - TBD
   * - STATUS_CHECK
     - No values sent with this command.
     - ``{completed: true, mode: 4, generatorWatts: 110}`` Values for ``mode`` and ``generatorWatts`` will depend on current state of rover.
   * - TAKE_SAMPLE
     - TBD
     - TBD
   * - MODE_CHANGE
     - Number between 1-4 representing rover mode (see modes)
     - ``{completed: true}``

Rover Modes
^^^^^^^^^^^
.. list-table::
   :widths: auto
   :header-rows: 1

   * - Mode
     - Restrictions
   * - LOW_POWER
     - Can't do anything in this mode.
   * - STATIONARY
     - Ready to take sample. Can't be moved in this state.
   * - NORMAL
     - None


Bonus Missions
--------------
Some wild and fun stuff...


Submitting Your Work
--------------------

.. todo:: DO THIS
