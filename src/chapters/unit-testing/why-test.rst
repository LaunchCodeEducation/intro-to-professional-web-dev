Why Test Your Code?
===================

Testing your code is part of the development process. Have you ever written a program and then walked away thinking, *I'm done!*, without having run it? Of course not. You are already used to testing and debugging programs as you write them. In fact, we devoted an entire chapter to :ref:`debugging <errors-and-debugging>` early in the course. 

Your development process probably looks something like this:

#. Write code
#. Run program
#. Notice error and investigate
#. Repeat these steps until there are no more errors

.. index:: ! unit testing

But there's a better way to test your code, using *automated* tests. There are many types of automated tests. This chapter focuses on **unit testing**, which tests the smallest components (or *units*) of code. These are typically individual functions.

Before we dive into the *how* of unit testing, let's discuss the *why*.

Know Your Code *Really* Works
-----------------------------

Manual testing can lead you to a complete, error-free program. But unit testing does even more than that.

Have you ever experienced one of this situation?

.. pull-quote:: You write a program and manually test it. Thinking it is complete, you turn it in only to find that it has a bug or use case that you didn't consider.

Unit testing helps you avoid this. By writing automated tests for your code, you can be confident that your code *really* works.

Find Regressions
----------------

.. index:: ! regression

What about this situation?

.. pull-quote:: You write feature #1 for a program. You then move on to feature #2. After finishing feature #2, you realize that your changes broke feature #1.

This is frustrating, right? With larger programs, it is common that adding can have unexpected consequences for other parts of a program, potentially breaking them. The introduction of such a bug is known as a **regression**. 

If you have a collection of tests that can run quickly and consistently, you will know *right away* if a regression has been introduced to a program. This will allow you to identify and fix it more quickly.

Define Program Expectations
-----------------------------

.. index:: ! self-documenting code

One of the most power aspects of unit testing is that it allows us to clearly define program expectations. As you will soon see, a good collection of unit tests can function as a set of *statements* about *how* the program should behave. You and others can read the tests and quickly get an idea of the specifics of program behavior. 

.. admonition:: Example

   Your coworker gives you a function that validates phone numbers, but doesn't provide much detail. Does it handle country codes? Does it require an area code? Does it allow parentheses around area codes? These details would be easily understood if the function had a collection of unit tests that described its behavior.

Code with a good, descriptive set of unit tests is sometimes called **self-documenting code**.

Let's go ahead and write our first unit test!
