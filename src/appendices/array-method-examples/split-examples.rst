.. _split-examples:

``split`` Examples
==================

The general syntax for this method is:

.. sourcecode:: js

   stringName.split('delimiter')

``split`` is actually a string method, but it complements the array method
``join``.

.. index:: ! delimiter
   single: array; delimiter

``split`` divides a string into smaller pieces, which are stored in a new
array. The **delimiter** argument determines how the string is broken apart.

.. admonition:: Example

   .. sourcecode:: js
      :linenos:

      let numbers = "1,2,3,4";
      let word = "Rutabaga";
      let phrase = "Bookkeeper of balloons."
      let arr = [];

      arr = numbers.split(',');  //split the string at each comma.
      console.log(arr);

      arr = phrase.split(' ');   //split the string at each space.
      console.log(arr);

      arr = word.split('');      //split the string at each character.
      console.log(arr);

   **Output**

   ::

      ['1', '2', '3', '4']
      ['Bookkeeper', 'of', 'balloons.']
      ['R', 'u', 't', 'a', 'b', 'a', 'g', 'a']
