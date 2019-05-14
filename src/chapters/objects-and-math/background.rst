Objects and Why They Matter
===========================

Like arrays, **objects** are data structures that can hold many values.
Unlike arrays, the values inside of objects are stored as **key/value pairs**.

This structure allows us to create more complex programs.

Initializing Objects
--------------------

Create object literals using { }
Describe the allowed data types of keys and values 

Objects use bracket notation like arrays too. To initialize an object,

.. sourcecode:: js

   var object = {key1: value1, key2:value2, key3:value3, ....};

If the object is quite large, you can also put the key/value pairs on a separate line like so:

.. sourcecode:: js

   var object = {
       key1: value1,
       key2: value2,
       key3: value3,
       .
       .
       .
   };

.. warning::

   When initializing an object like so, it is important to pay attention to spaces and tabs!


.. admonition:: Example

   Let's say that we want to create a small program for a zoo.
   We could create an object for storing the different data points about the animals in a zoo.

   .. sourcecode:: js

      var tortoiseOne = {
          species:"Galapagos Tortoise",
          name:"Pete",
          weight: 919,
          food:"veggies"
      };


Methods and Properties
----------------------

A **property** of an object is the value stored inside the object.
A **method** performs an action on the object, because it is a property that stores a function.

.. admonition:: Example

   In the case of Pete, our zoo's friendly Galapagos Tortoise, the object ``tortoiseOne`` has several properties for his species, name, weight, and diet.
   If we wanted to add a method to our object, we might add a function that returns a helpful statement for the general public.

   .. sourcecode:: js

      var tortoiseOne = {
          species:"Galapagos Tortoise",
          name:"Pete",
          weight: 919,
          food:"veggies",
          sign: function() {
              return this.name + " is a " + this.species;
          }
       };

In the example above, we saw a new keyword that we haven't seen before.
``this`` is a keyword that programmers use when they need to call upon a property in the object to finish the method for that same object.