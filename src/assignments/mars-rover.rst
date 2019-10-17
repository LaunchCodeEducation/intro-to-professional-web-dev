Assignment #3: Mars Rover
==========================

This task puts your unit testing, modules making, and exception handling knowledge to
use by writing tests and classes for the Mars rover named Curiosity.

.. figure:: figures/curiosity-rover-selfie.jpg
   :alt: Image of Curiosity rover taken by the rover on Mars.

   Selfie of Curiosity on Mars.

You will create a simulation for issuing commands to Curiosity. The idea is to
create a *command* at mission control, convert that command into a *message*
send it to the *rover*, then have the rover respond to that message.

We will provide the required features you need to implement in three separate classes:

#. ``Command``: 
   A type of object containing a ``commandType`` property. ``commandType`` is one
   of the given strings in the table below. Some ``commandTypes`` are coupled with
   a ``value`` property, but not all. Every ``Command`` object is a single instruction 
   to be delivered to the rover.
#. ``Message``:
   A ``Message`` object has a ``name`` and contains several ``Command`` objects. 
   ``Message`` is responsible for bundling the commands from mission control and 
   delivering them to the rover.
#. and ``Rover``:
   An object representing the mars rover. This class contains information on the rover's
   ``position``, operating ``mode``, and ``generatorWatts``. It also contains a function,
   ``receiveMessage`` that handles the various types of commands it receives and updates 
   the rover's properties.

In true TDD form, you will be asked to first write the appropriate units tests for 
these features, before writing the code in the given class to pass those tests. 

.. _rover-test-list:

.. Create the Required Files
.. --------------------------

.. In the starter code, the ``command.js`` and ``command.spec.js`` files are already
.. present.

.. .. At the same level as ``command.js``, create two more files---``message.js`` and
.. .. ``rover.js``. Similarly, in the same folder as ``command.spec.js``, create
.. .. ``message.spec.js`` and ``rover.spec.js``.

Getting Started
---------------

#. Fork the `Mars rover starter repl.it <https://repl.it/@launchcode/mars-rover-starter>`__.
#. Write a unit test for each item in the :ref:`Test List <rover-test-list>`
   shown below.

   .. note::
   
      One complete test has been created for you as an example.

#. Use :ref:`test-driven development (TDD) <tdd>` to create each of the
   :ref:`required classes and methods <rover-classes-methods>` described below.

#. Each class should be defined in its own file, which will be exported and
   imported as a module.


How-To TDD
----------

Recall that in TDD, you write the test for a given behavior before you code the
actual function. Feel free to review the
:ref:`Test/Code cycle <test-code-cycle>` while you work on this project.

a. Focus on one test at a time.
b. Write the test and *then* create the code to make it pass.
c. Only write the minimum amount of code needed to make the test pass.
d. There are some constraints on how you can implement these features. A list
   of :ref:`required classes and methods <rover-classes-methods>` is below.

Each numbered item describes a test. *You should use the given phrases as the
test descriptions* when creating your ``it`` statements. You must create 13
tests (14, if you do the bonus) for this assignment.

.. admonition:: Warning

   Did you catch the part about only working on ONE test at a time? Do NOT try
   to write all of the tests at once. Doing so will be inefficient and will
   cause excessive frustration.


``Command``
-----------

.. _command-class:

Command Class
^^^^^^^^^^^^^

We'll follow TDD practices for the creation of ``Message`` and ``Rover``, but for 
this class, ``Command``, we've provided the functionality. ``Command`` is already 
written for you and you do not need to modify it to write passing tests. Open up and 
examine the file ``command.js``. 

#. This class builds an object with two properties.
   ``constructor(commandType, value)``

   a. ``commandType`` is a string that represents the type of command. We will go over
      the details of the types when we get to the ``Rover`` class and tests. At this 
      time, note that a command type will be one of the following: ``'MODE_CHANGE'``, 
      ``'MOVE'``, or ``'STATUS_CHECK'``.
      
      i. To peek ahead at the full functionality of these types, refer to 
         :ref:`Command Types table <command-types-table>`. 

   b. ``value`` is a value related to the type of command.

.. admonition:: Example

   .. sourcecode:: js

      let modeCommand = new Command('MODE_CHANGE', 'LOW_POWER');
      let moveCommand = new Command('MOVE', 12000);

   ``'MODE_CHANGE'`` and ``'MOVE'`` are passed in as the ``commandType``

   ``'LOW_POWER'`` and 12000 are passed in as the ``value``. Different command 
   types require different kinds of values. ``'STATUS_CHECK'`` takes no value.
   
   Don't worry about the mode options for now. To peek ahead, see 
   :ref:`Rover Modes table <rover-modes-table>`.

