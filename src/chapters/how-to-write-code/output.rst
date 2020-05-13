Output With ``console.log``
===========================

In the :ref:`Hello World <hello-world>` section, you experimented with
displaying text on the screen. Technically, you sent the words to the
**console**, which is a simple window where the user can type commands or view
output. We used a print function without explicitly talking about how it works.
Let’s fix that now.

We *call* the print function using the syntax ``console.log()``. When the code
runs, we want it to tell the computer, *Please display what is inside the () on
the screen*. For us, the words are enough - we want to LOG the text to the
CONSOLE. However, the computer only understands binary or hexadecimal
instructions. We need the compiler to change the keywords *console* and *log*
into a format that the machine understands.

Examples
---------

Open the repl.it link in the example below, and note the difference between the
outputs:

.. replit:: js
   :slug: ConsoleLogExamples01
   :linenos:

   console.log('Hello, JavaScript.');
   console.log(2001);
   console.log("Spot", "the", "difference");
   console.log("Spot","the","difference");
   console.log('Launch' + 'Code');
   console.log("LaunchCode was founded in", 2013);

Observations line by line:

#. In the line 1, we print some text, which is surrounded by quotes.
#. In the line 2, we print a number. Note the absence of quote marks.
#. In line 3, we use three words, separated by commas, all within the same
   set of parentheses ``()``. When these three words print, they show up on
   the same line but separated by spaces.
#. The code in line 4 is just like line 3, only there are no spaces after the
   commas. How does this affect the output?
#. Line 5 also prints more words, but in this case the code uses ``+``
   instead of a comma. The result is to print the words without spaces in
   between.
#. Line 6 prints text and a number with a space in between.

Two Special Characters
-----------------------

One final observation for all of the examples above is that each time we use
``console.log``, a **newline** is inserted after the printed content. Think of
a newline as the same as hitting the Enter or Return key on your keyboard. The
cursor moves to the beginning of the next line.

For the computer, *newline* is an invisible character that is used to tell the
machine to move to the next line. It is possible to use this invisible
character with the special representation ``\n``.

.. admonition:: Try It

   Experiment with the newline character.

   .. replit:: js
      :slug: ConsoleLogExamples02
      :linenos:

      console.log("Some Programming Languages:");

      console.log("Python\nJavaScript\nJava\nC#\nSwift");

In addition to the newline character, there is also a special tab character,
``\t``. Go back to the eight examples above and experiment with using ``\t``
and ``\n``.
