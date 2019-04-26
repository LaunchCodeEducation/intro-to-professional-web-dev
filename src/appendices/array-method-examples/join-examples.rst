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
      let newString = '';

      newString = arr.join("+");
      console.log(newString);
      //prints '1+2+3+4'

      newString = words.join("");
      console.log(newString);
      //prints 'helloworld!'

      newString = words.join("_");
      console.log(newString);
      //prints 'hello_world_!'
