Studio: Functions
==================

The ``reverse`` method flips the order of the elements within an array.
However, ``reverse`` does not affect the digits or characters within those
elements.

.. admonition:: Example

   .. sourcecode:: js
      :linenos:

      let arr = ['hello', 'world', 123, 'orange'];

      arr.reverse()
      console.log(arr);

   **Console Output**

   ::

      ['orange', 123, 'world', 'hello']

What if we wanted the reversed array to be
``['egnaro', 321, 'dlrow', 'olleh']``?

Let's have some fun by creating a process that reverses BOTH the order of the
entries in an array AND the order of characters within the individual elements.

Remember that a function should perform only one task. To follow this best
practice, we will solve the array reversal by defining two functions - one that
reverses the characters in a string (or the digits in a number) and one that
flips the order of entries in the array.

Before You Start
----------------

If you are enrolled in a LaunchCode program, access this studio by following the repl.it classroom links posted in your class at learn.launchcode.org.

If you are working through this material on your own, use the repl.it links contained on this page.

Reverse Characters
-------------------

1. In the *composing functions* section, we examined a function that
   :ref:`reverses the characters in a string <reverse-a-string>` using the
   ``split`` and ``join`` methods. Let's rebuild that function now.

   a. Define the function as ``reverseCharacters``. Give it one parameter, which will
      be the string to reverse.
   b. Within the function, ``split`` the string into an array, then reverse the
      array.
   c. Use ``join`` to create the reversed string and *return* that string from the
      function.
   d. Below the function, define and initialize a variable to hold a string.
   e. Use ``console.log(reverseCharacters(myVariableName));`` to call the function and verify
      that it correctly reverses the characters in the string.
   f. *Optional*: Use method chaining to reduce the lines of code within the
      function.

`Code exercises 1 - 3 at repl.it <https://repl.it/@launchcode/FunctionsExercises03-05>`__

.. admonition:: Tip

   Use these sample strings for testing:

   a. ``'apple'``
   b. ``'LC101'``
   c. ``'Capitalized Letters'``
   d. ``'I love the smell of code in the morning.'``

Reverse Digits
---------------

2. The ``reverseCharacters`` function works great on strings, but what if the
   argument passed to the function is a number? Using
   ``console.log(reverseCharacters(1234));`` results in an error, since
   ``split`` only works on strings (TRY IT). When passed a number, we want the
   function to return a number with all the digits reversed (e.g. 1234 converts
   to 4321 and NOT the string ``"4321"``).

   a. Add an ``if`` statement to ``reverseCharacters`` to check the ``typeof`` the
      parameter.
   b. If ``typeof`` is 'string', return the reversed string as before.
   c. If ``typeof`` is 'number', convert the parameter to a string, reverse the
      characters, then convert it back into a number.
   d. Return the reversed number.
   e. Be sure to print the result returned by the function to verify that your code
      works for *both strings and numbers*. Do this before moving on to the
      next exercise.

.. admonition:: Tip

   Use these samples for testing:

   a. ``1234``
   b. ``'LC101'``
   c. ``8675309``
   d. ``'radar'``

Complete Reversal
------------------

3. Now we are ready to finish our complete reversal process. Create a new
   function with one parameter, which is the array we want to change. The
   function should:

   a. Define and initialize an empty array.
   b. Loop through the old array.
   c. For each element in the old array, call ``reverseCharacters`` to flip the
      characters or digits.
   d. Add the reversed string (or number) to the array defined in part 'a'.
   e. Return the final, reversed array.
   f. *Be sure to print the results from each test case in order to verify your
      code*.

.. admonition:: Tip

   Use this sample data for testing.

   .. list-table::
      :header-rows: 1

      * - Input
        - Output
      * - ``['apple', 'potato', 'Capitalized Words']``
        - ``['sdroW dezilatipaC', 'otatop', 'elppa']``
      * - ``[123, 8897, 42, 1138, 8675309]``
        - ``[9035768, 8311, 24, 7988, 321]``
      * - ``['hello', 'world', 123, 'orange']``
        - ``['egnaro', 321, 'dlrow', 'olleh']``

Bonus Missions
---------------

4. Define a function with one parameter, which will be a string. The function
   must do the following:

   a. Have a clear, descriptive name like ``funPhrase``.
   b. Retrieve only the last character from strings with lengths of 3 or less.
   c. Retrieve only the first 3 characters from strings with lengths larger
      than 3.
   d. Use a template literal to return the phrase ``We put the '___' in '___'.``
      Fill the first blank with the modified string, and fill the second blank
      with the original string.
   e. `Build your function at repl.it <https://repl.it/@launchcode/FunctionsExercises01>`__.

#. Now test your function:

   f. Outside of the function, define the variable ``str`` and initialize it
      with a string (e.g. ``'Functions rock!'``).
   g. Call your function and print the returned phrase.

#. The area of a rectangle is equal to its *length x width*.

   a. Define a function with the required parameters to calculate the area of a
      rectangle.
   b. The function should *return* the area, NOT print it.
   c. Call your area function by passing in two arguments - the length and
      width.
   d. If only one argument is passed to the function, then the shape is a
      square. Modify your code to deal with this case.
   e. Use a template literal to print, "The area is ____ cm^2."
   f. `Code the area function at repl.it <https://repl.it/@launchcode/FunctionsExercises02>`__.

.. admonition:: Tip

   Use these test cases.

   a. length = 2, width = 4 (area = 8)
   b. length = 14, width = 7 (area = 98)
   c. length = 20 (area = 400)
