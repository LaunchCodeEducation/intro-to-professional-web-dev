**slice** Examples
===================

The general syntax for this method is:

::

   arrayName.slice(starting index, ending index)

This method copies selected entries of an array into a new array. ``slice``
does NOT change the original array.

The ending index is optional.  If it is left out, ``slice`` returns a new array
that includes everything from the starting index to the end of the original
array.

If both indices are used, the new array contains everything from the starting
index up to BUT NOT INCLUDING the ending index.

.. admonition:: Example

   .. sourcecode:: js

      let arr = ['a', 'b', 'c', 'd', 'e'];

      arr.slice(2);
      //returns [ 'c', 'd', 'e' ]

      arr.slice(1,4);
      //returns [ 'b', 'c', 'd' ]

      console.log(arr);
      //prints ['a', 'b', 'c', 'd', 'e']
