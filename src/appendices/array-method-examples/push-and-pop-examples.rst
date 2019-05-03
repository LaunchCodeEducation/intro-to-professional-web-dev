.. _push-and-pop-examples:

**push** And **pop** Examples
==============================

**push**
---------

The general syntax for this method is:

::

   arrayName.push(item1, item2, ...)

This method adds one or more items to the END of an array and returns the
new length.

The new items may be of any data type.

.. admonition:: Example

   .. sourcecode:: js

      let arr = ['a', 'b', 'c'];

      arr.push('d', 'f', 42);
      //returns 6

      console.log(arr);
      //prints ['a', 'b', 'c', 'd', 'f', 42]

.. _pop:

**pop**
--------

The general syntax for this method is:

::

   arrayName.pop()

This method removes and returns the LAST element in an array.

No arguments are placed inside the parentheses ``()``.

.. admonition:: Example

   .. sourcecode:: js

      let arr = ['a', 'b', 'c', 'd', 'e'];

      arr.pop();
      //returns 'e'

      console.log(arr);
      //prints ['a', 'b', 'c', 'd']
