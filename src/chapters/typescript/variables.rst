Declaring and Using Variables
=============================

Since TypeScript is statically typed, the type of value is added to the variable declaration. However, we will still use our ``let`` and ``const`` keywords where appropriate.

The general format of a variable declaration is:

.. sourcecode:: js

   let variableName: type = value;

``number``
----------

When declaring a variable and using the ``number`` type, we add ``number`` to the variable declaration, like so:

.. sourcecode:: js

   let variableName: number = 10;

``string``
----------

When declaring a ``string``, we want to use the ``string`` keyword.

.. sourcecode:: js

    let variableName: string = "10";

``boolean``
-----------

The ``boolean`` keyword should be used when declaring a variable of the ``boolean`` type.

.. sourcecode:: js

    let variableName: boolean = true;

Examples
--------

Let's use some familiar variable declarations to compare between what we know how to do in JavaScript and what we are now learning about TypeScript.

.. sourcecode:: js
   :linenos:

   // In JavaScript, we have:

   let spaceShuttleName = "Determination";
   let shuttleSpeed = 17500;
   let distancetoMars = 225000000;
   let distancetoMoon =	384400;
   let milesperKilometer = 0.621;

   // The same declarations in TypeScript would be:

   let spaceShuttleName: string = "Determination";
   let shuttleSpeed: number = 17500;
   let distancetoMars: number = 225000000;
   let distancetoMoon: number =	384400;
   let milesperKilometer: number = 0.621;

Check Your Understanding
------------------------

.. admonition:: Question

   The correct declaration of the variable, ``astronautName``, that holds the value, ``"Sally Ride"``, is:

   a. ``let astronautName = "Sally Ride";``
   b. ``let astronautName = string: "Sally Ride";``
   c. ``let astronautName: string = "Sally Ride";``
   d. ``string astronautName = "Sally Ride";``
