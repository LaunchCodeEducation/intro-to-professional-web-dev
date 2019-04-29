Composing Functions
===================

.. index::
   single: function; composition
   see: composition; function composition

The practice of using functions to build other functions is known as **function composition**, or simply **composition**. To demonstrate, we consider a specific example.

Palindrome Checker
------------------

A palindrome can be defined as a word that is spelled the same backwards and forwards. Some examples are "tacocat", "kayak",  and "racecar".

.. note:: There are other factors that are sometimes included in the definition of a palindrome. For example, an alternative definition is that a palindrome is a sentence or phrase that contains letters in the same order, whether considered from beginning-to-end, or end-to beginning, ignoring punctuation, case, and spaces. 
   
   A sentence fitting this definition is, "A man, a plan, a canal: Panama." We will stick to our simpler definition for the purpose of this example.

We want to write a boolean function---a function that returns ``true`` or ``false``---to deteremine if a word is a palindrome.

One way to state the palindrome condition is to say that a palindrome is a string that is equal to its reverse. In other words, we can test for palindromes by taking a string, reversing it, and then comparing the reversed string to the original. If the two are equal, we have a palindrome.

To that end, it would be very useful to have a function that reversed a string, wouldn't it?

The **reverse** Function
^^^^^^^^^^^^^^^^^^^^^^^^

Let's write a function that, given a string, returns its reverse.

One approach uses the accumulator pattern:

.. sourcecode:: js

   function reverse(str) {
      let reversed = '';
      
      for (let i = 0; i < str.length; i++) {
         reversed = str[i] + reversed;
      }

      return reversed;
   }

.. todo:: add reference to the correct section of the string chapter

This is the same algorithm that we used to reverse a string in a previous chapter.

Another approach is to use the fact that there is a ``reverse`` method for arrays, and that the methods ``split`` and ``join`` allow us to go from strings to arrays and back (this was covered in section X).

.. todo:: Add reference to array chapter where this is covered

.. sourcecode:: js

   function reverse(str) {
      let lettersArray = str.split('');
      let reversedLettersArray = lettersArray.reverse();
      return reversedLettersArray.join('');
   }

Let's break down the steps carried out by this function:

#. **Turn the string into an array of characters.** We call ``str.split('')``, using the empty string as the splitting character, returns an array of the individual characters that make up the string.
#. **Reverse the array of characters.** To do this, we use the built-in array method ``reverse``.
#. **Join the reversed character array into a string.** We call ``.join('')``. Joining with the empty string is the same as concatenating each of the invididual characters together into a single string.

.. admonition:: Try It!

   Use method chaining to reduce the ``reverse`` function to a single line.

   `Try it at repl.it <https://repl.it/@launchcode/reverse-Function>`_


.. _palindrome-function:

The **isPalindrome** Function
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Using our ``reverse`` function for strings, we can create our palindrome checker. Recall that our approach will be to take the string argument, reverse it, and then compare the reversed string to the original string.

.. sourcecode:: js

   function reverse(str) {
      return str.split('').reverse().join('');
   }

   function isPalindrome(str) {
      return reverse(str) === str;
   }
   
Since ``isPalindrome`` uses our ``reverse`` function, this is an example of composition. 

.. admonition:: Try It!

   Does our ``isPalindrome`` function work? `Try it for yourself at repl.it! <https://repl.it/@launchcode/isPalindrome>`_


Functions Should Do Exactly One Thing
-------------------------------------

An important consideration when writing a function is size. By "size" we mean that functions should be short and, more importantly, *do exactly one thing.* 

This principle is easier to state than to put into practice. For example, what if we had written ``isPalindrome`` without breaking out the ``reverse`` code into a separate function?

.. sourcecode:: js


   function isPalindrome(str) {
      let reversed = str.split('').reverse().join('');
      return reversed === str;
   }

This function is still short, which is good. But does it do one thing (check if a string is a palindrome) or multiple things (check the string, *and* reverse a string)? This is a bit subjective, and here the answer is certainly debatable. 

Some cases will be much more clear-cut, however. Consider the sandwich function, ``makeSandwich``, from the section :ref:`sandwich-function`. Suppose we wanted to expand the capability of our program to not only make a sandwich, but to also pour a beverage (to go along with our lunch). It would be a bad idea to amend our function to do both, ending up with a function that has a name like ``makeSandwichAndPourDrink``.

A much better solution would look like this:

.. sourcecode:: js

   function makeSandwich( /*parameters*/ ) {
      // make the sandwich
   }

   function pourDrink( /*parameters*/ ) {
      // pour the drink
   }

   function makeLunch( /*parameters*/ ) {
      makeSandwich( /*parameters*/ );
      pourDrink( /*parameters*/ );
   }

Why is this better? Smaller functions are easier to debug, for one thing. And by separating single responsibilities into individual functions, we also make our code easier to read and more reusable. In looking at the ``makeLunch`` function, it is very clear what is going on. First, it makes a sandwich, then it pours a drink. 

Were the ``makeLunch`` function to simply contain all of the code necessary to carry out *both* tasks, there would be no clear separation between one task and the other, and the only way we might describe the various sections of the larger function would be to use comments. And, :ref:`as we've discussed <comments_lie>`, comments should be a secondary option for explaining your code.
