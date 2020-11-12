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

C. **Write conditional expressions to satisfy the safety rules below.** 

   #. ``crewStatus``

      - If the value is ``true``, print ``"Crew Ready"``
      - Else print ``"Crew Not Ready"``

      .. _booleans-and-conditionals-exercise-solutionsC1:

      .. sourcecode:: js
         :linenos:

         if (crewStatus) {
            console.log("Crew Ready");
         } else {
            console.log("Crew Not Ready");
         }

   #. ``computerStatusCode``

      - If the value is ``200``, print
        ``"Please stand by. Computer is rebooting."``
      - Else if the value is ``400``, print ``"Success! Computer online."``
      - Else print ``"ALERT: Computer offline!"``

      .. _booleans-and-conditionals-exercise-solutionsC2:

      .. sourcecode:: js
         :linenos:

         if (computerStatusCode === 200) {
            console.log("Please stand by. Computer is rebooting.");
         } else if (computerStatusCode === 400) {
            console.log("Success! Computer online.");
         } else {
            console.log("ALERT: Computer offline!");
         }

   #. ``shuttleSpeed``

      - If the value is ``> 17500``, print
        ``"ALERT: Escape velocity reached!"``
      - Else if the value is ``< 8000``, print
        ``"ALERT: Cannot maintain orbit!"``
      - Else print ``"Stable speed"``

      .. _booleans-and-conditionals-exercise-solutionsC3:

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