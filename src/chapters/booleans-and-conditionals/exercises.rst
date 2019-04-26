Exercises: Booleans and Conditionals
====================================

Attempt these exercises to test your understanding. 
Don't worry if you struggle while working on them. Struggling and recalling
the material will help you remember it.

| In class, be sure to ask about the topics you do not understand. You are NOT the only person who needs help.
    
.. note::

   When the term **print** is used, it means to output a value to the ``console``.

Declare and initialize variables in the table
----------------------------------------------

.. list-table::
   :widths: auto
   :header-rows: 1

   * - Variable
     - Value
   * - engineIndicatorLight
     - red blinking
   * - spaceSuitsOn
     - true
   * - shuttleCabinReady
     - true
   * - crewStatus
     - spaceSuitsOn && shuttleCabinReady
   * - computerStatusCode
     - 200
   * - shuttleSpeed
     - 15000

Examine the code below. What will be printed to the console?
----------------------------------------------------------------------
Use the value of ``engineIndicatorLight`` defined above to answer this question.

.. code-block:: javascript

   if (engineIndicatorLight === "green") {
      console.log("engines have started");
   } else if (engineIndicatorLight === "green blinking") {
      console.log("engines are preparing to start");
   } else {
      console.log("engines are off");
   }

Write conditional expressions to satisfy the safety rules below
----------------------------------------------------------------
Using the variables defined from the table above.

#. ``crewStatus``

   - if crewStatus is ``true``, print ``"Crew Ready"``
   - else print ``"Crew Not Ready"``

#. ``computerStatusCode``

   - if value is ``200``, print ``"Please stand by. Computer is rebooting."``
   - else if value is ``400``, print ``"Success! Computer online."``
   - else print ``"ALERT: Computer offline!"``

#. ``shuttleSpeed``

   - if value is ``> 17,500``, print ``"ALERT: Escape velocity reached!"``
   - else if value is ``< 8000``, print ``"ALERT: Cannot maintain orbit!"``
   - else print ``"Stable speed"``

Do these code blocks produce the same result?
---------------------------------------------
Answer Yes or No

.. code-block:: javascript

    if (crewStatus && computerStatusCode === 200 && spaceSuitsOn) {
        console.log("all systems go");
    } else {
        console.log("WARNING. Not ready");
    }

.. code-block:: javascript

    if (!crewStatus || computerStatusCode !== 200 || !spaceSuitsOn) {
        console.log("WARNING. Not ready");        
    } else {
        console.log("all systems go");
    }

Monitor fuel status
--------------------
**First, declare and initialize the following variables:**

.. list-table::
   :widths: auto
   :header-rows: 1

   * - Variable
     - Value
   * - fuelLevel
     - 21000
   * - engineTemperature
     - 1200

**Next, implement the checks below using** ``if / else if / else`` **statements.**

a. | If ``fuelLevel`` is above 20000 AND ``engineTemperature`` is below 2500,
   | print ``"Full tank.  Engines good."``
b. | If ``fuelLevel`` is above 10000 AND ``engineTemperature`` is below 2500,
   | print ``"Fuel level above 50%.  Engines good."``
c. | If ``fuelLevel`` is above 5000 AND ``engineTemperature`` is below 2500,
   | print ``"Fuel level above 25%.  Engines good."``
d. | If ``fuelLevel`` is below 5000 OR ``engineTemperature`` is above 2500,
   | print ``"Check fuel level.  Engines running hot."``
e. | If ``fuelLevel`` is below 1000 OR ``engineTemperature`` is above 3500 OR ``engineIndicatorLight`` is red blinking
   | print ``"ENGINE FAILURE IMMINENT!"``

.. note::
   Run your code several times with different values for ``fuelLevel``, ``engineTemperature`` and ``engineIndicatorLight``.
   You must make sure your code prints the correct phrase for each set of conditions.

Final bit of fun!
--------------------
| The shuttle should only launch if the fuel tank is full and the engine check is OK.  
| *However*, let's establish an override command to ignore any warnings and send the shuttle into space anyway!

**Create the variable** ``commandOverride`` **, and set it to be** ``true`` **or** ``false`` **.**

| If commandOverride is ``false``, then the shuttle should only lauch if the fuel and engine check are OK.
| If commandOverride is ``true``, then the shuttle will launch regardless of the fuel and engine status.

**Code the following** ``if / else`` **check:**

a. | If ``fuelLevel`` is above 20000 AND ``engineIndicatorLight`` is NOT red blinking OR ``commandOverride`` is true
   | print ``"Cleared to launch!"``
b. Else print ``"Launch scrubbed!"``
