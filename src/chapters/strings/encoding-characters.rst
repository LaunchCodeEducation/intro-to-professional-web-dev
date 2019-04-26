Encoding Characters
===================

.. index:: ! bit, character encoding

If you had microscope powerful enough to view the data stored on a computer's hard drive, or in its memory, you would see lots of 0s and 1s. Each such 0 and 1 is known as a **bit**. As we've seen, particularly in this chapter, we work with more complex data when we program, including numbers and strings. This section examines how such data is represented within a computer.

Representing Numbers
--------------------

.. index:: ! byte

.. index::
   pair: number; binary
   pair: number; decimal

A **byte** is a set of 8 bits. Since each bit can have one of two values, each byte can have 2\ :sup:`8` = 256 different values. These look like 00101101 or 11110011, and they represent a **binary number**, or a base-2 number. A binary number is a number representatation that uses only 0s and 1s. The numbers that you are used to using---which are built out of integers 0...9---are **decimal numbers**, or base-10 numbers.

It may not be obvious, but every decimal integer can be represented as a binary integer, and vice versa. There are 256 different values a byte may take, each of which can be used to represent an integer, from 0 to 255. 

.. note:: We will not discuss binary to decimal number conversion. If you are interested in learning more, there are `many <https://www.csetutor.com/how-to-convert-binary-to-decimal-examples/>`_ `tutorials <https://www.youtube.com/watch?v=wPvI19DmWQw>`_ `online <https://www.khanacademy.org/math/algebra-home/alg-intro-to-algebra/algebra-alternate-number-bases/v/decimal-to-binary>`_.

In this way, the bits in a computer can be viewed as integers. If you want to represent values greater than 255, just use more bits! 

Representing Strings
--------------------

Strings are collections of characters, so if we can represent each character as a number, then we'll have a way to go from a string to a collection of bits, and back again.

Character Encodings
^^^^^^^^^^^^^^^^^^^

.. index::
   pair: character; encoding

Unlike the natrual translation between binary and decimal numbers, there is no natural translation between integers and characters. For example, you might create a pairing of 0 to ``a``, 1 to ``b``, and so on. But what integer should be paired with ``$`` or a tab? Since there is no natural way to translate between characters and integers, computer scientists have had to make such translations up. Such translations are called **character encodings**.

.. index:: Unicode

There are many different encodings, some of which continue to evolve as the way in which we use data evolves. For instance, the most recent versions of the Unicode standard include emoji characters, such as 🌮.

The ASCII Encoding
^^^^^^^^^^^^^^^^^^

.. index:: ASCII

Most of the characters that you are used to using---including letters, numbers, whitespace, punctuation, and symbols---are part of the **ASCII** (pronounced *ASS-kee*) character encoding. This standard has changed very little since the 1960s, and it is the foundation of all other commonly-used encodings.

.. note:: ASCII stands for American Standard Code for Information Interchange, but most programmers never remember that, so you shouldn't try to either.

ASCII provides a standard translation of the most commonly-used characters to one of the integers 0...127, which means each character can be stored in a computer using a single byte. 

.. index::
   single: ASCII; table

ASCII maps ``a`` to 97, ``b`` to 98, and so on for lowercase letters, with ``z`` mapping to 122. Uppercase letters map to the values 65 through 90. The other integers between 0 and 127 represent symbols, punctuation, and other assorted odd characters. This scheme is called the **ASCII table**, and rather than replicate it here, we refer you to an `excellent one online <https://www.ascii-code.com/>`_.

In summary, strings are stored in a computer using the following process:

#. Break a string into its individual characters.
#. Use a character encoding, such as ASCII, to convert each of the characters to an integer.
#. Convert each integer to a series of bits using decimal-to-binary integer conversion.

.. admonition:: Fun Fact

   JavaScript uses the UTF-16 encoding, which includes ASCII as a subset. We will rarely need anything outside of its ASCII subset, so we will usually talk about "ASCII codes" in JavaScript.

Character Encodings in JavaScript
---------------------------------

JavaScript provides methods to convert from characters to ASCII codes and back.

The string method ``charCodeAt`` takes an index and returns the ASCII code of the character at that index.

.. admonition:: Example

   .. sourcecode:: js
   
      let nonprofit = "LaunchCode";

      for (let i = 0; i < nonprofit.length; i++) {
         console.log(nonprofit.charCodeAt(i));
      }

   **Output**

   ::

      76
      97
      117
      110
      99
      104
      67
      111
      100
      101


To convert from a character code to an actual character, use ``String.fromCharCode()``.

.. admonition:: Example

   .. sourcecode:: js
   
      let codes = [76, 97, 117, 110, 99, 104, 67, 111, 100, 101];
      let characters = "";

      for (let i = 0; i < codes.length; i++) {
         characters += String.fromCharCode(codes[i]);
      }

      console.log(characters);

   **Output**

   ::

      LaunchCode
      