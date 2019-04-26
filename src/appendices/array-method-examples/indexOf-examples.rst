.. _indexOf-examples:

**indexOf** Examples
=====================

The general syntax for this method is:

::

   arrayName.indexOf(item)

This method returns the index of the FIRST occurence of an item in the array.
If the item is not in the array, -1 is returned.

.. admonition:: Example

   .. sourcecode:: js

      let charles = [1, 7, 5, 9, 5];
      let otherArray = ['hello', 'world!'];

      charles.indexOf(5);
      //returns 2

      otherArray.indexOf('hi');
      //returns -1
