TDD in Action
=============

Fork `this repl.it <https://repl.it/@launchcode/Transmission-processor-TDD-starter>`_
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
small testable units. Let's review these and then we will
take it slow and handle these one at a time.

#. Take in a transmission string and return an object ``{}``.
#. Return ``-1`` if the transmission does NOT contain ``"::"``.
#. Returned object should contain an ``id`` property

   * The ``id`` is the part of the transmission *before* the ``"::"``

#. The ``id`` property should be of type ``Number``
#. Returned object should contain a ``rawData`` property

   * The ``rawData`` is the part of the transmission *after* the ``"::"``

#. Return -1 if the ``rawData`` part of the transmission does NOT start with ``<`` and end with ``>``


Let's Get Started!
------------------
1. Take in a transmission string and return an object ``{}``.

We need to write our first test. Go to ``processor.spec.js`` and add a test method.

.. sourcecode:: js
   :linenos:

   const assert = require('assert');

   describe("data-processor", function() {

      it("", function(){
         
      });

   });

Now we can write code to verify the stated behavior. We need to take in
a string and return an object. That is a clear and testable statement.
Let's write a test that uses a ``process`` function that takes a ``string``
and returns an ``{}``.


.. sourcecode:: js
   :linenos:

   const assert = require('assert');

   describe("transmission processor", function() {

      it("takes a string returns an object", function(){

      });

   });

.. sourcecode:: js
   :linenos:

   const assert = require('assert');

   describe("transmission processor", function() {

      it("takes a string returns an object", function(){
         // actual then expected
         assert.strictEqual(typeof processor("9701::<123>"), "object");
      });

   });



Try These On Your Own
----------------------
Use TDD to add these features.

1. Trim leading and trailing whitespace from transmission.
2. Return -1 if more than one ``"::"`` found in transmission
3. Return -1 for value of ``rawData`` if anything besides numbers are present
4. Allow for multiple ``rawData`` values

   * ``rawData`` would be returned as an array of numbers
   * Get the new test working and then fix any broken existing tests
   * Example Transmission:  ``"9701::<21212.232323.242424>"``
   * Result: ``{ id: 9701, rawData: [21212,232323,242424] }``

