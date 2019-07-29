.. _slice-examples:

``slice`` Examples
==================

The general syntax for this method is:

.. sourcecode:: js

   arrayName.slice(starting index, ending index)

This method copies a range of elements from one array into a new array. ``slice``
does NOT change the original array, but returns a new array.

The ending index is optional.  If it is left out, ``slice`` returns a new array
that includes everything from the starting index to the end of the original
array.

If both indices are used, the new array contains everything from the starting
index up to, but NOT including the ending index.

.. admonition:: Example

   .. sourcecode:: js
      :linenos:

      let arr = ['a', 'b', 'c', 'd', 'e'];

      arr.slice(2);

      arr.slice(1,4);

      console.log(arr);

   **Output**

   ::

      [ 'c', 'd', 'e' ]
      [ 'b', 'c', 'd' ]
      ['a', 'b', 'c', 'd', 'e']

