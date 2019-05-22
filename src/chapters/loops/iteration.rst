Iteration
=========

.. index:: ! iteration

When repeating the same action over and over again, a human is likely to make a mistake. Computers, however, possess the incredible ability to carry out repetitive tasks without making mistakes. 

To see this, let's consider an appropriate, if somewhat contrived, example. Suppose you want to print out the integers 0 through 50. With the tools you currently have at your disposal, your program would look like this:

.. sourcecode:: js
   :linenos:

   console.log(0);
   console.log(1);
   console.log(2);
   console.log(3);
   console.log(4);
   // and so on...

Not only is this highly repetetive, but it is also error-prone. Even if utilizing copy-paste functionality, the sheer volume of code makes it somewhat likely that we will make a simple mistake, such as skipping an integer or misspelling ``console``.

This code is also hard to modify. If we want to make a conceptually simple change---such as printing all the way to 100, or only printing even numbers---then we are forced to update an immense amount of code. Programming languages provide tools that allow us to repeat a sequence of statements in a much simpler way.

.. index::
   single: loop; for
   single: loop; while

Repeated execution of a sequence of statements is called **iteration**. This chapter explores two mechanisms that JavaScript provides to make iteration simple and flexible---the ``for`` and ``while`` loops.

To give you a taste of what's to come, here is how we could write the program above using a ``for`` loop.

.. sourcecode:: js
   :linenos:

   for (let i = 0; i < 51; i++) {
      console.log(i);
   }

We will explore the details of this syntax shortly, but it's worth taking a moment to marvel at the simplicity of this program compared to the one above. 

.. note:: It may seem odd to you that this loop uses the integer 51, but only prints up to 50. Why this is the case will become clear in the next section.

.. _dry-code:

.. index:: ! DRY

Learning about iteration using loops is also an opportunity to introduce one of the most widely-known mnemonic devices in programming: *Don't Repeat Yourself*, or **DRY**. A common piece of advice from instructors and experienced programmers is that you should "keep your code DRY." Let's learn how. 
