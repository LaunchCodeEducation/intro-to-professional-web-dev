.. _adding-class-methods:

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

Lead-in text to general syntax:

.. sourcecode:: js
   :linenos:

   class ClassName {
      constructor(parameters) {
         //assign properties with this.key = value
      }

      methodName(parameters) {
         //function code
      }
   }

Example in ``Astronaut``:

.. sourcecode:: js
   :linenos:

   class Astronaut {
      constructor(name, age, mass){
         this.name = name,
         this.age = age,
         this.mass = mass
      }

      reportStats() {
         let stats = `${this.name} is ${this.age} years old and has a mass of ${this.mass} kg.`;
         return stats;
      }
   }

More explanation text here...

Assigning Methods Inside ``constructor``
-----------------------------------------

Lead-in text to general syntax:

.. sourcecode:: js
   :linenos:

   class ClassName {
      constructor(parameters) {
         this.methodName = function(parameters) {
            //function code
         }
      }
   }

Example in ``Astronaut``:

.. sourcecode:: js
   :linenos:

   class Astronaut {
      constructor(name, age, mass){
         this.name = name,
         this.age = age,
         this.mass = mass
         this.reportStats = function() {
            let stats = `${this.name} is ${this.age} years old and has a mass of ${this.mass} kg.`;
            return stats;
         }
      }
   }

More explanation text here...

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

Check Your Understanding
-------------------------

   TODO: Add concept checks.
