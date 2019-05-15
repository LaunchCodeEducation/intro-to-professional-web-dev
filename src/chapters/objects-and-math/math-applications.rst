Combining ``Math`` Methods
===========================

Let's revisit the :ref:`loop studio <loop-studio>`, where we assembled meals
for the shuttle astronauts. In part A, you constructed a ``for`` loop to
iterate through the arrays in order. Astronaut 0 got all of the items at index
0, while astronaut 2 got all the kale, since that was stored at index 2.

It would be better if we could construct meals by selecting a *random* item
from each of the supply arrays. Let's see how we can use the ``Math`` object to
accomplish this.

.. _random-integer:

Generate a Random Integer
--------------------------

To select an item from an array, we must use an integer in the bracket
notation. Unfortunately, ``Math.random()`` returns a decimal value between 0
and 1, which will not work for index values.

The trick to creating a random integer is to multiply ``Math.random()`` by a
whole number and then round the result to remove the decimal portion. The
choice of using the ``ceil``, ``floor`` or ``round`` method affects the numbers
generated.

Explore the example below:

.. admonition:: Example

   .. sourcecode:: js

      for (i=0; i < 5; i++){
         let num = Math.random()*10;
         console.log(`floor = ${Math.floor(num)}, ceil = ${Math.ceil(num)}, round = ${Math.round(num)}`);
      }

   **Output**
   ::

      floor = 0, ceil = 1, round = 0
      floor = 6, ceil = 7, round = 7
      floor = 2, ceil = 3, round = 3
      floor = 8, ceil = 9, round = 8
      floor = 9, ceil = 10, round = 10

After multiplying ``Math.random()`` by 10, applying the ``floor`` method gives
numbers between 0 and 9. Using the ``ceil`` method shifts the range up one
digit, generating values between 1 and 10. Using the ``round`` method gives the
widest range, generating numbers between 0 and 10.

Rather than trying to remember which method to use, one choice is to ALWAYS
use ``floor`` to round to an integer:

#. ``Math.floor(Math.random()*10)`` generates a number from 0 - 9.
#. ``Math.floor(Math.random()*120)`` generates a number from 0 - 119.

To start our range at 1, just add 1 to the rounded value:

#. ``Math.floor(Math.random()*10) + 1``  generates a number from 1 - 10.
#. ``Math.floor(Math.random()*120) + 1``  generates a number from 1 - 120.

By changing the value that multiplies ``Math.round()`` we specify the range for
the numbers we want to generate.

#. ``Math.floor(Math.random()*maxValue)``  generates a number from
   0 to (``maxValue``-1).
#. ``Math.floor(Math.random()*maxValue) + 1``  generates a number from
   1 to ``maxValue``.

.. admonition:: Try It

   Explore generating random numbers at this `repl.it <https://repl.it/@launchcode/RandomNumberPractice>`__.

   #. Generate random integers from 1 - 100.
   #. Generate random integers from -5 - 0, but NOT including 0.
   #. *Challenge*: Generate random integers from 20 - 30.

Random Selection From an Array
-------------------------------

To select a random item from the array ``happiness = ['Hope', 'Joy', 'Peace',
'Love', 'Kindness', 'Puppies', 'Kittens', 'Tortoise']``, we need to make
JavaScript randomly generate an index value from 0 to 7.

Let's define a function that takes an array as a parameter. Since we might not
know how many items are in the array, we cannot multiply ``Math.round()`` by a
specific value.  Fortunately, we have the ``length`` property…

.. admonition:: Example

   .. sourcecode:: js
      :linenos:

      function randomSelection(arr){
         let index = Math.floor(Math.random()*arr.length);
         return arr[index];
      }

      let happiness = ['Hope', 'Joy', 'Peace', 'Love', 'Kindness', 'Puppies', 'Kittens', 'Tortoise'];

      for (i=0; i < 8; i++){
         console.log(randomSelection(happiness));
      }

   **Output**
   ::

      Tortoise
      Love
      Kindness
      Hope
      Kittens
      Kindness
      Love
      Hope

   Explore the code with this `repl.it <https://repl.it/@launchcode/KindnessSelection>`__.

The ``happiness`` array has a length of 8, so in line 2
``Math.floor(Math.random()*arr.length)`` evaluates as
``Math.floor(Math.random()*8)``, which generates an integer from 0 to 7.
Line 3 then returns a random selection from the array.

Random Meal Assembly
---------------------

Now that we have a function to randomly select an item from an array, let's add
it to our astronaut meal program.

.. sourcecode:: js
   :linenos:

      function randomSelection(arr){
         let index = Math.floor(Math.random()*arr.length);
         return arr[index];
      }

      let protein = ['chicken', 'pork', 'tofu', 'beef', 'fish', 'beans'];
      let grain = ['rice', 'pasta', 'corn', 'potato', 'quinoa', 'crackers'];
      let veggies = ['peas', 'green beans', 'kale', 'edamame', 'broccoli', 'asparagus'];
      let drinks = ['juice', 'milk', 'water', 'soy milk', 'soda', 'tea'];
      let dessert = ['apple', 'banana', 'more kale', 'ice cream', 'chocolate', 'kiwi'];

      let pantry = [protein, grain, veggies, drinks, dessert]; //LOOK! A 2-dimensional array.
      let numCrew = 6;

      for (i=0; i < numCrew; i++){ //create 1 meal for each crew member
         let meal = [];
         for (j = 0; j < pantry.length; j++){ //make 1 selection from each food array
            meal.push(randomSelection(pantry[j]));
         }
      }

**Output**
::

   [ 'tofu', 'pasta', 'peas', 'juice', 'kiwi' ]
   [ 'tofu', 'potato', 'green beans', 'soda', 'apple' ]
   [ 'pork', 'pasta', 'kale', 'soda', 'ice cream' ]
   [ 'beef', 'crackers', 'peas', 'water', 'kiwi' ]
   [ 'fish', 'corn', 'broccoli', 'soda', 'apple' ]
   [ 'chicken', 'quinoa', 'asparagus', 'tea', 'chocolate' ]

Is a walkthrough of the code necessary?

Check Your Understanding
-------------------------

   Suggestions?
