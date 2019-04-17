Style Guide
===========

When writing code there are specific language rules you must follow for your code to execute. In addition to those language rules
there are **style guides** which define style rules to be followed when writing code. These style rules are conventions about how to write the code.
For example: how to name variables, where to place brackets, where to put new lines.

Imagine a book written by multiple authors, each of which uses different practices for capitalization, indentation,
and punctuation. One writes in all-lowercase and never indents paragraphs. Another capitalizes every word and uses
only the period for punctuation. Such a book would be hard to read; reading code can be that bad if everyone isn't
following the same style guide conventions.

**Benefits of using a Style Guide**

- Consistently written code is easier to read
- Predictable variable and file names
- Clear rules to follow when writing code

There are multiple style guides for each language. For the sake of consistency, it's important to follow the style guide rules of your organization
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

Always Use Braces for If Statements and Loops
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Good**

.. sourcecode:: js

   if (fuelTempCelsius > -220) {
      console.log('WARNING');
   }

   for (let i=0; i < 100; i++) {
      console.log(i);
   }

**Bad**

.. sourcecode:: js

   if (fuelTempCelsius > -220)
      console.log('WARNING');

   for (let i=0; i < 100; i++)
      console.log(i);

Use Semicolons
^^^^^^^^^^^^^^

**Good**

.. sourcecode:: js

   let fuelTempCelsius = -200;
   if (fuelTempCelsius > -220) {
      console.log('WARNING');
   }

**Bad**

.. sourcecode:: js

   let fuelTempCelsius = -200
   if (fuelTempCelsius > -220) {
      console.log('WARNING')
   }

Indent Code Blocks One Tab
^^^^^^^^^^^^^^^^^^^^^^^^^^
Indentation is a key tool for making code readable. Indent one *Tab* inside each **code block**.
The definition of what a *Tab* is differs between teams. The important thing is to be consistent and use
the same *Tab* throughout your project.

**Good**

.. sourcecode:: js

   const drivingLogKm = [120, 34, 15, 71, 89, 94];
   let totalKm = 0;
   for (let i=0; i < drivingLogKm.length; i++) {
       totalKm = totalKm + drivingLogKm[i];
       console.log("Adding", drivingLogKm[i]);
       console.log("Total Kilometers", totalKm);
       if (drivingLogKm[i] > 100) {
           console.log("warning: trip distance longer than advised")
       }
   }
   if (totalKm > 1000) {
       console.log("Over limit for month");
   } else {
       console.log("Still under limit for month");
   }

**Bad**

.. sourcecode:: js

   const drivingLogKm = [120, 34, 15, 71, 89, 94];
   let totalKm = 0;
   for (let i=0; i < drivingLogKm.length; i++) {
   totalKm = totalKm + drivingLogKm[i];
   console.log("Adding", drivingLogKm[i]);
   console.log("Total Kilometers", totalKm);
   if (drivingLogKm[i] > 100) {
   console.log("warning: trip distance longer than advised")
   }
   }
   if (totalKm > 1000) {
   console.log("Over limit for month");
   } else {
   console.log("Still under limit for month");
   }
