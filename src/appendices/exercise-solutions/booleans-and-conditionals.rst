.. _booleans-and-conditionals-exercise-solutions:

Exercise Solutions: Booleans and Conditionals
=============================================

.. _booleans-and-conditionals-exercise-solutionsA:

A. **Declare and initialize the following variables for our space shuttle.**

   .. sourcecode:: js
      :linenos:

      let engineIndicatorLight = "red blinking";
      let spaceSuitsOn = true;
      let shuttleCabinReady = true;
      let crewStatus = spaceSuitsOn && shuttleCabinReady;
      let computerStatusCode = 200;
      let shuttleSpeed = 15000;

   :ref:`Back to the exercises <exercises-booleans-and-conditionals>`

C. **Write conditional expressions to satisfy the safety rules.** 

   a. .. _booleans-and-conditionals-exercise-solutionsCa:

      .. sourcecode:: js
         :linenos:

         if (crewStatus) {
            console.log("Crew Ready");
         } else {
            console.log("Crew Not Ready");
         }

   #. .. _booleans-and-conditionals-exercise-solutionsCb:

      .. sourcecode:: js
         :linenos:

         if (computerStatusCode === 200) {
            console.log("Please stand by. Computer is rebooting.");
         } else if (computerStatusCode === 400) {
            console.log("Success! Computer online.");
         } else {
            console.log("ALERT: Computer offline!");
         }

   #. .. _booleans-and-conditionals-exercise-solutionsCc:

      .. sourcecode:: js
         :linenos:

         if (shuttleSpeed > 17500) {
            console.log("ALERT: Escape velocity reached!");
         } else if (shuttleSpeed < 8000) {
            console.log("ALERT: Cannot maintain orbit!");
         } else {
            console.log("Stable speed.");
         }

   :ref:`Back to the exercises <exercises-booleans-and-conditionals>`

.. _booleans-and-conditionals-exercise-solutionsE:

E. **Monitor the shuttle's fuel status.**

   .. sourcecode:: js
      :linenos:

      if (fuelLevel < 1000 || engineTemperature > 3500 || engineIndicatorLight === "red blinking") {
         console.log("ENGINE FAILURE IMMINENT!");
      } else if (fuelLevel <= 5000 || engineTemperature > 2500) {
         console.log("Check fuel level. Engines running hot.");
      } else if (fuelLevel > 20000 && engineTemperature <= 2500) {
         console.log("Full tank. Engines good.");
      } else if (fuelLevel > 10000 && engineTemperature <= 2500) {
         console.log("Fuel level above 50%. Engines good.");
      } else if (fuelLevel > 5000 && engineTemperature <= 2500) {
         console.log("Fuel level above 25%. Engines good.");
      } else {
         console.log("Fuel and engine status pending...");
      }

   :ref:`Back to the exercises <exercises-booleans-and-conditionals>`