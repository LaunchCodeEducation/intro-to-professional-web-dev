Exporting Modules
==================

We learned how to pull in useful code in the form of *modules*, but what if
we write clever code that we want to share? Fortunately, Node allows us to make
our code available for use in other programs.

First, some basic points:

#. Every Node.js file is treated as a module (also called a *package*).
#. From a file, we can export a single function or a set of functions.

Starter Code
-------------

.. index:: ! export

We will use the following code sample to practice how to **export** our
work---making it available to import as a module.

.. replit:: js
   :slug: ExportPractice01
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

   function randomArrayElement(arr){
      let index = Math.floor(Math.random()*arr.length);
      return arr[index];
   }

These functions are in the ``practiceExports.js`` file, and our goal is to
import them into ``index.js``.

Exporting a Single Function
----------------------------

Let's start by exporting the ``isPalindrome`` function. At the bottom of the
``practiceExports.js`` code, add the line ``module.exports = isPalindrome;``.
This makes the function available to other files.

In ``index.js`` we import ``isPalindrome`` with a ``require`` statement. After
this, we can call the function from within ``index.js``.

.. admonition:: Try It

   Add the following code to ``index.js``, then click "Run".

   .. sourcecode:: js
      :linenos:

      const palindromeCheck = require('./practiceExports.js');

      console.log(typeof palindromeCheck);
      console.log(palindromeCheck('that'));
      console.log(palindromeCheck('radar'));

   **Console Output**

   ::

      function
      false
      true

There are several points to make about the code and output.

#. By setting ``module.exports`` equal to ``isPalindrome``, we exported that
   single function.
#. Even though we ``require`` the file ``practiceExports.js``, it only assigns
   ``isPalindrome`` to the variable ``palindromeCheck``. Thus, ``typeof
   palindromeCheck`` returns ``function``.
#. ``palindromeCheck`` now behaves in the same way as ``isPalindrome``, so
   calling ``palindromeCheck('that')`` evaluates to ``false``, since ``'that'``
   is not a palindrome.

Exporting Multiple Functions
-----------------------------

``practiceExports.js`` contains three functions, and we can export them by
using a different syntax for ``module.exports``. Instead of setting up a single
function, we will create an *object*.

To export multiple functions, the syntax is:

.. sourcecode:: js

   module.exports = {
      isPalindrome: isPalindrome,
      evenOrOdd: evenOrOdd,
      randomArrayElement: randomArrayElement
   }

Within the ``{}``, we create a series of key:value pairs. The *keys* will be
the names used in ``index.js`` to call the functions. The *values* are the
functions themselves. 

.. admonition:: Note

   We do not have to make the key match the name of the function, but doing so
   helps maintain consistency between files.

.. admonition:: Warning

   You might be tempted to use three statements to export the three functions:

   .. sourcecode:: js

      module.exports = isPalindrome;
      module.exports = evenOrOdd;
      module.exports = randomArrayElement;

   This will NOT work, because Node expects only ONE ``module.exports`` statement in a file. No error will be thrown if you use more than one, but ``require('./practiceExports.js')`` will only pull in the information from the LAST statement.

Try It
^^^^^^^

Modify ``module.exports`` in ``practiceExports.js`` to include the three
functions we want to export. We could include only one or two, but for this
practice let's use all of them.

Next, modify ``index.js`` as follows and click "Run":

.. sourcecode:: js
   :linenos:

   const practice = require('./practiceExports.js');

   console.log(typeof practice);
   console.log(practice);

``typeof`` indicates that ``practice`` is an object, and printing ``practice``
gives us a list of key/value pairs (e.g.
``isPalindrome: [Function: isPalindrome]``).

All of the functions from ``practiceExports`` are included in the ``practice``
object. To call then, we use dot notation---
``practice.functionName(argument)``.

Modify ``index.js`` again and click "Run":

.. sourcecode:: js
   :linenos:

   const practice = require('./practiceExports.js');
   let arr = ['Hello', 'World', 123, 987, 'LC101'];

   console.log(practice.isPalindrome('mom'));
   console.log(practice.evenOrOdd(9));

   for (i=0; i < 3; i++){
      console.log(practice.randomArrayElement(arr));
   }

**Console Output**

::

   true
   Odd
   123
   World
   LC101

Success! You exported your first module.

What If
--------



Check Your Understanding
-------------------------
