TDD in Action
=============

`Fork our starter code repl.it <https://repl.it/@launchcode/Transmission-processor-TDD-starter>`_
and follow along as we implement a project using TDD.

We need to write a Node module to process transmissions from the
`Voyager1 probe <https://voyager.jpl.nasa.gov/mission/>`_.

.. admonition:: Example

   Transmission

   .. sourcecode:: js

      "1410::<932829840830053761>"

   Expected Result

   .. sourcecode:: js

      {
         id: 1410,
         rawData: 932829840830053761
      }


Requirements
------------
The features for this project have already been broken down into
small testable units. Let's review them and then we will
take it slow, one step at a time.

#. Take in a transmission string and return an object.
#. Return ``-1`` if the transmission does NOT contain ``"::"``.
#. Returned object should contain an ``id`` property

   * The value of ``id`` is the part of the transmission *before* the ``"::"``

#. The ``id`` property should be of type ``Number``
#. Returned object should contain a ``rawData`` property

   * The value of ``rawData`` is the part of the transmission *after* the ``"::"``

#. Return -1 for the value ``rawData`` if the ``rawData`` part of the transmission does NOT start with ``<`` and end with ``>``


Requirement #1
--------------
*Requirement:* Take in a transmission string and return an object.

To get started on this we need to:

a. Create a blank test function.
b. Give the test a name that is a clear, testable statement.

Creating a blank test is easy, go to ``processor.spec.js`` and add an empty test method.
Tests in Jasmine are declared with an ``it`` function.
Remember that tests go inside of the ``describe`` function, which along with the string
parameter describe the group of tests inside.

.. sourcecode:: js
   :linenos:

   const assert = require('assert');

   describe("transmission processor", function() {

      it("", function(){

      });

   });

Give the test the name ``"takes a string returns an object"``.

.. sourcecode:: js
   :linenos:

   const assert = require('assert');

   describe("transmission processor", function() {

      it("takes a string returns an object", function() {

      });

   });

Now that we identified a clear goal for the test, let's add logic and ``assert`` calls
in the test to verify the desired behavior. *But wait...* we haven't added anything
except an empty at this point. There isn't any actual code to verify. That's okay,
this is part of the TDD process.

We are going to think about and visualize
how this feature should be implemented in code. Then we will write out in the test how
this new code will be used.

We need think of something that will satisfy this statement
``it("takes a string returns an object",``.
We have to determine what the ``it`` is. Let's define ``it`` as a function named
``processor``, which is imported from a module named ``processor``.

.. sourcecode:: js
   :linenos:

   const assert = require('assert');
   const processor = require('../processor.js');

   describe("transmission processor", function() {

      it("takes a string returns an object", function(){
         
      });

   });

We have an idea for a function named ``processor`` and we have imported it.
Keep in mind this function only exists as a concept and we are writing a test
to see if this concept makes sense.

Now for the real heart of the test. We are going to use ``assert.strictEqual`` to
verify that if we pass a string to ``processor`` that an object is returned.
Carefully review lines 7 and 8 shown below.

.. sourcecode:: js
   :linenos:

   const assert = require('assert');
   const processor = require('../processor.js');

   describe("transmission processor", function() {

      it("takes a string returns an object", function(){
         let result = processor("9701::<489584872710>");
         assert.strictEqual(typeof result, "object");
      });

   });

On line 7 the ``processor`` function is called, with the value being stored in a ``result``
variable. On line 8 the result of the expression ``typeof result`` is compared to the value
``"object"``. Reminder that the :ref:`typeof operator <typeof>` returns a string representation
of a type. If ``typeof result`` evaluates to the string ``"object"``, then we know that ``processor``
returned an object.

Code Red
^^^^^^^^
Let's run the test! Click the ``run >`` button in your repl.it.
You should see an error about ``processor.js`` not existing. This makes sense, because we have not
created the file yet. We are officially in the Red phase of Red, Green, Refactor!

::

   Error: Cannot find module '../processor.js'


Go Green!
^^^^^^^^^
Now that we have a failing test, we have only one choice. Make it pass.

a. Add a ``processor.js`` file to your repl.it.
b. Inside of the module declare a ``processor`` function that takes a parameter and returns an object.

Contents of the new ``processor.js`` file.

.. sourcecode:: js
   :linenos:

   function process(transmission) {
      return {};
   }

   module.exports = process;


.. figure:: figures/processor-module-added-to-replit.png
       :alt: Screen shot showing processor.js file added to replit with function in it.

       processor.js file

*Run the test again.*

We did it! ``1 spec, 0 failures`` means 1 passing
test. In repl.it you have to imagine the satisfying green color of a passing test.
::

   1 spec, 0 failures
   Finished in 0.011 seconds

Refactor if Needed
^^^^^^^^^^^^^^^^^^
This solution is very simple and does not need to be improved. The refactor step 
does not always lead to an actual changing of your code. The most important part is to
review your code to make sure that it's efficient and meets your team's standards.


Requirement #2
--------------
*Requirement:* Return ``-1`` if the transmission does NOT contain ``"::"``.

Next we have a negative test requirement that tells us what should happen if the data is invalid.
Before jumping into the code, let's review the steps we took to implement requirement #1.

Review of TDD process:

1. Create a blank test function.
2. Give the test a name that is a clear, testable statement.
3. Come up with test data that will trigger the described behavior.
4. Think about what is needed, then write code that fulfills the stated behavior.
5. Run the test and see the it fail.
6. Implement the new code or feature used in the test.
7. Run the test and see it pass.
8. Review to see if refactor needed.

For requirement #2, the solution for *steps 1 - 4* can be seen on lines *11 - 14* below.

.. sourcecode:: js
   :linenos:

   const assert = require('assert');
   const processor = require('../processor.js');

   describe("transmission processor", function() {

      it("takes a string returns an object", function(){
         let result = processor("9701::<489584872710>");
         assert.strictEqual(typeof result, "object");
      });

      it("returns -1 if '::' not found", function(){
         let result = processor("9701<489584872710>");
         assert.strictEqual(result, -1);
      });

   });

Now for *step 5*, run the test and see it fail. When you run the tests, you should see the below
error message. Notice that ``-1`` was the expected value, but the actual value was ``'object'``.
::

   Failures:
   1) transmission processor returns -1 if '::' not found
   Message:
    AssertionError [ERR_ASSERTION]: Input A expected to strictly equal input B:
    + expected - actual
    
    - 'object'
    + -1

