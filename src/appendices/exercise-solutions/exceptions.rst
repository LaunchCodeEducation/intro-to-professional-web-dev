.. _exceptions-exercise-solutions:

Exercise Solutions: Exceptions
==============================

.. _exceptions-exercise-solutionsA:

A. **Write a function that throws an exception.**

   .. sourcecode:: js
      :linenos:

      function divide(numerator, denominator) {
			if (denominator === 0) {
				throw Error('You cannot divide by zero!'); 
			}
			return numerator/denominator;
		}


   :ref:`Back to the exercises <exercises-exceptions>`