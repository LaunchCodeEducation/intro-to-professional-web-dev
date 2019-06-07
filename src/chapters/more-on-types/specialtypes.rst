Primitive Data Types
====================

.. index:: ! primitive

In JavaScript, data types can fall into one of two categories: primitive or object types.
A **primitive** data type is a basic building block.
Using primitive data types, we can build more complex data structures or object data types.

While object types such as objects and arrays are mutable, primitive data types are immutable.
Immutable data types are data types that cannot be changed once the value has been created.

Primitive data types include:

1. Strings
2. Numbers
3. Booleans
4. ``null``
5. ``undefined``

``undefined``
-------------

``undefined`` is a primitive data type in JavaScript which is assigned to declared variables, which have *not* been initialized.

.. sourcecode:: js

   let x;
   console.log(x)

Console Output

.. sourcecode:: bash

   undefined

``null``
--------

``null`` is similar to ``undefined`` in that it represents an unknown value, however, it is assigned to values that the programmer wishes to keep empty.

.. sourcecode:: js

   let x = null;
   console.log(x);

Console Output

.. sourcecode:: bash

   null