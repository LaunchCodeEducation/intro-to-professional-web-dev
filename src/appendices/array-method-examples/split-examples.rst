**split** Examples
===================

The general syntax for this method is:

::

   stringName.split('delimiter')

``split`` is actually a string method, but it complements the array method
``join``.

.. index:: ! delimiter
   single: array; delimiter

``split`` divides a string into smaller pieces, which are stored in a new
array. The **delimiter** argument determines how the string is broken apart.

.. admonition:: Example

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
