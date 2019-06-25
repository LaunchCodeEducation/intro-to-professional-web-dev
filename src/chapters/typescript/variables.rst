Declaring and Using Variables
=============================

TypeScript is strongly typed so you have to specify the type of variable when you declare it.

``number``
----------

The ``number`` type is the same as it is in JavaScript, however, when declaring a variable of number type, you must specify that the type is the number type.

.. sourcecode:: js

   let variableName: number = 10;

``string``
----------

The ``string`` type must also be specified.

.. sourcecode:: js

    let variableName: string = "10":

``boolean``
-----------

The ``boolean`` type should be specified.

.. sourcecode:: js

    let variableName: boolean = True;

``null`` and ``undefined``
--------------------------

``null`` and ``undefined`` are primitive data types in TypeScript, however, they are treated differently by TypeScript.
If you are planning on using ``null`` to define a property of an object that is not known yet, use the TypeScript optional parameter, ``?``.