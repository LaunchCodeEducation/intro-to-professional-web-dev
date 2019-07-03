Arrays in TypeScript
====================

.. index:: ! tuple

Arrays in TypeScript must contain values of the same type. 
When declaring an array, the type needs to be declared.

.. sourcecode:: js
   :linenos:

   let arrayName: number[] = [10,9,8];

What if the array needs to hold values of different types?

Now, we need a **tuple**. A tuple is a special structure in TypeScript that can hold as many values as needed of different types.

.. sourcecode:: js
   :linenos:

   let tupleName: [number, string, number];

   tupleName = [10, "9", 8];

Examples
--------

In JavaScript, we would declare an array holding items in our cargo hold like so:

.. sourcecode:: js

   let cargoHold = ['oxygen tanks', 'space suits', 'parrot', 'instruction manual', 'meal packs', 'slinky', 'security blanket'];

In TypeScript, we would declare the same ``cargoHold`` array a little differently:

.. sourcecode:: js

   let cargoHold: string[] = ['oxygen tanks', 'space suits', 'parrot', 'instruction manual', 'meal packs', 'slinky', 'security blanket'];

What about declaring arrays for elements on the Periodic Table? In JavaScript, that is a relatively simple task:

.. sourcecode:: js
   :linenos:

   let element1 = ['hydrogen', 'H', 1.008];
   let element2 = ['helium', 'He', 4.003];
   let element26 = ['iron', 'Fe', 55.85];

In TypeScript, however, an array can only hold values of one type, so we need to use a tuple.

.. sourcecode:: js
   :linenos:

   let element1: [string, string, number];
   element1 = ['hydrogen', 'H', 1.008];

   let element2: [string, string, number];
   element2 = ['helium', 'He', 4.003];

   let element26: [string, string, number];
   element26 = ['iron', 'Fe', 55.85];

Check Your Understanding
------------------------

.. admonition:: Question

   Which of the following statements is FALSE about a tuple in TypeScript?

   a. Tuples can hold as many elements as needed.
   b. Tuples hold values of one type.
   c. When declaring a tuple, programmers include the types of the values in a tuple.