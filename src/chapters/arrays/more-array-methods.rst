More Array Methods
==================

To continue our review of methods, here are some that are useful but not used
as frequently as ``includes``, ``indexOf``, ``length``, ``reverse`` and
``sort``.

.. list-table:: Removal Methods
   :header-rows: 1

   * - Methods That Remove Items
     - Description & ``Syntax``
     - Examples
   * - ``pop``
     - | ``arrayName.pop()``
       |
       | Removes and returns the LAST element in an array.
       |
       | No arguments are placed inside the parentheses ``()``.
     -
         .. sourcecode:: js

            let arr = ['a', 'b', 'c', 'd', 'e'];
            arr.pop();
            //returns 'e'

            console.log(arr);
            //prints ['a', 'b', 'c', 'd']

   * - ``shift``
     - | ``arrayName.shift()``
       |
       | Removes and returns the FIRST element in an array.
       |
       | No arguments are placed inside the parentheses ``()``.
     -
         .. sourcecode:: js

            let arr = ['a', 'b', 'c', 'd', 'e'];
            arr.shift();
            //returns 'a'

            console.log(arr);
            //prints ['b', 'c', 'd', 'e']

.. list-table:: Addition Methods
   :header-rows: 1

   * - Methods That Add Items
     - Description & ``Syntax``
     - Examples
   * - ``push``
     - | ``arr.push(item1, item2, ...)``
       |
       | Adds one or more elements to the END of an array and returns the new length.
       |
       | The new items may be of any data type.
     -
         .. sourcecode:: js

            let arr = ['a', 'b', 'c'];

            arr.push('d e', 'f', 42);
            //returns 6

            console.log(arr);
            //prints ['a', 'b', 'c', 'd e', 'f', 42]

   * - ``unshift``
     - | ``arr.unshift(item1, item2, ...)``
       |
       | Adds one or more elements to the START of an array and returns the new length.
       |
       | The new items may be of any data type.
     -
         .. sourcecode:: js

            let arr = ['a', 'b', 'c'];

            arr.unshift('hello', 121);
            //returns 5

            console.log(arr);
            //prints ['hello', 121, 'a', 'b', 'c']

.. list-table:: Array Creation Methods
   :header-rows: 1

   * - Methods That Create New Arrays
     - Description & ``Syntax``
     - Examples
   * - ``concat``
     - | ``arrayName.concat(otherArray1, otherArray2, ...)``
       |
       | Combines two or more arrays and returns the result as a new array.
     - ``concat`` examples are explored below.

   * - ``slice``
     - | ``arr.slice(starting index, ending index)``
       |
       | Returns selected entries of an array into a new array.
     - ``slice`` examples are explored below.

**concat** Examples
-------------------

The general syntax for this method is:

::

   arrayName.concat(otherArray1, otherArray2, ...)

This method adds the elements of one array to the end of another. The new array
must be stored in a variable or printed to the screen, because ``concat`` does
NOT alter the original arrays.

.. sourcecode:: js

   let arr = [1, 2, 3];
   let otherArray = ['M', 'F', 'E'];
   let newArray = [];

   newArray = arr.concat(otherArray);
   console.log(newArray);
   //prints [1, 2, 3, 'M', 'F', 'E']

   newArray = otherArr.concat(arr);
   console.log(newArray);
   //prints [ 'M', 'F', 'E', 1, 2, 3 ]

   console.log(arr.concat(otherArr, arr));
   //prints [ 1, 2, 3, 'M', 'F', 'E', 1, 2, 3 ]

   console.log(arr);
   //prints [1, 2, 3]

**slice** Examples
-------------------

The general syntax for this method is:

::

   arrayName.slice(starting index, ending index)

The ending index is optional.  If it is left out, ``slice`` returns a new array
that includes everything from the starting index to the end of the original array.

If both indices are used, the new array contains everything from the starting
index up to BUT NOT INCLUDING the ending index.

.. sourcecode:: js

   let arr = ['a', 'b', 'c', 'd', 'e'];

   arr.slice(2);
   //returns [ 'c', 'd', 'e' ]

   arr.slice(1,4);
   //returns [ 'b', 'c', 'd' ]