Now that we've gone over the class, let's check out the tests.

.. _command-tests:

Command Tests
^^^^^^^^^^^^^

To begin, open and examine ``spec/command.spec.js``. One test has been created for 
you. When a user creates a new ``Command`` object from the class, we want to make 
sure they pass a command type as the first argument.

#. Note that the test description reads, "throws error if a command type is NOT
   passed into the constructor as the first parameter".

   a. So far, you have only used ``assert`` methods to check for equality.
      Using ``assert.throws`` to verify if a specific error is thrown is a new
      concept. To learn how to use this new ability of ``assert``, look at the
      constructor in ``command.js`` and look at the test description in
      ``command.spec.js``. You can also look at the
      `official Node.js assert.throws documentation <https://nodejs.org/docs/latest-v10.x/api/assert.html#assert_assert_throws_fn_error_message>`__.
   b. Click "Run" to verify that the test passes. Next, comment out lines 4-6 in
      ``command.js``. Click "Run" again to verify that the test fails (the
      expected error is not thrown when the ``Command`` class is called).
   c. Restore lines 4-6 to ``throw Error("Command type required.");``.
   d. Change line 12 in ``command.spec.js`` to ``message: 'Oops'``. Click "Run"
      again to verify that the test fails (the error message did not match
      ``"Command type required."``).
   e. Restore line 12 to ``message: "Command type required."``.

#. Create a second ``Command`` test using, "constructor sets command type" as the
   description. This test checks that the ``constructor`` in the ``Command``
   class correctly sets the ``commandType`` property in the new object.

   a. Without editing, ``command.js`` contains the correct code. Click "Run" to verity that the first
      and second tests both pass.
   b. You do not need to use ``assert.throws()`` in this test.
   c. You may not need to know the specific types of commands to write this test.

#. Code a third test using, "constructor sets a value passed in as the 2nd
   argument" as the description. This test checks that the ``constructor``
   correctly sets the ``value`` property in the new object.

   a. You may not need to know a proper ``value`` in order to write this test.
   
#. Click "Run" to verity that all 3 command tests pass.

Refer to the :ref:`Command Class <command-class>` description below for more
details about command objects.

.. admonition:: Note

   As you move through the remaining instructions, the amount of guidance will
   decrease. Refer to your earlier, passing tests to help you construct new
   tests and passing code.

Message Tests
^^^^^^^^^^^^^

Create the following tests in ``spec/message.spec.js``, and write the code to
make them pass in ``message.js``. Remember to use the given phrase as the test
description.

4. For this test description use the text, "throws error if a name is NOT
   passed into the constructor as the first parameter". Review the first test
   in ``command.spec.js`` for an example of how to write this test.

   a. When you click "Run", the test should fail, since you have no code in
      the ``Message`` class yet.
   b. Add ``exports`` and ``require`` statements as needed for your modules.
   c. Look at the code in ``command.js``. Use that to help you write the
      ``Message`` class in ``message.js`` so that your test passes. Refer to
      the :ref:`Message Class <message-class>` description below for more
      details.

#. Use "constructor sets name" as the description. The test confirms
   that the ``constructor`` in the ``Message`` class correctly sets the
   ``name`` property in a new message object.
#. Use "contains a commands array passed into the constructor as 2nd argument".
   This test confirms that the ``commands`` property of a new message object
   contains the data passed in from the ``Message(name, commands)`` call.

   a. Hint: Inside this test, you will have to create a ``commands`` array, fill
      it with some ``Command`` objects, and pass it into the ``Message``
      constructor.

.. admonition:: Warning

   You are moving onto the red planet now. Be prepared for fewer instructions.

Rover Tests
^^^^^^^^^^^^

Create the following tests in ``spec/rover.spec.js``, and write the code to
make them pass in ``rover.js``. Remember to use the given phrase as the test
description.

7. "constructor sets position and default values for mode and generatorWatts".
   Refer to the :ref:`Rover Class <rover-class>` description below for these
   default values.
#. "response returned by receiveMessage contains name of message"
#. "response returned by receiveMessage includes two results if two commands
   are sent in the message"
#. "responds correctly to status check command"

   a. For the ``STATUS_CHECK`` command, ``receiveMessage(message)`` returns an
      object with 4 properties---``completed``, ``mode``, ``generatorWatts``,
      and ``position``. The test should check each of these for accuracy.
   b. See the :ref:`Rover Command Types <command-types-table>` table for more
      details.

