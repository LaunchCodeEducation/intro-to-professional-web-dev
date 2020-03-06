Exercises: Booleans and Conditionals
====================================

Attempt these exercises to test your understanding. Don't worry if you struggle
while working on them. Struggling and then reviewing the material will help you
remember it.

In class, be sure to ask about the topics you do not understand. You are NOT
the only person who needs help.

`Code exercises 1 & 2 here <https://repl.it/@launchcode/ConditionalsExercises01>`__.

#. Declare and initialize the following variables for our space shuttle:

   .. list-table::
      :widths: auto
      :header-rows: 1

      * - Variable
        - Value
      * - ``engineIndicatorLight``
        - ``"red blinking"``
      * - ``spaceSuitsOn``
        - ``true``
      * - ``shuttleCabinReady``
        - ``true``
      * - ``crewStatus``
        - ``spaceSuitsOn && shuttleCabinReady``
      * - ``computerStatusCode``
        - ``200``
      * - ``shuttleSpeed``
        - ``15000``

#. Examine the code below. What will be printed to the console?

   Use the value of ``engineIndicatorLight`` defined above to answer this
   question.

   .. sourcecode:: js
      :linenos:

      if (engineIndicatorLight === "green") {
         console.log("engines have started");
      } else if (engineIndicatorLight === "green blinking") {
         console.log("engines are preparing to start");
      } else {
         console.log("engines are off");
      }

#. Write conditional expressions to satisfy the safety rules below, using the
   variables defined from the table above.
   `Code exercises 3 & 4 here <https://repl.it/@launchcode/ConditionalsExercises02>`__.

   #. ``crewStatus``

      - If the value is ``true``, print ``"Crew Ready"``
      - Else print ``"Crew Not Ready"``

   #. ``computerStatusCode``

      - If the value is ``200``, print
        ``"Please stand by. Computer is rebooting."``
      - Else if the value is ``400``, print ``"Success! Computer online."``
      - Else print ``"ALERT: Computer offline!"``

   #. ``shuttleSpeed``

      - If the value is ``> 17500``, print
        ``"ALERT: Escape velocity reached!"``
      - Else if the value is ``< 8000``, print
        ``"ALERT: Cannot maintain orbit!"``
      - Else print ``"Stable speed"``

#. PREDICT:

   Do these code blocks produce the same result? Answer Yes or No.

   .. sourcecode:: js
      :linenos:

      if (crewStatus && computerStatusCode === 200 && spaceSuitsOn) {
         console.log("all systems go");
      } else {
         console.log("WARNING. Not ready");
      }

   .. sourcecode:: js
      :linenos:

      if (!crewStatus || computerStatusCode !== 200 || !spaceSuitsOn) {
         console.log("WARNING. Not ready");
      } else {
         console.log("all systems go");
      }

#. The remaining exercises implement conditional code to monitor the shuttle's
   fuel status. `Code exercises 5 & 6 here <https://repl.it/@launchcode/ConditionalsExercises03>`__.
   Implement the checks below using ``if`` / ``else if`` / ``else``
   statements. Order is important when working with conditionals, and the
   checks below are NOT written in the correct sequence. Please read ALL of the
   checks before coding and then decide on the best order for the conditionals.

   #. If ``fuelLevel`` is above 20000 AND ``engineTemperature`` is at or below
      2500, print ``"Full tank. Engines good."``
   #. If ``fuelLevel`` is above 10000 AND ``engineTemperature`` is at or below
      2500, print ``"Fuel level above 50%.  Engines good."``
   #. If ``fuelLevel`` is above 5000 AND ``engineTemperature`` is at or below
      2500, print ``"Fuel level above 25%. Engines good."``
   #. If ``fuelLevel`` is at or below 5000 OR ``engineTemperature`` is above
      2500, print ``"Check fuel level. Engines running hot."``
   #. If ``fuelLevel`` is below 1000 OR ``engineTemperature`` is above 3500 OR
      ``engineIndicatorLight`` is red blinking, print ``"ENGINE FAILURE
      IMMINENT!"``
   #. Otherwise, print ``"Fuel and engine status pending..."``

.. admonition:: Try It

   Run your code several times to make sure it prints the correct phrase for
   each set of conditions.

   .. list-table::
      :widths: auto
      :header-rows: 1

      * - **fuelLevel**
        - **engineTemperature**
        - **engineIndicatorLight**
        - **Result**
      * - Any
        - Any
        - ``red blinking``
        - ``ENGINE FAILURE IMMINENT!``
      * - 21000
        - 1200
        - NOT ``red blinking``
        - ``Full tank. Engines good.``
      * - 900
        - Any
        - Any
        - ``ENGINE FAILURE IMMINENT!``
      * - 5000
        - 1200
        - NOT ``red blinking``
        - ``Check fuel level. Engines running hot.``
      * - 12000
        - 2600
        - NOT ``red blinking``
        - ``Check fuel level. Engines running hot.``
      * - 18000
        - 2500
        - NOT ``red blinking``
        - ``Fuel level above 50%. Engines good.``

6. Final bit of fun!

   The shuttle should only launch if the fuel tank is full and the engine check
   is OK. *However*, let's establish an override command to ignore any warnings
   and send the shuttle into space anyway!

   #. Create the variable ``commandOverride``, and set it to be ``true`` *or*
      ``false``.

      If ``commandOverride`` is ``false``, then the shuttle should only launch
      if the fuel and engine check are OK.

      If ``commandOverride`` is ``true``, then the shuttle will launch
      regardless of the fuel and engine status.

   #. Code the following ``if`` / ``else`` check:

      If ``fuelLevel`` is above 20000 AND ``engineIndicatorLight`` is NOT
      red blinking OR ``commandOverride`` is true print ``"Cleared to
      launch!"``

      Else print ``"Launch scrubbed!"``
