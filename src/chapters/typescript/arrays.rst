Arrays in TypeScript
--------------------

.. index:: ! tuple

Arrays in TypeScript must all be one type. 
When declaring an array, the type needs to be declared.

.. sourcecode:: js
   :linenos:

   let arrayName = number [];

   arrayName = [10,9,8];

What if the array needs to hold values of different types?

Now, we need a **tuple**. A tuple is a special structure in TypeScript that can hold as many values as needed of different types.

.. sourcecode:: js
   :linenos:

   let tupleName = [number, string, number];

   tupleName = [10, "9", 8];