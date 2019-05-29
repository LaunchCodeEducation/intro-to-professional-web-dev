Test-Driven Development
=======================
We all want to write code that *works*! How do you know if your code works? You can
manually run your code and review a list of requirements to ensure all are covered.
Or you could write a unit test for each requirement.

.. index:: ! TDD

.. index::
   single: TDD; test-driven development

.. index::
   single: unit testing; TDD

**Test-driven development (TDD)** is a software development process where every feature is
proven to work by having a descriptive and passing unit test. This is enforced by focusing
on the test first. The test process drives the progress of the code and feature.

The TDD process requires a list of small features that are turned into unit tests.
The focus on discrete aspects can lead to clean, clearly defined code.

.. note::

   Using the TDD process is not required when using unit tests. TDD is a process that some
   organizations choose to use.


The Test/Code Cycle
-------------------
When adding a feature with the TDD process, you start by writing a unit test. As with any
unit test, the test should describe a feature or behavior that the code supports.

Because this test is for a feature that does NOT yet exist, we will have to think about
how this feature will be implemented. Is a new parameter needed, maybe a entire new function?

Next write the unit test as if the parameter or function you just imagined already exists.
This may seem a bit odd, but the process of thinking through how new code will be used
helps find bugs and design flaws earlier.

Now run the test! The test should fail or possibly your code will not compile because you
have referenced something that does not exist yet.

Finally you write the code that will make the new test pass. Normally this is where you
would have started, but with TDD the new working code is the last step.

Coding this way builds confidence in your code. No matter how large your code base may
get, you know that each part has a test to validate it's functionality.


Red, Green, Refactor
--------------------

.. index:: ! red green refactor

.. index::
   single: TDD; red green refactor

.. index::
   single: unit testing; red green refactor

While adding new features and making our code work is the main goal, we also want to write
readable, efficient code that we are proud of. The red, green, refactor mantra
describes the process of writing tests, seeing them pass, and then making the code better.
This process is a cycle of three steps. The red and green colors refer to test results which
are often styled with red for failing tests and green for passing tests.

1. Red -> Write a failing test.
2. Green -> Make it pass by implementing the code.
3. Refactor -> Make the code better.


    .. figure:: figures/red-green-refactor-cycle.png
       :alt: Graphic showing the cycle of phases from red the writing test, green making the test pass, and grey of refactoring code to be better which points back to red.

       Red, green, refactor cycle.

Refactoring code means to keep the same overall feature, but change how that feature
is implemented. Examples of this are using different data structures, reducing the
number of times needed to loop through an array, or even moving duplicate logic into
a function so it can be reused.

The refactor will likely require that you change code used in the unit test. That's ok,
the refactor is also done in a TDD process. Decide what is the best way to implement the
feature and then change the unit test to use this new idea. See the test fail, then
implement the refactor idea. Finally see the tests pass with the refactored design.

.. todo:: create our own version of this figure (I copied this from lynda site)


Tests as Documentation
----------------------
Remembering what and why your code does may not seem hard at this time, however as the
number of projects increase and size of the projects grow, so does the need for documentation.

Documentation can be in the form of code comments or external text documents. These can
be helpful, but have one major drawback which is that they can get out of date very
quickly. Out dated, incorrect documentation is very frustrating for a user.

Properly designed unit tests are runnable documentation for your project. Because unit
tests are runnable code that declares and verifies features, they can NEVER get out of
sync with the updated code. If feature is added or removed, the tests must be updated
in order to make them pass.
