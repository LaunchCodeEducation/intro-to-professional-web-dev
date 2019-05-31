Jasmine in Action
=================

.. index:: test case

Testing is a bit of an art; there are no hard and fast rules about how to go about writing good tests. That said, there are some general principles that you should follow. In this section, we explore some of these.

In particular, we focus on identifying good **test cases** by working through a specific example. A test case is a single situation that is being tested.

What to Test
------------

When writing tests for your code, what should you test? You can't test *every* possible situation or input. But you also don't want to leave out important cases. A function or program that isn't well-tested might have bugs lurking beneath the surface. 

.. note:: Since we are focused on *unit* testing, in this chapter we will generally use the term "unit" to refer to the function or program under consideration.

Regardless of the situation, there are two types of test cases that you should consider: positive/negative tests and edge cases.

A **positive test** is a test case that gives the unit valid data, or, in the case of boolean functions, data that should result in a return value of ``true``. A **negative test** gives the unit *invalid* data, or data that should result in a return value of ``false``.

An **edge case** is a test case that provides input at the extreme edge of what the unit should be able to handle. For example, if a function should work for input values between 0 and 100 then we should test not just values like 5, 50, and 75, but also 0 and 100. These values are at the literal *edge* of acceptable input values. Depending on the behavior function, we may also want to include a negative test with values -1 and 101. 

.. admonition:: Example

   Suppose a program has a collection of addresses for houses within a given city. It has a function, ``getNeighbors``, that will return the immediate neighbors of a given address (those addresses on either side adjacent to the given address).

   Edge cases for this program would include houses on a corner, houses adjacent to a property with no address (for example, a park), and houses in the middle of a block with an alley on one side. 

Considering postive, negetive, and edge tests will go a long way toward helping you create well-tested code.

Let's see these in action, by writing tests for :ref:`our isPalindrome function <palindrome-function>`.

Setting Up
----------

Here's the function we want to test:

.. replit:: js
   :linenos:
   :slug: isPalindrome

   function reverse(str) {
      return str.split('').reverse().join('');
   }

   function isPalindrome(str) {
      return reverse(str) === str;
   }

Code along with us by forking `our repl.it starter code project <https://repl.it/@launchcode/isPalindrome-With-Tests-Starter>`_, which includes the above code in ``palindrome.js`` and the Jasmine test runner code in ``index.js``. Note that we have removed the ``console.log`` statements from the original code and exported the ``isPalindrome`` function:

.. sourcecode:: js

   module.exports = isPalindrome;

.. tip:: When creating a unit-tested project, *always* start by copying the Jasmine test runner code into ``index.js`` and putting the code you want to test in an appropriately named ``.js`` file.

You have become used to testing your code by running it and printint output with ``console.log``. When writing unit-tested code, we no longer need to take this approach. 

.. tip:: If you find yourself tempted to add a ``console.log`` statement to your code, write a unit test instead! You would mostly likely remove that ``console.log`` after getting your code to work, while the test will remain for you and other developers to use in the future.

Finally, create ``spec/`` and add a spec file, ``palindrome.spec.js``. This file should include imports and a describe block:

.. sourcecode:: js
   :linenos:

   const isPalindrome = require('../palindrome.js');
   const assert = require('assert');

   describe("isPalindrome", function(){

      // TODO - write some tests!

   });

Okay, let's write some tests!

Positive and Negative Test Cases
--------------------------------

Positve Test Cases
^^^^^^^^^^^^^^^^^^

We'll start with positive and negative tests. For ``isPalindrome``, some positive tests have inputs:

- ``"a"``
- ``"aaaa"``
- ``"aba"``
- ``"racecar"``

Calling ``isPalindrome`` with these inputs should return ``true`` in each case. Notice that these tests are a simple as possible. Keeping test inputs simple, while still covering your desired test cases, will make it easier to fix a but in the event that a unit test failes.

Let's add tests for these inputs to ``spec/palindrome.spec.js``:

.. sourcecode:: js
   :linenos:

   const isPalindrome = require('../palindrome.js');
   const assert = require('assert');

   describe("isPalindrome", function(){

      it("should return true for a single letter", function(){
         assert.strictEqual(isPalindrome("a"), true);
      });

      it("should return true for a single letter repeated", function(){
         assert.strictEqual(isPalindrome("aaa"), true);
      });

      it("should return true for a simple palindrome", function(){
         assert.strictEqual(isPalindrome("aba"), true);
      });

      it("should return true for a longer palindrome", function(){
         assert.strictEqual(isPalindrome("racecar"), true);
      });

   });

