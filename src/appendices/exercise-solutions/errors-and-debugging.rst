.. _errors-and-debugging-exercise-solutions:

Exercise Solutions: Errors and Debugging
========================================

.. _errors-and-debugging-exercise-solutionsA:

A. **Line 4 needs a closing parenthesis:**

   .. sourcecode:: js
      :lineno-start: 4

      if (fuelLevel >= 20000) {
     

   :ref:`Back to the exercises <exercises-errors-and-debugging>`

.. _errors-and-debugging-exercise-solutionsC:

C. ``fuellevel`` **should be** ``fuelLevel`` **on Line 7:**

   .. sourcecode:: js
      :lineno-start: 7

      if (fuelLevel >= 20000) {
     

   :ref:`Back to the exercises <exercises-errors-and-debugging>`

E. **Check your logic**

   .. _errors-and-debugging-exercise-solutionsEa:

   a. **Should the shuttle have launched? Did it?**
      
      The shuttle should not have launched. However, the messages to the console tell a different story.
      Without any changes, the original code outputs:

      .. sourcecode:: bash

         WARNING: Insufficient fuel!
         Crew & computer cleared.
         10, 9, 8, 7, 6, 5, 4, 3, 2, 1...
         Liftoff!

   .. _errors-and-debugging-exercise-solutionsEc:

   c. **Given** ``crewStatus`` **and** ``computerStatus``, **should** ``launchReady`` **be true or false after this check?**

      With their initial values set to ``true`` and ``'green'``, line 14 evaluates to ``true`` and ``launchReady`` is 
      set to ``true``.
      If it's value on dependent on the value of these variables only (``crewStatus`` and ``computerStatus``),
      then ``launchReady`` should be ``true`` after this check.

   .. _errors-and-debugging-exercise-solutionsEe:

   e. **Repair the launch readiness checks:**

      .. sourcecode:: js
         :linenos:

         let launchReady = false;
         let crewReady = false; 
         let fuelLevel = 17000;
         let crewStatus = true;
         let computerStatus = 'green';

         if (fuelLevel >= 20000) {
            console.log('Fuel level cleared.');
            launchReady = true;
         } else {
            console.log('WARNING: Insufficient fuel!');
            launchReady = false;
         }
         console.log("launchReady = ", launchReady);

         if (crewStatus && computerStatus === 'green'){
            console.log('Crew & computer cleared.');
            crewReady = true;
         } else {
            console.log('WARNING: Crew or computer not ready!');
            crewReady = false;
         }
         console.log("crewReady = ", crewReady);

     

   :ref:`Back to the exercises <exercises-errors-and-debugging>`