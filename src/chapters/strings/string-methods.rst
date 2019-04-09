.. _string-methods:

String Methods
==============

JavaScript provides many useful methods for string objects. Recall that a method is a function that "belongs to" a specific object. Methods will typically result in some operation being carried out on the data within an object. For strings, this means that our methods will typically transform the characters of the given string in some way.

As we have learned, strings are immutable. Therefore, string methods will not change the value of a string itself, but instead will *return* a new string that is the result of the given operation.

We saw this behavior in our first string method example.

.. admonition:: Example

   .. sourcecode:: js
   
      let nonprofit = "LaunchCode";

      console.log(nonprofit.toLowerCase());
      console.log(nonprofit);

   **Output**

   ::

      launchcode
      LaunchCode

While ``nonprofit.toLowerCase()`` evaluated to ``"launchcode"``, the value of ``nonprofit`` was left unchanged. This will be case for each of the string methods.

- Use common string methods: ``indexOf``, ``charAt``, ``toLowerCase``, ``toUpperCase``, ``trim``, ``replace``, ``substring``, ``slice``

Examples
--------
