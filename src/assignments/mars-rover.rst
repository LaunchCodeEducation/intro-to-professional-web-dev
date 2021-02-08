.. _mars-rover1:

Assignment #3: Mars Rover
=========================

This task puts your unit testing, modules making, and exception handling knowledge to
use by writing tests and classes for the Mars rover named Curiosity.

.. figure:: figures/curiosity-rover-selfie.jpg
   :alt: Curiosity rover taken by the rover on Mars.

   Selfie of Curiosity on Mars.

You will create a simulation for issuing commands to Curiosity. The idea is to
create a *command* at mission control, convert that command into a *message*
send it to the *rover*, then have the rover respond to that message.

We will provide descriptions of the required features you need to implement in 
three separate classes:

#. ``Command``: 
   A type of object containing a ``commandType`` property. ``commandType`` is one
   of the given strings in the table below. Some ``commandTypes`` are coupled with
   a ``value`` property, but not all. Every ``Command`` object is a single instruction 
   to be delivered to the rover.
#. ``Message``:
   A ``Message`` object has a ``name`` and contains several ``Command`` objects. 
   ``Message`` is responsible for bundling the commands from mission control and 
   delivering them to the rover.
#. ``Rover``:
   An object representing the mars rover. This class contains information on the rover's
   ``position``, operating ``mode``, and ``generatorWatts``. It also contains a function,
   ``receiveMessage`` that handles the various types of commands it receives and updates 
   the rover's properties.

In true TDD form, you will be asked to first write the appropriate units tests for 
these features, then write the code in the given class to pass those tests. 

Get the Starter Code
--------------------

In `Canvas <learn.launchcode.org>`__, Graded Assignment #3: Mars Rover contains a GitHub Classroom assignment invitation link.
Refer back to the GitHub Classroom instructions from Graded Assignment #0: Hello World for submission instructions.

How-To TDD
----------

Recall that in TDD, you write the test for a given behavior before you code the
actual function. Feel free to review the
:ref:`Test/Code cycle <test-code-cycle>` while you work on this project.

a. Focus on one test at a time.
b. Write the test and *then* create the code to make it pass.
c. Only write the minimum amount of code needed to make the test pass.
d. There are some constraints on how you can implement these features. A description
   of each class is below.

Each numbered item describes a test. *You should use the given phrases as the
test descriptions* when creating your ``it`` statements. You must create 13
tests for this assignment.

.. admonition:: Warning

   Do NOT try to write all of the tests at once. Doing so will be inefficient and will
   cause excessive frustration.


``Command``
-----------

.. _command-class:

``Command`` Class Description
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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

``Command`` Tests
^^^^^^^^^^^^^^^^^

To begin, open and examine ``spec/command.spec.js``. One test has been created for 
you. When a user creates a new ``Command`` object from the class, we want to make 
sure they pass a command type as the first argument.

Test 1 
~~~~~~
   
Note that the test description reads, "throws error if a command type is NOT
passed into the constructor as the first parameter".

a. So far, you have many used expectations to check for equality.
   In the chapter on exceptions, we shared an example of how we might use an expectation to check if an exception is thrown.
   Refer back to that :ref:`example <exception-expectations>` for guidance on the syntax.
b. Click "Run" to verify that the test passes. Next, comment out lines 4-6 in
   ``command.js``. Click "Run" again to verify that the test fails (the
   expected error is not thrown when the ``Command`` class is called).
c. Restore lines 4-6 to ``throw Error("Command type required.");``.
d. Change line 12 in ``command.spec.js`` to ``message: 'Oops'``. Click "Run"
   again to verify that the test fails (the error message did not match
   ``"Command type required."``).
e. Restore line 12 to ``message: "Command type required."``.

Test 2
~~~~~~

Create a second ``Command`` test using, "constructor sets command type" as the
description. This test checks that the ``constructor`` in the ``Command``
class correctly sets the ``commandType`` property in the new object.

a. Without editing, ``command.js`` contains the correct code. Click "Run" to verify that the first
   and second tests both pass.
b. You do not need to use ``expect().toThrow()``.
c. You may not need to know the specific types of commands to write this test.

Test 3 
~~~~~~

Code a third test using, "constructor sets a value passed in as the 2nd
argument" as the description. This test checks that the ``constructor``
correctly sets the ``value`` property in the new object.

a. You may not need to know a proper ``value`` in order to write this test.
   
Click "Run" to verify that all 3 command tests pass.

.. admonition:: Note

   As you move through the remaining instructions, the amount of guidance will
   decrease. Refer to your earlier, passing tests to help you construct new
   tests and passing code.

Great job, astronaut! When you are ready to keep going, check out :ref:`Part 2 <mars-rover2>`!