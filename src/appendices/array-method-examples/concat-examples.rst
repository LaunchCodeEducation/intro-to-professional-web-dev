.. _concat-examples:

``concat`` Examples
====================

The general syntax for this method is:

.. sourcecode:: bash

   arrayName.concat(otherArray1, otherArray2, ...)

This method adds the elements of one array to the end of another. The new array
must be stored in a variable or printed to the screen, because ``concat`` does
NOT alter the original arrays.

.. admonition:: Example

   .. sourcecode:: js
      :linenos:

      let arr = [1, 2, 3];
      let otherArray = ['M', 'F', 'E'];
      let newArray = [];

      newArray = arr.concat(otherArray);
      console.log(newArray);

      newArray = otherArray.concat(arr);
      console.log(newArray);

      console.log(arr.concat(otherArray, arr));

      console.log(arr);

   **Output**

   ::

      [1, 2, 3, 'M', 'F', 'E']
      [ 'M', 'F', 'E', 1, 2, 3 ]
      [ 1, 2, 3, 'M', 'F', 'E', 1, 2, 3 ]
      [1, 2, 3]