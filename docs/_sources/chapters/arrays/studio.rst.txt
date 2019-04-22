[str1, str2, str3] Studio
==========================

Strings are **ordered collections** of *characters*, which are strings of
length 1. The characters in a string can be accessed using
**bracket notation**.

Arrays are ordered collections of elements, which can be strings, numbers,
other arrays, etc. The elements stored in an array can be accessed using
bracket notation.

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

Control+click (or right click) to: **Repl.it link**

Array and String Conversion
----------------------------

2. Use methods ``split`` and ``join`` to convert back and forth between strings
   and arrays. Use delimiters to split a string into an array, then modify the
   array and convert it back to a printable string.

   a. Some task...
   b. Some follow-up task...
   c. Some final task...

**Repl.it link**

Multi-dimensional Arrays
-------------------------

3. Arrays can store other arrays!

   a. Use ``split`` to define and initialize the inventory for four cabinets
      inside the cargo hold. Alphebitize the contents of each cabinet.

      i. "water bottles, meal packs, snacks, chocolate"
      ii. "space suits, jet packs, tool belts, thermal detonators"
      iii. "parrots, cats, moose, alien eggs"
      iv. "blankets, pillows, eyepatches, alarm clocks"

   b. Initialize the ``cargoHold`` array and add the cabinet arrays to it. Print
      the ``cargoHold`` to verify its structure.
   c. Query the user to select a cabinet in the ``cargoHold`` (0-3).
   d. Use bracket notation and a template literal to display the contents of
      the selected cabinet.
   e. *Bonus Mission*: Modify the code to query the user for BOTH a cabinet in
      ``cargoHold`` AND a particular item. Use the ``includes`` method to check
      if the cabinet contains the selected item. Use a template literal to
      print "Cabinet ____ DOES/DOES NOT contain ____."

**Repl.it link**

Additional Ideas (Feedback Requested)
-------------------------------------

4. Practice using the ``split`` and ``join`` methods to convert between strings
   and arrays.  We can also use string methods in the process.

   a. The ``reverse`` method operates on arrays, but not on strings. Use this
      fact to reverse the order of characters in a string. Store the result in
      a new variable, then print the original and reversed string.
   b. **Palindromes** are words that have the same spelling forwards and backwards.
      For example, "soda" (ados) is NOT a palindrome, but "pop" (pop) and
      "radar" (radar) are.  Modify your code by adding an ``if`` statement to
      check if a word is a palindrome.  If the string is a palindrome, print,
      "___ is a palindrome!"  Otherwise, print, "___ is NOT a palindrome."
   c. Use string methods to enhance your code.  The username check should NOT
      be case sensitive.  Ex: 'Dad' vs. 'dad' would be considered a match.
   d. *Bonus Mission*: What if the string is a phrase rather than a single word?
      Any spaces may throw off the check (e.g. ``'taco cat'`` is a palindrome,
      but a simple reversal produces the different string ``'tac ocat'``).
      Modify your code to deal with this "space problem".

**Repl.it link**

5. Practice using the ``split`` and ``join`` methods to convert between strings
   and arrays.  We can also use string methods in the process.

   a. Reverse the order of characters in a string. Store the result in a new variable,
      then print the original and reversed string.
   b. Use the ``trim`` method to remove leading/trailing whitespace to compare
      two usernames (strings).  Also, use an ``if`` statement and template
      literal to print, " '___' and '___' are matching usernames!" Otherwise,
      print, " '___' and '___' are NOT matching usernames."
   c. Use string methods to enhance your code.  The username check should NOT be
      case sensitive.  Ex: 'Dad' vs. 'dad' would be considered a match.
   d. What if we need to compare phrases that have inconsistent spacing between
      the words?  These spaces will throw off the check (e.g. ``'taco cat'``
      and ``'taco    cat'`` are the same phrase, but the ``===`` comparison
      returns ``false``).  Modify your code to deal with this spacing problem.

**Repl.it link**
