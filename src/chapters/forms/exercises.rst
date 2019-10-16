Exercises: Forms
================

Hello programmer, we need you to make a Rocket Simulation form. Please follow
the steps below and good luck!

Code your solution in `this repl.it <https://repl.it/@launchcode/Exercises-rocket-simulation>`_.

#. Create a ``<form>`` with these attributes.

   a. Set ``method`` to ``"POST"``
   b. Set ``action`` to ``"https://handlers.education.launchcode.org/request-parrot"``

#. Add a ``<label>`` and ``<input>`` for Test Name to the ``<form>``.

   a. ``<label>Test Name <input type="text" name="testName"/></label>``.

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

#. Can you submit the form now? What is missing?
#. Add a ``<button>Run Simulation</button>`` to the ``<form>``.
#. Enter a value into the "testName" input and submit the form.

   a. Was the value properly submitted to the form handler?

#. Next add these five ``inputs`` to the ``<form>``.

   a. Pay attention to the types and possible options.
   b. Also add a ``<label>`` for each input.

.. list-table::
   :header-rows: 1

   * - Display Name
     - Input Type
     - Input Name
     - Possible Values
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
     - No Wind: with value 0, Mild: with value 10, Strong: with value 20
   * - Use production grade servers
     - checkbox
     - ``productionServers``
     - on or off


.. admonition:: Example

   What the form will look like *before* submission.

   .. figure:: figures/rocket-simulation-example.png
         :alt: Rocket simulation form with all input fields filled out.


   **Submitted Values**

   ::

      testName=Moon+Shot
      testDate=2020-07-16
      rocketType=Lynx
      boosterCount=3
      windRating=10
      productionServers=on


Bonus Mission
-------------

Use an event handler and the *submit* event to validate that all inputs have
values. Do NOT let the form be submitted if inputs are empty.
