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
#. Write a unit test for each item in the :ref:`Test List <rover-test-list>` shown below.

   * Some tests have been created for you as examples.

#. Write classes and methods for each :ref:`required class and method <rover-classes-methods>` shown below.

#. Each class should be defined in it's own file and exported and imported using modules.

.. _rover-test-list:

Test List
---------
Focus on one test at a time. Write the test and *then* the code to make it pass. Only write the minimum
amount of code needed to make the test pass. There are some constraints on
how you can implement these features. A list of :ref:`required classes and methods <rover-classes-methods>` is below.

Each numbered item describes a test. You should use these exact phrases as the test description. You will have
11 tests (12, if you do the bonus) at the end of this assignment.

Message Tests
^^^^^^^^^^^^^
To be written in ``spec/message.spec.js``.

1. Throws error if name NOT passed into constructor as first parameter

   * This test is provided in the starter code. The code to make it pass is also included.

2. Constructor sets name
3. Contains commands passed into constructor as 2nd argument

Command Tests
^^^^^^^^^^^^^
To be written in ``spec/command.spec.js``.

4. Throws error if type is NOT passed into constructor as first parameter

Rover Tests
^^^^^^^^^^^
To be written in ``spec/rover.spec.js``.

5. Constructor sets position and default values for mode and generatorWatts
6. Response returned by receiveMessage contains name of message
7. Response returned by receiveMessage includes two results, if two commands are sent in message
8. Responds correctly to status check
9. Responds with correct status after MODE_CHANGE
10. Responds with false completed value, if attempt to move while in LOW_POWER mode
11. Responds with position for move command

.. _rover-classes-methods:

Required Classes and Methods
----------------------------
Message Class
^^^^^^^^^^^^^

* ``constructor(name, commands)``

  * ``name`` is a string that is the name of the message.
  * ``commands`` is an array of ``Command`` objects.

.. admonition:: Example

   .. sourcecode:: js

      let commands = [new Command('MODE_CHANGE', 'LOW_POWER'), new Command('STATUS_CHECK')];
      let message = new Message('e1', commands);

Command Class
^^^^^^^^^^^^^

* ``constructor(commandType, value)``

  * ``commandType`` is a string that represents the type of command (see :ref:`Command Types table <command-types-table>` for possible values)
  * ``value`` is a value related to the type of command.

.. admonition:: Example

   * ``'MODE_CHANGE'`` is passed in as the ``commandType``
   * ``'LOW_POWER'`` is passed in as the ``value``. For a list of all modes, see :ref:`Rover Modes table <rover-modes-table>`.

   .. sourcecode:: js

      let command = new Command('MODE_CHANGE', 'LOW_POWER');



Rover Class
^^^^^^^^^^^

* ``constructor(position)``

  * ``position`` is a number representing the rover's position.
  * Sets ``this.position`` to ``position``
  * Sets ``this.mode`` to ``'NORMAL'``
  * Sets default value for ``generatorWatts`` to 110

* ``receiveMessage(message)``

  * ``message`` is a ``Message`` object
  * Returns an object containing a result for each ``Command`` in ``message.commands``

    * Specific details about what is returned are in the :ref:`Test List <rover-test-list>`

.. admonition:: Example

   .. sourcecode:: js

      let commands = [new Command('MODE_CHANGE', 'LOW_POWER'), new Command('STATUS_CHECK')];
      let message = new Message('e1', commands);
      let rover = new Rover(98382);
      let response = rover.receiveMessage(message);

.. _command-types-table:

Rover Commands Types
--------------------
.. list-table::
   :widths: auto
   :header-rows: 1

   * - Command
     - Value sent with command
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

.. _rover-modes-table:

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
Add the following test that checks for unknown commands in ``spec/rover.spec.js``.

12. Responds with completed false and a message for an unknown command


Submitting Your Work
--------------------

In Canvas, open the Mars Rover assignment and click the "Submit" button.
An input box will appear.

Copy the URL for your repl.it project and paste it into the box, then click
"Submit" again.
