[str1, str2, str3] Studio (Strings & Arrays Studio)
---------------------------------------------------

Strings are **ordered collections** of **characters**, which are strings of
length 1. The characters in a string can be accessed using
**bracket notation**.

Arrays are ordered collections of elements, which can be strings, numbers,
other arrays, etc. The elements stored in an array can be accessed using
bracket notation.

Strings are **immutable**, whereas arrays can be changed.

Strings and arrays have **properties** and **methods** that allow us to easily
perform some useful actions.

1. Use string methods to convert a word into pseudo-pig latin.

   a. Remove the first three letters from a string and move them to the end.
      Ex: ``'LaunchCode'`` becomes ``'nchCodeLau'``. Use a template literal to
      print the original and modified string in a descriptive phrase.
   b. Modify your code to accept user input. Query the user to enter the
      number of letters that will be relocated.
   c. Add validation to your code to reject user inputs that are longer than the
      word.

Control+click (or right click) to: **Repl.it link**

|

2. Practice using the ``split`` and ``join`` methods to convert between strings
and arrays.  We can also use string methods in the process.

   a. The ``reverse`` method operates on arrays, but not on strings. Use this
      fact to reverse the order of characters in a string. Store the result in
      a new variable, then print the original and reversed string.
   b. Use the ``trim`` method to remove any leading/trailing whitespace to
      compare two usernames (strings).  Also, use an ``if`` statement and a
      template literal to print, " '___' and '___' are matching usernames!"
      Otherwise, print, " '___' and '___' are NOT matching usernames."
   c. Use string methods to enhance your code.  The username check should NOT
      be case sensitive.  Ex: 'Dad' vs. 'dad' would be considered a match.
   d. What if we need to compare phrases that have inconsistent spacing between
      the words?  These spaces will throw off the check (e.g. ``'taco cat'``
      and ``'taco    cat'`` are the same phrase, but the ``===`` comparison
      returns ``false``). Modify your code to deal with this spacing problem.

**Repl.it link**

|

3. Inventory task (multi-dim array).  Access and modify items?

   a. "stores" as individual arrays, each containing a list of numbers, strings
      and/or arrays.
   b. "franchise" as an array of the stores.
   c. Use bracket notation to access a store (e.g. franchise[2]) and check for
      an item (e.g. 'eggs') using the ``includes`` method.
   d. If found, print the store and item indices (e.g. "Store 1, index 3").
   e. Use this task as an introduction to the next big topic - loops?

**Repl.it link**
