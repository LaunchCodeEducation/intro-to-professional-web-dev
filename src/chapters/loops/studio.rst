.. _loop-studio:

Studio: Loops
=============

Now that we've launched our shuttle, let's use loops (iteration) to
automate some tasks.

Fork this `repl <https://replit.com/@launchcode/loopsstudio>`__ to start coding. Before you dive in, you might notice that we have several files and folders inside.
Your work will go into ``solution.js``, but please feel free to explore the program and please don't edit anything outside ``solution.js``.

Part A: Put dinner together
---------------------------
#. First, inside ``solution.js``, use the variables provided to store the following arrays.

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


2. Inside of ``mealAssembly()``, write a ``for`` loop to assemble ``numMeals`` meals.

   a. The meals must include one item from each category in the ``pantry`` array.

      .. admonition:: Hint

         The computer needs to know how many crew members to prepare food for and what ingredients. Consider creating a nested loop that will create a meal for each crew member and then add it into a larger collection of meals.

   b. Each ingredient can only be used ONCE.
   c. Add each meal to the ``meals`` array once it is assembled.
   d. To test your own solution, scroll down to another function defined in this file called ``runProgram()``. Uncomment the lines that call the ``mealAssembly`` function and print the result. Use the repl.it 'Run' button as usual to see your results printed to the console.

Part B: Collect User Input
--------------------------

Update ``askForNumber()`` to add user input and validation.

1. Using a ``while`` loop, ask the user to select the number of meals to assemble. Validate the input to make sure it is an integer from 1 - 6.
2. Save the result to the ``numMeals`` variable returned by the function.
3. Test your solution to this part by returning to the ``runProgram()`` function in the file and uncommenting the section labelled for testing Part B.


Part C: Create a Password Generator
-----------------------------------

Working and living aboard this amazing space shuttle requires you to pay the utmost attention to cybersecurity.
Once you are done working on the meal system, you are prompted to create a new password that will be used for the next 24 hours.
Having run out of strong password ideas, your shuttle captain has encouraged you to make a password generator for yourself.

Write your code inside ``generatePassword()``.

1. Construct a ``for`` loop that combines the two strings together, alternating the characters from each source, and saves the combined string to the ``code`` variable.

   .. admonition:: Examples

      #. If ``string1 = "1234"`` and ``string2 = "5678"``, then the output will be "15263748".
      #. If ``string1 = "ABCDEF"`` and ``string2 = "notyet"``, then the output will be "AnBoCtDyEeFt".
      #. If ``string1 = "LoOt"`` and ``string2 = "oku!"``, then the output will be "LookOut!".

Checking Your Work
------------------

If you want to make sure that you have checked all the boxes, run the following command in your shell on replit.

::
   
   npm test

This command runs the Jasmine tests that are checking your work for you. If you have a test that fails, check out the name of the test to get a hint as to what you are missing.
If you need a refresher on how running the tests works, check out the appendix on :ref:`Tested Code <tested-code>`.
