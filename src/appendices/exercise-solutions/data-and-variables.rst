.. _data-and-variables-exercise-solutions:

Exercise Solutions: Data and Variables
======================================

.. _data-and-variables-exercise-solutionsA:

A. **Declare and assign variables**

   Declare and assign a variable for each item in the list.

   .. sourcecode:: js
      :linenos:

      let shuttleName = 'Determination';
      let shuttleSpeedMph = 17500;
      let distanceToMarsKm = 225000000;
      let distanceToMoonKm = 38400;
      const milesPerKm = 0.621;

   :ref:`Back to the exercises <exercises-data-and-variables>`


C. **Calculate a space mission!**

   We need to determine how many days it will take to reach Mars.

   #. Create and assign a miles to Mars variable. You can get the miles to Mars
      by multiplying the distance to Mars in kilometers by the miles per
      kilometer.

      .. _data-and-variables-exercise-solutionsC1:

      .. sourcecode:: js

         let milesToMars = kilometersToMars * milesPerKilometer;

   #. Next, we need a variable to hold the hours it would take to get to Mars.
      To get the hours, you need to divide the miles to Mars by the
      shuttle's speed.

      .. _data-and-variables-exercise-solutionsC2:

      .. sourcecode:: js

         let hoursToMars = milesToMars / shuttleSpeedMph;

   #. Finally, declare a variable and assign it the value of days to Mars. In
      order to get the days it will take to reach Mars, you need to divide the
      hours it will take to reach Mars by 24.

      .. _data-and-variables-exercise-solutionsC3:
      
      .. sourcecode:: js

         let daysToMars = hoursToMars / 24;

   :ref:`Back to the exercises <exercises-data-and-variables>`

.. _data-and-variables-exercise-solutionsE:

E. **Now calculate a trip to the Moon**

   Repeat the calculations, but this time determine the number of days it would
   take to travel to the Moon and print to the screen a sentence that says
   ``"_____ will take ___ days to reach the Moon."``.

   .. sourcecode:: js
      :linenos:

      let milesToMoon = kilometersToMoon * milesPerKilometer;
      let hoursToMoon = milesToMoon / shuttleSpeedMph;
      let daysToMoon = hoursToMoon / 24;
      console.log(shuttleName + " will take " + daysToMoon + " days to reach the Moon.");

   :ref:`Back to the exercises <exercises-data-and-variables>`
