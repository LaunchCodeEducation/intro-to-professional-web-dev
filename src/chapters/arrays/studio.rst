Strings & Arrays Studio
========================

Strings are **ordered collections** of *characters*, which are strings of
length 1. The characters in a string can be accessed using
**bracket notation**.

Arrays are ordered collections of items, which can be strings, numbers,
other arrays, etc. The items/elements/entries stored in an array can be
accessed using bracket notation.

Strings are **immutable**, whereas arrays can be changed.

Strings and arrays have **properties** and **methods** that allow us to easily
perform some useful actions.

String Modification
-------------------

1. Use string methods to convert a word into pseudo-pig latin.

   a. Remove the first three characters from a string and add them to the end.
      Ex: ``'LaunchCode'`` becomes ``'nchCodeLau'``. Use a template literal to
      print the original and modified string in a descriptive phrase.
   b. Modify your code to accept user input. Query the user to enter the
      number of letters that will be relocated.
   c. Add validation to your code to deal with user inputs that are longer than the
      word. In such cases, default to moving 3 characters. Also, the template
      literal should note the error.

Control+click (or right click) to: `Code it here <https://repl.it/@launchcode/StringandArrayStudio01>`__

Array and String Conversion
----------------------------

2. The ``split`` and ``join`` methods convert back and forth between strings
   and arrays. Use **delimiters** as reference points to split a string into an
   array, then modify the array and convert it back to a printable string.

   a. For a given string, use the ``includes`` method to check to see if the
      words are separated by commas (``,``), semicolons (``;``) or just spaces.
   b. If the string uses commas to separate the words, ``split`` it into an array, reverse
      the entries, and then ``join`` the array into a new comma separated
      string.
   c. If the string uses semicolons to separate the words, ``split`` it into an array,
      alphabetize the entries, and then ``join`` the array into a new comma
      separated string.
   d. If the string uses spaces to separate the words, ``split`` it into an array, reverse
      alphabetize the entries, and then ``join`` the array into a new space
      separated string.
   e. *Consider*: What if the string uses 'comma spaces' (, ) to separate the list? Modify your
      code to produce the same result as part "b", making sure that the extra
      spaces are NOT part of the final string.

`Code it here <https://repl.it/@launchcode/StringandArrayStudio02>`__

Multi-dimensional Arrays
-------------------------

3. Arrays can store other arrays!

   a. The cargo hold in our shuttle contains several smaller storage spaces. Use
      ``split`` to convert the following strings into four cabinet arrays.
      Alphebitize the contents of each cabinet.

      i. "water bottles, meal packs, snacks, chocolate"
      ii. "space suits, jet packs, tool belts, thermal detonators"
      iii. "parrots, cats, moose, alien eggs"
      iv. "blankets, pillows, eyepatches, alarm clocks"

   b. Initialize a ``cargoHold`` array and add the cabinet arrays to it. Print
      ``cargoHold`` to verify its structure.
   c. Query the user to select a cabinet (0-3) in the ``cargoHold``.
   d. Use bracket notation and a template literal to display the contents of
      the selected cabinet. If the user entered an invalid number, print an
      error message instead.
   e. *Bonus Mission*: Modify the code to query the user for BOTH a cabinet in
      ``cargoHold`` AND a particular item. Use the ``includes`` method to check
      if the cabinet contains the selected item, then print "Cabinet ____
      DOES/DOES NOT contain ____."

`Code it here <https://repl.it/@launchcode/StringandArrayStudio03>`__

Additional Ideas (Feedback Requested)
-------------------------------------

4. Practice using the ``split`` and ``join`` methods to convert between strings
   and arrays. We will also use other string or array methods in the process.

   a. The ``reverse`` method operates on arrays, but not on strings. Use this
      fact to reverse the order of characters in a string. Store the result in
      a new variable, then print the original and reversed string.
   b. **Palindromes** are words that have the same spelling forwards and backwards.
      For example, "soda" (ados) is NOT a palindrome, but "pop" (pop) and
      "radar" (radar) are.  Modify your code by adding an ``if`` statement to
      check if a word is a palindrome.  If the string is a palindrome, print,
      "___ is a palindrome!"  Otherwise, print, "___ is NOT a palindrome."
   c. Use string methods to enhance your code.  The palindrome check should NOT
      be case sensitive.  Ex: 'Dad' vs. 'daD' would be considered a match.
   d. *Bonus Mission*: What if the string is a phrase rather than a single word?
      Any spaces may throw off the check (e.g. ``'taco cat'`` is a palindrome,
      but a simple reversal produces the different string ``'tac ocat'``).
      Modify your code to deal with this spacing problem.

**Repl.it link**

5. Practice using the ``split`` and ``join`` methods to convert between strings
   and arrays. We will also use other string or array methods in the process.

   a. The ``reverse`` method operates on arrays, but not on strings. Use this
      fact to reverse the order of characters in a string. Store the result in
      a new variable, then print the original and reversed string.
   b. Use the ``trim`` method to remove leading/trailing whitespace to compare
      two usernames (strings).  Also, use an ``if`` statement and a template
      literal to print, " '___' and '___' are matching usernames!" Otherwise
      print, " '___' and '___' are NOT matching usernames."
   c. Use string methods to enhance your code.  The username check should NOT be
      case sensitive.  Ex: 'Dad' vs. 'dad' would be considered a match.
   d. What if we need to compare phrases that have inconsistent spacing between
      the words?  These spaces will throw off the check (e.g. ``'taco cat'``
      and ``'taco    cat'`` are the same phrase, but the ``===`` comparison
      returns ``false``).  Modify your code to deal with this spacing problem.

**Repl.it link**
