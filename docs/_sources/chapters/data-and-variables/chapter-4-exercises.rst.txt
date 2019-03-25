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
   * - Orbit Speed (mph)
     - 17,500
   * - Distance to Mars (km)
     - 225,000,000
   * - Distance to the Moon (km)
     - 384,400

#. Declare and assign a variable for each item in the table above. 
   Example: ``spaceShuttleName = "Determination";``
#. Print out the type of each variable you declared using the ``typeof`` operator.
   Example: ``console.log(typeof spaceShuttleName)``
#. Now let's calculate a space mission. How many days will it take to travel to Mars?

   a. First, we need to convert the distance to Mars from kilometers into miles. Use your declared variables to hold this result (hint: ``milesToMars = 0.621 * kilometers``) 
   b. Next we need a variable to hold the hours it would take to get to Mars (hint: ``hoursToMars = milesToMars / orbitSpeed``)
   c. Finally declare a variable to assign the value of days to Mars (hint: ``daysToMars = hoursToMars / 24``)
   
#. Using the variables declared above, print to the screen a sentence that says "It will take the shuttle Determination ___ days to reach Mars" 
#. Repeat parts 3 and 4 for a space mission to the Moon