Next is *step 6*, write code that will make the test pass. Go to ``processor.js`` and update the ``processor`` function
to check the ``transmission`` argument for the presence of ``'::'``.

.. sourcecode:: js
   :linenos:

   function process(transmission) {
      if (transmission.indexOf("::") < 0) {
         // Data is invalid
         return -1;
      }
      return {};
   }

   module.exports = process;

Lucky *step 7* is to run the tests again. They should both pass.

::

   2 specs, 0 failures
   Finished in 0.035 seconds

Finally *step 8* is to review the code to see if it needs to be refactored. As with the first requirement
our code is quite simple and can not be improved at this time.


Requirement #3
--------------
*Requirement:* Returned object should contain an ``id`` property.
The ``id`` is the part of the transmission *before* the ``"::"``

The same steps will be followed, even though they are not explicitly listed.

See lines *16 - 19* to see the test added for this requirement. To test
this case ``notStrictEqual`` was used, which is checking if the two values
are NOT equal. ``notStrictEqual`` is used to make sure that ``result.id``
is NOT equal to ``undefined``. Remember that if you reference a property on an
object that does NOT exist, ``undefined`` is returned.

.. sourcecode:: js
   :linenos:

   const assert = require('assert');
   const processor = require('../processor.js');

   describe("transmission processor", function() {

      it("takes a string returns an object", function(){
         let result = processor("9701::<489584872710>");
         assert.strictEqual(typeof result, "object");
      });

      it("returns -1 if '::' not found", function(){
         let result = processor("9701<489584872710>");
         assert.strictEqual(result, -1);
      });

      it("returns id in object", function() {
        let result = processor("9701::<489584872710>");
        assert.notStrictEqual(result.id, undefined);
      });

   });

The fail message looks a little different than what we have seen. The phrase
"Identical input passed to notStrictEqual" lets us know that the two values
were equal when we didn't expect them to be.

::

   Failures:
   1) transmission processor returns id in object
   Message:
      AssertionError [ERR_ASSERTION]: Identical input passed to notStrictEqual: undefined

The object returned from ``processor`` doesn't have an id property. We need to
split the transmission on ``'::'`` and then add that value to the object with
the key ``id``. See solution in ``processor.js`` below.

.. sourcecode:: js
   :linenos:

   function process(transmission) {
      if (transmission.indexOf("::") < 0) {
         // Data is invalid
         return -1;
      }
      let parts = transmission.split("::");
      return {
         id: parts[0]
      };
   }

   module.exports = process;

That did it. The tests pass. :)

::

  3 specs, 0 failures
  Finished in 0.011 seconds


Requirement #4
--------------
*Requirement:* The ``id`` property should be of type ``Number``

Again the same steps are followed, though not listed.

New test to be added to ``specs/processor.spec.js``

.. sourcecode:: js
   :linenos:

   it("converts id to a number", function() {
      let result = processor("9701::<489584872710>");
      assert.strictEqual(result.id, 9701);
   });

Fail Message

