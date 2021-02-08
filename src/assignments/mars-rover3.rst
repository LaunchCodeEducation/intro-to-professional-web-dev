.. _mars-rover3:

Mars Rover, Part 3
==================

With :ref:`Part 2 <mars-rover2>` completed, let's turn our attention to the final class, the ``Rover`` class.

``Rover``
---------

``Rover`` receives a message object, updates its properties from the message, and 
returns the results.

Remember to use TDD to write the class by first reading the class description, writing tests, and then coding the class!

.. _rover-class:

Rover Class Description
^^^^^^^^^^^^^^^^^^^^^^^

This class builds a rover object with a few properties, and it also contains
a function outside of ``constructor`` to handle updates to its properties.

#. ``constructor(position)``

   a. ``position`` is a number representing the rover's position.
   b. Sets ``this.position`` to ``position``
   c. Sets ``this.mode`` to ``'NORMAL'``
   d. Sets default value for ``generatorWatts`` to 110

#. ``receiveMessage(message)``

   a. ``message`` is a ``Message`` object
   b. Returns an object containing at least two properties:
         
      i. ``message``: the name of the original ``Message`` object
      ii. ``results``: an array of *results*. Each element in the array is an 
          object that corresponds to one ``Command`` in ``message.commands``.
         
   c. Updates certain properties of the rover object

      i. Details about how to respond to different commands are in the
         :ref:`Command Types table <command-types-table>`.

.. admonition:: Example

   .. sourcecode:: js

      let commands = [new Command('MODE_CHANGE', 'LOW_POWER'), new Command('STATUS_CHECK')];
      let message = new Message('Test message with two commands', commands);
      let rover = new Rover(98382);    // Passes 98382 as the rover's position.
      let response = rover.receiveMessage(message);

      console.log(response);

   **Output**

   ::

      {
         message: 'Test message with two commands',
         results: [
            {
               completed: true
            },
            {
               completed: true, 
               roverStatus: { mode: 'LOW_POWER', generatorWatts: 110, position: 98382 }
            }
         ]
      }

``Rover`` Tests
^^^^^^^^^^^^^^^

Create ``spec/rover.spec.js`` and write the following tests. Write the code to
make them pass in ``rover.js``. Remember to use the given phrase as the test
description.

Test 7 
~~~~~~

"constructor sets position and default values for mode and generatorWatts".
Refer to the :ref:`Rover Class <rover-class>` description above for these
default values.

Test 8
~~~~~~

"response returned by receiveMessage contains name of message"

Test 9
~~~~~~

"response returned by receiveMessage includes two results if two commands
are sent in the message"

Test 10
~~~~~~~

"responds correctly to status check command"

a. For the ``STATUS_CHECK`` command, ``receiveMessage(message).results`` 
   includes a ``roverStatus`` object describing the current state of the 
   rover object --- ``mode``, ``generatorWatts``, and ``position``. The test 
   should check each of these for accuracy.
b. See the :ref:`Rover Command Types <command-types-table>` table for more
   details.

Test 11
~~~~~~~

"responds correctly to mode change command". 

a. The test should check the ``completed`` property and rover mode for accuracy.
b. The rover has two modes that can be passed a values to a mode change command,
   'LOW_POWER' and 'NORMAL'.

Test 12
~~~~~~~

"responds with false completed value when attempting to move in LOW_POWER
mode". 

a. The test should check the ``completed`` property for accuracy and confirm 
   that the rover position did not change.
b. Use the :ref:`Rover Modes table <rover-modes-table>` for guidance on how
   to handle move commands in different modes.

Test 13
~~~~~~~

"responds with position for move command".

a. A ``MOVE`` command will update the rover's position with the position value in 
   the command.

.. _command-types-table:

Rover Command Types
--------------------
.. list-table::
   :widths: auto
   :header-rows: 1

   * - Command
     - Value sent with command
     - Updates to ``Rover`` object
     - Result returned
   * - MOVE
     - Number representing the position the rover should move to.
     - ``position``
     - ``{completed: true}``
   * - STATUS_CHECK
     - No values sent with this command.
     - No updates
     - ``{completed: true, roverStatus: {mode: 'NORMAL', generatorWatts: 110, position: 87382098}}`` Values for ``mode``, ``generatorWatts``, ``position`` will depend on current state of rover.
   * - MODE_CHANGE
     - String representing rover mode (see modes)
     - ``mode``
     - ``{completed: true}``

.. note::

   The response value for ``completed`` will be ``false`` if the command could
   NOT be completed.

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


Submitting Your Work
--------------------

Push up your work to your Github repository.
If you have written 13 passing specs and your 3 classes are complete, then you should get a green check mark.

.. admonition:: Tip

   If you believe that your assignment is correct, but you are not getting a green check mark, make sure that you did not edit either ``studentgrading.spec.js``, ``grading.js``, or any file in the ``helpers`` directory inside ``spec``.
   Changes to these files could cause the autograder to malfunction.

In Canvas, open the Mars Rover assignment and click the "Submit" button.
An input box will appear.

Copy the URL for your Github repo and paste it into the box, then click
"Submit" again.
