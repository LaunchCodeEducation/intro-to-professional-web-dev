Loop Studio
============

Now that we’ve launched our shuttle, let’s use loops (iteration) to
automate some tasks.

Part A (Put dinner together)
----------------------------
#. First, initialize variables to store the following arrays.  Remember to use descriptive names.
    | Protein options: [‘chicken’, ‘pork’, ‘beef’, ‘fish’, ‘beans’, ‘tofu’]
    | Grain options: [‘rice’, ‘pasta’, ‘potato’, ‘quinoa’, ‘crackers’, ‘corn’]
    | Vegetable options: [‘peas’, ‘green beans’, ‘edamame’, ‘broccoli’,
        ‘asparagus’, ‘kale’]
    | Beverage options: [‘juice’, ‘milk’, ‘soy milk’, ‘soda’, ‘tea’, ‘water’]
    | Dessert options: [‘apple’, ‘banana’, ‘ice cream’, ‘chocolate’, ‘kiwi’,
        ‘more kale’]

    Control+click (or right-click) to: `Code here <https://repl.it/@launchcode/LoopstudiopartsAandC>`__

#. Construct a ``for`` loop that assembles a meal for each of 6 astronauts.
    a. The meals must include one item from each of the source arrays.
    b. Print the meal information for each astronaut.

#. Optional: *Skill boost!* To enhance your learning, modify your code to:
    a. Use string formatting to print something more interesting than “[‘chicken’, ‘rice’, ‘peas’, ‘juice’, ‘apple’]” for the meal outputs.
    b. Use an “array of arrays” to store the food options in a ‘pantry’.

.. image:: figures/array-of-arrays.png
    :height: 300px

Part B (Self-destruct system)
-----------------------------

If the shuttle gets hijacked by space pirates, the astronauts can activate
a self-destruct sequence to provide some drama for the viewers at home.

In order to prevent a rogue ‘naut from activating the code, it takes **two**
crew members to begin the countdown.  Each person must enter a different
code, after which the computer will ‘zip’ them together before overloading
the engines.

4. Construct a ``for`` loop that combines two strings together, alternating the characters from each source.
    | *Examples:*
    | a) If ``string`` = “1234” and ``otherString`` = “5678”, then the
        output will be “15263748”.
    | b) If ``code1`` = "ABCDEF" and ``code2`` = “notyet”, then the output
        will be “AnBoCtDyEeFt”.
    | c) If ``ka`` = “LoOt” and ``blam`` = “oku!”, then the output will be
        “LookOut!”.

    Control+click (or right-click) to: `Code here <https://repl.it/@launchcode/LoopstudiopartB>`__

Part C (Refinements)
--------------------

Update your code from part A to add user input and validation.

5. Using a ``while`` loop, ask the user to select the number of meals to assemble.
    Validate the input to make sure it is an integer from 1 - 6.

#. Optional: *Skill boost!* Modify your code to check each meal for kale.
    a. If present, after the meal output add, “Don’t worry, you can have
    double chocolate tomorrow.”
