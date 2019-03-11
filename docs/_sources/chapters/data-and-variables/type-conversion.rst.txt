Type Conversion
===============

.. index:: ! Number(), ! String()

.. index::
   pair: type; conversion

Sometimes it is necessary to convert values from one type to another. JavaScript provides a few simple functions that will allow us to do that. The functions ``Number()`` and ``String()`` will (attempt to) convert their arguments into types ``number`` and ``string``, respectively. We call these **type conversion** functions.

The ``Number()`` function can take a floating point number or a string, and turn it into an integer. For floating point numbers, it *discards* the decimal portion of the number - a process we call *truncation towards zero* on the number line. Let us see this in action:

.. code-block:: js

    // parse a string to produce an int
    console.log("2345", Number("2345"));

    // Number even works on numbers
    console.log(17, Number(17));

    // This throws an error
    console.log(Number("23bottles"));


The last case shows that a string has to be a syntactically legal number, otherwise you'll get one of those pesky runtime errors. Modify the example by deleting the ``bottles`` and rerun the program. You should see the integer ``23``.


The type converter ``String()`` turns its argument into a string. Remember that when we print a string, the quotes are removed. However, if we print the type, we can see that it is definitely ``'string'``.

.. code-block:: js

    console.log(String(17));
    console.log(String(123.45));
    console.log(typeof String(123.45));

Check Your Understanding
------------------------

.. todo:: add check for type conversion
   

   
