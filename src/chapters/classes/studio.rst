Studio: Classes
================

Let's create a class to handle new animal crew candidates!

Edit the `practice file <https://repl.it/@launchcode/ClassStudio01>`__ as you
complete the studio activity.

Part 1 - Add Class Properties
------------------------------

#. Declare a class called ``CrewCandidate`` with a ``constructor`` that takes
   three parameters---name, mass, and scores. Note that ``scores`` will be an
   array of test results.

#. Create objects for the following candidates:

   a. Bubba Bear has a mass of 135 kg and test scores of 88, 85, and 90.
   b. Malia Maltese has a mass of 1.5 kg and test scores of 93, 88, and 97.
   c. Glad Gator has a mass of 225 kg and test scores of 75, 78, and 62.

Use ``console.log`` for each object to verify that your class correctly assigns
the key/value pairs.

Part 2 - Add First Class Method
--------------------------------

As our candidates complete more tests, we need to be able to add the new
scores to their records.

#. Add an ``addScore`` function to ``CrewCandidate``. The function must take
   a new score as a parameter. Code this function OUTSIDE of ``constructor``.
   (If you need to review the syntax, revisit
   :ref:`Assigning Class Methods <adding-class-methods>`.

#. When passed a score, the function adds the value to ``this.scores`` with the
   :ref:`push array method <push-and-pop-examples>`.

#. Test out your new method by adding a score of ``83`` to Bubba's record, then
   print out the new score array with ``objectName.scores``.

Part 3 - Add More Methods
--------------------------



:ref:`round to 1 decimal place <rounding-to-decimal-places>`

Part 4 - Bonus Mission
-----------------------
