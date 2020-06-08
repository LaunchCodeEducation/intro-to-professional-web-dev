Categories of Errors
====================

It is useful to distinguish between categories of errors in order to quickly
identify and fix them. Each category manifests itself in a different way, and
some strategies may be more useful for certain types of errors.

Stages of JavaScript Execution
------------------------------

In order to understand programming errors it is useful to understand the two
stages of code execution.

Parsing
^^^^^^^

.. index:: ! code parsing

Before code can be run, it must first be parsed, or validated and prepared for
execution. This is known as the **parsing stage**, and you can think of it like
the pre-flight check for a plane or space craft. 

A lot of detailed, low-level tasks are carried out during this process, but it
is enough for us to understand that parsing verifies the syntax and structure
of the code.

.. _error-categories:

Execution
^^^^^^^^^

Once our code has been parsed, its syntax has been verified and the program is
ready to run. The **execution stage** is when the actions written into our
program---printing to the console, prompting the user for input, making
calculations, etc.---are actually carried out. You can think of this stage as
the plane taking flight. 

Syntax Errors
-------------

.. index:: syntax

JavaScript can only execute a program if the program is syntactically correct.
**Syntax** refers to the structure of a language (spoken, programming, or
otherwise) and the rules about that structure. For example, in English, a
sentence must begin with a capital letter and end with appropriate punctuation.

.. index::
   single: error; syntax

A **syntax error** is a violation of the formal rules for a given language.

.. admonition:: Examples

   this sentence contains a syntax error. 

   So does this one

For most readers of English, a few syntax errors are not a significant problem.
Our brains are often flexible enough to determine the intended meaning of a
sentence even if it contains one or more syntax errors.

Programming languages are not so forgiving. If there is a single syntax error anywhere in your program, JavaScript will display an error message and quit immediately. Since syntax is validated during the parsing stage, syntax errors are the first we see when running a program.

During the first few weeks of your programming career, you will probably spend a lot of time tracking down syntax errors. However, as you gain experience, you will make fewer errors, and you will find your errors faster.

.. admonition:: Try It!

   Find the syntax errors in the program.

   .. replit:: js
      :linenos:
      :slug: Syntax-Errors

      let day = Wednesday;
      console.log(day;


.. admonition:: Question

   What syntax errors did you find? What was the specific error message provided by JavaScript in each case?

Runtime Errors
--------------

.. index::
   single: error; runtime

.. index:: exception

The second category consists of **runtime errors**, so called because they do not appear until you run the program. These errors are also called **exceptions** because they usually indicate that something exceptional (and bad) has happened.

Runtime errors occur during the execution phase of a program, so we will only encounter them after the syntax of our program is completely correct.

A common runtime error occurs when we try to use a variable that has not been created yet. This can happen if you misspell the name of a variable, as the following example shows.

.. admonition:: Example

   .. sourcecode:: js
      :linenos:

      let firstName = "Jack";
      console.log(firstname);

   **Console Output**

   ::

      ReferenceError: firstname is not defined
         at evalmachine.<anonymous>:2:13
         at Script.runInContext (vm.js:107:20)
         at Object.runInContext (vm.js:285:6)
         at evaluate (/run_dir/repl.js:133:14)
         at ReadStream.<anonymous> (/run_dir/repl.js:116:5)
         at ReadStream.emit (events.js:189:13)
         at addChunk (_stream_readable.js:284:12)
         at readableAddChunk (_stream_readable.js:265:11)
         at ReadStream.Readable.push (_stream_readable.js:220:10)
         at lazyFs.read (internal/fs/streams.js:181:12)

The syntax of our program is correct, but when the program executes, an error occurs at line 2. We attempt to print the value of the variable ``firstname``, but such a variable does not exist.

Logic Errors
------------

.. index::
   single: error; logic

The third type of error is the **logic error**. If there is a logic error in your program, it will run successfully and not generate any error messages. However, the program will not work as intended.

The characteristic of logic errors is that the program you wrote is not the program you wanted. For example, say you want a program to calculate your daily earnings based on your weekly salary. You might try the following:

.. admonition:: Example

   .. sourcecode:: js
      :linenos:

      let weeklyPay = 600;

      let dailyEarnings = weeklyPay / 7;
      console.log(dailyEarnings);

   **Console Output**

   ::

      85.71428571428571

The result surprises you because you thought you were making at least $100 per day (you work Monday through Friday). According to this program, though, you are making about $85 per day. The error is a logic one because you divided your weekly pay by 7. It would have been more accurate to divide your weekly pay by 5, since that is how many days a week you come to work. 

Identifying logic errors can be tricky because unlike syntax and runtime problems, there are no error messages to help us identify the issue. We must examine the output of the program and work backward to figure out what it is doing wrong.

Check Your Understanding
------------------------

.. admonition:: Question

   Label each of the following as either a syntax, runtime, or logic error.

   #. Trying to use a variable that has not been defined.
   #. Leaving off a close parenthesis, ``)``, when calling ``console.log``.
   #. Forgetting to divide by 100 when printing a percentage amount.


   