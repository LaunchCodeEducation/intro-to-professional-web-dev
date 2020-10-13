Hello, Jasmine!
===============

.. index:: ! Jasmine

In order to unit test our code, we need to use a module. Such a module is called a **unit-testing framework**, **test runner**, or **test harness**, and there are `many to choose from <https://en.wikipedia.org/wiki/List_of_unit_testing_frameworks#JavaScript>`_.

We will use `Jasmine <https://jasmine.github.io/>`_, a popular JavaScript testing framework.

Using Jasmine
-------------

.. index::
   single: Jasmine; installing

Jasmine is an npm module that can be installed and used in a manner similar to
``readline-sync``. Usually, Jasmine must be manually installed into a project,
but we do not need to learn how to do this yet.

In this chapter we will continue to use repl.it, which automatically installs
npm modules when it runs a program that contains a ``require`` statement.

.. admonition:: Try It!

   Run some `tests for the reverse function <https://repl.it/@launchcode/reverse-Function-With-Tests>`_. This is the same ``reverse`` function that :ref:`we wrote previously <reverse_func>`. 

   Don't worry about understanding the code at this point, just hit *run* to execute the tests. How many total tests are there? How many passed? How many failed? 

.. index::
   single: Jasmine; project structure

A project using Jasmine has several components. Here's the project structure:

.. figure:: figures/jasmine-project-structure.png
   :alt: A small project with three important files: index.js, reverse.js, reverse.spec.js

   A Jasmine project

There are three important files:

#. ``reverse.js`` contains the ``reverse`` function, which must be exported for use in other files.
#. ``spec/reverse.spec.js`` contains the tests for ``reverse``.
#. ``index.js`` contains the Jasmine code needed to run the tests. This is the file that executes when you hit *run* in repl.it.

.. warning:: Jasmine can be set up and used in many different ways. If you are looking for an answer on the Internet (like on Stack Overflow or in the Jasmine documentation) you will see widely varying usages of Jasmine that don't apply to your situation. Rely on this book as your main reference, and you'll be fine.

Hello, Jasmine!
---------------

Let's build a "Hello, World!" Jasmine project, to get familiar with the basic components. Open and fork `this repl.it project <https://repl.it/@launchcode/Hello-Jasmine-Starter-Code>`_

We will walk you through the steps needed to get a simple Jasmine project up and running. Code along with us throughout this section.

``index.js``
^^^^^^^^^^^^

This is the main project file. Up until now, ``index.js`` is where you have been writing the code for a given exercise or assignment. Now that we are writing tests for our code, ``index.js`` will contain the Jasmine code to find and execute the tests. Our project-specific code will live in other files.

.. sourcecode:: js
   :linenos:

   const Jasmine = require('jasmine');
   const jasmine = new Jasmine();

   jasmine.loadConfig({
      spec_dir: 'spec',
      spec_files: [
         "**/*[sS]pec.js"
      ],
   });

   jasmine.execute();

There are three main components of this program:

#. Lines 1-2 import the Jasmine module and create a new Jasmine object, ``jasmine``. This object is responsible for finding and executing our tests.
#. Lines 4-9 configure Jasmine to look for tests in the ``spec/`` directory of our project. Any file in this directory of the form ``fileName.spec.js`` will be assumed to contain tests, and will be executed by Jasmine.
#. Line 11 triggers Jasmine to find and execute the tests.

.. admonition:: Try It!

   Hit *run* on the project. Two things happen:

   - repl.it installs Jasmine.
   - Jasmine searches for tests, finding none.

Let's add some code to test.

.. _hello.js:

``hello.js``
^^^^^^^^^^^^

If you have not already done so, click *Fork* on the repl.it menu bar so you
can edit the starter code.

Create a new file in your project by clicking the icon in the menu bar.

.. figure:: figures/replit-new-file-button.png
   :alt: Repl.it menu button for creating new files

Name the new file ``hello.js``, then add this code:

.. sourcecode:: js
   :linenos:

   function hello(name) {
      if (name === undefined)
         name = "World";

      return "Hello, " + name + "!";
   }

The ``hello`` function takes a single argument representing a person's name and returns a string greeting that person. If the function is called without an argument, the function returns ``"Hello, World!"``.

To use this function outside ``hello.js`` we must export it. Add this statement at the bottom of the file.

.. sourcecode:: js

   module.exports = hello;

``spec/hello.spec.js``
^^^^^^^^^^^^^^^^^^^^^^

Now that we have a function to test, let's write some test code. Add a folder named ``spec`` to the project. Within the folder, create the file ``hello.spec.js``. It is conventional to put tests for ``fileName.js`` in ``spec/fileName.spec.js``. This makes it easy to find the tests associated with a given file.

Your file tree should look something like this:

.. figure:: figures/hello-test-file-tree.png
   :alt: File tree for test project

At the top of the ``hello.spec.js`` file, import your function from ``hello.js``, along with the ``assert`` module:

.. sourcecode:: js
   :linenos:

   const hello = require('../hello.js');
   const assert = require('assert');

Below that, call the function ``describe``, passing in the name of the function we want to test along with an empty anonymous function. ``describe`` is a Jasmine function that is used to group related tests. Related tests are placed *within* the anonymous function that it receives.

.. sourcecode:: js

   describe("hello", function(){

   });

.. _feedback:

Specifications and Assertions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. index::
   single: Jasmine; specification
   single: specification
   single: assertion

There are two cases we want to test:

#. The function is called with a string argument. In this case, a customized greeting should be returned.
#. The function is called with no argument. In this case, the general greeting should be returned.

Within ``describe``'s function argument, place a test for case 1:

.. sourcecode:: js

   it("should return custom message when name is specified", function(){
      assert.strictEqual(hello("Jasmine"), "Hello, Jasmine!");
   });

The ``it`` function is part of the Jasmine framework as well. Calling ``it`` creates a **specification**, or **spec**, which is a description of expected behavior. The first argument to ``it`` is a string describing the expected behavior. This string serves to document the test and is also used in reporting test results. Your expectation strings will usually begin with "should", followed by an expected action.

The second argument to ``it`` is yet another anonymous function. This function contains the test code itself, which takes the form of an **assertion**. An assertion is a declaration of expected behavior *in code*. Let's examine the contents of the anonymous function:

.. sourcecode:: js

   assert.strictEqual(hello("Jasmine"), "Hello, Jasmine!");

Calling ``assert.strictEqual`` with two arguments declares that we expect the two arguments to be (strictly) equal. As you get started with unit testing, nearly *all* of your tests will take this form. The first argument to ``assert.strictEqual`` is a call to the function ``hello``. The second argument is the expected output from that function call. 

If the two arguments are indeed equal, the test will pass. Otherwise, the test will fail. In this case, we are declaring that ``hello("Jasmine")`` should return the value ``"Hello, Jasmine!"``.

.. note::

   Jasmine also has a ``.equal`` comparison, which tests for *loose* equality. The difference between loose and strict equality with Jasmine is the same as that of :ref:`JavaScript in general <equality>`.
   For this reason, we prefer ``.strictEqual`` over ``.equal``.

Your test file should now look like this:

.. sourcecode:: js
   :linenos:

   const hello = require('../hello.js');
   const assert = require('assert');

   describe("hello world test", function(){

      it("should return a custom message when name is specified", function(){
         assert.strictEqual(hello("Jasmine"), "Hello, Jasmine!");
      });

   });

Test Reporting
^^^^^^^^^^^^^^

This is a fully-functioning test file. Hit *run* to see for yourself. If all goes well, the output will look like this:

.. sourcecode:: none
   :linenos:

   Randomized with seed 00798
   Started
   .


   1 spec, 0 failures
   Finished in 0.016 seconds
   Randomized with seed 00798 (jasmine --random=true --seed=00798)

The most important line in the output is this one:

::

   1 spec, 0 failures

