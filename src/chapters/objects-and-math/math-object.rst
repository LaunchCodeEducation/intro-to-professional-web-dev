The ``Math`` Object
====================

JavaScript provides several built-in objects, which can be called directly by
the user. One of these is the ``Math`` object, which contains more than the
standard mathematical operations (``+, -, *, /``).

In the previous sections, we learned how to construct, modify, and use objects
such as ``giraffe``. However, JavaScript built-in objects cannot be modified
by the user.

   Unlike other objects, the ``Math`` object is *immutable*.

``Math`` Properties Are Constants
----------------------------------

The ``Math`` object has 8 defined properties. These represent *mathematical
constants*, like the value for pi (π) or the square root of 2.

Instead of defining a variable to hold as many digits of pi as we can remember,
JavaScript stores the value for us. To use this value, we do NOT need to
create a new object. By using dot notation and calling ``Math.PI``, we can
access the value of pi.

.. admonition:: Example

   .. sourcecode:: js
      :linenos:

      console.log(Math.PI);
      console.log(Math.PI*4);
      console.log(Math.PI + Math.PI);

   **Output**
   ::

      3.141592653589793
      12.566370614359172
      6.283185307179586

As stated above, the properties within ``Math`` *cannot* be changed by the
user.

.. admonition:: Example

   .. sourcecode:: js
      :linenos:

      console.log(Math.PI);

      Math.PI = 1234;

      console.log(Math.PI);

   **Output**
   ::

      3.141592653589793
      3.141592653589793

To use one of the other constants stored in ``Math``, we replace ``PI`` with
the property name (e.g. ``SQRT2`` stores the value for the square root of 2).

Other ``Math`` Properties
--------------------------

Besides the value of pi, JavaScript provides `7 other constants <https://www.w3schools.com/jsref/jsref_obj_math.asp>`__.
How useful you find each of these depends on the type of project you need to
complete.

More powerful uses of the ``Math`` object involve using *methods*, which we
will examine next.
