.. _loop-studio:

Studio: Loops
=============

Now that we've launched our shuttle, let's use loops (iteration) to
automate some tasks.

Fork this repl to start coding. Before you dive in, you might notice that we have several files and folders inside.
Your work will go into ``solution.js``, but please feel free to explore the program and please don't edit anything outside ``solution.js``.

Part A: Put dinner together
---------------------------
#. First, initialize ``numMeals`` to -1 and use the other variables to store the following arrays.

   - Protein options:

     ::

        ['chicken', 'pork', 'tofu', 'beef', 'fish', 'beans']

   - Grain options:

     ::

        ['rice', 'pasta', 'corn', 'potato', 'quinoa', 'crackers']

   - Vegetable options:

     ::

        ['peas', 'green beans', 'kale', 'edamame', 'broccoli', 'asparagus']

   - Beverage options:

     ::

        ['juice', 'milk', 'water', 'soy milk', 'soda', 'tea']

   - Dessert options

     ::

        ['apple', 'banana', 'more kale', 'ice cream', 'chocolate', 'kiwi']


2. Inside of ``mealAssembly``, write a ``for`` loop to assemble ``numMeals`` meals.

   a. The meals must include one item from each of the source arrays.
   b. Each ingredient can only be used ONCE.
   c. Add each meal to ``meals`` once it is assembled.
   d. At the end, return ``meals``.

Part B: Collect User Input
--------------------------

Update ``askForNumber()`` to add user input and validation.

3. Using a ``while`` loop, ask the user to select the number of meals to assemble. Validate the input to make sure it is an integer from 1 - 6.
4. Return ``numMeals``.


Part C: Create a Password Generator
-----------------------------------

Working and living aboard this amazing space shuttle requires you to pay the utmost attention to cybersecurity.
Once you are done working on the meal system, you are prompted to create a new password that will be used for the next 24 hours.
Having run out of strong password ideas, your shuttle captain has encouraged you to make a password generator for yourself.

Write your code inside ``generatePassword()``.

1. Construct a ``for`` loop that combines the two strings together, alternating the characters from each source.

   .. admonition:: Examples

      #. If ``string1 = "1234"`` and ``string2 = "5678"``, then the output will be "15263748".
      #. If ``string1 = "ABCDEF"`` and ``string2 = "notyet"``, then the output will be "AnBoCtDyEeFt".
      #. If ``string1 = "LoOt"`` and ``string2 = "oku!"``, then the output will be "LookOut!".

2. Return the resulting combined string.

Part D: Put it all together!
----------------------------

Finally, turn your attention to ``runProgram()``.

1. Write a ``for`` loop that uses ``mealPrintout()`` to format the printing of each meal in ``mealsFor6``.
2. Write another ``for`` loop that uses ``mealPrintout()`` to format the printing of each meal in ``mealsForX``.
3. Initialize the two strings, ``password1`` and ``password2``.
4. Run your program to see how it works!

If you want to make sure that you have checked all the boxes, run the following command in your terminal on replit.

::
   npm test

This command runs the Jasmine tests that are checking your work for you. If you have a test that fails, check out the name of the test to get a hint as to waht you are missing.

