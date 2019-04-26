.. _shift-and-unshift-examples:

**shift** And **unshift** Examples
===================================

**shift**
---------

The general syntax for this method is:

::

   arrayName.shift()

This method removes and returns the FIRST element in an array.

No arguments are placed inside the parentheses ``()``.

.. admonition:: Example

   .. sourcecode:: js

      let arr = ['a', 'b', 'c', 'd', 'e'];

      arr.shift();
      //returns 'a'

      console.log(arr);
      //prints ['b', 'c', 'd', 'e']

**unshift**
-----------

The general syntax for this method is:

::

   arrayName.unshift(item1, item2, ...)

This method adds one or more items to the START of an array and returns the
new length.

The new items may be of any data type.

.. admonition:: Example

   .. sourcecode:: js

      let arr = ['a', 'b', 'c'];

      arr.unshift('hello', 121);
      //returns 5

      console.log(arr);
      //prints ['hello', 121, 'a', 'b', 'c']
