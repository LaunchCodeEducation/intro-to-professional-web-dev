Array Methods
==============

.. index::
   single: array; methods

As with strings, JavaScript provides us with useful **methods** for arrays.
Unlike strings, arrays are *mutable* and can be changed.

Some methods alter an array, while others *return* values. For example,
``console.log([1, 2, 3].includes(2))`` prints ``true``. The  action
``[1, 2, 3].includes(2)`` checks the array to see if it contains the item ``2``
and then *returns* a boolean which can be printed (or assigned to a variable).

Common Array Methods
--------------------

Here is a sample of the most frequently used array methods. More complete lists
can be found here:

#. Novice list: `W3 Schools Array Methods <https://www.w3schools.com/jsref/jsref_obj_array.asp>`__
#. More detailed list: `MDN Web Docs <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array>`__

To see detailed examples for a particular method, control-click
(or right-click) on its name.

.. list-table:: Methods That Return Information About The Array
   :header-rows: 1

   * - Method
     - Syntax
     - Description
   * - :ref:`includes <includes-examples>`
     - ``arrayName.includes(item)``
     - Checks if an array contains the specified item.

   * - :ref:`indexOf <indexOf-examples>`
     - ``arrayName.indexOf(item)``
     - Returns the index of the FIRST occurence of an item in the array. If the item is not in the array, -1 is returned.

.. list-table:: Methods That Rearrange The Entries In The Array
   :header-rows: 1

   * - Method
     - Syntax
     - Description
   * - :ref:`reverse <reverse-example>`
     - ``arrayName.reverse()``
     - Pretty straightforward. Reverses the order of the elements in an array.

   * - :ref:`sort <sort-examples>`
     - ``arrayName.sort()``
     - Arranges the elements of an array into increasing order (kinda).

.. list-table:: Methods That Add Or Remove Entries From An Array
   :header-rows: 1

   * - Method
     - Syntax
     - Description
   * - :ref:`pop <push-and-pop-examples>`
     - ``arrayName.pop()``
     - Removes and returns the LAST element in an array.

   * - :ref:`push <push-and-pop-examples>`
     - ``arrayName.push(item1, item2, ...)``
     - Adds one or more items to the END of an array and returns the new length.

   * - :ref:`shift <shift-and-unshift-examples>`
     - ``arrayName.shift()``
     - Removes and returns the FIRST element in an array.

   * - :ref:`splice <splice-examples>`
     - ``arrayName.splice(index, number, item1, item2, ...)``
     - Adds, removes or replaces one or more elements anywhere in the array.

   * - :ref:`unshift <shift-and-unshift-examples>`
     - ``arrayName.unshift(item1, item2, ...)``
     - Adds one or more items to the START of an array and returns the new length.

.. list-table:: Methods That Create New Arrays
   :header-rows: 1

   * - Method
     - Syntax
     - Description
   * - :ref:`concat <concat-examples>`
     - ``arr.concat(otherArray1, otherArray2, ...)``
     - Combines two or more arrays and returns the result as a new array.

   * - :ref:`join <join-examples>`
     - ``arr.join('connecter')``
     - Combines all the elements of an array into a string.

   * - :ref:`slice <slice-examples>`
     - ``arr.slice(start index, end index)``
     - Copies selected entries of an array into a new array.

   * - :ref:`split <split-examples>`
     - ``stringName.split('delimiter')``
     - Divides a string into smaller pieces, which are stored in a new array.
