Input with ``readline-sync``
=============================

``console.log`` works fine for printing static (unchanging) messages to the
screen. If we wanted to print a phrase greeting a specific user, then
``console.log("Hello, Dave.");`` would be OK as long as Dave is the actual
user.

What if we want to greet someone else? We could change the string inside the
``()`` to be ``'Hello, Sarah'`` or ``'Hello, Elastigirl'`` or any other name we
need. However, this is inefficient. Also, what if we do not know the name of
the user beforehand? We need to make our code more general and able to respond
to different conditions.

It would be great if we could ask the user to enter a name, store that string
in a variable, and then print a personalized greeting using ``console.log``.
Variables to the rescue!

Requesting Data
----------------

.. index:: ! input

.. index:: ! prompt

To personalize the greeting, we have to get **input** from the user. This
involves displaying a **prompt** on the screen (e.g. "Please enter a number:
"), and then waiting for the user to respond. Whatever information the user
enters gets stored for later use.

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

In line 1 ``const input = require(`readline-sync`)`` pulls in all the functions
that allow us to get data from the user and assigns them to the variable
``input``.

Recall that ``const`` ensures that ``input`` cannot be changed.

How to Prompt the User
^^^^^^^^^^^^^^^^^^^^^^^

To display a prompt and wait for a response, we use the following syntax:
``let info = input.question("Question text... ");``.

When JavaScript evaluates the expression, it follows the instructions:

#. Display ``Question text`` on the screen.
#. Wait for the user to respond.
#. Store the data in the variable ``info``.

For our greeting program, we would code
``let name = input.question("Enter your name: ");``. The user enters a name and
presses the Return or Enter key. When this happens, any text entered is
collected by the input function and stored in ``name``.

.. admonition:: Try It

   Let's play around with the ``input`` statement. Open the repl.it link below
   and click the "Run" button.

   .. replit:: js
      :slug: InputExamples01
      :linenos:

      const input = require(`readline-sync`);

      let name = input.question("Enter your name: ");

Note that after entering a name, the program does not actually DO anything with
the information. If we want to print the data as part of a message, we need to
put ``name`` inside a ``console.log`` statement.

After line 3, add ``console.log("Hello, " + name + "!");``, then run the
code several times, trying different responses to the input prompt.

By storing the user's name inside ``name``, we gain the ability to hold onto
the data and use it when and where we see fit.

Try adding another ``+ name`` term inside the ``console.log`` statement and see
what happens. Next, add code to prompt the user for a second name. Store the
response in ``otherName``, then print both names using ``console.log``.

.. admonition:: Try It

   Update your code to request a user's first and last name, then print an
   output that looks like:

   ::

      First name: Elite
      Last name: Coder
      Last, First: Coder, Elite

Critical Input Detail
----------------------

There is one very important quirk about the input function that we need to
remember. Given ``console.log(7 + 2);``, the output would be ``9``.

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

The quirk with the ``input`` function is that it *treats all entries as
strings*, so numbers get concatenated rather than added.  Just like
"Hello, " + "World" outputs as ``Hello, World``, "7" + "2" outputs as ``72``.

   JavaScript treats input entries as strings!

If we want our program to perform math on the entered numbers, we must
:ref:`use type conversion <type-conversion>` to change the string values into
numbers.

.. admonition:: Try It

   #. Use ``Number`` to convert ``num1`` and ``num2`` from strings to numbers.
      Run the program and examine the result.
   #. Instead of using two steps to assign ``num1`` and then convert it, combine
      the steps in line 3. Place ``input.question("Enter a number: ")`` inside
      the ``Number`` function. Run the program and examine the result.
   #. Repeat step 2 for ``num2``
   #. What happens if a user enters ``Hi`` instead of a number?

Check Your Understanding
------------------------

.. admonition:: Question

   What is printed when the following program runs?

   .. sourcecode:: js
      :linenos:

      const input = require(`readline-sync`);

      let info = input.question("Please enter your age: ");
      //The user enters 25.

      console.log(typeof info);

   #. ``string``
   #. ``number``
   #. ``info``
   #. ``25``
