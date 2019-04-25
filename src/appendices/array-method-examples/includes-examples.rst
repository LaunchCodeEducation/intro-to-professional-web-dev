**includes** Examples
=====================

The general syntax for this method is:

::

   arrayName.includes(item)

This method checks if an array contains the element specified in the
parentheses ``()``.

Returns ``true`` or ``false``.

.. admonition:: Example

   .. sourcecode:: js

      let charles = [1, 7, 5, 9, 5];
      let otherArr = ['hello', 'world!'];

      charles.includes(5);
      //returns true

      otherArr.includes('hi');
      //returns false
