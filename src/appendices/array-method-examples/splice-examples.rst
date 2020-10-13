.. _splice-examples:

``splice`` Examples
===================

The general syntax for this method is:

::

   arrayName.splice(index, number of elements to change, item1, item2, ...);

Inside the parentheses ``()``, only the first argument is required.

The ``splice`` method modifies one or more elements anywhere in the array.
Entries can be added, removed, or changed. This method requires practice.

Hang on, here we go:

Removing Elements
-----------------

To remove elements from an array, the ``splice`` method needs 1 or 2 arguments.

#. Given only one argument, ``splice(index)`` removes every entry from
   ``index`` to the end of the array.

   .. admonition:: Example

      .. sourcecode:: js
         :linenos:

         let arr = ['a', 'b', 'c', 'd', 'e', 'f'];

         arr.splice(2);    //Everything from index 2 and beyond is removed.
         console.log(arr);

      **Output**

      ::

         ['a', 'b']

#. With two arguments, ``splice(index, number of items)`` starts at ``index``
   and removes the specified ``number of items`` from the array.

   .. admonition:: Example

      .. sourcecode:: js
         :linenos:

         let arr = ['a', 'b', 'c', 'd', 'e', 'f'];

         arr.splice(2,3);    //Start at index 2 and remove 3 total entries.
         console.log(arr);

         arr.splice(1,1);    //Start at index 1 and remove 1 entry.
         console.log(arr);

      **Output**

      ::

         [ 'a', 'b', 'f' ]
         [ 'a', 'f' ]

Adding or Replacing Elements
----------------------------

To add or replace elements in an array, the ``splice`` method requires 3 or
more arguments.

#. To add elements, set the ``number of elements`` argument to ``0`` and follow
   this with the new items.

   .. admonition:: Example

      ``splice(index, 0, new item)`` starts at ``index`` and *INSERTS* the new
      items. Existing elements get shifted further down the array.

      .. sourcecode:: js
         :linenos:

         let arr = ['a', 'b', 'c', 'd', 'e', 'f'];

         arr.splice(2,0,'hello');     //Start at index 2, remove 0 entries, and add 'hello'.
         console.log(arr);

      **Output**

      ::

         [ 'a', 'b', 'hello', 'c', 'd', 'e', 'f' ]

#. To replace elements in an array, the ``number of elements`` argument must
   be a positive integer. Follow this with the new items for the array.

   .. admonition:: Example

      ``splice(index, number of items, new items)`` starts at ``index`` and
      *REPLACES* the ``number of items`` with the new ones.

      .. sourcecode:: js
         :linenos:

         let arr = ['a', 'b', 'c', 'd', 'e', 'f'];

         arr.splice(2,3,'hello', 9);    //Start at index 2, replace 3 entries with 'hello' and 9.
         console.log(arr);

      **Output**

      ::

         [ 'a', 'b', 'hello', 9, 'f' ]
