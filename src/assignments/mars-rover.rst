Assignment #3: Mars Rover
=========================
This task is going to put your unit tests, modules, and exceptions knowledge to use
by writing tests and classes for the Mars rover named Curiosity.

.. figure:: figures/curiosity-rover-selfie.jpg
   :alt: Image of Curiosity rover taken by the rover on Mars.

   Selfie of Curiosity on Mars.


Requirements
------------

#. Fork the `Mars rover starter repl.it <https://repl.it/@launchcode/mars-rover-starter>`_.
#. Write a unit test for each item in the Test List shown below.

   * Some tests have been created for you as examples.

#. Create or update these classes: `Rover`, `Message`, `Command`.

   * Details for each class are below.

#. Use modules

   * Each class should be defined in it's own file and exported and imported using modules.


Test List
---------
Focus on one test at a time. Write the test and *then* the code to make it pass. Only write the minimum
amount of code needed to make the test pass. There are some constraints on
how you can implement these features. A list of required classes and methods is below.

Use these exact phrases as the test description.

Message Tests
^^^^^^^^^^^^^
To be written in ``spec/message.spec.js``.

1. throws error if name NOT passed into constructor as first parameter

   * This test is provided in the starter code. The code to make it pass is also included.

2. constructor sets name
3. contains commands passed into constructor as 2nd argument

Command Tests
^^^^^^^^^^^^^
To be written in ``spec/command.spec.js``.

4. throws error if type is NOT passed into constructor as first parameter

Rover Tests
^^^^^^^^^^^
To be written in ``spec/rover.spec.js``.

5. constructor sets position and default values for mode and generatorWatts
6. response returned by receiveMessage contains name of message
7. response returned by receiveMessage includes two results, if two commands are sent in message
8. responds correctly to status check
9. responds with correct status after MODE_CHANGE
10. responds with false completed value, if attempt to move while in LOW_POWER mode
11. responds with position for move command


Required Classes and Methods
----------------------------
Message Class
^^^^^^^^^^^^^

* ``constructor(name, commands)``

  * ``name`` string name of message
  * ``commands`` is an array of ``Command`` objects
  * Example: ``let message = new Message('e1', commands);``

Command Class
^^^^^^^^^^^^^

* ``constructor(type, value)``

  * ``type`` is a string that represents the command type (see table below for possible values)
  * ``value`` is a value related to the type of command. Example: the mode the rover should change to.
  * Example: ``let command = new Command('MODE_CHANGE', 'LOW_POWER');``

Rover Class
^^^^^^^^^^^

* ``constructor(position)``
  * Sets ``this.position`` to ``position``
  * Sets ``this.mode`` to ``'NORMAL'``
  * Default value for generatorWatts is 110
  * Example: ``new Rover('Example Rover');``

* ``receiveMessage(message)``

  * ``message`` is a ``Message`` object
  * Example: ``let response = rover.receiveMessage(message);``


Rover Commands
--------------
.. list-table::
   :widths: auto
   :header-rows: 1

   * - Command
     - Value(s) sent with command
     - Result
   * - MOVE
     - Number representing the position the rover should move to.
     - ``{completed: true, position: 88929237}``
   * - STATUS_CHECK
     - No values sent with this command.
     - ``{completed: true, mode: 'NORMAL', generatorWatts: 110, position: 87382098}`` Values for ``mode``, ``generatorWatts``, ``position`` will depend on current state of rover.
   * - MODE_CHANGE
     - String representing rover mode (see modes)
     - ``{completed: true}``

.. note:: The response value for ``completed`` will be ``false`` if the command could NOT be completed.


Rover Modes
-----------
.. list-table::
   :widths: auto
   :header-rows: 1

   * - Mode
     - Restrictions
   * - LOW_POWER
     - Can't be moved in this state.
   * - NORMAL
     - None


Bonus Mission
-------------
Add this test to ``spec/rover.spec.js``.

12. respond with completed false and message for unknown command


Submitting Your Work
--------------------

.. todo:: DO THIS
