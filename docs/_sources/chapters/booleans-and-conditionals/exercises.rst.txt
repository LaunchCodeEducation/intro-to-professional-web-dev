Chapter 5 Exercises
===================


    
1. Declare and initialize variables in the table.

.. list-table::
   :widths: auto
   :header-rows: 1

   * - Variable
     - Value
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

Example:

.. code-block:: javascript

    spacSuitsOn = true;

2. Write conditional expressions and ``if``,  ``else if``, and ``else`` statements for the below rules.
   
   * crewStatus

     - if value is true, print **"Crew Ready"**
     - else print **"Crew Not Ready"**

   * computerStatusCode

     - if value is **200**, print **"Success, computer working fine"**
     - else if value is **400**, print **"ALERT: computer not functioning"**

   * shuttleSpeed

     - if value is **> 17,500**, print **"ALERT: could escape orbit"**
     - else if value is **< 8000**, print **"ALERT: could fall out of orbit"**
     - else print **"Stable speed"**

Example:

.. code-block:: javascript

    if (crewStatus) {
        console.log("crew ready");
    }

3. Do these code blocks produce the same result?
    
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

4. Use the below rules to implement the logic for "thing that reads light waves sensor" using boolean expressions and ``if``,  ``else if``, and ``else`` statements.

   * variables

     - colorCode
     - waveLength

   * if colorCode is "2A109" OR waveLength is 4883.1

     - print "Water found"

   * else if colorCode is "482C0" OR waveLength is 2392

     - print "Carbon found"

   * else if colorCode is "Z491" OR waveLength is 560

     - print "Silicon found"

   * else print "Non target element found"

5. TODO: have students find bug in code. maybe an if/else chain that has wrong logic
