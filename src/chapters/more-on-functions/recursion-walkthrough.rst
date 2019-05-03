Recursion Walkthrough
======================

The best way to ease into the concept of recursion is to start by taking baby
steps through a loop task.

Let's revisit the array method ``join``, which combines the elements of an
array into a single string. If we have ``arr = ['L', 'C', '1', '0', '1']``,
then arr.join('') returns the string ``'LC101'``.

We could reproduce this action with either a ``for`` or a ``while`` loop.

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

Inside the each loop, the code simply adds two strings together - whatever is
stored in ``newString`` plus one element from the array. In the ``for`` loop,
the element is the next item in the sequence of entries.  In the ``while``
loop, the element is always the first entry from whatever remains in the array.

OK, so the loops join the array elements together. Now let's see how to
accomplish the same task without a ``for`` or ``while`` statement.

Bring In Recursion Concepts
----------------------------

First, state the problem to solve: *Combine the elements from an array into a
string*.

Next, split the problem into small, identical steps. Looking at the loops
above, the "identical step" is just adding two strings together - ``newString``
and the next entry in the array.

Next, build a function to accomplish the small steps.  Let's call the function
``addEntry``, and we will set an array as the parameter.

.. sourcecode:: js

   function addEntry(arrayName){
      //some code here
   }

We want this function to repeat over and over again until the task is complete.

We will add code to the function soon, but we need to take a moment to consider
how to repeatedly call the function without using ``for`` or ``while``.

Identifying the Base Case
^^^^^^^^^^^^^^^^^^^^^^^^^^

``for`` and ``while`` loops end when a particular condition evaluates to
``false``. In the examples above, these conditions are ``i < arr.length`` and
``arr.length > 0``, respectively.

With recursion, we will not know how many times ``addEntry`` must be called. To
make sure the code stops at the proper time, we need to identify a condtion
that ends the process. This is called the **base case**.

Inside ``addEntry``, we use a simple ``if`` statement to check of the base case
is ``true``.  If so, the recursion ends and the task is complete. If not, the
function calls itself again.

.. sourcecode:: js

   function addEntry(arrayName){
      if (baseCase is true){
         //solve last step
         //end recursion
      } else {
         //solve small step
         //call addEntry again
      }
   }

Setting Up A Function To Call Itself
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
