Why Use Anonymous Functions?
============================

At this point, you may be asking yourself why you are learning anonymous functions. They seem strange at first, and their utility is not immediately obvious. While the opinions of programmers differ, we will discuss the two main reasons that *we* think anonymous functions are useful.

Anonymous Functions Can Be Single-Use
-------------------------------------

There are many situations in which you will need to create a function that will only be used once. To see this, recall one of our earlier examples.

.. admonition:: Example

   Defining an anonymous function at the same time it is passed into another function prevents it from being used elsewhere in the program.

   .. sourcecode:: js
   
      setTimeout(function () {
         console.log("The future is now!");
      }, 5000);

In programs that use lots of functions---such as web applications, as you will soon learn---defining them anonymously and directy within a function call can reduce the number of names you need to come up with in your program. 

Anonymous Functions Are Ubiquitous in JavaScript
------------------------------------------------

Like it or not, JavaScript programmers use anonymous functions *a lot*. Many of them use anonymous functions with the same gusto that some people put ketchup or hot sauce on nearly everything they eat. For these programmers, just because an anonymous function isn't need to solve a problem doesn't mean that it *shouldn't* be used to solve the problem.

Any programming problem in JavaScript can be solved *without* using anonymous functions, so the extent to which you use them in your own code is somewhat a matter of taste. We will take the middle road throughout the rest of this course, regularly using both anonymous and named functions.

Check Your Understanding
------------------------

.. admonition:: Question

   Explain the difference between named and anonymous functions,
   including an example of how an anonymous function might be used.
