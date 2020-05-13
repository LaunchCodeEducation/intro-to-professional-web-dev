Special Characters
==================

.. index::
   single: character; special
   single: newline
   single: tab

Aside from letters, numbers, and symbols, there is another class of characters
that we will occasionally use in strings, known as **special characters**.
These characters consist of special character combinations that all begin with
a ``\`` (backslash). They allow us to include characters in strings that would
be difficult or impossible to include otherwise, such as Unicode characters
that are not on our keyboards, control characters, and whitespace characters.

The most commonly-used special characters are ``\n`` and ``\t``, which are the
newline and tab characters, respectively. They work as you would expect.

.. admonition:: Example

   .. sourcecode:: js

      console.log("A message\nbroken across lines,\n\tand indented");

   **Console Output**

   ::

      A message
      broken across lines,
         and indented

.. index:: unicode

We can also represent Unicode characters (most of which aren't on a normal keyboard) using special character combinations of the form ``\uXXXX``, where the Xs are combinations referenced by the `Unicode table <https://unicode-table.com/en/>`_. This allows us to use character sets other than the basic Latin characters that English is based on, such as Greek, Cyrillic, and Arabic, as well as a wider array of symbols.

.. admonition:: Example

   .. sourcecode:: js

      console.log("The interrobang character, \u203d, combines ? and !");

   **Console Output**

   ::

      The interrobang character, ‽, combines ? and !

.. index::
   single: character; escaping
   see: escaping; character escaping

We can also use the backslash, ``\``, to include quotes within a string. This
is known as **escaping** a character.

.. admonition:: Example

   .. sourcecode:: js

      console.log("\"The dog's favorite toy is a stuffed hedgehog,\" said Chris");

   **Console Output**

   ::

      "The dog's favorite toy is a stuffed hedgehog," said Chris

Check Your Understanding
------------------------

.. admonition:: Question

   Which of the options below prints ``'Launch'`` and ``'Code'`` on separate
   lines?

   #. ``console.log('Launch\nCode');``
   #. ``console.log('Launch/nCode');``
   #. ``console.log('Launch', 'Code');``
   #. ``console.log('Launch\tCode');``
   #. ``console.log('Launch/tCode');``

.. Answer = a
