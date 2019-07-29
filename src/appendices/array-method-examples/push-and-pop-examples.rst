.. _push-and-pop-examples:

``push`` And ``pop`` Examples
=============================

``push``
--------

The general syntax for this method is:

.. sourcecode:: js

   arrayName.push(item1, item2, ...)

This method adds one or more items to the END of an array and returns the
new length.

The new items may be of any data type.

.. admonition:: Example

   .. sourcecode:: js
      :linenos:

      let arr = ['a', 'b', 'c'];

      console.log(arr.push('d', 'f', 42));

      console.log(arr);

   **Output**

   ::

      6
      ['a', 'b', 'c', 'd', 'f', 42]

.. _pop:

``pop``
-------

The general syntax for this method is:

.. sourcecode:: js

   arrayName.pop()

This method removes and returns the LAST element in an array.

No arguments are placed inside the parentheses ``()``.

.. admonition:: Example

   .. sourcecode:: js
      :linenos:

      let arr = ['a', 'b', 'c', 'd', 'e'];

      arr.pop();

      console.log(arr);

   **Output**

   ::

      e
      ['a', 'b', 'c', 'd']
