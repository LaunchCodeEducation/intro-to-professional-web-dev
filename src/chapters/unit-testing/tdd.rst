Test-Driven Development
=======================
.. index:: ! TDD

.. index::
   single: TDD; test-driven development

.. index::
   single: unit testing; TDD

Now that we know more about unit testing, we are going to learn a new way of using them.
So far we have written tests to verify functionality of *existing* code. Next we are going
to use tests to verify functionality of code that does NOT already exist. This may sound
odd, but this process has many benefits as we will learn.

As the name sounds **Test-driven development (TDD)** is a software development process
where the unit tests are written first. However that doesn't tell the entire story.
Writing the tests first and intentionally thinking more about the code design leads to
better code. The name comes from the idea of the tests *driving* the development process.

Before we can start using TDD, we need a list of discrete features that can be turned into
unit tests. This will help keep our tests and code easy to read and will build or confidence
as we add functionality.

.. note::

   Using the TDD process is not required when using unit tests. TDD is a process that some
   organizations choose to use.


The Test/Code Cycle
-------------------
With TDD you start with the unit test first. As with any unit test, the test should describe
a feature or behavior that the code supports.

Because this unit test is for a feature that does NOT yet exist, we will have to think about
how this feature will be implemented. Is a new parameter needed, maybe a entire new function?

Next write the unit test as if the parameter or function you just imagined already exists.
This may seem a bit odd, but the process of thinking through how new code will be used
helps avoid bugs and design flaws earlier.

Now run the test! The test should fail or possibly your code will not compile because you
have referenced code that does not exist yet.

Finally, write code to pass the new test. In the earlier chapters, this is where you started,
but with TDD writing new code is the *last* step.

Coding this way builds confidence in your code. No matter how large your code base may
get, you know that each part has a test to validate it's functionality.


Red, Green, Refactor
--------------------

.. index:: ! red green refactor

.. index::
   single: TDD; red green refactor

.. index::
   single: TDD; red, green, refactor

.. index::
   single: unit testing; red green refactor

While adding new features and making our code work is the main goal, we also want to write
readable, efficient code that makes us proud. The red, green, refactor mantra
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
is implemented. Since we have a test to verify our code, we can change the code with
confidence, knowing that any regression will be immediately identified by the test.
Here are a few examples of refactoring using different data structures, reducing the
number of times needed to loop through an array, or even moving duplicate logic into
a function so it can be reused.

The refactor is also done in a TDD process. Decide on what is the improved way of implementing the
feature and then change the unit test to use this new idea. See the test fail, then
implement the refactor idea. Finally see the tests pass with the refactored design.

.. todo:: create our own version of this figure (I copied this from lynda site)
