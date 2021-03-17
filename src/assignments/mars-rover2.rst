.. _mars-rover2:

Mars Rover, Part 2
==================

In :ref:`Part 1 <mars-rover1>`, you have got a copy of the starter code and taken an initial dive into how the ``Command`` class.
Now's let turn our focus to the ``Message`` class!

``Message``
-----------

Recall, the role of a message object is to bundle commands to send to the rover.

Remember with TDD, to first read through the description of the class. Then read through the given tests and think about what each test means for the desired behavior of the class. 
Only then should you start coding the ``Message`` class.

.. _message-class:

``Message`` Class Description
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. This class builds an object with two properties.
   ``constructor(name, commands)``

   a. ``name`` is a string that is the name of the message.
   b. ``commands`` is an array of ``Command`` objects.

.. admonition:: Example

   .. sourcecode:: js

      let commands = [new Command('MODE_CHANGE', 'LOW_POWER'), new Command('STATUS_CHECK')];
      let message = new Message('Test message with two commands', commands);

``Message`` Tests
^^^^^^^^^^^^^^^^^

At the same level as ``command.spec.js``, look for a file called ``message.spec.js`` and 
read the unit tests for the ``Message`` class as described below. After reading about the test, add the necessary code to the ``Message`` class.

Test 4
~~~~~~

This test description is "throws error if a name is NOT
passed into the constructor as the first parameter". Review the first test
in ``command.spec.js`` for an example of how this test works.

a. When you click "Run", the test will likely fail, because you have no 
   ``Message`` class yet.

b. Create a ``message.js`` file and add ``exports`` 
   and ``require`` statements as needed for your modules.

   .. admonition:: Tip

      For help using ``require`` to import a ``class``, notice in ``command.js``
      that the ``Command`` class is exported using:
      
      .. sourcecode:: js
      
         module.exports = Command;

      In ``spec/command.spec.js``, the ``Command`` class is imported with this
      statement:
      
      .. sourcecode:: js 
      
         const Command = require('../command.js');

c. Look at the code in ``command.js``. Use that to help you write the
   ``Message`` class in ``message.js`` so that your test passes. Refer to
   the :ref:`Message Class <message-class>` description above for more
   details.

Test 5
~~~~~~

The description is "constructor sets name". The test confirms
that the ``constructor`` in the ``Message`` class correctly sets the
``name`` property in a new message object. 

Test 6
~~~~~~

The description reads "contains a commands array passed into the constructor as 2nd argument".
This test confirms that the ``commands`` property of a new message object
contains the data passed in from the ``Message(name, commands)`` call.

.. admonition:: Warning

   You are moving onto the red planet now. Be prepared for fewer instructions.

The final class we need to work on is ``Rover``. Let's check it out in :ref:`Part 3 <mars-rover3>`!