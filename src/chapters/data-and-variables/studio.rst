
.. _studio-chapter-4:

=============================
Studio: Launch Checklist LC04
=============================

In this studio you are going to write the code that displays 
the very important **Launch Checklist LC04**. The **LC04** displays 
statuses and information related to the space shuttle, astronauts, and the rockets 
before launch.

Declare and Initialize Variables
--------------------------------
Declare and initialize a variable for every data point listed in the table below.
Be careful to pay attention to the types of the values.

.. note::

   For the ``date`` and ``time`` values use the ``string`` type. Later in the class you will learn other ways 
   of working with date and time in JavaScript.

.. list-table::
   :widths: auto
   :header-rows: 0

   * - date
     - Monday 2019-03-18
   * - time
     - 10:05:34 AM
   * - astronautCount
     - 7
   * - astronautStatus
     - ready
   * - averageAstronautWeightKg
     - 80.7
   * - crewWeightKg
     - astronautCount * averageAstronautWeightKg
   * - fuelWeightKg
     - 760,000
   * - shuttleWeightKg
     - 74842.31
   * - totalWeightKg
     - crewWeightKg + fuelWeightKg + shuttleWeightKg
   * - fuelTempCelsius
     - -225
   * - fuelLevel
     - 100%
   * - weatherStatus
     - clear

Generate the LC04 Form
----------------------
Display the **LC04** using ``console.log()`` statements and the variables you declared and initialized.

| The generated report should look exactly like the below example, including spaces, dashes, >, and \*.

LC04 - Example Output
---------------------

.. sourcecode:: console
   
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
   * Fuel temp celsius: -225C
   * Fuel level: 100%

   -------------------------------------
   > WEIGHT DATA
   -------------------------------------
   * Crew weight: 564.9kg
   * Fuel weight: 760000kg
   * Shuttle weight: 74842.31kg
   * Total weight: 835407.21kg

   -------------------------------------
   > FLIGHT PLAN
   -------------------------------------
   * weather: clear

   -------------------------------------
   > OVERALL STATUS
   -------------------------------------
   * Clear for take off: YES
