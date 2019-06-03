Input with ``readline-sync``
=============================

``console.log`` works fine for printing static (unchanging) messages to the
screen. If we wanted to print a phrase greeting a specific user, then
``console.log("Hello, Dave.");`` would be OK as long as Dave is the actual
user.

What if we want to greet someone else? We can change the text inside the ``()``
to be 'Hello, Sarah,' or 'Hello, Elastigirl,' or any other name we need.
However, this is inefficient. Also, what if we do not know the name of the user
beforehand? We need to make the code more general and able to respond to
different conditions.

.. index:: ! input

.. index:: ! prompt

To do this, we can ask the user to enter a name, and then print that data using
``console.log``. We have to get **input** from the user. This involves
displaying a **prompt** on the screen (e.g. "Please enter a number: "), and
then waiting for the user to respond. Whatever information the user enters gets
stored for later use.

As we saw earlier, each programming language has its own way of accomplishing
the same task. For example, the Python syntax is ``input("Please enter your
name: ")``, while C# uses ``Console.ReadLine();``.

JavaScript also has a built-in module for collecting data from the user, called
``readline-sync``. Unfortunately, using this module requires more than a single
line of code.

Syntax
-------

Gathering input from the user requires the following setup:

.. sourcecode:: js
   :linenos:

   const input = require(`readline-sync`);

   let info = input.question("Question text... ");

There is a lot going on here behind the scenes, but for now you should follow
this bit of wisdom:

   I turn the key, and it goes.

Most of us do not need to know all the details about how cars, phones, or
microwave ovens work. We just know enough to interact with them in our day to
day lives. Similarly, we do not need to understand how ``readline-sync`` works
at this time. We just need to know enough to collect information from a user.

As you move through the course, you WILL learn about all of the pieces that fit
together to make this process work. For now, here is a brief overview.

Load the Module
^^^^^^^^^^^^^^^^

In line 1 ``require(`readline-sync`)`` pulls in all the functions that allow
us to get data from the user.

``input =`` assigns all of these functions to ``input``.

The meaning of ``const`` will be discussed in the next chapter.

How to Prompt the User
^^^^^^^^^^^^^^^^^^^^^^^

To display a prompt and wait for a response, we use the following syntax:
``input.question("Question text... ");``.

When JavaScript evaluates the expression, it follows the instructions:

#. Display ``Question text`` on the screen.
#. Wait for the user to respond.

For our greeting program, we would code ``input.question("Enter your name:
");``. The user enters a name and presses the Return or Enter key. When
this happens, any text entered is collected by the input function.

.. admonition:: Try It

   Let's play around with the ``input`` statement. Open the repl.it link below
   and click the "Run" button.

   .. replit:: js
      :slug: InputExamples01
      :linenos:

      const input = require(`readline-sync`);

      input.question("Enter your name: ");

Note that after entering a name, the program does not actually DO anything with
the information. If we want to print the data as part of a message, we need to
put it inside a ``console.log`` statement. ``input.question()`` can be used
just like any other sample of text.

Change line 3 to
``console.log("Hello, " + input.question("Enter your name: "));``, then run the
code several times, trying different responses to the input prompt. The program
collects the user's information first, and then prints the output.

Storing the Data for Later
^^^^^^^^^^^^^^^^^^^^^^^^^^^

As written, our code prompts the user for information just before that data
gets used. What if we need to collect input but use it at a later time?

JavaScript (and all other programming languages) allow us to store data inside
a container called a *variable*. Do not worry about the nitty-gritty technical
details here. In the next chapter we dive deep into the concepts behind data
and variables.

For now, let's assign a container called ``name`` to store the name entered by
the user. Modify your code as follows:

.. sourcecode:: js
   :linenos:

   const input = require(`readline-sync`);

   let name = input.question("Enter your name: ");

   console.log("Hello, " + name);

Run the new code several times, and try different responses to the input
prompt. Note how the code stores the data inside ``name``, and then recalls
that information by adding ``name`` to the ``console.log`` statement in line 5.

By storing the user's name inside ``name``, we gain the ability to hold onto
the data and use it when and where we see fit.

Try adding another ``+ name`` term inside the ``()`` in line 5 and see what
happens. Next, add code to line 4 to prompt the user for a second name. Store
the response in ``name2``, then print both names using the ``console.log``
statement.

Last Input Detail
------------------

There is one very important quirk about the JavaScript input function that you
need to understand. From an earlier example, we printed the sum of two numbers
using ``console.log(7 + 2);``. In this case, the output would be ``9``.

Now explore the following code, which prompts the user for two numbers and then
prints their sum:

.. replit:: js
   :slug: InputExamples02
   :linenos:

   const input = require(`readline-sync`);

   let num1 = input.question("Enter a number: ");
   let num2 = input.question("Enter another number: ");

   console.log(num1 + num2);

Run the program, enter your choice of numbers, and examine the output. Do you
see what you expected?

If we enter ``7`` and ``2``, we expect an output of ``9``.  We do NOT expect
``72``, but that is the result printed. What gives?!?!?

The quirk with the ``input`` function is that it *treats all entries as text*,
so numbers get combined rather than added.  Just like "Hello, " + "World"
outputs as ``Hello, World``, "7" + "2" outputs as ``72``.

   JavaScript treats input entries as text!

In the next chapter, we will learn how to make JavaScript treat a text input as
a numerical value.
