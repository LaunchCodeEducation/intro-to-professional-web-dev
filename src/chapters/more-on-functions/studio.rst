Studio: More Functions
==========================

Sort Numbers For Real
----------------------

Recall that using the ``sort`` method on an array of numbers
:ref:`produced an unexpected result <sort-examples>`, since JavaScript converts
the numbers to strings by default. Let's fix this!

Here is one approach to sorting an array:

#. Find the minimum value in an array,
#. Add that value to a new array,
#. Remove the entry from the old array,
#. Repeat steps 1 - 3 until the numbers are all in order.

Part A: Find the Minimum Value
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Create a function with an array of numbers as its parameter. The function
should iterate through the array and return the minimum value from the
array. 

*Hint*: Use what you know about ``if`` statements to identify and
store the smallest value within the array.

.. tip::

   Use this sample data for testing.

   .. sourcecode:: js
      :linenos:

      [ 5, 10, 2, 42 ]
      [ -2, 0, -10, -44, 5, 3, 0, 3 ]
      [ 200, 5, 4, 10, 8, 5, -3.3, 4.4, 0 ]

`Code studio part A at repl.it <https://repl.it/@launchcode/MoreFuncsStudio01>`__.

Part B: Create a New Sorted Array
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Create another function with an array of numbers as its parameter. Within
this function:

a. Define a new, empty array to hold the final sorted numbers.
b. Use your function from the previous exercise to find the minimum value in
   the old array.
c. Add the minimum value to the new array, and remove the minimum value from
   the old array.
d. Repeat parts b & c until the old array is empty.
e. Return the new sorted array.
f. *Be sure to print the results in order to verify your code*.

`Code studio part B at repl.it <https://repl.it/@launchcode/MoreFuncsStudio02>`__.

.. tip:: *Which type of loop?*

   Either a ``for`` or ``while`` loop will work inside this function, but one
   IS a better choice. Consider what the function must accomplish vs. the
   behavior of each type of loop. Which one best serves if the array has an
   unknown length?

More on Sorting Numbers
------------------------

The sorting approach used above is an example of a *selection sort*. The
function repeatedly checks an array for the minimum value, then places that
value into a new container.

Selection sorting is NOT the most efficient way to accomplish the task, since
it requires the function to pass through the array once for each item within
the array. This takes way too much time for large arrays.

Fortunately, JavaScript has an elegant way to properly sort numbers.

.. tip::

   Here is a nice, visual comparison of `different sorting methods <https://www.toptal.com/developers/sorting-algorithms>`__.

   Feel free to Google "bubble sort JavaScript" to explore a different way to
   order numbers in an array.

.. _js-sort-numbers:

Part C: Number Sorting the Easy Way
------------------------------------

If you Google "JavaScript sort array of numbers" (or something similar), many
options appear, and they all give pretty much the same result. The sites just
differ in how much detail they provide when explaining the solution.

One reference is here: `W3Schools <https://www.w3schools.com/jsref/jsref_sort.asp>`_.

End result: the JavaScript syntax for numerical sorting is
``arrayName.sort(function(a, b){return a-b});``.

Here, the anonymous function determines which element is larger and swaps the
positions if necessary. This is all that ``sort`` needs to order the entire
array.

Using the sytax listed above:

a. Sort each sample array in increasing order.
b. Sort each sample array in decreasing order.
c. Does the function alter ``arrayName``?
d. Did your sorting function from part B alter ``arrayName``?

`Code studio part C at repl.it <https://repl.it/@launchcode/MoreFuncsStudio03>`__.

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

Bonus Mission
--------------

Refactor your sorting function from Part B to use recursion.
