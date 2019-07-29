Exercises
=========

Zero Division: Throw
--------------------

Write a function called divide that takes two parameters: a ``numerator`` and a
``denominator``.

Your function should return the result of ``numerator / denominator``.

However, if the ``denominator`` is zero you should throw an error informing the
user they attempted to divide by zero. The error text should be ``Attempted to divide by zero.``

.. admonition:: Note

   Hint: You can use an ``if / throw`` statement to complete this exercise.

Test Student Labs
-----------------

A teacher has created a ``gradeLabs`` function that verifies if student programming labs work.
This function loops over an array of JavaScript objects that *should* contain a ``student``
property and ``runLab`` property.

The ``runLab`` property is expected to be a function containing the student's code. The ``runLab``
function is called and the result is compared to the expected result. If the result and expected
result don't match, then the lab is considered a failure.

.. sourcecode:: js
   :linenos:

    function gradeLabs(labs) {
      for (let i=0; i < labs.length; i++) {
         let lab = labs[i];
         let result = lab.runLab(3);
         console.log(`${lab.student} code worked: ${result === 27}`);
      }
    }

   let studentLabs = [
      {
         student: 'Carly',
         runLab: function (num) {
            return Math.pow(num, num);
         }
      },
      {
         student: 'Erica',
         runLab: function (num) {
            return num * num;
         }
      }
   ];

   gradeLabs(studentLabs);

The ``gradeLabs`` function works for the majority of cases. However what happens if a student named their function incorrectly?
Run ``gradeLabs`` and pass it ``studentLabs2`` as defined below.

.. sourcecode:: js
   :linenos:

   let studentLabs2 = [
      {
         student: 'Jim',
         myCode: function (num) {
            return num + num;
         }
      },
      {
         student: 'Jessica',
         runLab: function (num) {
            return Math.pow(num, num);
         }
      }
   ];

   gradeLabs(studentLabs2);

Upon running the second example, the teacher gets a ``TypeError: lab.runLab is not a function``.

Your task is to add a ``try`` ``catch`` block inside of ``gradeLabs`` to catch an exception if the ``runLab`` function is not defined.
