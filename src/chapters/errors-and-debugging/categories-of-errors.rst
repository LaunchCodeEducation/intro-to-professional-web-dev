Categories of Errors
====================

It is useful to distinguish between categories of errors in order to identify and fix them more quickly. Each category of error manifests itself in a different way, and different strategies may be more useful for certain categories of errors.

Stages of JavaScript Execution
------------------------------

In order to understand programming errors it is useful to understand the two stages of code execution.

Parsing
^^^^^^^

.. index:: ! code parsing

Before code can be run, it must first be parsed, or validated and prepared for execution. This is known as the **parsing stage**, and you can think of it as the analog of a pre-flight check for a plane or space craft. 

A lot of detailed, low-level tasks are carried out during this process, but it is enough for us to understand that during parsing is when the syntax and structure of the code is evaluated.

Execution
^^^^^^^^^

Once our code has been parsed, its syntax has been verified as correct and the program is ready to run. The **execution stage** is the point at which the actions we have written into our program---printing output to the console, prompting the user for input, making calculations, etc.---are actually carried out. You can this of this stage as the analog of a plane taking flight. 

Syntax Errors
-------------

.. index:: syntax

JavaScript can only execute a program if the program is syntactically correct. **Syntax** refers to the structure of a language (spoken, programming, or otherwise) and the rules about that structure. For example, in English, a sentence must begin with a capital letter and end with appropriate punchation. 

.. index::
   single: error; syntax

A **syntax error** is a violation of the formal syntax rules for a given language.

.. admonition:: Example

   this sentence contains a syntax error. 
   
   So does this one

For most readers of English, a few syntax errors are not a significant problem. Our brains are often flexible enough to determine the intended meaning of a sentence even if it contains one more more syntax errors.

Programming languages are not so forgiving. If there is a single syntax error anywhere in your program, JavaScript will display an error message and quit immediately. Since syntax is validated during the parsing stage, syntax errors are the first we see when running a program.

During the first few weeks of your programming career, you will probably spend a lot of time tracking down syntax errors. However, as you gain experience, you will make fewer errors and you will also be able to find your errors faster.

.. admonition:: Try It!

   Find the syntax errors in the program.

   .. sourcecode:: js

      let day = Wednesday;
      console.log(day;

   `Run this program at repl.it <https://repl.it/@launchcode/Syntax-Errors>`_


.. admonition:: Question

   What syntax errors did you find? What was the specific error message provided by JavaScript in each case?

Runtime Errors
--------------

.. index::
   single: error; runtime

.. index:: exception

The second category of error is a **runtime error**, so called because the error does not appear until you run the program. These errors are also called **exceptions** because they usually indicate that something exceptional (and bad) has happened.

Runtime errors occur during the execution phase of a program. This means that we will only encounter a runtime error once the syntax of our program has been validated. We will only see runtime errors after we have fixed any syntax errors. 

A common runtime error occurs when we try to use a variable that has not been created yet. This can happen if you misspell the name of a variable, as the following example shows.

.. admonition:: Example

   .. sourcecode:: js
      :linenos:
   
      let firstName = "Jack";
      console.log(firstname);

   **Output**

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

The syntax of our program is correct, but when the program executes an error occurs when it reaches line 2. We attempt to print the value of the variable ``firstname``, but such a variable does not exist.

Logic Errors
------------

.. index::
   single: error; logic

The third type of error is the **logic error**. If there is a logic error in your program, it will run successfully in the sense that the computer will not generate any error messages. However, the program will not work as intended.

With a logic error, the problem is that the program you wrote is not the program you wanted to write. For example, say you were writing a program to calculate your daily earnings based on your weekly salary. You might write a program like the following:

.. admonition:: Example
   
   .. sourcecode:: js

      let weeklyPay = 600;

      let dailyEarnings = weeklyPay / 7;
      console.log(dailyEarnings);

   **Output**

   ::

      85.71428571428571

The result surprises you because you thought you were making at least $100 per day (you work Monday thru Friday). According to this program, though, you are making about $85 per day. The error is a logic one because you divided your weekly pay by 7. It would have been more accurate to divide your weekly pay by 5, since that is how many days a week you are actually working. 

Identifying logic errors can be tricky because it requires us to work backward by looking at the output of the program and trying to figure out what it is doing. There are no error messages to help us identify the issue.

Check Your Understanding
------------------------

.. admonition:: Question

   Label each of the following as either a syntax, runtime, or logic error.

   #. Trying to use a variable that has not been defined.
   #. Leaving off a close-parens, ``)``, when calling ``console.log``.
   #. Forgetting to divide by 100 when printing a percentage amount.


   