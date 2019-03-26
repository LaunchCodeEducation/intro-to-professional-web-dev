Chapter 4 Exercises
===================

These exercises will check your understanding of the topics in this chapter. Practice 

For the following exercises, you will use the information given below about your space shuttle.

.. list-table:: Space Shuttle Information
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

#. | Declare and assign a variable for each item in the table above. 
   | Example: ``spaceShuttleName = "Determination";``
#. | Print out the type of each variable you declared using the ``typeof`` operator.
   | Example: ``console.log(typeof spaceShuttleName);``
#. Now let's calculate a space mission! We need to determine how many days it will take to reach Mars.

   a. | First, convert the distance to Mars from kilometers into miles. Use your declared variables to calculate the result.
      | *Hint*: ``milesToMars = 0.621 * kilometersToMars``
   b. | Next, we need a variable to hold the hours it would take to get to Mars.
      | *Hint*: ``hoursToMars = milesToMars / shuttleSpeed``
   c. | Finally, declare a variable and assign it the value of days to Mars.
      | *Hint*: ``daysToMars = hoursToMars / 24``
#. | Using your result from 3c above, print to the screen a sentence that says, 
   | **"Determination will take ___ days to reach Mars."**
#. Repeat questions 3 and 4 for a space mission to the Moon.
