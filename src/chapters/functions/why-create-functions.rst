Why Create Functions?
=====================

After wading through all of the new syntax necessary to create a function, you
might be asking yourself, *Why would I ever want to do this?* Good question! We
have a few answers.

Functions Reduce Repetition
---------------------------

Like loops, functions help us keep our code DRY. When we need to repeat the same basic task in multiple parts of a program, a function will allow us to package up that task into a neat, reusable form. Loops enable the same task to be repeated many times in succession, while functions enable the same task to be repeated in different portions of a program.

Functions Make Your Code More Readable
--------------------------------------

Placing a piece of functionality within a function allows us to put a name on that functionality. Consider our :ref:`palindrome example <palindrome-function>`. One way to write that function is:

.. sourcecode:: js
   :linenos:

   function isPalindrome(str) {

      let reversed = '';

      for (let i = 0; i < str.length; i++) {
         reversed = str[i] + reversed;
      }

      return reversed === str;
   }

While the variable name ``reversed`` is descriptive, giving us a sense of what is going on with the ``for`` loop, the function becomes even more readable when we break out the reversing behavior into a separate function.

.. sourcecode:: js
   :linenos:

   function reverse(str) {
      let reversed = '';

      for (let i = 0; i < str.length; i++) {
         reversed = str[i] + reversed;
      }
      return reversed;
   }

   function isPalindrome(str) {
      return reversed(str) === str;
   }

Aside from following the principle that functions should do only one thing, the logic within ``isPalindrome`` is more clear and self-descriptive. The function itself says, *a string is a palindrome if it is equal to its reverse*. To draw this same conclusion from the example above, without a ``reverse`` function, we are required to analyze more of the program's logic.

Functions Reduce Complexity
---------------------------

Large programs can be broken down into smaller parts using functions. Imagine a car built out of a single, large piece of metal. Were such a car to break down, diagnosing the problem would be difficult, and fixing it nearly impossible. The mechanic would have to determine where the issue was, then cut apart the bad portion, create a custom-made replacement portion, and weld it into place. 

The complexity of this situation becomes much less when a car is made up of lots of small parts, each of which can be tested and replaced individually. The same thing happens with code. While there are many other organizational units for programs---including modules, files, and packages---functions are the most basic and universal organizational tool. 

Functions Enable Code Sharing
-----------------------------

Encapsulating behavior within a function makes it easy to reuse that code
within a program, but it also allows you to share that behavior across files
and even different projects. This becomes critically important when you start
working on bigger programs that consist of a large number of files.

You will explore this idea in the :ref:`Modules chapter <modules-index>`.

Functions Save Millions of Lives Every Day
------------------------------------------

Okay, not really. But the point is, functions are incredibly powerful tools that you will come to appreciate and find indispensable. Ask a professional programmer if they could do their job without functions, and the answer will be an emphatic "NO!" 

While functions may seem abstract and difficult to learn at first, repeated practice will lead to mastery. We promise that your work will be worth it. 
