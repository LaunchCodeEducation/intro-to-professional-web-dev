.. _shift-and-unshift-examples:

``shift`` And ``unshift`` Examples
==================================

``shift``
---------

The general syntax for this method is:

.. sourcecode:: js

   arrayName.shift()

This method removes and returns the FIRST element in an array.

No arguments are placed inside the parentheses ``()``.

.. admonition:: Example

   .. sourcecode:: js
      :linenos:

      let arr = ['a', 'b', 'c', 'd', 'e'];

      arr.shift();

      console.log(arr);

   **Output**

   ::

      'a'
      ['b', 'c', 'd', 'e']

.. _unshift:

``unshift``
-----------

The general syntax for this method is:

.. sourcecode:: js

   arrayName.unshift(item1, item2, ...)

This method adds one or more items to the START of an array and returns the
new length.

The new items may be of any data type.

.. admonition:: Example

   .. sourcecode:: js
      :linenos:

      let arr = ['a', 'b', 'c'];

      arr.unshift('hello', 121);

      console.log(arr);

   **Output**

   ::

      5
      ['hello', 121, 'a', 'b', 'c']
