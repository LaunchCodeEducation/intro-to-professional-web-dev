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
#. Create or update these classes: `Rover`, `Message`, `Command`

   * Details for each class are below

#. Use modules. Each class should be defined in it's own file and exported and imported using modules.


Detailed Requirements
---------------------
Unit tests verify and document functionality. For this assignment your job is to implement the tests listed below.
As an example, one test and the code that makes it pass has been provided in the starter project.

Focus on one test at a time. Write the test and then the code to complete that test. There are some constraints on
how you can implement these features. A list of required classes and methods is below.

Test List
^^^^^^^^^
Use these exact phrases as the test description.

Message Tests

#. throws error if name no passed into constructor as first parameter
#. should have a name if one passed into constructor
#. should have array of commands if passed in as 2nd argument to constructor

Command Tests

#. throws error if number is NOT passed into constructor as first parameter

Rover Tests

#. throws error if name no passed into constructor as first parameter
#. has name with default values for mode and generatorWatts when created by constructor

   * Default value for mode is NORMAL
   * Default value for generatorWatts is 110

#. receiveMessage throws exception if first parameter is NOT a message object
#. response returned by receiveMessage contains name of message response is for
#. response returned by receiveMessage includes two results if two commands are sent in message
#. receiveMessage responds correctly to status check

Required Classes and Methods
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Message Class

* ``constructor(name, commands)``

  * ``name`` string name of message
  * ``commands`` is an array of ``Command`` objects

Command Class

* ``constructor(type, value)``

  * ``type`` is a number that represents the command (see table below)
  * ``value`` is a value related to the type of command. Example: the mode the rover should change to.

Rover Class

* ``constructor(name)``

  * ``name`` string name of message

* ``receiveMessage(message)``

  * ``message`` is a ``Message`` object

Rover Commands
^^^^^^^^^^^^^^
.. list-table::
   :widths: auto
   :header-rows: 1

   * - Command
     - Number
     - Value(s) sent with command
     - Result returned
   * - MOVE
     - 1
     - TBD
     - TBD
   * - STATUS_CHECK
     - 2
     - No values sent with this command.
     - ``{completed: true, mode: 4, generatorWatts: 110}`` Values for ``mode`` and ``generatorWatts`` will depend on current state of rover.
   * - TAKE_SAMPLE
     - 3
     - TBD
     - TBD
   * - MODE_CHANGE
     - 4
     - Number between 1-4 representing rover mode (see modes)
     - ``{completed: true}``

Rover Modes
^^^^^^^^^^^
.. list-table::
   :widths: auto
   :header-rows: 1

   * - Mode
     - Number
     - Restrictions
   * - LOW_POWER
     - 1
     - Can't do anything in this mode.
   * - STATIONARY
     - 3
     - Ready to take sample. Can't be moved in this state.
   * - NORMAL
     - 3
     - None


Bonus Missions
--------------
Some wild and fun stuff...


Submitting Your Work
--------------------

.. todo:: DO THIS
