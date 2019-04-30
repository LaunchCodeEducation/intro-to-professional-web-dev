Exercises: Functions
=====================

Complete Reversal
------------------

The ``reverse`` method flips the order of the elements within an array.
However, ``reverse`` does not affect the digits or characters within those
elements.

.. admonition:: Example

   .. sourcecode:: js

      let arr = ['hello', 'world', 123, 'orange'];

      arr.reverse()
      console.log(arr);

   **Output**

   ::

      ['orange', 123, 'world', 'hello']

      instead of ['egnaro', 321, 'dlrow', 'olleh']

Let's have some fun by creating a process that reverses BOTH the order of the
entries in an array AND the order of characters within the individual elements.

Remember that a function should perform only one task. To follow this best
practice, we will solve the array reversal by defining two functions - one that
reverses the characters in a string (or the digits in a number) and one that
flips the order of entries in the array.

1. Create a function with one parameter that represents a string or a number.
   When passed a string, the function returns a string with all the characters
   reversed (e.g. "Rutabaga" becomes "agabatuR"). When passed a number, the
   function returns a number with all the digits reversed (e.g. 1234 converts
   to 4321 and NOT the string ``"4321"``). *Be sure to print the result
   returned by the function to verify that your code works*. Do this before
   moving on to the next exercise.

|

2. Create a function with one parameter, which is the array we want to
   completely reverse. The function loops through the old array and returns a
   new array with all the elements reversed by order and by characters/digits.
   Hint - You can always call your letter-revsersal function from within your
   array-reversal function. *Be sure to print the results from each exercise in
   order to verify your code*.

.. admonition:: Sample arrays for testing

   .. sourcecode:: js

      ['apple', 'potato', 'Capitalized Words']
      [123, 8897, 42, 1168, 8675309]
      ['hello', 'world', 123, 'orange']

[Repl.it link: Code your answers **here**.]

Sort Numbers For Real
----------------------

Recall that using the ``sort`` method on an array of numbers produced an
unexpected result, since JavaScript converts the numbers to strings by default
(TODO - add reference to the ``sort`` example page).  Let's fix this!

3. Create a function with an array of numbers as its parameter. The function
   should iterate through the array and return the minimum value from the
   array. *Hint*: Use what you know about ``if`` statements to identify and
   store the smallest value within the array.

.. admonition:: Sample arrays for testing

   .. sourcecode:: js

      [ 5, 10, 2, 42 ]
      [ -2, 0, -10, -44, 5, 3, 0, 3 ]
      [ 200, 5, 4, 10, 8, 5, -3.3, 4.4, 0 ]

4. Create another function with an array of numbers as its parameter.  Within
   this function:

   a. Define a new, empty array to hold the final sorted numbers.
   b. Use your function from the previous exercise to find the minimum value in
      the old array.
   c. Add the minimum value to the new array, and remove the minimum value from
      the old array.
   d. Repeat parts b & c until the old array is empty.
   e. Return the new sorted array.

*Hint*: Either a ``for`` or ``while`` loop will work inside this function, but
there IS a better choice.  Consider the task the function must accomplish as
well as the characteristics of each type of loop. Which one best serves if the
array has an unknown length?

*Be sure to print the results in order to verify your code*.

[Repl.it link: Code your answers **here**.]
