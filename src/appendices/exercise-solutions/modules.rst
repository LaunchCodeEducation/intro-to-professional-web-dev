.. _modules-solutions:

Exercise Solutions: Modules
===========================

.. _modules-solutions1:

Export Finished Modules
-----------------------

#. In ``averages.js``, add code to export all of the functions within an
   object.

   .. sourcecode:: js
      :linenos:

      module.exports = {
         averageForStudent: averageForStudent,
         averageForTest: averageForTest
      };

.. _modules-solutions2:

Code and Export a New Module
----------------------------

#. Add code to complete the ``randomFromArray`` function. It should take an
   array as an argument and then return a randomly selected element from that array.

   .. sourcecode:: js
      :linenos:

      function randomFromArray(arr){
         let index = Math.floor(Math.random()*arr.length);
         return arr[index];
      }

.. _modules-solutions3:

Import Required Modules
-----------------------

#. Assign ``readline-sync`` to the ``input`` variable.

   .. sourcecode:: js

      const input = require('readline-sync');

#. Assign the ``printAll`` function from ``display.js`` to the ``printAll`` variable.

   .. sourcecode:: js

      const printAll = require('./display.js');

.. _modules-solutions4:

Finish the Project
------------------

#. Line 21 - Call ``printAll`` to display all of the tests and student
   scores. Be sure to pass in the correct arguments.

   .. sourcecode:: js
      :lineno-start: 21

      printAll(astronauts, testTitles, scores);

#. Line 29 - Call ``averageForStudent`` (with the proper arguments) to print
   each astronaut's average score.

   .. sourcecode:: js
      :lineno-start: 29
   
      let avg = averages.averageForStudent(j, scores);