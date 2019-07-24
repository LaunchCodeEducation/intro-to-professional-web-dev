.. _indexOf-examples:

``indexOf`` Examples
=====================

The general syntax for this method is:

.. sourcecode:: js

   arrayName.indexOf(item)

This method returns the index of the FIRST occurence of an item in the array.
If the item is not in the array, -1 is returned.

.. admonition:: Example

   .. sourcecode:: js
      :linenos:

      let charles = [1, 7, 5, 9, 5];
      let otherArray = ['hello', 'world!'];

      console.log(charles.indexOf(5));

      console.log(otherArray.indexOf('hi'));

   **Output**

   ::

      2
      -1
