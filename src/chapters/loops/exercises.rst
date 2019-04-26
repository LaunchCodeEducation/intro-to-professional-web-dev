Exercises: Loops
================

| Practice makes better.  Repetition is a good thing.
| Repetition is a good thing.
| Repetition is a good thing.
| Repetition is a good thing.

WAIT!!!  Why type "Repetition is a good thing," four times when we can code
a better result?  How about printing the phrase 100 times instead?

.. sourcecode:: javascript

    for (i=0; i < 100; i++){
        console.log("Repetition is a good thing.")
    }

Loops simplify repetitive tasks!

``for`` Practice
-----------------

Control+click (or right-click) to: `Repl.it here <https://repl.it/@launchcode/ForLoopExercises>`__

#. Construct ``for`` loops that accomplish the following tasks:
    | a. Print the numbers 0 - 20, one number per line.
    | b. Print only the ODD values from 3 - 29, one number per line.
    | c. Print the EVEN numbers 12 to -14 in descending order, one number
        per line.
    | d. ``for`` **,** ``if`` **and** ``%`` - Print the numbers 50 - 20 in descending order, but only
        if the numbers are multiples of 3.  (Your code should work even if
        you replace 50 or 20 with other numbers).

#. Initialize two variables to hold the string ``'LaunchCode'`` and the array ``[1, 5, ‘LC101’, ‘blue’, 42]``, then construct ``for`` loops to accomplish the following tasks:
    | a. Print each element of the array to a new line.
    | b. Print each character of the string - in reverse order - to a new line.

#. Construct a ``for`` loop that sorts the array ``[2, 3, 13, 18, -5, 38, -10, 11, 0, 104]`` into two new arrays:
    | a. One array contains the even numbers, and the other holds the odds.
    | b. Print the arrays to confirm the results.

``while`` Practice
-------------------

Control+click (or right-click) to: `Repl.it here <https://repl.it/@launchcode/WhileLoopExercises>`__

Define three variables for the LaunchCode shuttle - one for the starting
fuel level, another for the number of astronauts aboard, and the third for
the altitude the shuttle reaches.

4. Construct ``while`` loops to do the following:
    | a. Prompt the user to enter the starting fuel level.  The loop should continue until
        the user enters a positive value greater than 5000 but less than 30000.
    | b. Use a second loop to query the user for the number of astronauts
        (up to a maximum of 7). Validate the entry by having the loop continue until
        the user enters an integer from 1 - 7.
    | c. Use a final loop to monitor the fuel status and the altitude of the
        shuttle.  Each iteration, decrease the fuel level by 100 units for each
        astronaut aboard.  Also, increase the altitude by 50 kilometers.

#. After the loops complete, output the result with the phrase, “The shuttle gained an altitude of ___ km.”
    | If the altitude is 2000 km or higher, add “Orbit achieved!”
    | Otherwise add, “Failed to reach orbit.”
