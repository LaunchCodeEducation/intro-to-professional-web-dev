Recursion
==========

Quick Review
-------------

In the previous chapter, we learned how to define a function and its
parameters.

.. admonition:: Example

   .. sourcecode:: js

      function addTwoToNumber(num){
         return num += 2;
      }

      console.log(addTwoToNumber(12));

   **Output**

   .. sourcecode:: js

      14

When called, the parameter ``num`` is passed an argument, which in this case is
the number 12. The function executes and returns the value 14, which is then
printed by the ``console.log`` statement.

Functions Can Call Other Functions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Functions should only accomplish one simple task each. To solve more
complicated tasks, one small function must call other functions.

.. admonition:: Example

   .. sourcecode:: js

      function addTwoToNumber(num){
         return num += 2;
      }

      function addFiveToNumber(value){
         let result = addTwoToNumber(value) + 3;
         return result;
      }

      console.log(addFiveToNumber(12))

   **Output**

   .. sourcecode:: js

      17

Of course, there is no need to write a function to add 5 to a value, but the
example demonstrates calling a function from within a function.

Next Step: What is 'Recursion'?
--------------------------------

Rules for Recursion
--------------------
