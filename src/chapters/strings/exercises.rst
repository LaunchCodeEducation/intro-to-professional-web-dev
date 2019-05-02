Exercises: Strings
------------------

1. Identify the result for each of the following statements:

   a. ``'JavaScript'[8]``
   b. ``"Strings are sequences of characters."[5]``
   c. ``"Wonderful".length``
   d. ``"Do spaces count?".length``

|

2. The ``length`` method returns how many characters are in a string. However,
   the method will NOT give us the length of a number. If ``num = 1001``,
   ``num.length`` returns ``undefined`` rather than 4.

   a. Use type conversion to print the length (number of digits) of an integer.
   b. Print the number of digits in a DECIMAL value (e.g. ``num = 123.45`` has 5
      digits but a length of 6).
   c. What if ``num`` could be EITHER an integer or a decimal?  Add an ``if/else``
      statement so your code can handle both cases.  (Hint: Consider the
      ``indexOf()`` or ``includes()`` string methods).

Control+click (or right click) to: `Code it here <https://repl.it/@launchcode/StringExercises02/>`__

|

3. Remember, strings are *immutable*. Consider a string that represents a
   strand of DNA: ``dna = " TCG-TAC-gaC-TAC-CGT-CAG-ACT-TAa-CcA-GTC-cAt-AGA-GCT    "``.
   There are some typos in the string that we would like to fix:

   a. Use the ``trim()`` method to remove the leading and trailing whitespace,
      and then print the results.
   b. Change all of the letters in the dna string to UPPERCASE and print the
      result.
   c. Note that if you try ``console.log(dna)`` after applying the methods, the
      original, flawed string is displayed. To fix this, you need to
      *reassign* the changes back to ``dna``. Apply these fixes to your
      code so that ``console.log(dna)`` prints the DNA strand in UPPERCASE
      with no whitespace.

`Code it here <https://repl.it/@launchcode/StringExercises03/>`__

|

4. Let's use string methods to do more work on the DNA strand:

   a. Replace the gene ``'GCT'`` with ``'AGG'``, and then print the altered
      strand.
   b. Look for the gene ``'CAT'`` with ``indexOf()``. If found print, ``'CAT gene
      found'``, otherwise print, ``'CAT gene NOT found'``.
   c. Use ``slice()`` to print out the fifth gene (set of 3 characters) from
      the DNA strand.
   d. Use a template literal to print, ``"The DNA string is ___ characters long."``
   e. Just for fun, apply methods to ``dna`` and use another template literal to
      print, ``'taco cat'``.

`Code it here <https://repl.it/@launchcode/DNA-strings/>`__

|

5. If we want to turn the string ``'JavaScript'`` into ``'JS'``, we might try
   ``.remove()``. Unfortunately, there is no such method in JavaScript.
   However, we can use our cleverness to achieve the same result.

   a. Use string concatenation and two ``slice()``'s to print ``'JS'`` from
      ``'JavaScript'``.
   b. Without using ``slice()``, use method chaining to accomplish the same
      thing.
   c. Use bracket notation and a template literal to print, ``"The abbreviation for
      'JavaScript' is 'JS'."``
   d. Just for fun, try chaining 3 or more methods together, and then print the
      result.

`Code it here <https://repl.it/@launchcode/StringExercises05/>`__

|

6. Some programming languages (like Python) include a ``title()`` method to
   return a string with Every Word Capitalized (e.g. ``'title case'.title()``
   returns ``Title Case``).  JavaScript has no ``title()`` method, but that
   won't stop us! Use the string methods you know to print ``'Title Case'``
   from the string ``'title case'``.

`Code it here <https://repl.it/@launchcode/StringExercises06/>`__
