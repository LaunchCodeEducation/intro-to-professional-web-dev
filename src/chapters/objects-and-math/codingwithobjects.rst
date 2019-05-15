Coding With Objects
===================

Booleans and Objects
--------------------

Objects are not stored by their properties, but by reference. That can lead to some confusion when comparing objects.

.. admonition:: Example

   Let's see how this could effect our zoo! Surely, the zoo has more than one tortoise and the second tortoise is named Patricia!

   .. sourcecode:: js

      var tortoiseTwo = {
          species:"Galapagos Tortoise",
          name:"Patricia",
          weight: 800,
          food:"veggies",
          sign: function() {
              return this.name + " is a " + this.species;
          }
       };

   Because Pete and Patricia are members of the same species and have the same diet, you might notice that many of their points are equal and that some are not.
   Pete weighs more than Patricia and of course, they have different names!

   For this example, we will remove the ``name`` and ``weight`` properties.

   .. sourcecode:: js

      var tortoiseOne = {
          species:"Galapagos Tortoise",
          food:"veggies",
          sign: function() {
              return this.name + " is a " + this.species;
          }
       };

       var tortoiseTwo = {
          species:"Galapagos Tortoise",
          food:"veggies",
          sign: function() {
              return this.name + " is a " + this.species;
          }
       };

       console.log(tortoiseOne === tortoiseTwo);

   ::

      False

   So if the objects contain properties that have the same keys and equal values, why is the output false?

Objects are stored by reference in memory, which means that even though ``tortoiseOne`` and ``tortoiseTwo`` have the same keys and values, they are stored in separate locations in memory.
This means that though you can compare the values inside individual keys in objects for inequality, you cannot compare the objects themselves for equality.

Iterating Through Objects
-------------------------

Sometimes, you find yourself wanting to iterate through all of the values in an object, much like you would do with an array.
Like with an array, you can use a ``for`` loop to do just that! An easy way to do this is with a different ``for`` loop structure.

.. sourcecode:: js

   var b = {key1: value1, key2:value2, key3:value3};

   for (a in b) {
       console.log(b[a]);
   }

Console Output

::

   value1
   value2
   value3


.. admonition:: Try It

   Can you write a ``for..in`` loop to print to the console the values in the ``tortoiseOne`` object?



Objects and Functions
---------------------

Objects can also be the input parameter for a function or the return value of the function.
Objects will be passed by reference so any change to the object in the function will change the object itself.

