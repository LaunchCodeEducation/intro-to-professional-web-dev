Type Conversion
===============

.. index:: ! Number(), ! String(), function, returns

.. index::
   pair: type; conversion

Sometimes it is necessary to convert values from one type to another. JavaScript provides a few simple functions that will allow us to do that. The functions ``Number()`` and ``String()`` will (attempt to) convert their arguments into types ``number`` and ``string``, respectively. We call these **type conversion** functions.

The ``Number()`` function can take a string and turn it into an integer. Let us see this in action:

.. sourcecode:: js

    // prints 2345
    console.log(Number("2345"));

    // prints 'number'
    console.log(typeof Number("2345"))

    // Number even works on numbers
    console.log(17, Number(17));

.. note:: As with expressions, we say that a function **returns** a value.

What happens of we attempt to conver a string that doesn't directly represent a number into a number?

.. sourcecode:: js

    // Prints NaN
    console.log(Number("23bottles"));


This example shows that a string has to be a syntactically legal number for conversion to go as expected. Examples of such strings are ``"34"`` or ``"-2.5"``. If the value cannot be cleanly converted to a number then ``NaN`` will be returned, which stands for "not a number."

.. index:: NaN

.. note:: ``NaN`` is a **special value** in JavaScript that represents that state of data not being a number. We will learn more about ``NaN`` and other special values in a later chapter.

The type converter ``String()`` turns its argument into a string. Remember that when we print a string, the quotes are removed. However, if we print the type, we can see that it is definitely ``'string'``.

.. sourcecode:: js

    console.log(String(17));
    console.log(String(123.45));
    console.log(typeof String(123.45));

Check Your Understanding
------------------------

.. admonition:: Question

   The conversion function ``Number()`` *always* returns a 
   

   
