Chapter 5 Exercises
===================

Attempt these excersises to test your understanding. 
Don't worry if you struggle while working on them. Struggling and recalling
the material will make you remember it.

| Be sure to ask about the topics you don't understand in class, you won't be the only person that needs help with that topic.
    
.. note::

   When the term **print** is used, that means to output a value to the ``console`` 
   using ``console.log("text or a variable name")``.  
   
   | Print ``"hello"`` means ``console.log("hello")``

Declare and initialize variables in the table
----------------------------------------------
Write variables for these values.

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

Read the below code. What will be printed to the console?
----------------------------------------------------------------------
Answer using the value of ``engineIndicatorLight`` that is defined in the table above.

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

   - if value is ``200``, print ``"Please stand by. Computer is rebooting"``
   - else if value is ``400``, print ``"Success! Computer working fine"``
   - else print ``"ALERT: Computer not functioning"``

#. ``shuttleSpeed``

   - if value is ``> 17,500``, print ``"ALERT: could escape orbit"``
   - else if value is ``< 8000``, print ``"ALERT: could fall out of orbit"``
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

Implement logic for spectrometer
--------------------------------
A spectrometer is used to identify what objects/planets/gases are physically made of.

| Implement the below rules using ``if``, ``else if``, and ``else`` statements.

* variables defined by spectrometer

  * ``colorCode``
  * ``waveLength``

* if ``colorCode`` is ``"2A109"`` OR ``waveLength`` is ``2985`` nanometers.

  * print ``"Water found"``

* else if ``colorCode`` is ``"482C0"`` AND ``waveLength`` is ``589.0`` OR ``589.6`` nanometers.

  * print ``"Sodium found"``

* else if ``colorCode`` is ``"Z491"`` OR ``waveLength`` is ``656`` OR ``486`` OR ``434`` nanometers.

  * print ``"Hydrogen found"``

* else print ``"Non target element found"``

Fix the fuel status system
--------------------------------
The below logic prints out the status of the fuel system. Sadly the code has a bug.

| Please fix the code to print ``"Full tank"`` if ``fuelRemaining`` is equal to ``20,000``

.. sourcecode:: javascript

   const fuelRemaining = 21000;

   if (fuelRemaining > 15000) {
      console.log("75% fuel left");
   } else if (fuelRemaining === 20000) {
      console.log("Full tank");
   } else if (fuelRemaining > 10000) {
      console.log("50% fuel left");
   } else if (fuelRemaining > 5000) {
      console.log("25% fuel left");
   } else {
      console.log("Warning: fuel low");
   }