::

   Failures:
   1) transmission processor converts id to a number
   Message:
      AssertionError [ERR_ASSERTION]: Input A expected to strictly equal input B:
      + expected - actual

      - '9701'
      + 9701


Convert the id part of the string to be of type ``number``.

.. sourcecode:: js
   :linenos:

   function process(transmission) {
      if (transmission.indexOf("::") < 0) {
         // Data is invalid
         return -1;
      }
      let parts = transmission.split("::");
      return {
         id: Number(parts[0])
      };
   }

   module.exports = process;

Now for the great feeling of a passing tests!

::

  4 specs, 0 failures
  Finished in 0.061 seconds

.. note::

   You may be wondering what happens if that data is bad and the id can't be
   turned into a number. That is a negative test case related to this feature
   and is left for you to address in the final section.


Requirement #5
--------------
*Requirement:* Returned object should contain a ``rawData`` property. The ``rawData``
is the part of the transmission *after* the ``"::"``

New test to be added to ``specs/processor.spec.js``

.. sourcecode:: js
   :linenos:

   it("returns rawData in object", function() {
      let result = processor("9701::<487297403495720912>");
      assert.notStrictEqual(result.rawData, undefined);
   });

Fail Message

::

   Failures:
   1) transmission processor returns rawData in object
   Message:
      AssertionError [ERR_ASSERTION]: Identical input passed to notStrictEqual: undefined


We need to extract the rawData from the second half of the transmission string after it's
been split. Then return that in the object.

.. sourcecode:: js
   :linenos:

   function process(transmission) {
      if (transmission.indexOf("::") < 0) {
         // Data is invalid
         return -1;
      }
      let parts = transmission.split("::");
      let rawData = parts[1];
      return {
         id: Number(parts[0]),
         rawData: rawData
      };
   }

   module.exports = process;

It's that time again, our tests pass!

::

  5 specs, 0 failures
  Finished in 0.041 seconds


Requirement #6
--------------
*Requirement:* Return -1 for the value ``rawData`` if the ``rawData`` part of
the transmission does NOT start with ``<`` and end with ``>``

Let's think about what test data to use for this requirement. What ways could the
transmission data be invalid?

1. It could be missing ``<`` at the beginning
2. It could be missing ``>`` at the end
3. It could be missing both ``<`` and ``>``
4. Has ``<`` but is in the wrong place
5. Has ``>`` but is in the wrong place

All these cases need to be covered by a test. Let's start with #1, which
is missing ``<`` at the beginning.

New test to be added to ``specs/processor.spec.js``

.. sourcecode:: js
   :linenos:

   it("returns -1 for rawData if missing < at position 0", function() {
      let result = processor("9701::487297403495720912>");
      assert.strictEqual(result.rawData, -1);
   });

Fail Message

::

   Failures:
   1) transmission processor returns -1 for rawData if missing < at position 0
   Message:
      AssertionError [ERR_ASSERTION]: Input A expected to strictly equal input B:
      + expected - actual
      
      - '487297403495720912>'
      + -1

New code added to ``processor.js`` to make tests pass. Note that we don't simply return
``-1``, the requirement is to return the object and set the value of ``rawData`` to ``-1``.

.. sourcecode:: js
   :linenos:

   function process(transmission) {
      if (transmission.indexOf("::") < 0) {
         // Data is invalid
         return -1;
      }
      let parts = transmission.split("::");
      let rawData = parts[1];
      if (rawData[0] !== "<") {
         rawData = -1;
      }
      return {
         id: Number(parts[0]),
         rawData: rawData
      };
   }

   module.exports = process;

You know what's next, our tests pass!

::

  6 specs, 0 failures
  Finished in 0.056 seconds

.. admonition:: Try It!

   The test data we used was missing ``<`` at the beginning. Add tests
   to cover these cases. ``-1`` should be returned as the value for
   ``rawData`` for all of these.

   * ``"9701::8729740349572>0912"``
   * ``9701::4872<97403495720912"``
   * ``9701::487297403495720912"``
   * ``9701::<487297403495<720912>"``


Use TDD to Add These Features
-----------------------------
Use the steps demonstrated above to implement all or some of the below features.
Take your time, you can do it!

#. Trim leading and trailing whitespace from ``transmission``.
#. Return -1 if the ``id`` part of the ``transmission`` can not be converted to a number.
#. Return -1 if more than one ``"::"`` found in ``transmission``
#. Return -1 for value of ``rawData`` if anything besides numbers are present
#. Allow for multiple ``rawData`` values

   * ``rawData`` would be returned as an array of numbers
   * Get the new test working and then fix any broken existing tests
   * Example Transmission:  ``"9701::<21212.232323.242424>"``
   * Result: ``{ id: 9701, rawData: [21212,232323,242424] }``
