Function Input and Output
=========================

In the introduction to this chapter, we used the metaphor of the :ref:`function machine <function-machine>`, noting that the machine takes *input* and provides *output*. This section focuses on the details of these two aspects of function behavior.

Return Statements
-----------------

.. index::
   single: return
   single: return; value

Some functions return values that are useful. In particular, the type conversion functions convert input to the specified data type and return the result---calling ``Number("3.14")`` returns the value ``3.14``.

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

Notice that ``sumToN`` does not print anything; the output comes from the final line of the program, which prints the value *returned by* the function call ``sumToN(3)``. 

Now that we have return statements in our coding toolbox, we will very rarely print anything *within* a function. If we want to see the value returned by a function then we must print it *after* calling the function. 

.. admonition:: Question

   The function ``sumToN`` uses a pattern that we have seen previously. What is it called? 

Using **return** is Optional
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

As we saw with our initial examples of function definitions, not every function explicitly returns a value. At its simplest, a function can even have an empty body.

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

Over the past two sections, we introduced two function-related concepts that are very similar, and are often confusing to distinguish: *arguments* and *parameters*. The difference between the two is subtle, so we will attempt to clear that up now.

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

The value ``"Lamar"`` that is used when we invoke the function on line 5 is an **argument**. It is a *specific value* that is used during the function call. 

The difference between a parameter and an argument is the same as that between a variable and a value. A variable *refers to* a specific value, just like a parameter *refers to* a specific argument when a function is called. Like a value, an argument is a concrete piece of data.

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

      repeater('Bob');

   #. ``"BobBob"``
   #. Nothing (no return value)
   #. ``undefined``
   #. The value of ``Bob``

.. admonition:: Question

   #. What does the following code *output*?

   .. sourcecode:: js

      function repeater(str) {
          let repeated = str + str;
          console.log(repeated);
      }

      repeater('Bob');

   #. ``"BobBob"``
   #. Nothing (no output)
   #. ``undefined``
   #. The value of ``Bob``

