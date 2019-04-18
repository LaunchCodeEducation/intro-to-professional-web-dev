String Exercises
----------------

1. Identify what is returned for each of the following:

   a. 'JavaScript'[8]
   b. “Strings are sequences of characters.”[5]
   c. “Wonderful”.length
   d. "Do spaces count?".length

|

2. Consider the following variables:

   a. Explore and describe the difference between ``console.log(fruit,texture,carb)`` vs. string
      concatenation - ``console.log(fruit+texture+carb)``.
   b. Modify the string concatenation to make the two outputs match.

.. sourcecode:: javascript

   let fruit = 'banana';
   let texture = 'nut';
   let carb = 'bread';

Control+click (or right click) to: `Code it here <https://repl.it/@launchcode/StringExercises02/>`__

|

3. The ``.length`` method returns how many characters are in a string.
   However, the method will NOT give us the length of a number. If
   ``num = 1001``, ``num.length`` returns ``undefined`` rather than 4. Use type
   conversion to print the length (number of digits) of an integer.

`Code it here <https://repl.it/@launchcode/StringExercises03/>`__

|

4. Use string methods to do the following:

   a. Replace the first occurrence of 'a' in ``JavaScript`` with another letter.
      Print the result to confirm your code.
   b. Replace 'Java' in ``JavaScript`` with 'Rutabaga'.  Print the result and it's
      length.
   c. Find the index of 'd' in *"This is a really long phrase, and I do not want
      to count the characters to find the location of the first 'd' "*.  Then
      print, *"I do not want to count the characters to find the location of
      the first 'd' "* WITHOUT using ``console.log("I do not want to count the
      characters to find the location of the first 'd' ")``.

`Code it here <https://repl.it/@launchcode/StringExercises04/>`__

|

5. If we want to turn the string ``JavaScript`` into ``JS``, we might try
   ``.remove``. Unfortunately, there is no such method in JavaScript.  However,
   we can use our cleverness to achieve the same result.

   a. Use string concatenation and two ``.slice``'s to print ``JS`` from
      ``JavaScript``.
   b. Without using ``.slice``, use method chaining to accomplish the same
      thing.
   c. Use bracket notation and a template literal to print, *"The abbreviation for
      'JavaScript' is 'JS'."*

`Code it here <https://repl.it/@launchcode/StringExercises05/>`__

|

6. Some programming languages (like Python) include a ``title`` method to
   return a string with Every Word Capitalized (e.g. ``'title case'.title()``
   returns ``Title Case``).  JavaScript has no ``.title`` method, but that
   won't stop us! Use the string methods you know to print 'Title Case' from
   the string ``title case``.

`Code it here <https://repl.it/@launchcode/StringExercises06/>`__
