.. _string-replace-examples:

``replace`` Examples
====================

The general syntax for this method is:

.. sourcecode:: js

   stringName.replace(searchChar, replacementChar);

Given a search string ``searchChar`` and a replacement value ``replacementChar``, this method returns a copy of ``stringName`` with the *first* occurrence of ``searchChar`` replaced by ``replacementChar``.

.. note::

   The ``replace`` method can be used in more powerful ways utilizing regular expressions. We will not cover those here, but you can `read more at MDN <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/replace>`_.

.. admonition:: Example

   .. sourcecode:: js
         
      "carrot".replace("r", "t");

      "Launch Code".replace(" ", "");

   **Output**

   .. sourcecode:: bash

      catrot
      LaunchCode

.. admonition:: Example

   Some email providers, including Gmail, allow users to put a ``.`` anywhere before the ``@`` symbol. This means that ``fake.email@launchcode.org`` is the same as ``fakeemail@launchcode.org``.

   Remove the ``.`` before the ``@`` symbol in an email address.

   .. sourcecode:: js
   
      let input = "fake.email@launchcode.org";
      let email = input.replace(".", "");
      console.log(email);

   **Output**

   .. sourcecode:: bash

      fakeemail@launchcode.org

   This example illustrates a common use case of ``replace``, which is to *remove* a character by replacing it with the empty string.

.. warning::

   Notice in the last example that if there is not a ``.`` before the ``@`` symbol, the ``.`` that is part of the domain, ``launchcode.org`` would be inadvertently removed. In a real application, we would want to isolate the portion in front of ``@`` using ``slice``.
