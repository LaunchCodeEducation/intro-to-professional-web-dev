Making A Function Call Itself
==============================

Congratulations! Identifying the base case is often the trickiest part of
building a recursive function.

We've made it this far with ``combineEntries``:

.. sourcecode:: js

   function combineEntries(arrayName){
      if (arrayName.length === 1){
         return arrayName[0];
      } else {
         //solve next small step
         //call combineEntries again
      }
   }

Now we are ready to take the next step.

A Visual Representation
------------------------

For arrays with more than one entry, we need to make ``combineEntries``
consider the first element and then *check what is left in the array*. If the
rest of the array contains more than one item, ``combineEntries`` calls iteslf
again and repeats the process with a smaller set of entries.

To help us visualize what's going on, let's start with the base case ``['L']``:

.. figure:: figures/base-case-recursion.png
   :alt: Visual representation for the base case.

Nothing complicated here.  ``combineEntries`` sees only one item in the array,
so it returns ``'L'``.

Now let's consider an array with two elements ``['L', 'C']``:

.. figure:: figures/second-case-recursion.png
   :alt: Visual representation for the second-easiest case.

In this case, ``combineEntries`` executes the ``else`` statement. We have no
code for this yet, but we can still consider the logic:

a. ``combineEntries`` returns ``'L'`` and calls itself again to evaluate what is
   left inside the array (``['C']``).
b. When passed ``['C']``, which is the base case, ``combineEntries`` returns
   ``'C'``.
c. The strings ``'L'`` and ``'C'`` get combined and returned as the final
   result.

Next, let's consider an array with three elements ``['L', 'C', '1']``:

.. figure:: figures/third-case-recursion.png
   :alt: Visual representation for the third-easiest case.

As before, ``combineEntries`` executes the ``else`` statement, and we can
follow the logic:

a. ``combineEntries`` returns ``'L'`` and calls itself again to evaluate what is
   left inside the array (``['C', '1']``).
b. When passed ``['C', '1']``, ``combineEntries`` returns ``'C'`` and calls
   itself again to evaluate what is left inside the array (``['1']``).
c. When passed ``['1']``, which is the base case, ``combineEntries`` returns
   ``'1'``.
d. The strings ``'C'`` and ``'1'`` get combined and returned.
e. The strings ``'L'`` and ``'C1'`` get combined and returned as the final
   result.

As we make the array longer, ``combineEntries`` calls itself more times. Each
call evaluates a smaller and smaller section of the array until reaching the
base case. This sets up a series of return events - each one selecting a
single entry from the array. Rather than building ``'LC101'`` from left to
right, recursion constructs the string starting with the base case and
adding new characters to the front:

a. ``'1'``
b. ``'01'``
c. ``'101'``
d. ``'C101'``
e. ``'LC101'``

Looping Without **for** or **while**
-------------------------------------

So how do we code the ``else`` statement in ``combineEntries``? Recall the
requirements:

a. Make ``combineEntries`` consider the first element,
b. If the rest of the array has more than one entry, call ``combineEntries``
   with a smaller array.

Bracket notation takes care of part a: ``arrayName[0]``.

| For part b, remember that the :ref:`slice method <slice-examples>` returns
   selected entries from an array. To return everything BUT the first entry in
| ``arr = ['L', 'C', '1', '0', '1']``, use ``arr.slice(1)``.

Let's add the bracket notation and the ``slice`` method to our function:

.. sourcecode:: js

   function combineEntries(arrayName){
      if (arrayName.length === 1){
         return arrayName[0];
      } else {
         return arrayName[0]+combineEntries(arrayName.slice(1));
      }
   }

See it in action **here** (TODO: Repl.it link).

The full picture:

.. figure:: figures/Qualitative-recursion.png
   :alt: Visual representation of calling addEntry multiple times.

Check Your Understanding
-------------------------

ID the recursive statement when...
