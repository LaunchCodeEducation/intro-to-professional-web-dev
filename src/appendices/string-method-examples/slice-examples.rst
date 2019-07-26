.. _string-slice-examples:

``slice`` Examples
==================

The general syntax for this method is:

.. sourcecode:: js

   stringName.slice(i, j);

Given a starting index ``i`` and an optional ending index ``j``, return the substring consisting of characters from index ``i`` through index ``j-1``. If the ending index is ommitted, the returned substring includes all characters from the starting index through the end of the string. 

.. sourcecode:: js

   "LaunchCode".slice(0, 6);

   "LaunchCode".slice(6);

**Output**

.. sourcecode:: bash

   Launch
   Code

On some websites, the portion of an email address before the ``@`` symbol is used as a username. We can extract this portion of an email address using ``slice`` in conjunction with ``indexOf``.

.. admonition:: Example

   .. sourcecode:: js
      :linenos:
   
      let input = "fake.email@launchcode.org";
      let atIndex = input.indexOf("@");
      let username = input.slice(0, atIndex);
      console.log(username);

   **Output**

   .. sourcecode:: bash

      fake.email
