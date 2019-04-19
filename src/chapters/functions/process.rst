.. _sandwich-function:

A Good Function-Writing Process
===============================

The function is the most complex JavaScript construct that we have seen. A function has more components to its syntax than conditionals or loops. In addition, these components can be used in more complicated ways than those other constructs.

To avoid frustration and bugs, it's important to approach writing functions in an intentional, structured way. This is especially true as the functions that you write become more and more complex. 

In this section, we outline what we think is the best approach. To provide concrete examples, we will consider a fictional function that is able to make a sandwich.

Design Your Function
--------------------

Before putting fingers to keyboard, it is important to have a clear idea of what you want your function to do. You should ask yourself the following questions:

- What data (that is, parameters) does my function need to do its job?
- Should my function return a value? (Hint: The answer is almost always "yes.")
- What type of value should my function return?
- What is a good, descriptive name for my function?
- What types do we expect the parameters to be?
- What are good names for my parameters? 

For our sandwich function, the answers might look like this:

.. list-table:: Specification for a Sandwich Function
   :stub-columns: 1

   * - Paremeters
     - bread, filling, condiments
   * - Return Value
     - The finished sandwich
   * - Return Type
     - An object of type ``'sandwich'`` :sup:`*`
   * - Function name
     - ``makeSandwich``
   * - Parameter names and types
     - ``breadType`` (string), ``fillingType`` (string), ``condiments`` (array of strings)
    

\* *We know such a type doesn't exist in JavaScript, but the point we want to make is that you have to be specific. For example, we know we don't want to return a string that describes the sandwich. What use would that be? Additionally, we will learn how to make custom data types in a later lesson, so you could theoretically actually return something of type sandwich.*

Create the Basic Structure
--------------------------

Now it is time to start coding. Using the design decisions that you have just made, write the minimal syntax needed to create the function.

Here's what an outline of our sandwich function would look like:

.. sourcecode:: js

   function makeSandwich(breadType, fillingType, condiments) {

      // TODO: make a sandwich with the given ingredients

   }

Doing this step before writing the body will prevent silly mistakes like leaving off a ``}`` or forgetting to define a parameter.

Write the Body
--------------

With the basic structure in place, go ahead and start writing the function body. Be sure to alternate between sub-tasks and running your code. *Do not wait until you have written the entire function body before testing your code!*

We can't emphasize this enough. Going long stretches of time between program executions is a good way to end up frustrated. Recall in the chapter on debugging that we made the following recommendation to avoid bugs:

.. todo:: Pull quote from debugging chapter, with reference link

This applies *especially* to writing functions. Every good professional programmer works in this way: write a few lines of code, run it, debug any errors, repeat.

Following these steps won't prevent you from making mistakes, but it will certainly reduce the number of bugs that you create while achieving good, working code faster. 

