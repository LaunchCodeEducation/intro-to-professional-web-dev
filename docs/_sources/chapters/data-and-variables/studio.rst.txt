
.. studio-chapter-4::

=============================
Studio: Launch Checklist LC04
=============================

In this studio you are going to write the code that displays 
the very important **Launch Checklist LC04**. The **LC04** displays 
statuses and information related to the space shuttle, astronauts, and the rockets 
before launch.

Requirements
------------

Declare and Initialize Variables
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Declare and initialize a variable for every data point listed in the table below.
Be careful to pay attention to the types of the values.

TODO: Short example code?

.. list-table::
   :widths: auto
   :header-rows: 0

   * - date
     - "Monday 2019-03-18"
   * - time
     - "10:05:34 AM"
   * - astronautCount
     - 7
   * - astronautStatus
     - "ready"
   * - fuelWeightKiloGrams
     - 760,000
   * - fuelTempCelsius
     - -225
   * - fuelStatus
     - "full"
   * - weatherStatus
     - "clear"
   * - payLoadSecured
     - "yes"

Generate the LC04 Form
^^^^^^^^^^^^^^^^^^^^^^
Use the variables you declared and initialized to build and display the **LC04** using 
``console.log()`` statements.

The generated report should exactly like the below example, including spaces, dashes, >, and *.

LC04 - Example Output
^^^^^^^^^^^^^^^^^^^^^

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
   * Fuel weight: 760000KG
   * Fuel status: full
   
   -------------------------------------
   > FLIGHT PLAN
   -------------------------------------
   * weather: clear

   -------------------------------------
   > OVERALL STATUS
   -------------------------------------
   * Clear for take off: YES


How to Turn it In?
------------------
* Codio instructions
* Non codio instructions?
