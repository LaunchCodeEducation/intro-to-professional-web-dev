Creating Functions
==================

While using functions that are built into JavaScript is useful, the most powerful aspect of functions is the ability of the programmer to create their own functions. 

.. index::
   single: function; definition
   single: function; syntax

There are several ways to define functions in JavaScript. We will introduce one technique in this chapter and a second technique in the next.

Function Syntax
---------------

To create a function, use the following syntax:

.. sourcecode:: js

   function myFunction(parameter1, parameter2,..., parameterN) {

      // function body

   }

.. index::
   single: function; keyword

Here, ``function`` is a keyword that instructs JavaScript to create a new function using the definition that follows. Since ``function`` is a keyword, it may not be used elsewhere, for example as the name of a function or variable.

.. index::
   single: function; name

Following ``function`` is the **function name**, which is ``myFunction`` in the generic example above. The function name is determined by you, the programmer, and should therefore follow best practices. In particular, function names should use camel case and have descriptive names. We will have more to say about naming functions near the end of this chapter.

.. index::
   single: function; parameter

Within parentheses, following the function name, we define the **function parameters**, or simply **parameters**. Think of parameters as variables that can be used only within the function itself. The number and names of the parameters are determined by the programmer, based on what they want the function to do. A function may also be defined with no parameters at all.

.. index:: Typescript

.. note:: Many programming languages require you to state which data type each parameter should be (for example, string or number). In such languages, if you try to call a function with a parameter of incorrect type, an error results. 

JavaScript *does not* allow you to specify the types of parameters, though the JavaScript extension TypeScript does. We will learn a bit of TypeScript later on.

After the parameters and closing parenthesis, within currly brackets, ``{ }``, is the **function body**. This is where the actions that the function should carry out are defined. The function body can consist of any amount of code.

An Example
^^^^^^^^^^

Let's see function syntax in action. We first consider a program that prints an array of names.

.. sourcecode:: js

   let names = ["Lena", "James", "Julio"];

   for (let i = 0; i < names.length; i++) {
      console.log(names[i]);
   }

Following this pattern, we can create a function that prints *any* array of names.

.. sourcecode:: js

   function printNames(names) {
      for (let i = 0; i < names.length; i++) {
         console.log(names[i]);
      }
   }

Breaking down the components of a function using our new terminology gives us:

- **Function name**: ``printNames``
- **Parameter(s)**: ``names``
- **Body**: 

  .. sourcecode:: js
  
     for (let i = 0; i < names.length; i++) {
         console.log(names[i]);
      }

Notice that there is nothing about this function that forces ``names`` to actually contain names, or even strings. The function will work the same for any array it is given. Therefore, a better name for this function would be ``printArray``.

Our function can be used the same was as each of the built-in functions we have become used to, by calling it.

.. sourcecode:: js

   function printArray(names) {
      for (let i = 0; i < names.length; i++) {
         console.log(names[i]);
      }
   }

   printArray(["Lena", "James", "Julio"]);
   console.log("---");
   printArray(["orange", "apple", "pear"]);

**Output**

::

   Lena
   James
   Julio
   ---
   orange
   apple
   pear

.. index:: ! abstraction

This example illustrates how functions allow us to make our code **abstract**. Abstraction is the process of taking something specific and making it more general. In this example, a loop that prints the contents of a specific array variable (something specific) is transformed into a function that prints the contents of *any* array (something general).

Defining and Calling
--------------------

When we define a function, we are making it available for later use. The function does not execute when it is defined; it must be called in order to execute. This is not only a common point of confusion for new programmers, but can also be the source of logic errors in programs.

Let's see how this works explicitly.

.. admonition:: Try It!

   What happens if we define a function without calling it?

   .. sourcecode:: js
   
      function sayHello() {
         console.log("Hello, World!");
      }
      
      `Run this program at repl.it <https://repl.it/@launchcode/Function-Defnition>`_.


.. admonition:: Question

   What is printed when this program runs? 

In order for a function to run, it must be explicitly called.

.. admonition:: Example

   .. sourcecode:: js
   
      function sayHello() {
         console.log("Hello, World!");
      }

      sayHello();

   **Output**

   ::

      Hello, World!

   
Return Statements
-----------------

.. index::
   single: return
   single: return; value

We have seen that some functions return values that are useful. In particular, the type conversion functions returned the result of converting the input value to the specified data type---calling ``Number("3.14")`` returns the value ``3.14``.

Returning a Value
^^^^^^^^^^^^^^^^^

To return a value from functions that *we* create, we can use a **return statement**. A return statement has the form:

.. sourcecode:: js

   return someVal;

where ``someVal`` is any value. 

.. admonition:: Example

   This function has a single parameter, ``n``, which is expected to be a positive integer. It returns the sum 1+2+...+n. 

   .. sourcecode:: js
   
      function sumToN(n) {
         let sum = 0;
         for (let i = 0; i <= n; i++) {
            sum += i;
         }
         return sum;
      }

      console.log(sumToN(3));

   **Output**
   
   ::

      6

Notice that ``sumToN`` does not print anything; the output comes from the final line of the program, which prints the value *returned by* the function call ``sumToN(3)``. Now that we have return statements in our coding toolbox, we will very rarely print anything within a function. If we want to see the value returned by a function then we must print it *after* calling the function. 

.. admonition:: Question

   The function ``sumToN`` uses a pattern that we have seen previously. What is it called? 

Using **return** is Optional
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

