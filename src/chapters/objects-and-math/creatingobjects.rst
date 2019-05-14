Modifying Objects
=================

Accessing Properties
--------------------

When using objects, programmers oftentimes want to get the value of one of the properties or change that value.
To access the value of a property, you need to use the key of that property. 

You can do so two ways: with bracket syntax or dot-notation.

Using brackets, the code would be something like: ``object["key"]``.
With dot notation, the code would be something like: ``object.key``.

Either way will return the same value, so the difference between the two is about readability and accessing the property.

Modifying Properties
--------------------

A programmer can modify the value that a property holds by using the notation above.

.. sourcecode:: js

   var object = {
       key1: value1,
       key2: value2
   };
   
   console.log(object.key1);

   object.key1 = value3;

   console.log(object.key1);

Console Output

::

  value1
  value3


.. warning::
 
   Objects are mutable.
   You may remember from our discussion about strings and arrays, that mutability means that a data structure can be modified without making a copy.
   This is important to remember for objects, because when you change the value of a property, a copy of the object is not made, so proceed with caution!