#. "responds with correct status after MODE_CHANGE". The test should check the
   ``completed`` property and rover mode for accuracy.
#. "responds with false completed value when attempting to move in LOW_POWER
   mode". The test should check the ``completed`` property for accuracy and
   confirm that the rover position did not change.
#. "responds with position for move command".

.. _rover-classes-methods:

Required Classes and Methods
----------------------------

The ``Command`` class is already provided for you in ``command.js``. You will
need to create a ``message.js`` file for the ``Message`` class and a
``rover.js`` file for the ``Rover`` class. The ``Message`` and ``Rover``
classes will need to be exported from their files and imported into the test
files.

.. admonition:: Tip

   For help using ``require`` to import a ``class``, notice in ``command.js``
   that the ``Command`` class is exported using ``module.exports = Command;``.
   In ``spec/command.spec.js`` the ``Command`` class is imported with this
   statement ``const Command = require('../command.js');``.

.. .. _command-class:

.. Command Class
.. ^^^^^^^^^^^^^

.. #. This class builds an object with two properties.
..    ``constructor(commandType, value)``

..    a. ``commandType`` is a string that represents the type of command (see
..       :ref:`Command Types table <command-types-table>` for possible values)
..    b. ``value`` is a value related to the type of command.

.. .. admonition:: Example

..    .. sourcecode:: js

..       let modeCommand = new Command('MODE_CHANGE', 'LOW_POWER');
..       let moveCommand = new Command('MOVE', 12000);

..    ``'MODE_CHANGE'`` and ``MOVE`` are passed in as the ``commandType``

..    ``'LOW_POWER'`` and 12000 are passed in as the ``value``. For a list of all
..    modes, see :ref:`Rover Modes table <rover-modes-table>`.

.. _message-class:

Message Class
^^^^^^^^^^^^^

#. This class builds an object with two properties.
   ``constructor(name, commands)``

   a. ``name`` is a string that is the name of the message.
   b. ``commands`` is an array of ``Command`` objects.

.. admonition:: Example

   .. sourcecode:: js

      let commands = [new Command('MODE_CHANGE', 'LOW_POWER'), new Command('STATUS_CHECK')];
      let message = new Message('Test message with two commands', commands);

.. _rover-class:

Rover Class
^^^^^^^^^^^

This class builds a rover object with one property, but it also contains
several functions outside of ``constructor``.

#. ``constructor(position)``

   a. ``position`` is a number representing the rover's position.
   b. Sets ``this.position`` to ``position``
   c. Sets ``this.mode`` to ``'NORMAL'``
   d. Sets default value for ``generatorWatts`` to 110

#. ``receiveMessage(message)``

   a. ``message`` is a ``Message`` object
   b. Returns an object containing two properties---the original message and an
      array of *results*. Each element in the array is an object that
      corresponds to one ``Command`` in ``message.commands``.
   c. Specific details about how to respond to different commands are in the
      :ref:`Test List <rover-test-list>`.

.. admonition:: Example

   .. sourcecode:: js

      let commands = [new Command('MODE_CHANGE', 'LOW_POWER'), new Command('STATUS_CHECK')];
      let message = new Message('Test message with two commands', commands);
      let rover = new Rover(98382);    // Passes 98382 as the rover's position.
      let response = rover.receiveMessage(message);

      console.log(response.message);
      console.log(response.results);

   **Output**

   ::

      Test message with two commands
      [
         {completed: true},
         {completed: true, mode: 'LOW_POWER', generatorWatts: 110, position: 98382}
      ]

.. _command-types-table:

Rover Command Types
--------------------
.. list-table::
   :widths: auto
   :header-rows: 1

   * - Command
     - Value sent with command
     - Result returned from ``receiveMessage``
   * - MOVE
     - Number representing the position the rover should move to.
     - ``{completed: true, position: 88929237}``
   * - STATUS_CHECK
     - No values sent with this command.
     - ``{completed: true, mode: 'NORMAL', generatorWatts: 110, position: 87382098}`` Values for ``mode``, ``generatorWatts``, ``position`` will depend on current state of rover.
   * - MODE_CHANGE
     - String representing rover mode (see modes)
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


Bonus Mission
--------------

Add the following test that checks for unknown commands in
``spec/rover.spec.js``.

14. Responds with, "completed false and a message for an unknown command".

Submitting Your Work
--------------------

In Canvas, open the Mars Rover assignment and click the "Submit" button.
An input box will appear.

Copy the URL for your repl.it project and paste it into the box, then click
"Submit" again.
