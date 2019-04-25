Array Methods
==============

As with strings, JavaScript provides us with useful **methods** for arrays.
Unlike strings, arrays are *mutable* and can be changed.

Some methods alter an array, while others *return* values. For example,
``console.log(arrayName.length)`` prints the number of entries inside the
array. The ``arrayName.length`` action *returns* an integer, which can be
printed (or assigned to a variable).

Common Array Methods
--------------------

Here is a sample of the simplest and most frequently used array methods. More
complete lists can be found here:

#. Novice list: `W3 Array Methods <https://www.w3schools.com/jsref/jsref_obj_array.asp>`__
#. More detailed list: `MDN Web Docs <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array>`__

.. list-table:: Informational Methods
   :header-rows: 1

   * - Methods That Provide Information
     - Description & ``Syntax``
     - Examples
   * - ``includes``
     - | ``arrayName.includes(item)``
       |
       | Check if an array contains the element specified in the parentheses ``()``.
       |
       | Returns ``true`` or ``false``.
     -
         .. sourcecode:: js

            let charles = [1, 7, 5, 9, 5];
            let otherArr = ['hello', 'world!'];

            charles.includes(5);
            //returns true

            otherArr.includes('hi');
            //returns false


   * - ``indexOf``
     - | ``arrayName.indexOf(item)``
       |
       | Returns the index of the FIRST occurence of an item in the array. If the
         item is not in the array, -1 is returned.
     -
         .. sourcecode:: js

            let charles = [1, 7, 5, 9, 5];
            let otherArray = ['hello', 'world!'];

            charles.indexOf(5);
            //returns 2

            otherArray.indexOf('hi');
            //returns -1


   * - ``length``
     - | ``arrayName.length``
       |
       | This is a **property** rather than a method.  It returns the number of elements in an array.
     -
         .. sourcecode:: js

            let charles = [1, 7, 5, 9, 5];

            charles.length;
            //returns 5

.. list-table:: Rearranging Methods
   :header-rows: 1

   * - Methods That Rearrange Items
     - Description & ``Syntax``
     - Examples
   * - ``reverse``
     - | ``arrayName.reverse()``
       |
       | Pretty straightforward. Reverses the order of the elements in an array.
       |
       | No arguments are placed inside the parentheses ``()``.
     -
         .. sourcecode:: js

            let arr = ['At', 'banana', 'orange', 'apple', 'zoo'];

            arr.reverse();
            console.log(arr);
            //prints [ 'zoo', 'apple', 'orange', 'banana', 'At' ]


   * - ``sort``
     - | ``arrayName.sort()``
       |
       | Arranges the elements of an array into increasing order (kinda).
       |
       | No arguments are placed inside the parentheses ``()``.
     - ``sort`` examples are explored below.

**sort** Examples
-----------------

The general syntax for this method is:

::

  arrayName.sort()

This method arranges the elements of an array into increasing order.  For
strings, this means alphabetical order.  HOWEVER, the results are not always
what we expect.

#. Alphabetical order.

   .. sourcecode:: js

      let letters = ['f', 'c', 'B', 'X', 'a'];

      letters.sort();
      console.log(letters);
      //prints [ 'B', 'X', 'a', 'c', 'f' ]

From the alphabet song, we know that 'a' comes before 'B' (and certainly before
'X'), but JavaScript treats capital and lowercase letters differently.  The
default sort order places capital letters before lowercase.

2. When numbers and strings are sorted, the default order places numbers before
   all letters.

   .. sourcecode:: js

      let mixed = ['a', 'A', 20, 40];

      mixed.sort();
      console.log(mixed);
      //prints [ 20, 40, 'A', 'a' ]

#. Numerical sorting.

   .. sourcecode:: js

      let numbers = [2, 8, 10, 400, 30];

      numbers.sort();
      console.log(numbers);
      //prints [ 10, 2, 30, 400, 8 ]

Here JavaScript gets truly bizarre. How is 8 larger than 400?

When JavaScript sorts, it converts all entries into strings by default. Just
like 'Apple' comes before 'Pear' because 'A' comes before 'P', the string '400'
begins with a '4' which comes before any string starting with an '8'. Looking
only at the first digit in each number, we see the expected progression
(1, 2, 3, 4, 8).

Later in this course, we will explore ways to fix this issue and correctly sort
numerical arrays.
