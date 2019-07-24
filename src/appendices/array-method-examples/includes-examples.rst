.. _includes-examples:

``includes`` Examples
=====================

The general syntax for this method is:

.. sourcecode:: js

   arrayName.includes(item)

This method checks if an array contains the item specified in the
parentheses ``()``, and returns ``true`` or ``false``.

.. admonition:: Example

   .. sourcecode:: js
      :linenos:

      let charles = [1, 7, 5, 9, 5];
      let otherArr = ['hello', 'world!'];

      console.log(charles.includes(5));

      console.log(otherArr.includes('hi'));

   **Output**

   .. sourcecode:: bash

      true
      false
