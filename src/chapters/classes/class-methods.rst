.. _adding-class-methods:

Assigning Class Methods
========================

Just as with objects, we may want to add methods to our classes in addition to properties. 
So far, we have learned how to set the values of the class's properties inside the ``constructor``.

When assigning methods in classes, we can either create them `outside` or `inside` the ``constructor``.

Assigning Methods Outside ``constructor``
-----------------------------------------

When assigning methods outside of the ``constructor``, we simply declare our methods the same way we would normally do for :ref:`objects <objects-intro>`.

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

.. admonition:: Example

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

      let fox = new Astronaut('Fox', 7, 12);
      console.log(fox.reportStats());

   **Console Output**

   ::

      Fox is 7 years old and has a mass of 12 kg.

   We declared our method, ``reportStats()`` outside of the constructor.
   When we declare a new instance of the ``Astronaut`` class, we can use the ``reportStats()`` method to return a concise string containing all of the info we would need about an astronaut.

Assigning Methods Inside ``constructor``
-----------------------------------------

When declaring methods inside the ``constructor``, we need to make use of the ``this`` keyword, just as we would with our properties.

.. sourcecode:: js
   :linenos:

   class ClassName {
      constructor(parameters) {
         this.methodName = function(parameters) {
            //function code
         }
      }
   }

.. admonition:: Example

   Let's consider the ``Astronaut`` class that we have been working with.
   When assigning the method, ``reportStats()``, inside the ``constructor``, we would do so like this:

   .. sourcecode:: js
      :linenos:

      class Astronaut {
         constructor(name, age, mass){
            this.name = name,
            this.age = age,
            this.mass = mass,
            this.reportStats = function() {
               let stats = `${this.name} is ${this.age} years old and has a mass of ${this.mass} kg.`;
               return stats;
            }
         }
      }

      let fox = new Astronaut('Fox', 7, 12);

      console.log(fox.reportStats());


   **Console Output**

   ::

      Fox is 7 years old and has a mass of 12 kg.

   Initially, this may seem to produce the same result as assigning ``reportStats()`` outside of the constructor.
   We will weigh the pros and cons of both methods below.

Which Way is Preferred?
------------------------

.. admonition:: Try It!

   Try comparing the outputs of ``fox`` and ``hippo`` to see the effect of assigning a method `inside` the constructor versus `outside` the constructor.

   .. replit:: js
      :slug: ClassMethodsTryIt
      :linenos:

      // Here we assign the method inside the constructor
      class AstronautI {
         constructor(name, age, mass){
            this.name = name,
            this.age = age,
            this.mass = mass,
            this.reportStats = function() {
               let stats = `${this.name} is ${this.age} years old and has a mass of ${this.mass} kg.`;
               return stats;
            }
         }
      }

      // Here we assign the method outside fo the constructor
      class AstronautO {
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

      let fox = new AstronautI('Fox', 7, 12);
      let hippo = new AstronautO('Hippo', 25, 1000);

      console.log(fox);
      console.log(hippo);


In the case of assigning the method `inside` the constructor, each ``Astronaut`` objects carries around the code for ``reportStats()``.
With today's computers, this is a relatively minor concern. However, each ``Astronaut`` has extra code that may not be needed.
This consumes memory, which you need to consider since today's businesses want efficient code that does not tax their systems.

Because of this, if a method is the same for ALL objects of a class, define that method `outside` of the constructor.
Each object does not need a copy of identical code.
Therefore, the declaration of a method outside of the constructor will not consume as much memory.

Check Your Understanding
-------------------------

.. admonition:: Question

   What is the method assignment of this class missing?

   .. sourcecode:: js
      :linenos:

      class Plant {
         constructor(type, height) {
            this.type = type,
            this.height = height
         }

         grow  {
            this.height = this.height + 1
         }
      }
