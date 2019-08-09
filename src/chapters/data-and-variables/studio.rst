
.. _studio-launch-checklist-LC04:

Studio: Data and Variables
===========================

In this studio, you are going to write code to display the *very important*
**Launch Checklist LC04**.

**LC04** displays information related to the space shuttle, astronauts, and
rockets before launch.

Click this link to open the `starter repl.it file <https://repl.it/@launchcode/Studio-Data-and-Variables>`__.

Declare and Initialize Variables
---------------------------------

Declare and initialize a variable for every data point listed in the table
below. Remember to account for the different data types.

.. admonition:: Note

   For now, use the ``string`` type for the ``date`` and ``time`` values. Later
   in the class, we will learn other ways to work with date and time in
   JavaScript.

.. list-table::
   :widths: auto
   :header-rows: 1

   * - Variable
     - Value
   * - ``date``
     - Monday 2019-03-18
   * - ``time``
     - 10:05:34 AM
   * - ``astronautCount``
     - 7
   * - ``astronautStatus``
     - ready
   * - ``averageAstronautMassKg``
     - 80.7
   * - ``crewMassKg``
     - ``astronautCount`` * ``averageAstronautMassKg``
   * - ``fuelMassKg``
     - 760,000
   * - ``shuttleMassKg``
     - 74842.31
   * - ``totalMassKg``
     - ``crewMassKg`` + ``fuelMassKg`` + ``shuttleMassKg``
   * - ``fuelTempCelsius``
     - -225
   * - ``fuelLevel``
     - 100%
   * - ``weatherStatus``
     - clear

Generate the LC04 Form
-----------------------

Display **LC04** to the console using the variables you declared and
initialized.

The generated report should look *exactly* like the example below---including
spaces and symbols (-, >, and \*).

Example Output
^^^^^^^^^^^^^^^

Note that your output will should change when you assign different values to
``astronautCount``, ``fuelMassKg``, etc. The point is to AVOID coding specific
values into the ``console.log`` statements. Use your variable names instead.

::

   -------------------------------------
   > LC04 - LAUNCH CHECKLIST
   -------------------------------------
   Date: Monday 2019-03-18
   Time: 10:05:34 AM

   -------------------------------------
   > ASTRONAUT INFO
   -------------------------------------
   * count: 7
   * status: ready

   -------------------------------------
   > FUEL DATA
   -------------------------------------
   * Fuel temp celsius: -225 C
   * Fuel level: 100%

   -------------------------------------
   > WEIGHT DATA
   -------------------------------------
   * Crew mass: 564.9 kg
   * Fuel mass: 760000 kg
   * Shuttle mass: 74842.31 kg
   * Total mass: 835407.21 kg

   -------------------------------------
   > FLIGHT PLAN
   -------------------------------------
   * weather: clear

   -------------------------------------
   > OVERALL STATUS
   -------------------------------------
   * Clear for takeoff: YES

Show Off Your Code
-------------------

When finished, show your code to your TA so they can verify your work.

If you do not finish before the end of class, login to Repl.it and save your
work. Complete the studio at home, then copy the URL for your project and
submit it to your TA.

Bonus Mission
--------------

Use ``readline-sync`` to prompt the user to enter the value for
``astronautCount``.

The values printed for ``astronautCount``, ``crewMassKg``, and ``totalMassKg`` should
change based on the number of astronauts on the shuttle. (Don't forget to
convert the input value from a string to a number).
