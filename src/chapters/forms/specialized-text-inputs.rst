Specialized Text Inputs
=======================
For these text inputs the browser will validate and provide feedback to the user based on
rules for the declared type.


.. role:: raw-html(raw)
   :format: html

.. list-table::
   :header-rows: 1

   * - Type
     - Syntax
     - Description
     - Demo
   * - date
     - ``<input type="date" name="flightDate"/>``
     - Browser validates the value is a valid date
       format. Some browsers provide a *date picker*.
     - :raw-html:`<input type="date" name="flightDate"/>`
   * - email
     - ``<input type="email" name="emailAddress"/>``
     - Browser validates the value is a valid email address format.
     - :raw-html:`<input type="email" name="emailAddress"/>`
   * - number
     - ``<input type="number" name="fuelTemp"/>``
     - Browser validates the value is a valid number format.
     - :raw-html:`<input type="number" name="fuelTemp"/>`


Example
-------
.. admonition:: Example

    .. sourcecode:: html

       <form action="https://handlers.education.launchcode.org/request-parrot" method="post">
         <label>Email<input type="email" name="emailAddress"/></label>
         <label>Report Date<input type="date" name="reportDate"/></label>
         <label>Crew Count<input type="number"
         name="crewCount" min="1" max="10"/></label>
         <button>Send Report</button>
       </form>

    .. figure:: figures/specialized-inputs-example.png
       :alt: Form with Code Name, Code Word, and Description field. All fields have values.

    **Submitted Values**

    ::

      emailAddress=c.danvers@us.af.mil
      reportDate=2019-03-08
      crewCount=8

    `Run it <https://repl.it/@launchcode/specialized-inputs-example>`_
