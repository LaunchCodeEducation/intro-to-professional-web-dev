
.. _studio-chapter-4:

=============================
Studio: Launch Checklist LC04
=============================

| In this studio you are going to write code to display the *very important* **Launch Checklist LC04**. 
| **LC04** displays information related to the space shuttle, astronauts, and rockets before launch.

Declare and Initialize Variables
--------------------------------
Declare and initialize a variable for every data point listed in the table below.
Remember to account for the different data types.

.. note::

   For now, use the ``string`` type for the ``date`` and ``time`` values. Later in the class, we will learn other ways 
   to work with date and time in JavaScript.

.. list-table::
   :widths: auto
   :header-rows: 1

   * - Variable
     - Value
   * - date
     - Monday 2019-03-18
   * - time
     - 10:05:34 AM
   * - astronautCount
     - 7
   * - astronautStatus
     - ready
   * - averageAstronautMass_kg
     - 80.7
   * - crewMass_kg
     - astronautCount * averageAstronautMass_kg
   * - fuelMass_kg
     - 760,000
   * - shuttleMass_kg
     - 74842.31
   * - totalMass_kg
     - crewMass_kg + fuelMass_kg + shuttleMass_kg
   * - fuelTempCelsius
     - -225
   * - fuelLevel
     - 100%
   * - weatherStatus
     - clear

Generate the LC04 Form
----------------------
Display **LC04** to the ``console`` using the variables you declared and initialized.

The generated report should look *EXACTLY* like the example below -- including spaces, dashes, >, and \*.

**Example:**

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
