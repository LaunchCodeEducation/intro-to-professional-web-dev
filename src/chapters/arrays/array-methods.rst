Array Methods
=============

As with strings, JavaScript provides us with useful **methods** for arrays.
Unlike strings, arrays are *mutable* and can be changed.

Some methods alter an array, while others *return* values. For example,
``console.log(arrayName.length)`` prints the number of entries inside the
array. The ``arrayName.length`` action *returns* an integer, which can be
printed (or assigned to a variable).

Common Array Methods
--------------------

Here is a summary of the most frequently used array methods. More complete
lists can be found here:

#. Novice list: `W3 Array Methods <https://www.w3schools.com/jsref/jsref_obj_array.asp>`__
#. More detailed list: `MDN Web Docs <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array>`__

.. list-table:: Informational Methods
   :header-rows: 1

   * - Methods That Provide Information
     - Description & *Syntax*
     - Examples
   * - ``includes``
     - | *arrayName.includes(item)*
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
     - | *arrayName.indexOf(item)*
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
     - | *arrayName.length*
       |
       | This is a **property** rather than a method.  It returns the number of elements in an array.
     -
         .. sourcecode:: js

            let charles = [1, 7, 5, 9, 5];

            charles.length;
            //returns 5

.. list-table:: Removal Methods
   :header-rows: 1

   * - Methods That Remove Items
     - Description & *Syntax*
     - Examples
   * - ``pop``
     - | *arrayName.pop()*
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
     - | *arrayName.shift()*
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
     - Description & *Syntax*
     - Examples
   * - ``push``
     - | *arr.push(item1, item2, ...)*
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
     - | *arr.unshift(item1, item2, ...)*
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

.. list-table:: Add, Remove or Modify
   :header-rows: 1

   * - Methods That Add or Remove Items
     - Description
     - Examples
   * - ``splice``
     - | Adds one or more elements to an array at a specified index.
       |
       | Removes one or more elements from an array at a specified index.
       |
       | Replaces one or more elements in an array with new items.
     - See below for syntax and examples of ``splice``.

.. list-table:: Rearranging Methods
   :header-rows: 1

   * - Methods That Rearrange Items
     - Description & *Syntax*
     - Examples
   * - ``reverse``
     - | *arrayName.reverse()*
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
     - | *arrayName.sort()*
       |
       | Arranges the elements of an array into increasing order (kinda).
       |
       | No arguments are placed inside the parentheses ``()``.
     - See below for examples of ``sort``.

.. list-table:: Array Creation Methods
   :header-rows: 1

   * - Methods That Create New Arrays
     - Description & *Syntax*
     - Examples
   * - ``join``
     - | *arr.join('element connecter')*
       |
       | Combines all the elements of an array into a string.
       |
       | The entry inside the parentheses ``()`` specifies the delimiter used to
         join the separate elements.
     -
         .. sourcecode:: js

            let arr = [1, 2, 3, 4];
            let words = ['hello', 'world', '!'];

            console.log(arr.join("+"));
            //prints '1+2+3+4'

            console.log(words.join(""));
            //prints 'helloworld!'

            console.log(words.join("_"));
            //prints 'hello_world_!'


   * - ``concat``
     - | *arrayName.concat(otherArray1, otherArray2, ...)*
       |
       | Combines two or more arrays and returns the result as a new array.
     - See below for examples of ``concat``.


   * - ``slice``
     - | *arr.slice(starting index, ending index)*
       |
       | Returns selected entries of an array into a new array.
     - See below for examples of ``slice``.

   * - ``split``
     - | *stringName.split('delimiter')*
       |
       | Divides a string into an array of smaller strings.
       |
       | The entry inside the parentheses ``()`` (the **delimiter**) determines
         how the string will be split.
     - See below for examples of ``split``.

Detailed Examples
-----------------

Some of the arrays listed above require a closer look. These examples are
arranged from least tricky to more tricky.

``concat``
++++++++++

*Syntax = arrayName.concat(otherArray1, otherArray2, ...)*

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

``split``
++++++++++

*Syntax = stringName.split('delimiter')*

``split`` is actually a string method, but it complements the array method
``join``.

``split`` divides a string into smaller pieces, which are stored in a new
array. The delimiter argument determines how the string is broken apart.

.. sourcecode:: js

   let numbers = "1,2,3,4";
   let word = "Rutabaga";
   let phrase = "Bookkeeper of balloons."
   let arr = [];

   arr = numbers.split(',');  //split the string at each comma.
   console.log(arr);
   //prints ['1', '2', '3', '4']  Note that the numbers are strings.

   arr = phrase.split(' ');   //split the string at each space.
   console.log(arr);
   //prints ['Bookkeeper', 'of', 'balloons']

   arr = word.split('');      //split the string at each character.
   console.log(arr);
   //prints ['R', 'u', 't', 'a', 'b', 'a', 'g', 'a']

``slice``
++++++++++

*Syntax = arrayName.slice(starting index, ending index)*

The ending index is optional.  If it is left out, ``slice`` returns a new array
that includes everything from the starting index to the end of the original array.

If both indices are included in the parentheses ``()``, the new array contains
everything from the starting index up to BUT NOT INCLUDING the ending index.

.. sourcecode:: js

   let arr = ['a', 'b', 'c', 'd', 'e'];

   arr.slice(2);
   //returns [ 'c', 'd', 'e' ]

   arr.slice(1,4);
   //returns [ 'b', 'c', 'd' ]

``sort``
++++++++++

*Syntax = arrayName.sort()*

This method arranges the elements of an array into increasing order.  For
strings, this means alphabetical order.  HOWEVER, the results are not always
what we expect.

.. sourcecode:: js

   let letters = ['f', 'c', 'B', 'X', 'a'];

   letters.sort();
   console.log(letters);
   //prints [ 'B', 'X', 'a', 'c', 'f' ]

From the alphabet song, we know that 'a' comes before 'B' (and certainly before
'X'), but JavaScript treats capital and lowercase letters differently.  The
default sort order places capital letters before lowercase.

.. sourcecode:: js

   let mixed = ['A', 'a', 20, 40];

   mixed.sort();
   console.log(mixed);
   //prints [ 20, 40, 'A', 'a' ]

When numbers and strings are sorted, the default order places numbers before
all letters.

.. sourcecode:: js

   let numbers = [2, 8, 10, 400, 30];

   numbers.sort();
   console.log(numbers);
   //prints ``[ 10, 2, 30, 400, 8 ]``

Here JavaScript gets truly bizarre.  Since when is 8 larger than 400?  The
reason is that when JavaScript sorts, it converts all numbers into strings by
default.  Just like 'Apple' comes before 'Pear' because 'A' comes before 'P',
the string '400' begins with a '4' which comes before any string starting with
an '8'.  Looking only at the first digit in each number, we see the expected
progression (1, 2, 3, 4, 8).

Later in this course, we will explore ways to fix this issue and correctly sort
numerical arrays.
