Parameters and Variables
========================

Earlier, we said that a parameter "behaves like a variable that exists only within the function." While this is true, the relationship between variables and parameters is a bit more complicated.

.. _function-scope:

Function Scope
--------------

.. index:: scope

.. index::
   single: function; scope

The **scope** of a variable is the extent to which a variable is visible within
a program. Scope consists of all locations within a program where a variable
can be used or modified. Introducing functions gives us one of our first
examples of limited variable scope---a situation in which a variable is not
visible throughout an entire program.

In particular, *a variable defined using `let` within a function is not visible outside of that function.*

.. admonition:: Example

   This function takes a string and returns the result of removing all hyphens, ``-``, from the string.

   .. sourcecode:: js
      :linenos:

      function removeHyphens(str) {
         let strWithoutHyphens = ''

         for (let i = 0; i < str.length; i++) {
            if (str[i] !== '-') {
               strWithoutHyphens += str[i];
            }
         }

         return strWithoutHyphens;
      }

      let launchCodePhone = "314-254-0107";
      console.log(removeHyphens(launchCodePhone));
      console.log(strWithoutHyphens);

   **Console Output**

   ::

      3142540107
      ReferenceError: strWithoutHyphens is not defined
      (rest of error message omitted)

The last line of this program tries to print the variable ``strWithoutHyphens``
to the console, resulting in an error. The previous line calls
``removeHyphens``, at the end of which ``strWithoutHyphens`` has the value
``"3142540107"``. However, once the function finishes execution all variables
and parameters within the function are destroyed. This is why the last line
results in a ``ReferenceError``; there is no variable named
``strWithoutHyphens`` in existence when that line executes.

This is what we mean when we refer to scope. A variable is not necessarily usable throughout an entire program. Where it can be used depends on the context in which it is defined. For variables *and* parameters within a function, their scope is known as **function scope**. This means that they are only visible within the function in which they are defined.

Variable Shadowing
------------------

We just learned that variables and parameters defined within a function are not visible outside of that function. The opposite scenario is more complicated; a variable defined outside a function *may* be visible within the function, in certain circumstances.

.. admonition:: Example

   In some cases, a variable defined outside of a function may be visible within the function.

   .. sourcecode:: js
      :linenos:
   
      let message = "Hello, World!";

      function printMessage() {
         console.log(message);
      }

      printMessage();

   **Console Output**

   ::

      Hello, World!      

Even though ``message`` is defined outside the function, it is still visible within the function. When ``printMessage`` is called and ``console.log(message);`` executes, ``message`` has the value ``"Hello, World!"``, so that value is printed to the console. This means that the scope of ``message`` extends to the function ``printMessage``.


.. admonition:: Warning

   It is NOT the case that all variables defined outside of a function are
   visible within *every* function. The reality is a bit more nuanced than
   this, and will be explored in depth in a later chapter.

   There is, however, a specific type of variable that is visible to every
   function, known as a **global variable**. We
   :ref:`remarked earlier <global-var-intro>` that a global variable is
   created when initializing a variable without using ``let``, ``const``, or
   ``var``, and they should be used very rarely.

.. admonition:: Try It!

   What is the output of the following program? Form a hypothesis for yourself before running it.

   Once you have answered that question, try relocating the declaring ``message`` to other locations to see how it affects the program. For example, you might try placing it within or after ``printMessage``.

   .. replit:: js
      :linenos:
      :slug: Function-Scope
   
      let message = "Hello, World!";

      function printMessage() {
         console.log(message);
      }

      printMessage();
      message = "Goodbye";
      printMessage();

.. index::
   single: variable; shadowing

An interesting thing happens when a function parameter has the same name as a variable that is in-scope. 

.. admonition:: Example

   .. sourcecode:: js
      :linenos:
   
      let message = "Hello, World!";

      function printMessage(message) {
         console.log(message);
      }

      printMessage("Goodbye");
      
   **Console Output**

   ::

      Goodbye

While the variable ``message`` declared on line 1 is technically visible within ``printMessage`` (that is, it is in-scope), it is hidden by the function parameter of the same name. When ``printMessage("Goodbye")`` is called and ``console.log(message)`` executes, ``message`` has the value ``"Goodbye"``, which is the argument passed into the function. This phenomenon is called **shadowing**, based on the metaphor that a function parameter "casts it's shadow over" a variable of the same name, effectively hiding it. 

There is no good reason to intentionally use variable shadowing in your program. In fact, doing so can lead to confusion over which of the two variables is being used in a given situation. For this reason, *you should avoid naming variables and function parameters the same name.*

Check Your Understanding
------------------------

.. admonition:: Question

   What does the following code output?

   .. sourcecode:: js
      :linenos:

      let num = 42;

      function isEven (num) { 
         return num % 2 === 0; 
      }

      console.log(isEven(43));
