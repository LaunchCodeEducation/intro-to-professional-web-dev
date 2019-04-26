.. _splice-examples:

**splice** Examples
====================

The general syntax for this method is:

::

   arrayName.splice(index, number of elements to change, item1, item2, ...)

Inside the parentheses ``()``, only the first argument is required.

The ``splice`` method modifies one or more elements anywhere in the array.
Entries can be added, removed or changed. This method requires practice.

Hang on, here we go:

.. admonition:: Example

   Given only one argument, ``splice(index)`` removes every entry from ``index``
   to the end of the array.

   .. sourcecode:: js

      let arr = ['a', 'b', 'c', 'd', 'e', 'f'];

      arr.splice(2);    //Everything from index 2 and beyond is removed.
      console.log(arr);
      //prints [ 'a', 'b' ]

.. admonition:: Example

   With two arguments, ``splice(index, number of items)`` starts at ``index``
   and removes the number of items.

   .. sourcecode:: js

      let arr = ['a', 'b', 'c', 'd', 'e', 'f'];

      arr.splice(2,3);    //Start at index 2 and remove 3 total entries.
      console.log(arr);
      //prints [ 'a', 'b', 'f' ]

      arr.splice(1,1);    //Start at index 1 and remove 1 entry.
      console.log(arr);
      //prints [ 'a', 'f' ]

.. admonition:: Example

   Given three or more arguments, ``splice(index, 0, new item)`` starts at
   ``index`` and *ADDS* the new items.

   .. sourcecode:: js

      let arr = ['a', 'b', 'c', 'd', 'e', 'f'];

      arr.splice(2,0,'hello');     //Start at index 2, remove 0 entries, and add 'hello'.
      console.log(arr);
      //prints [ 'a', 'b', 'hello', 'c', 'd', 'e', 'f' ]

.. admonition:: Example

   Given three or more arguments, ``splice(index, number of items, new items)``
   starts at ``index`` and *REPLACES* the number of items with the new ones.

   .. sourcecode:: js

      let arr = ['a', 'b', 'c', 'd', 'e', 'f'];

      arr.splice(2,3,'hello', 9);    //Start at index 2, replace 3 entries with 'hello' and 9.
      console.log(arr);
      //prints [ 'a', 'b', 'hello', 9, 'f' ]
