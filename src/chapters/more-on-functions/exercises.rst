Exercises: Functions
=====================

Who Was That Masked Function?
------------------------------



Sort Numbers For Real
----------------------

Recall that using the ``sort`` method on an array of numbers produced an
unexpected result, since JavaScript converts the numbers to strings by default
(TODO - add reference to the ``sort`` example page).  Let's fix this!

3. Create a function with an array of numbers as its parameter. The function
   should iterate through the array and return the minimum value from the
   array. *Hint*: Use what you know about ``if`` statements to identify and
   store the smallest value within the array.

.. admonition:: Sample arrays for testing

   .. sourcecode:: js

      [ 5, 10, 2, 42 ]
      [ -2, 0, -10, -44, 5, 3, 0, 3 ]
      [ 200, 5, 4, 10, 8, 5, -3.3, 4.4, 0 ]

4. Create another function with an array of numbers as its parameter.  Within
   this function:

   a. Define a new, empty array to hold the final sorted numbers.
   b. Use your function from the previous exercise to find the minimum value in
      the old array.
   c. Add the minimum value to the new array, and remove the minimum value from
      the old array.
   d. Repeat parts b & c until the old array is empty.
   e. Return the new sorted array.

*Hint*: Either a ``for`` or ``while`` loop will work inside this function, but
there IS a better choice.  Consider the task the function must accomplish as
well as the characteristics of each type of loop. Which one best serves if the
array has an unknown length?

*Be sure to print the results in order to verify your code*.

[TODO: Add repl.it link.]

More on Sorting Numbers
------------------------

The sorting approach used above is not the only way of accomplishing the task,
nor is it the best. Details on why can be found **here** (TODO: link to
appendix). Feel free to look up "bubble sort" to explore a different way to
order numbers in an array.

Fortunately, JavaScript has an elegant way to properly sort numbers.

If you Google "JavaScript sort array of numbers" (or something similar), many
options appear, and they all give pretty much the same result. The sites just
differ in how much detail they provide when explaining the solution.

One reference is here: `W3Schools <https://www.w3schools.com/jsref/jsref_sort.asp>`_.

End result - the JavaScript syntax for numerical sorting is
``arrayName.sort(function(a, b){return a-b});``.

.. admonition:: Note

   You do NOT need to understand HOW the sorting function works. You just need to
   be able to use it.

So Why Write A Sorting Function?
---------------------------------

Each programming language (Python, Java, C#, JavaScript, etc.) has built-in
sorting methods, so why did we ask you to build one?

It's kind of a programming right of passage - design an efficient sorting
function. Also, sorting can help you land a job.

As part of a tech interview, you will probably be asked to do some live-coding.
One standard, go-to question is to sort an array WITHOUT relying on the built
in methods. Knowing how to think though a sorting task, generate the code and
then clearly explain your approach will significantly boost your appeal to an
employer.
