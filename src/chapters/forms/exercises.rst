Exercises: Forms
================
Hello programmer, we need you to make a Rocket Simulation form. Below are the requirements. Good luck!

Code your solution in `this repl.it <https://repl.it/@launchcode/Exercises-rocket-simulation>`_.

**Submission Details**

* Set the ``method`` to ``"POST"``
* Set the ``action`` to ``"https://www.w3schools.com/action_page.php"``

**Fields**

.. list-table::
   :header-rows: 1

   * - Display Name
     - Input Type
     - Input Name
     - Possible Values
   * - Test Name
     - text
     - ``testName``
     - No limitations
   * - Test Date
     - date
     - ``testDate``
     - Date format mm/dd/yyyy
   * - Rocket Type
     - select
     - ``rocketType``
     - Brant, Lynx, Orion, Terrier
   * - Number of Rocket Boosters
     - number
     - ``boosterCount``
     - A positive number less than 10
   * - Wind Rating
     - radio
     - ``windRating``
     - No Wind: w/ value 0, Mild: w/ value 10, Strong: w/ value 20
   * - Use production grade servers
     - checkbox
     - ``productionServers``
     - on or off

.. admonition:: Example

   .. figure:: figures/rocket-simulation-example.png
         :alt: Rocket simulation form with all input fields filled out.


   **Submitted Values**

   ::

      testName=Moon+Shot&testDate=2020-07-16&rocketType=Lynx&boosterCount=3&windRating=10&productionServers=on


Bonus Mission
-------------

Use an event handler and the *submit* event to validate that all inputs have values. Do not
let the form be submitted if inputs are empty.
