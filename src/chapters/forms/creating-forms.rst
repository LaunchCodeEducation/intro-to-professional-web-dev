Forms
=====

.. index:: ! form

Web pages are used to display and accept data, is not a provocative statement. In this chapter
we are going to learn more about how web pages handle data input using HTML forms.
An HTML **form** is used to accept input from the user and send that data to the server.


Create a Form
-------------
To declare a form in HTML use the ``<form>`` tag with open and closing tags. This form element
will service as container for various types of other elements that are designed to capture
input from the user.

.. sourcecode:: html
   :linenos:

   <html>
      <head>
         <title>Form Example</title>
      </head>
      <body>
         <!-- empty form -->
         <form></form>
      </body>
   </html>

By default an empty ``<form></form>`` will not appear on a web page until inputs have been
added inside of it. Below we have added one basic
``<input>`` tag.

.. sourcecode:: html
   :linenos:

   <html>
      <head>
         <title>Form Example</title>
      </head>
      <body>
         <form>
            <input type="text"/>
         </form>
      </body>
   </html>


Input Element
-------------

.. index:: ! input

The ``input`` element is used to add interactive fields, which allow the user to enter data.
``input`` elements have two very important attributes: *name* and a *type*.

- ``name`` attribute is used to identify the input's value when the data is submitted
- ``type`` attribute defines which type of value of the input represents

.. sourcecode:: html

   <input type="text" name="username"/>

.. warning::

   Values are NOT submitted for an ``<input>`` unless it has a ``name`` attribute.

.. index:: ! label

Forms normally contain more than one input. ``<label>`` tags are used to provide a textual
label, which informs the user of the purpose of the field. The simplest usage of
``<label>`` tags is to *wrap* them around ``<input>`` tags.

.. sourcecode:: html
   :linenos:

   <html>
      <head>
         <title>Form Example</title>
      </head>
      <body>
         <form>
            <label>Username <input type="text" name="username"/></label>
            <label>Team Name <input type="text" name="team"/></label>
         </form>
      </body>
   </html>

.. figure:: figures/label-example.png
   :alt: HTML that includes a form tag with two input elements. Each element is inside of a label element.

A second way to relate a ``<label>`` tag to an ``<input>`` is to use the ``id`` attribute of
``input`` and the ``for`` attribute of ``label``. When ``for`` is used, the ``<input>``
does NOT have to be inside of the ``<label>``.


.. sourcecode:: html

   <label for="username"/><input id="username" name="username" type="text"/>

What happens when a ``<label>`` is clicked? The answer depends on what the ``<label>`` is
associated to.

.. index:: ! focus

For *text* inputs, when the label is clicked, then the input gains *focus*. An element with
**focus** is currently selected by the browser and ready to receive input.

For *non-text* based inputs, when the label is clicked, a value is selected. This behavior
can be seen with ``radio`` and ``checkbox`` elements which we will learn more about soon.


Check Your Understanding
------------------------

.. admonition:: Question

   Are ``<input>`` tags without ``name`` attributes submitted?

.. admonition:: Question

   What does the ``for`` attribute relate to in ``<label for="emailAddress">`` tags?
