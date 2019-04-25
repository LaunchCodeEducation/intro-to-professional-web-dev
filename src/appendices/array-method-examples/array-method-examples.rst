Array Method Examples
=====================

**concat**
-----------

Syntax & description reminder...

Examples

**includes**
-------------

Syntax & description reminder...

Examples

**indexOf**
-------------

Syntax & description reminder...

Examples

**join**
---------

Syntax & description reminder...

Examples

**pop**
--------

Syntax & description reminder...

Examples

**push**
---------

Syntax & description reminder...

Examples

**reverse**
------------

Syntax & description reminder...

Examples

**shift**
----------

Syntax & description reminder...

Examples

**slice**
----------

Syntax & description reminder...

Examples

**sort**
---------

The general syntax for this method is:

::

  arrayName.sort()

This method arranges the elements of an array into increasing order.  For
strings, this means alphabetical order.  HOWEVER, the results are not always
what we expect.

#. Alphabetical order.

   .. sourcecode:: js

      let letters = ['f', 'c', 'B', 'X', 'a'];

      letters.sort();
      console.log(letters);
      //prints [ 'B', 'X', 'a', 'c', 'f' ]

From the alphabet song, we know that 'a' comes before 'B' (and certainly before
'X'), but JavaScript treats capital and lowercase letters differently.  The
default sort order places capital letters before lowercase.

2. When numbers and strings are sorted, the default order places numbers before
   all letters.

   .. sourcecode:: js

      let mixed = ['a', 'A', 20, 40];

      mixed.sort();
      console.log(mixed);
      //prints [ 20, 40, 'A', 'a' ]

#. Numerical sorting.

   .. sourcecode:: js

      let numbers = [2, 8, 10, 400, 30];

      numbers.sort();
      console.log(numbers);
      //prints [ 10, 2, 30, 400, 8 ]

Here JavaScript gets truly bizarre. How is 8 larger than 400?

When JavaScript sorts, it converts all entries into strings by default. Just
like 'Apple' comes before 'Pear' because 'A' comes before 'P', the string '400'
begins with a '4' which comes before any string starting with an '8'. Looking
only at the first digit in each number, we see the expected progression
(1, 2, 3, 4, 8).

Later in this course, we will explore ways to fix this issue and correctly sort
numerical arrays.

**splice**
-----------

Syntax & description reminder...

Examples

**split**
----------

Syntax & description reminder...

Examples

**unshift**
------------

Syntax & description reminder...

Examples
