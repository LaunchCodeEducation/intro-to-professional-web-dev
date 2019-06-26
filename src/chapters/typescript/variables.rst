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

    let variableName: string = "10":

``boolean``
-----------

The ``boolean`` keyword should be used when declaring a variable of the ``boolean`` type.

.. sourcecode:: js

    let variableName: boolean = true;

``null`` and ``undefined``
--------------------------

``null`` and ``undefined`` are primitive data types in TypeScript, however, they are treated differently by TypeScript.
If you are planning on using ``null`` to define a property of an object that is not known yet, use the TypeScript optional parameter, ``?``.

Let's take a look at how that would look in TypeScript.

In JavaScript, we might have an object that looks like so:

.. sourcecode:: js
   :linenos:

   let giraffeTwo = {
        species: "Reticulated Giraffe",
        name: "Alicia",
        weight: null,
        age: 10,
        diet: "leaves"
   };

This code may look familiar from the chapter on primitive data types.

If we wanted to declare the same object in TypeScript, we would have to use the optional parameter for the ``weight`` property.

.. sourcecode:: js
   :linenos:

   interface giraffeTwo = {
        species: string;
        name: string;
        weight?: number;
        age: number;
        diet: string;
   };