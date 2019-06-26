Classes in TypeScript
---------------------

Classes in TypeScript look some like this:

.. sourcecode:: js
   :linenos:

   class Astronaut {
      name: string;
      constructor(firstName: string, lastName: string) {
         this.name = firstName + " " + lastName;
      }
      greet() {
         return "Hello, " + this.name;
      }
   }

   let Bob = Astronaut("Bob","Smith");

You may remember the ``this`` and ``new`` keywords from working with classes in JavaScript.
Earlier in the chapter, we also noted that when declaring variables in TypeScript, we have to specify the type of value.
The same applies to function parameters, as you can see in the constructor.

Classes in TypeScript can also use the ``extends`` keyword to denote child and parent classes, as shown here:

.. sourcecode:: js
   :linenos:

   class Panthera {
      roar: string;
      constructor(currentRoar: string) {
         this.roar = currentRoar;
      }
   }

   class Tiger extends Panthera {
      stripes: boolean = true;

   }

   let tigger = new Tiger("loud");
   console.log(tigger.roar);
   console.log(tigger.stripes);


``export`` is used to make the class available in the global scope.