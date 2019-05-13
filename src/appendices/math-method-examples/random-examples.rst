.. _random-examples:

``Math.random`` Examples
=========================

The general syntax for this method is:

::

   Math.random()

This method returns a random decimal value between 0 and 1, which can be stored
in a variable or used in a calculation.

Note that 0 is a possible selection, but 1 is NOT.

.. admonition:: Example

   .. sourcecode:: js
      :linenos:

      for (i=0; i<5; i++){
         let randNum = Math.random();
         console.log(randNum);
      }

   **Output**
   ::

      0.34992592600591066
      0.11861535165960668
      0.019710093901842862
      0.7751799992655235
      0.46782849511194136

If a random integer must be generated, the result of ``Math.random()`` can be
manipulated with operators (``+, -, *, /``) and other ``Math`` methods.

.. admonition:: Example

   .. sourcecode:: js
      :linenos:

      for (i=0; i<5; i++){
         let randNum = Math.random()*100;
         console.log(Math.floor(randNum));
      }
      //Creates a random number from 0 to 99.

   **Output**
   ::

      76
      56
      24
      7
      37