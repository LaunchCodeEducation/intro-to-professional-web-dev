.. _join-examples:

``join`` Examples
==================

The general syntax for this method is:

.. sourcecode:: js

   arrayName.join('connector')

``join`` combines all the elements of an array into a string. The *connector*
determines the string that "glues" the array elements together.

.. admonition:: Example

   .. sourcecode:: js
      :linenos:

      let arr = [1, 2, 3, 4];
      let words = ['hello', 'world', '!'];
      let newString = '';

      newString = arr.join("+");
      console.log(newString);

      newString = words.join("");
      console.log(newString);

      newString = words.join("_");
      console.log(newString);

   **Output**

   ::

      1+2+3+4
      helloworld!
      hello_world_!