It tells us that Jasmine found 1 test specification, and that 0 of the specs failed. In other words, *our test passed!* The third line also contains useful information. It will contain one dot (``.``) for each successful test, and an ``F`` for each failed test. As our test suite grows, this becomes a nice visual indicator of the status of our tests.

Let's see what a test failure looks like. Go back to ``hello.js`` and remove the ``"!"`` from the return statement:

.. sourcecode:: js

   return "Hello, " + name;

Run the tests again. This time, the output looks quite different:

.. sourcecode:: none
   :linenos:

   Randomized with seed 98738
   Started
   F

   Failures:
   1) hello world test should return a custom message when name is specified
   Message:
      AssertionError [ERR_ASSERTION]: Input A expected to strictly equal input B:
      + expected - actual

      - 'Hello, Jasmine'
      + 'Hello, Jasmine!'
   Stack:
      error properties: Object({ generatedMessage: true, code: 'ERR_ASSERTION', actual: 'Hello, Jasmine', expected: 'Hello, Jasmine!', operator: 'strictEqual' })
         at <Jasmine>
         at UserContext.<anonymous> (/home/runner/spec/reverse.spec.js:23:14)
         at <Jasmine>
         at runCallback (timers.js:705:18)
         at tryOnImmediate (timers.js:676:5)
         at processImmediate (timers.js:658:5)

   1 specs, 1 failure
   Finished in 0.021 seconds

We intentionally made a test fail. The failing test appears in the ``Failures:`` section on line 5. This
describes exactly what went wrong. The test expected the value ``'Hello, Jasmine!'`` but received ``'Hello, Jasmine'``.
Notice that the failure description is the result of joining the two string arguments from ``describe`` and ``it``.
This is why we intentionally defined those strings the way we did.

The ``Stack:`` section on line 13 can be mostly ignored for now.
Line 22 has a key statistic showing how many tests, called specs, were run and how many failed ``1 specs, 1 failure``.

Put ``hello.js`` back as it was and run the tests again to make sure it works.

Let's add a final spec to test our other case.

.. sourcecode:: js

   it("should return a general greeting when name is not specified", function(){
        assert.strictEqual(hello(), "Hello, World!");
    });

This spec declares that calling ``hello()`` should return ``"Hello, World!"``. Run the tests again and you'll see this output:

::

   Randomized with seed 81081
   Started
   ..


   2 specs, 0 failures
   Finished in 0.025 seconds
   Randomized with seed 81081 (jasmine --random=true --seed=81081)

Nice work! You just created your first program with a full test suite. You can view `our full Hello, Jasmine! project <https://repl.it/@launchcode/Hello-Jasmine>`_ for reference.

There are a lot of details in the setup of these tests, so take a few minutes to look over the code and describe to yourself what each component is doing.

.. note::

   There are many ways to structure test specifications. If you look at the official Jasmine documentation, you'll see specs with different code in place of ``assert.strictEqual``:

   .. sourcecode:: js

      expect(hello()).toBe("Hello, World!");

   We have chosen to use ``assert.strictEqual`` because its syntax is more similar to common testing frameworks in other languages like Java and C#. Learning to use ``assert.strictEqual`` will make it easier for you to transition to one of those frameworks later in the class.

Check Your Understanding
-------------------------

.. admonition:: Question

   Examine the function below, which checks if two strings match:

   .. sourcecode:: js
      :linenos:

      function doStringsMatch(string1, string2){
         if (string1 === string2) {
            return 'Strings match!';
         } else {
            return 'No match!';
         }
      }

   Which of the following tests checks if the function properly handles
   case-*sensitive* answers.

   a. ``assert.strictEqual(doStringsMatch('Flower', 'Flower'), 'Strings match!');``
   b. ``assert.strictEqual(doStringsMatch('Flower', 'flower'), 'No match!');``
   c. ``assert.strictEqual(doStringsMatch('Flower', 'plant'), 'No match!');``
   d. ``assert.strictEqual(doStringsMatch('Flower', ''), 'No match!');``
