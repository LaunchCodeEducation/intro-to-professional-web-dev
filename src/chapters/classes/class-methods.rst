.. _adding-class-methods:

Assigning Class Methods
========================

Just as with objects, we may want to add methods to our classes in addition to properties. 
Previously, we learned how to use constructors in class declarations to set the values of the properties.
When working with assigning methods in classes, we can either create them `outside` or `inside` in the ``constructor``.

Assigning Methods Outside ``constructor``
-----------------------------------------

When assigning methods outside of the ``constructor``, we simply declare our methods the same way that we would normally do for objects.

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

   Initially, this may seem to produce the same result as assigning ``reportStats()`` outside of the constructor.
   We will weigh the pros and cons of both methods below.

Which Way is Preferred?
------------------------

When we try to compare the outputs of our classes in code, we notice that only when we assigned the method `inside` the ``constructor``, that ``reportStats()`` method was output.
Try declaring the ``Astronaut`` class in Repl.it to see what we mean.

In the case of assigning the method `inside` the constructor, each ``Astronaut`` objects carries around the code for ``reportStats()``.
With today's computers, this is a relatively minor concern, however, each ``Astronaut`` has extra code that may not be needed in each case.
This can consume memory, which is something you should be aware of as today's businesses will want efficient code that does not tax their systems.

Because of this, if a method is the same for ALL objects of a class, define that method `outside` of the constructor.
Each object does not need a copy of identical code and declaring a method outside of the class will not consume as much memory.

Check Your Understanding
-------------------------
