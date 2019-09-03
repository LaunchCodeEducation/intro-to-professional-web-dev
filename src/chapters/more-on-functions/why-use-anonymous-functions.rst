Why Use Anonymous Functions?
============================

At this point, you may be asking yourself *Why am I learning anonymous
functions?* They seem strange, and their utility may not be immediately
obvious. While the opinions of programmers differ, there are two main reasons
why *we* think anonymous functions are important to understand.

Anonymous Functions Can Be Single-Use
-------------------------------------

There are many situations in which you will need to create a function that will
only be used once. To see this, recall one of our earlier examples.

.. admonition:: Example

   The anonymous function created in this example cannot be used outside of ``setTimeout``.

   .. sourcecode:: js
      :linenos:

      setTimeout(function () {
         console.log("The future is now!");
      }, 5000);

Defining an anonymous function at the same time it is passed as an argument
prevents it from being used elsewhere in the program.

Additionally, in programs that use lots of functions---such as web
applications, as you will soon learn---defining functions anonymously, and
directly within a function call, can reduce the number of names you need to
create.

Anonymous Functions Are Ubiquitous in JavaScript
------------------------------------------------

JavaScript programmers use anonymous functions *a lot*. Many programmers use
anonymous functions with the same gusto as that friend of yours who puts hot
sauce on *everything*.

Just because an anonymous function isn't needed to solve a problem doesn't mean
that it *shouldn't* be used to solve the problem. Avoiding JavaScript code that
uses anonymous functions is impossible.

Any programming problem in JavaScript can be solved *without* using anonymous
functions. Thus, the extent to which you use them in your own code is somewhat
a matter of taste. We will take the middle road throughout the rest of this
course, regularly using both anonymous and named functions.

Check Your Understanding
------------------------

.. admonition:: Question

   Explain the difference between named and anonymous functions,
   including an example of how an anonymous function can be used.
