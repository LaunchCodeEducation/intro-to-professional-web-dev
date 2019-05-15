Modifying Objects
=================

Accessing Properties
--------------------

When using objects, programmers oftentimes want to get the value of one of the properties or change that value.
To access the value of a property, you need to use the key of that property. 

You can do so two ways: with bracket syntax or dot-notation.

Using brackets, the code would be something like: ``object["key"]``. The only restraint on naming a key was that it had to be a valid JavaScript string.
Since a key could potentially have a space in it, bracket syntax would be the only way to access the value in that property because of the quotes.
With dot notation, the code would be something like: ``object.key``. Notice that the key is no longer surrounded by quotes. However, keys are still strings.

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
   This is important to remember for objects, because when you change the value of a property, a copy of the object is not made and the original is modified.
   So proceed with caution!

Check Your Understanding
------------------------

All of the questions below refer to an object called ``giraffe``. Here is the object literal for ``giraffe``.

.. sourcecode:: js

   var giraffe = {
     species: "Reticulated Giraffe",
     name: "Cynthia",
     weight: 15,
     age: 1500,
     diet: "leaves"
   }

.. admonition:: Question

   We want to add a method for easily increasing Cynthia's age on her birthday. What is missing from our method?

   ``birthday: function () {age = age + 1;}``

.. admonition:: Question

   Could we use bracket notation, dot notation or both to access the properties of ``giraffe``?
   