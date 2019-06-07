Exporting Modules
==================

We learned how to pull in useful code in the form of *modules*, but what if
we have written clever code that we want to share? Fortunately, Node allows
us to make our code available for other programs.

First, some basic points:

#. Every Node.js file is treated as a module (also called a *package*).
#. From a file, we can export a single function or a set of functions.

Starter Code
-------------

.. index:: ! export

We will use the following code sample to practice how to **export** our
work---making it available to import as a module.

.. replit:: js
   :slug: SomeName
   :linenos:

   function isPalindrome(str){
      return str === str.split('').reverse().join('');
   }

   function evenOrOdd(num){
      if (num%2===0){
         return "Even";
      } else {
         return "Odd";
      }
   }

   function randomSelection(arr){
      let index = Math.floor(Math.random()*arr.length);
      return arr[index];
   }
