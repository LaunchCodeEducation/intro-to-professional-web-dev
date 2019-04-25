**join** Examples
------------------

The general syntax for this method is:

::

   arrayName.join('connecter')

``join`` combines all the elements of an array into a string. The *connector*
determines the string that "glues" the array elements together.

.. admonition:: Example

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
