Style Guide
===========

When writing code there are the specific language rules you must follow for your code to execute. In addition to those language rules
there are **style guides** which define style rules to be followed when writing code.

There are multiple style guides for each language. For consistency sake, it's important to follow the style guide rules of your organization
or company when writing code. The style guide for this course is below.

JavaScript Style Guide
----------------------

Camel Case Variable Names
^^^^^^^^^^^^^^^^^^^^^^^^^
Camel case is defined as starting with a lowercase word and then using uppercase for the first letter of
any additional words in the variable name.

**Good**

.. sourcecode:: js

   const astronautCount = 7;
   const fuelTempCelsius = -225;
   let isReady = false;

**Bad**

.. sourcecode:: js

   const AstronautCount = 7;
   const fuel_temp_celsius = -225;
   let is_ready = false;

Descriptive Variable Names
^^^^^^^^^^^^^^^^^^^^^^^^^^
Variable names should convey meaning.

**Good**

.. sourcecode:: js

   const astronautCount = 7;
   const fuelTempCelsius = -225;
   let isReady = false;

**Bad**

.. sourcecode:: js

   const c = 7;
   const fuelTempC = -225;
   let ir = false;

Opening Braces and Statements on Same Line
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Put opening braces on the same line as the statement.

**Good**

.. sourcecode:: js

   if (fuelTempCelsius > -220) {
      console.log('WARNING');
   } else {
      console.log('Temp fine');
   }

**Bad**

.. sourcecode:: js


   if (fuelTempCelsius > -220) 
   {
      console.log('WARNING');
   } 
   else 
   {
      console.log('Temp fine');
   }

Always use Braces for If Statements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Good**

.. sourcecode:: js

   if (fuelTempCelsius > -220) {
      console.log('WARNING');
   }

**Bad**

.. sourcecode:: js

   if (fuelTempCelsius > -220) 
      console.log('WARNING');

Use Semicolons
^^^^^^^^^^^^^^

**Good**

.. sourcecode:: js

   let ir = false;

   if (fuelTempCelsius > -220) {
      console.log('WARNING');
   }

**Bad**

.. sourcecode:: js

   let ir = false

   if (fuelTempCelsius > -220) {
      console.log('WARNING')
   }
