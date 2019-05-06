Recursion Walkthrough: The Base Case
=====================================

To ease into the concept of recursion, let's start with a loop task.

In the Arrays chapter, we examined  the ``join`` method, which combines the
elements of an array into a single string. If we have
``arr = ['L', 'C', '1', '0', '1']``, then ``arr.join('')`` returns the string
``'LC101'``.

We can reproduce this action with either a ``for`` or a ``while`` loop.

Joining Array Elements With a Loop
-----------------------------------

Examine the code samples below:

.. list-table::
   :header-rows: 1

   * - Use a ``for`` loop to iterate through the array and add each entry into the ``newString`` variable.
     - Use a ``while`` loop to add the first element in the array to ``newString``, then remove that element from the array.

   * - .. sourcecode:: js

         let arr = ['L', 'C', '1', '0', '1'];
         let newString = '';

         for (i = 0; i < arr.length; i++){
            newString = newString + arr[i];
         }

         console.log(newString);
         console.log(arr);

       **Output**

       .. sourcecode:: js

         'LC101'
         ['L', 'C', '1', '0', '1']

     - .. sourcecode:: js

         let arr = ['L', 'C', '1', '0', '1'];
         let newString = '';

         while (arr.length > 0){
            newString += arr[0];
            arr.shift();
         }
         console.log(newString);
         console.log(arr);

       **Output**

       .. sourcecode:: js

         'LC101'
         [ ]

Inside each loop, the code simply adds two strings together - whatever is
stored in ``newString`` plus one element from the array. In the ``for`` loop,
the element is the next item in the sequence of entries.  In the ``while``
loop, the element is always the first entry from whatever remains in the array.

OK, the loops join the array elements together. Now let's see how to
accomplish the same task without a ``for`` or ``while`` statement.

Bring In Recursion Concepts
----------------------------

First, state the problem to solve: *Combine the elements from an array into a
string*.

Second, split the problem into small, identical steps: Looking at the loops
above, the "identical step" is just adding two strings together - ``newString``
and the next entry in the array.

Third, build a function to accomplish the small steps: Let's call the function
``combineEntries``, and we will set an array as the parameter.

.. sourcecode:: js

   function combineEntries(arrayName){
      //some code here
   }

We want ``combineEntries`` to repeat over and over again until the task is
complete.

How do we make this happen without using ``for`` or ``while``?

.. index:: ! base case

Identifying the Base Case
--------------------------

| ``for`` and ``while`` loops end when a particular condition evaluates to
   ``false``. In the examples above, these conditions are
| ``i < arr.length`` and ``arr.length > 0``, respectively.

With recursion, we do not know how many times ``combineEntries`` must be
called. To make sure the code stops at the proper time, we need to identify a
condition that ends the process. This is called the **base case**, and it
represents the simplest possible task for our function.

``if`` the base case is ``true``, the recursion ends and the task is complete.
``if`` the base case is ``false``, the function calls itself again.

We check for the base case like this:

.. sourcecode:: js

   function combineEntries(arrayName){
      if (baseCase is true){
         //solve last step
         //end recursion
      } else {
         //solve next small step
         //call combineEntries again
      }
   }

For the joining task, the *base case* occurs when we pass in a one-element
array (e.g. ``[ 'L' ]``). With no other elements to join together, the function
just needs to return ``'L'``.

Let's update ``combineEntries`` to check if the array contains only one item.

.. sourcecode:: js

   function combineEntries(arrayName){
      if (arrayName.length === 1){
         return arrayName[0];
      } else {
         //solve next small step
         //call combineEntries again
      }
   }

``arrayName.length === 1`` sets up the condition for ending the recursion
process. If it is ``true``, the single entry gets returned, and the function
stops. Otherwise, ``combineEntries`` gets called again.

Check Your Understanding
-------------------------

Identify the base case when...
