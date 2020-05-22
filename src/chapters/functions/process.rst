.. _sandwich-function:

A Good Function-Writing Process
===============================

The function is the most complex JavaScript construct that we have seen. Functions have more components to their syntax than conditionals or loops, and can be used in more intricate ways than those constructs.

To avoid frustration and bugs, it's important to approach writing functions in an intentional, structured way. This is essential as you start to write more complex functions. 

In this section, we outline what we think is the best approach. To provide concrete examples, we will consider a fictional function that is able to make a sandwich.

Step 1: Design Your Function
----------------------------

Before putting fingers to keyboard, it is important to have a clear idea of what you want your function to do. You should ask yourself the following questions:

- What data (that is, parameters) does my function need to do its job?
- Should my function return a value? (Hint: The answer is almost always "yes.")
- What should be the data type of my function's return value?
- What is a good, descriptive name for my function?
- What data types do we expect the parameters to be?
- What are good names for my parameters? 

For our sandwich function, the answers might look like this:

.. list-table:: Specification for a Sandwich Function
   :stub-columns: 1

   * - Parameters
     - bread, filling, condiments
   * - Return Value
     - The finished sandwich
   * - Return Type
     - An object of type ``'sandwich'`` :sup:`*`
   * - Function name
     - ``makeSandwich``
   * - Parameter names and types
     - ``breadType`` (string), ``fillingType`` (string), ``condiments`` (array of strings)
    
\* *JavaScript does not actually have a "sandwich" data type, but we want our function to be as flexible as possible. For now, recognize that returning a simple string to describe the sandwich will not be useful. In later lessons, we will learn how to create custom data types, so making a virtual, code-based "sandwich" here is not a problem.*

Step 2: Create the Basic Structure
----------------------------------

Now it is time to start coding. Using the design decisions you just made, write the minimal syntax needed to create the function.

Here's what an outline of our sandwich function would look like:

.. sourcecode:: js
   :linenos:

   function makeSandwich(breadType, fillingType, condiments) {

      // TODO: make a sandwich with the given ingredients

   }

Doing this step before writing the body will prevent silly mistakes like leaving off a ``}`` or forgetting to define a parameter.

Step 3: Write the Body
----------------------

With the basic structure in place, go ahead and start writing the function body. Be sure to alternate between sub-tasks and running your code. *Do not wait until you have written the entire function body before testing your code!*

We can't emphasize this enough. Going long stretches of time without running the program is a good way to end up frustrated. Recall :ref:`in the chapter on debugging <how-to-avoid-debugging>` that we made the following recommendation to avoid bugs:

.. pull-quote:: Get something working and keep it working.

This applies *especially* to writing functions. Every good professional programmer works in this way: write a few lines of code, run it, debug any errors, repeat.

Following these steps won't prevent you from making mistakes, but it will certainly reduce the number of bugs you create. This helps you more quickly produce solid, working code.