As we saw with our initial examples of function definitions, it is not required that every function explicitly return a value. At it's simplest, a function can even have an empty body.

.. sourcecode:: js

   function doNothing() {}

This function is completely valid, if usefuless. While it doesn't have a return statement, a value is still implicitly returned by JavaScript.

.. admonition:: Example

   A function without a return statement returns the special value ``undefined``.

   .. sourcecode:: js
   
      function doNothing() {}

      let returnVal = doNothing();
      console.log(returnVal);

   **Output**

   ::

      undefined

**return** Terminates Function Execution
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When a return statement executes, the function terminates, regardless of whether or not there is any code following the return statement. This means that you must be careful to use ``return`` only when the work of the function has been completed.

.. admonition:: Example

   This ``console.log`` statement in this function never executes, since the function returns before it is reached.

   .. sourcecode:: js

      function pastThePointOfReturn() {
         return "I'm done!";
         console.log("This will not be printed");
      }

      console.log(pastThePointOfReturn());
   
   **Output**

   ::

      I'm done!

We can use the fact that ``return`` stops the execution of a function intentionally, to force a function to stop execution.

.. admonition:: Example

   This function prints out the integers 1...n using an infinite ``while`` loop, which nonetheless terminates when the ``return`` statement is executed.

   .. sourcecode:: js
   
      function countToN(n) {
         let count = 1;
         while (true) {
            if (count > n) {
               return;
            }
            console.log(count);
            count++;
         }
      }
   

Boolean Functions
^^^^^^^^^^^^^^^^^

.. index::
   pair: function; boolean

A function that returns a boolean value is known as a **boolean function**. Perhaps the simplest such function is one that tests an integer to determine if it is even.

.. admonition:: Example

   .. sourcecode:: js

      function isEven(n) {
         if (n % 2 === 0) {
            return true;
         } else {
            return false;
         }
      }

      console.log(isEven(4));
      console.log(isEven(7));

   **Output**

   ::

      true
      false

It is conventional to name boolean functions by starting with either ``is`` or ``has``, which creates a nice semantic effect when reading the code. For example, reading ``isEven(4)`` communicates to the reader that the function should answer the question, "Is 4 even?" This is a convention so widely used by programmers that it extends to nearly every language. 

Let's return to the ``isEven`` function above, to see how we can use the power of return statements to make it even better.

Since ``return`` terminates the function, we can leave out the ``else`` clause and have the same effect. This is because if ``n`` is even, the return statement in the ``if`` block will execute and the function will end. If ``n`` is odd, the ``if`` block will be skipped and the second return statement will execute.

.. sourcecode:: js

   function isEven(n) {
      if (n % 2 === 0) {
         return true;
      }
      return false;
   }

This updated version works exactly the same as our initial function. 

Additionally, notice that the function returns ``true`` when ``n % 2 === 0`` returns ``true``, and it returns ``false`` when ``n % 2 === 0`` returns ``false``. In other words, the return value is *exactly the same* as the value of ``n % 2 === 0``. This means that we can simplify the function even further by returning the value of this expression.

.. sourcecode:: js

   function isEven(n) {
      return n % 2 === 0;
   }

This version of ``isEven`` is better than the first two, not because it is shorter (shorter isn't always better), but because it is simpler to read. We don't have to break down the conditional logic to see what is being returned.

Most boolean functions can be written so that they return the value of a boolean expression, rather than explicitly returning ``true`` or ``false``. 

Parmeters and Arguments
-----------------------

.. index::
   single: function; argument
   single: function; parameter

Over the past two sections, we introduced two function-related concepts that are very similar, and are often confusing to distinguish: arguments and parameters. If it isn't clear to you what the difference between these two are, then you are not alone. We will attempt to clear that up right now, however.

The easiest way to talk about the difference between arguments and parameters is by referring to an example.

.. admonition:: Example

   The function ``hello`` takes a single value, which we expect to be a person's name, and returns a message that greets that person. 

   .. sourcecode:: js
      :linenos:

      function hello(name) {
         return `Hello, ${name}!`;
      }

      console.log(hello("Lamar"));

   **Output**

   ::

      Hello, Lamar!


In this example, ``name`` is a **parameter**. It is part of the function definition, and *behaves like a variable* that exists only within the function.

The value ``"Lamar"`` that is use when we invoke the function on line 5 is an **argument**. It is a *specific value* that is used during the function call. 

You should think of the difference between an parameter and an argument as being the same as that between a variable and a value. A variable *refers to* a specific value, just like a parameter *refers to* a specific argument when a function is called. Like a value, a variable is a concrete piece of data.

Check Your Understanding
------------------------

.. admonition:: Question

   What does the following code output?

   .. sourcecode:: js

      function plusTwo(num) {
          return num + 2;
      }

      let a = 2;

      for (let i=0; i < 4; i++) {
          a = plusTwo(a);
      }

      console.log(a);

.. admonition:: Question

   What does the following function return?

   .. sourcecode:: js

      function repeater(str) {
          let repeated = str + str;
          console.log(repeated);
      }

   #. The value of ``repeated``
   #. Nothing (no return value)
   #. ``undefined``
   #. The value of ``str``

.. admonition:: Question

   #. What does the following code *output* when executed?

   .. sourcecode:: js

      function repeater(str) {
          let repeated = str + str;
          console.log(repeated);
      }

   #. The value of ``repeated``
   #. Nothing (no output)
   #. ``undefined``
   #. The value of ``str``