Note the clear test case descriptions (for example, "should return true for a single letter repeated"), which will help us easily identify the expected behavior of our code later.

After adding the positive tests to your file, run them to make sure they all pass.

Negative Test Cases
^^^^^^^^^^^^^^^^^^^

For ``isPalindrome``, some negative tests have inputs:

- ``"ab"``
- ``"launchcode"``
- ``"abA"``
- ``"so many dynamos"``

Calling ``isPalindrome`` with these inputs should return ``false`` in each case. The last two of these negative tests deserve a bit more discussion.

When writing our ``isPalindrome`` function initially, we made two important decisions:

- Case should be considered, and
- whitespace should be considered.

The definition of a palindrome differs sometimes on these two matters, so it's important to test them.

Testing with input ``"abA"``` ensures that case is considered, since the lowercase version of this string, ``"aba"``, *is* a palindrome. Testing with ``"so many dynamos"`` ensures that whitespace is considered, since the version of this string with whitespace removed, ``"somanydynamos"``, *is* a palindrome.

.. note:: It's important to isolate your test cases. For example, ``"So Many Dynamos"`` is a poor choice of input for a negative test, since it contains *two* characteristics that are being tested for, case and the presence of whitespace. If a test with this input failed, it would NOT be clear why it failed.

Including specific tests that demonstrate how *our* ``isPalindrome`` function behaves in these situations helps make our code *self-documenting*. Someone can read our tests and easily see that we *do* consider case and whitespace.

Let's add some test for these negative cases. Add these within the ``describe`` call.

.. sourcecode:: js

   it("should return false for a longer non-palindrome", function(){
      assert.strictEqual(isPalindrome("launchcode"), false);
   });

   it("should return false for a simple non-palindrome", function(){
      assert.strictEqual(isPalindrome("ab"), false);
   });

   it("should be case-sensitive", function(){
      assert.strictEqual(isPalindrome("abA"), false);
   });

   it("should consider whitespace", function(){
      assert.strictEqual(isPalindrome("so many dynamos"), false);
   });
   
Now run the tests to make sure they pass. Your code now includes a set of tests that considers a wide variety of positive and negative cases.

Edge Cases
----------

Recall our definition of **edge case**:

.. pull-quote::

   An edge case is a test case that provides input at the extreme edge of what the unit should be able to handle.

Edge cases can look very different for different units of code. Most of the examples we provided above dealt with numerical edge cases. However, edge cases can also be non-numeric. 

In the case of ``isPalindrome``, the most obvious edge case would be that of the empty string, ``""``. This is the smallest possible string that we can use when calling ``isPalindrome``. Not only is it the smallest, but it is essentially *different* from the next longest string, ``"a"``---one has characters and one doesn't. 

Should the empty string be considered a palindrome? That decision is up to us, the programmer, and there is not right or wrong answer. In our case, we have decided to take a very literal definition of the term "palindrome" by considering case and whitespace. In other words, our definition says that a string is a palindrome exactly when it equals its reverse. Since the reverse of ``""`` is also ``""``, it makes sense to consider the emtpy string a palindrome.

Let's add this test case to our spec:

.. sourcecode:: js

   it("should consider the empty string a palindrome", function(){
      assert.strictEqual(isPalindrome(""), true);
   });

Now run the tests, which should all pass.

You might think that another edge case is that of the longest possible palindrome. Such a palindrome would be as long as the longest possible string in JavaScript. This case is not worth considering for a couple of reasons:

- The length of the longest string `can vary across different JavaScript implementations <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/length#Description>`_.
- The most recent JavaScript specification, ES2016, states that the maximum allowed length of a string should be 2 :sup:`53` - 1 characters. This is a LOT of characters, and it is unrealistic to expect that our function will ever be given such a string.

Toward a Better Testing Workflow
--------------------------------

In this case, we had a well-written function to write tests for, so it was straightforward to create tests that pass. Most situations will not be this simple. You will often find yourself writing tests for code only to discover a bug, forcing you to go back and update your code. That's okay! This is precisely what tests are for.

The workflow for this situation is:

#. Write code
#. Write tests
#. Fix any bugs found while testing

The rest of the chapter focuses on a programming technique that allows you to completly *eliminate* the third step, by reversing the order of the first two:

#. Write tests
#. Write code

As you will soon learn, writing your tests *before* writing your code is a great way to enhance your programming efficiency and quality.
