.. _concat-examples:

**concat** Examples
====================

The general syntax for this method is:

::

   arrayName.concat(otherArray1, otherArray2, ...)

This method adds the elements of one array to the end of another. The new array
must be stored in a variable or printed to the screen, because ``concat`` does
NOT alter the original arrays.

.. admonition:: Example

   .. sourcecode:: js

      let arr = [1, 2, 3];
      let otherArray = ['M', 'F', 'E'];
      let newArray = [];

      newArray = arr.concat(otherArray);
      console.log(newArray);
      //prints [1, 2, 3, 'M', 'F', 'E']

      newArray = otherArr.concat(arr);
      console.log(newArray);
      //prints [ 'M', 'F', 'E', 1, 2, 3 ]

      console.log(arr.concat(otherArr, arr));
      //prints [ 1, 2, 3, 'M', 'F', 'E', 1, 2, 3 ]

      console.log(arr);
      //prints [1, 2, 3]
