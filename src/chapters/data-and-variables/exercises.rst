Exercises: Data and Variables
=============================

Exercises appear regularly in the book. Just like the concept checks, these
exercises will check your understanding of the topics in this chapter. They
also provide good practice for the new skills.

Unlike the concept checks, you will need a code editor to complete the
exercises. Fortunately, you :ref:`created a free account <hello-world>` on
Repl.it as part of the prep work.

If you are enrolled in a LaunchCode program, access these exercises by following the
repl.it classroom links posted in your class at `<https://learn.launchcode.org>`__.

If you are working through this material on your own, use this 
`repl.it link <https://repl.it/@launchcode/Exercises-Data-and-Variables>`__.

The Data
--------

Use the information given below about your space shuttle to complete the
exercises:

.. list-table::
   :widths: auto
   :header-rows: 1

   * - Data
     - Value
   * - Name of the space shuttle
     - Determination
   * - Shuttle Speed (mph)
     - 17,500
   * - Distance to Mars (km)
     - 225,000,000
   * - Distance to the Moon (km)
     - 384,400
   * - Miles per kilometer
     - 0.621

The Exercises
-------------

A. **Declare and assign variables**

   Declare and assign a variable for each item in the list above.

   *Hint*: When declaring and assigning your variables, remember that you will
   need to use that variable throughout the rest of the exercises. Make sure
   that you are using the correct data type!

#. **Print out the type of each variable**

   For each variable you declared in part A, use the ``typeof``
   operator to print its type to the console, one item per line.

   Click "Run" (in repl.it) and verify that your code works before moving to part C.

#. **Calculate a space mission!**

   We need to determine how many days it will take to reach Mars.

   #. Create and assign a miles to Mars variable. You can get the miles to Mars
      by multiplying the distance to Mars in kilometers by the miles per
      kilometer.
   #. Next, we need a variable to hold the hours it would take to get to Mars.
      To get the hours, you need to divide the miles to Mars by the
      shuttle's speed.
   #. Finally, declare a variable and assign it the value of days to Mars. In
      order to get the days it will take to reach Mars, you need to divide the
      hours it will take to reach Mars by 24.

#. **Print out the results of your calculations**

   Using variables from above, print to the screen a sentence that
   says ``"_____ will take ___ days to reach Mars."`` Fill in the blanks with 
   the shuttle name and the calculated time.

   Click "Run" (in repl.it) and verify that your code works before moving on.

#. **Now calculate a trip to the Moon**

   Repeat the calculations, but this time determine the number of days it would
   take to travel to the Moon and print to the screen a sentence that says
   ``"_____ will take ___ days to reach the Moon."``.
