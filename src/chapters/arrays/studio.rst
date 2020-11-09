Studio: Strings and Arrays
==========================

Strings are **ordered collections** of *characters*, which are strings of
length 1. The characters in a string can be accessed using
**bracket notation**.

Arrays are ordered collections of items, which can be strings, numbers,
other arrays, etc. The items/elements/entries stored in an array can be
accessed using bracket notation.

Strings are **immutable**, whereas arrays can be changed.

Strings and arrays have **properties** and **methods** that allow us to easily
perform some useful actions.

Before You Start
----------------

If you are enrolled in a LaunchCode program, access this studio by following the repl.it classroom links posted in your class at `learn.launchcode.org <https://learn.launchcode.org/>`_.

If you are working through this material on your own, use the repl.it links contained on this page.

String Modification
-------------------

Use string methods to convert a word into pseudo-pig latin.

a. Remove the first three characters from a string and add them to the end.
   Ex: ``'LaunchCode'`` becomes ``'nchCodeLau'``. Use a template literal to
   print the original and modified string in a descriptive phrase.
b. Modify your code to accept user input. Query the user to enter the
   number of letters that will be relocated.
c. Add validation to your code to deal with user inputs that are longer than the
   word. In such cases, default to moving 3 characters. Also, the template
   literal should note the error.

`Code it at repl.it <https://repl.it/@launchcode/StringandArrayStudio01>`__

Array and String Conversion
----------------------------

The ``split`` and ``join`` methods convert back and forth between strings
and arrays. Use **delimiters** as reference points to split a string into an
array, then modify the array and convert it back to a printable string.

a. For a given string, use the ``includes`` method to check to see if the
   words are separated by commas (``,``), semicolons (``;``) or just spaces.
b. If the string uses commas to separate the words, ``split`` it into an array,
   reverse the entries, and then ``join`` the array into a new comma separated
   string. For example, ``"up,to,code,fun"`` becomes ``"fun,code,to,up"``.
c. If the string uses semicolons to separate the words, ``split`` it into an
   array, alphabetize the entries, and then ``join`` the array into a new
   hyphen separated string. For example, ``"up;to;code;fun"`` becomes
   ``"code-fun-to-up"``.
d. If the string uses spaces to separate the words, ``split`` it into an array,
   reverse alphabetize the entries, and then ``join`` the array into a new
   space separated string. For example, ``"to code up fun"`` becomes
   ``"up to fun code"``.
e. *Consider*: What if the string uses 'comma spaces' (, ) to separate the
   list? Modify your code to produce the same result as part "b", making sure
   that the extra spaces are NOT part of the final string.

`Code it at repl.it <https://repl.it/@launchcode/StringandArrayStudio02>`__

Bonus Mission: Multi-dimensional Arrays
---------------------------------------

Arrays can store other arrays!

a. The cargo hold in our shuttle contains several smaller storage spaces. Use
   ``split`` to convert the following strings into four cabinet arrays.
   Alphabetize the contents of each cabinet.

   i. ``"water bottles, meal packs, snacks, chocolate"``
   ii. ``"space suits, jet packs, tool belts, thermal detonators"``
   iii. ``"parrots, cats, moose, alien eggs"``
   iv. ``"blankets, pillows, eyepatches, alarm clocks"``

b. Initialize a ``cargoHold`` array and add the cabinet arrays to it. Print
   ``cargoHold`` to verify its structure.
c. Query the user to select a cabinet (0-3) in the ``cargoHold``.
d. Use bracket notation and a template literal to display the contents of
   the selected cabinet. If the user entered an invalid number, print an
   error message instead.
e. *Bonus to the Bonus*: Modify the code to query the user for BOTH a cabinet in
   ``cargoHold`` AND a particular item. Use the ``includes`` method to check
   if the cabinet contains the selected item, then print ``"Cabinet ____
   DOES/DOES NOT contain ____."``

`Code it at repl.it <https://repl.it/@launchcode/StringandArrayStudio03>`__
