.. _debugging-logic-errors:

Debugging Logic Errors
======================

We can debug runtime and syntax errors using the error messages produced. Logic errors, however, do not generally produce error messages. This sometimes makes them tougher to debug.

While we can't provide a step-by-step approach that applies to every possible logic error, we *can* give you some solid strategies. Two such strategies---using debugger tools and writing tests---will be covered in future lessons. In this section, we start with a basic and effective way to debug logic errors.

Printing Values
---------------

When your code runs but doesn't produce the expected results, it is important to check the values of the variables being used.

Let's look at a program that has a logical bug.

.. replit:: js
   :linenos:
   :slug: Degrees-C-to-K-Logic-Error

   const input = require('readline-sync');

   let degreesC = input.question('Temp in degrees C:');
   let degreesK = degreesC + 273.15;

   console.log('Degrees K:', degreesK);

This program asks the user for a temperature in degrees celsius and attempts to convert it to degrees Kelvin. Degrees Kelvin differs from degrees celsius by 273.15. So if we enter 100 (in celsius) we should see a converted value of 373.15 (in Kelvin). However, running the program as-is and entering 100 gives the message:

::

   Temp in degrees C:  100
   Degrees K: 100273.15

This is clearly incorrect. But the program does not generate an error, so it is not immediately clear what the issue is. To figure it out, we'll use ``console.log`` to see what the values of key variables are when the program runs. 

Let's first make sure that the ``degreesC`` variable looks like it should by adding a ``console.log`` statement just after we create this variable.

.. sourcecode:: js
   :linenos:

   const input = require('readline-sync');

   let degreesC = input.question('Temp in degrees C: ');
   console.log(degreesC);
   let degreesK = degreesC + 273.15;

   console.log('Degrees K:', degreesK);

Running this with an input of 100 gives the output:

::

   Temp in degrees C:  100
   100
   Degrees K: 100273.15

The second line is the value of ``degreesC``, which appears to be correct. But the final answer is still incorrect, so we need to keep digging for more information.

Looking at the line in which we set ``degreesK``, we see that we use ``degreesC`` as a numeric value in our calculation. Let's see what the data type of ``degreesC`` is. In the end, we want it to be a number.

.. sourcecode:: js
   :linenos:

   const input = require('readline-sync');

   let degreesC = input.question('Temp in degrees C: ');
   console.log(typeof degreesC);
   let degreesK = degreesC + 273.15;

   console.log('Degrees K:', degreesK);

Running this with an input of 100 gives the output:

::

   Temp in degrees C:  100
   string
   Degrees K: 100273.15

That's it! The variable ``degreesC`` has the value ``100``, but it is a string rather than a number. So when we set ``degreesK`` with the formula ``degreesC + 273.15``, we are actually performing string concatenation instead of addition: ``"100" + 273.15`` is ``"100273.15"``.

We can fix our program by converting the user's input to the number data type.

.. sourcecode:: js
   :linenos:

   const input = require('readline-sync');

   let degreesC = input.question('Temp in degrees C: ');
   degreesC = Number(degreesC);
   let degreesK = degreesC + 273.15;

   console.log('Degrees K:', degreesK);

Running this with an input of 100 gives the output:

::

   Temp in degrees C:  100
   Degrees K: 373.15

Note that after debugging we removed all of our ``console.log`` statements. Be sure to do the same when using this debugging technique.

