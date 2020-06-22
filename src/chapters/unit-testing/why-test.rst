Why Test Your Code?
===================

Checking your code is part of the development process. Developers rarely write
code without verifying it. You are used to debugging programs as you write
them. In fact, we devoted an entire chapter to
:ref:`debugging <errors-and-debugging>` early in the course.

Your development process probably looks something like this:

#. Write code
#. Run program
#. Notice error and investigate
#. Repeat these steps until there are no more errors

.. index:: ! unit testing

But there's a better way to test your code, using *automated* tests. Automated tests actively test your code and help to remove the
burden of manual testing. There are many types of automated tests. This chapter focuses on **unit testing**, which tests the smallest
components (or *units*) of code. These are typically individual functions.

Before we dive into the *how* of unit testing, let's discuss the *why*.


Know Your Code *Really* Works
-----------------------------

Manual testing can eventually lead you to a complete, error-free program. Unit testing provides a better alternative.

This might sound familiar:

.. pull-quote::

   You write a program and manually test it. Thinking it is complete, you turn it in only to find that it has a bug
   or use case that you didn't consider.

The unit testing process helps avoid this by starting with a list of specific, clearly stated
behaviors that the program should satisfy. The behaviors are then converted into automated tests that demonstrate
program behavior and provide a framework for writing code that *really* works.


Find Regressions
----------------

.. index:: ! regression

What about this situation?

.. pull-quote:: You write feature #1 for a program. You then move on to feature #2. After finishing feature #2, you realize that your changes broke feature #1.

This is frustrating, right? Especially with larger programs, adding new features often causes unexpected
problems in other parts of the code, potentially breaking the entire program. The introduction of such a bug is
known as a **regression**.

If you have a collection of tests that can run quickly and consistently, you will know *right away* when a
regression appears in your program. This allows you to identify and fix it more quickly.


Tests as Documentation
----------------------

.. index:: ! self-documenting code

One of the most powerful aspects of unit testing is that it allows us to clearly define program expectations.
A good collection of unit tests can function as a set of *statements* about *how*
the program should behave. You and others can read the tests and quickly get an idea of the specifics of
program behavior.

.. admonition:: Example

   Your coworker gives you a function that validates phone numbers, but doesn't provide much detail. Does it handle country codes? Does it require an area code? Does it allow parentheses around area codes? These details would be easily understood if the function had a collection of unit tests that described its behavior.

Code with a good, descriptive set of unit tests is sometimes called **self-documenting code**.

Remembering what your code does and why you structured it a certain way is easy for small programs.
However, as the number of your projects increase and their size grows, the need for documentation
becomes critical.

Documentation can be in the form of code comments or external text documents. These can
be helpful, but have one major drawback which is that they can get out of date very
quickly. Out dated, incorrect documentation is very frustrating for a user.

Properly designed unit tests are runnable documentation for your project. Because unit
tests are runnable code that declares and verifies features, they can NEVER get out of
sync with the updated code. If a feature is added or removed, the tests must be updated
in order to make them pass.


Let's go ahead and write our first unit test!
