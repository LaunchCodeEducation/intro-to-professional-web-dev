.. _array-methods:

Array Methods
==============

.. index::
   single: array; methods

As with strings, JavaScript provides us with useful **methods** for arrays.
These methods will either *alter* an existing array, *return* information about
the array, or *create and return* a new array.

Common Array Methods
--------------------

Here is a sample of the most frequently used array methods. More complete lists
can be found here:

#. `W3 Schools Array Methods <https://www.w3schools.com/jsref/jsref_obj_array.asp>`__
#. `MDN Web Docs <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array>`__

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
     - Reverses the order of the elements in an array.

   * - :ref:`sort <sort-examples>`
     - ``arrayName.sort()``
     - Arranges the elements of an array into increasing order (kinda).

.. list-table:: Methods That Add Or Remove Entries From An Array
   :header-rows: 1

   * - Method
     - Syntax
     - Description
   * - :ref:`pop <pop>`
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

   * - :ref:`unshift <unshift>`
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

Check Your Understanding
------------------------

Follow the links in the table above for the ``sort``, ``slice``, ``split`` and
``join`` methods. Review the content and then answer the following questions.

.. admonition:: Question

   What is printed by the following code?

   .. sourcecode:: javascript

      let charles = ['coder', 'Tech', 47, 23, 350];
      charles.sort();
      console.log(charles);

   a. ``[350, 23, 47, 'Tech', 'coder']``
   b. ``['coder', 'Tech', 23, 47, 350]``
   c. ``[23, 47, 350, 'coder', 'Tech']``
   d. ``[23, 350, 47, 'Tech', 'coder']``

.. admonition:: Question

   | Which statement converts the string ``str = 'LaunchCode students rock!'`` into the array
   | ``['LaunchCode', 'students', 'rock!']``?

   a. ``str.join(" ");``
   b. ``str.split(" ");``
   c. ``str.join("");``
   d. ``str.split("");``

.. admonition:: Question

   What is printed by the following program?

   .. sourcecode:: js

      let groceryBag = ['bananas', 'apples', 'edamame', 'chips', 'cucumbers', 'milk', 'cheese'];
      let selectedItems = [];

      selectedItems = groceryBag.slice(2, 5).sort();
      console.log(selectedItems);

   a. ``['chips', 'cucumbers', 'edamame']``
   b. ``['chips', 'cucumbers', 'edamame', 'milk']``
   c. ``['cheese', 'chips', 'cucumbers']``
   d. ``['cheese', 'chips', 'cucumbers', 'edamame']``
