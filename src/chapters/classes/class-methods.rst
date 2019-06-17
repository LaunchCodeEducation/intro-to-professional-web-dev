Assigning Class Methods
========================

Some intro stuff here with the example:

.. sourcecode:: js
   :linenos:

   class Astronaut {
      constructor(name, age, mass){
         this.name = name,
         this.age = age,
         this.mass = mass
      }
   }

   let fox = new Astronaut('Fox', 7, 12);

   console.log(`${fox.name} is ${fox.age} years old and has a mass of ${fox.mass} kg.`);

**Console Output**

::

   Fox is 7 years old and has a mass of 12 kg.

We could replace the template literal in line 11 with a function that returns
the same phrase...

Assigning Methods Outside ``constructor``
-----------------------------------------

Assigning Methods Inside ``constructor``
-----------------------------------------

Which Way is Preferred?
------------------------

Compare outputs from placing ``reportStats()`` outside vs. inside
``constructor``:

Outside: Astronaut { name: 'Fox', age: 7, mass: 12 }

Inside: Astronaut { name: 'Fox', age: 7, mass: 12, reportStats: [Function] }

In the latter case, each ``Astronaut`` objects carries around the code for
``reportStats()``. Repetitive and memory consuming (though this is a minor
concern with today's systems). Remember the DRY idea.

If a method is the same for ALL objects of a class, then define that method
OUTSIDE of the constructor. That way, each object need not carry a copy of
identical code.
