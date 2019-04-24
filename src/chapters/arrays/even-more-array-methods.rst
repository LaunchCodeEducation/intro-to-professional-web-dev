Even More Array Methods
=======================

You will find the methods ``split``, ``join`` and ``splice`` useful, but they
are used less often and are not as straighforward as the other methods.

``split``, ``join`` and ``splice`` create new arrays which can be assigned to
a variable.

The ``join`` Method
---------------------

The general syntax for this method is:

::

   arrayName.join('connecter')

``join`` combines all the elements of an array into a string. The *connector*
determines the string that "glues" the array elements together.

.. sourcecode:: js

    let arr = [1, 2, 3, 4];
    let words = ['hello', 'world', '!'];
    let newArray = [];

    newArray = arr.join("+");
    console.log(newArray);
    //prints '1+2+3+4'

    newArray = words.join("");
    console.log(newArray);
    //prints 'helloworld!'

    newArray = words.join("_");
    console.log(newArray);
    //prints 'hello_world_!'

The ``split`` Method
---------------------

The general syntax for this method is:

::

   stringName.split('delimiter')

``split`` is actually a string method, but it complements the array method
``join``.

``split`` divides a string into smaller pieces, which are stored in a new
array. The **delimiter** argument determines how the string is broken apart.

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

The ``splice`` Method
----------------------

The general syntax for this method is:

::

   arrayName.splice(index, number of elements to change, item1, item2, …)

Inside the parentheses ``()``, only the first argument is required.

The ``splice`` method modifies one or more elements anywhere in the array.
Entries can be added, removed or changed. This method requires practice.

Hang on, here we go:

#. Given only one argument, ``splice(index)`` removes every entry from
   ``index`` to the end of the array.

   .. sourcecode:: js

      let arr = ['a', 'b', 'c', 'd', 'e', 'f'];

      arr.splice(2);    //Everything from index 2 and beyond is removed.
      console.log(arr);
      //prints [ 'a', 'b' ]

#. With two arguments, ``splice(index, number of items)`` starts at ``index``
   and removes the number of items.

   .. sourcecode:: js

      let arr = ['a', 'b', 'c', 'd', 'e', 'f'];

      arr.splice(2,3);    //Start at index 2 and remove 3 total entries.
      console.log(arr);
      //prints [ 'a', 'b', 'f' ]

      arr.splice(1,1);    //Start at index 1 and remove 1 entry.
      console.log(arr);
      //prints [ 'a', 'f' ]

#. Given three or more arguments, ``splice(index, 0, new item)`` starts at
   ``index`` and *ADDS* the new items.

   .. sourcecode:: js

      let arr = ['a', 'b', 'c', 'd', 'e', 'f'];

      arr.splice(2,0,'hello');     //Start at index 2, remove 0 entries, and add 'hello'.
      console.log(arr);
      //prints [ 'a', 'b', 'hello', 'c', 'd', 'e', 'f' ]

#. Given three or more arguments, ``splice(index, number of items, new items)``
   starts at ``index`` and *REPLACES* the number of items with the new ones.

   .. sourcecode:: js

      let arr = ['a', 'b', 'c', 'd', 'e', 'f'];

      arr.splice(2,3,'hello', 9);    //Start at index 2, replace 3 entries with 'hello' and 9.
      console.log(arr);
      //prints [ 'a', 'b', 'hello', 9, 'f' ]
