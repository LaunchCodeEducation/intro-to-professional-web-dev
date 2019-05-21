Terminating a Loop With ``break``
---------------------------------

.. index:: 
   single: ! break
   single: loop; termination

JavaScript, like most programming languages, provides a mechanism for terminating a loop before it would complete otherwise. The ``break`` keyword, when used within a loop, will immediately terminate the execution of any loop. Program execution then continues at the next line of code below the loop.

.. admonition:: Example

   This loop executes 12 times, for values of ``i`` from 0 to 11. During the twelfth iteration, ``i`` is 11 and the condition ``i > 10`` evaluates to ``true`` for the first time and execution reaches the ``break`` statement. The loop is immediately terminated at that point.

   .. sourcecode:: js
      :linenos:

      for (let i = 0; i < 42; i++) {
         
         // rest of loop body

         if (i > 10) {
            break;
         }

      }

The ``break`` statement can also be used within a ``while`` loop. Consider a situation where we are searching for a particular element in an array. (We have seen that JavaScript has array methods that can carry out array searches, but many programming languages do not.) 

We can use a ``while`` loop to say, *while we have not reached the end of the array, continue iterating*. We can then include a ``break`` within a conditional check to say, *when we have found the element we are searching for, exit the loop*.

.. admonition:: Example

   A ``while`` loop can be used with ``break`` to search for an element in an array. 

   .. sourcecode:: js
      :linenos:

      let numbers = [ /* some numbers */ ];
      let searchVal = 42;
      let i = 0;

      while (i < numbers.length) {
         if (numbers[i] === searchVal) {
            break;
         }
         i++;
      }

      if (i < numbers.length) {
         console.log("The value", searchVal, "was located at index", i);
      } else {
         console.log("The value", searchVal, "is not in the array.");
      }

Notice that we use a ``while`` loop in this example, rather than a ``for`` loop. This is because our loop variable, ``i``, is used outside the loop. When we use a ``for`` loop in the way we have been, the loop variable exists only within the loop.
