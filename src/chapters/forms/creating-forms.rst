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
added inside of it. Inputs will allows the user to enter data. Below we have added one basic
``<input>`` tag.

.. sourcecode:: html
   :linenos:

   <html>
      <head>
         <title>Form Example</title>
      </head>
      <body>
         <form>
            <input type="text">
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

   <input type="text" name="username">

.. warning::

   Your form will NOT submit a value for an ``<input>`` unless it has a ``name`` attribute.

Forms normally contain more than one input. ``<label>`` tags are used provide a textual label,
which informs the user of what data to enter into each field. The simplest usage of
``<label>`` tags is to *wrap* them around ``<input>`` tags.

.. sourcecode:: html
   :linenos:

   <html>
      <head>
         <title>Form Example</title>
      </head>
      <body>
         <form>
            <label>Username <input type="text" name="username"></label>
            <label>Team Name <input type="text" name="teamName"></label>
         </form>
      </body>
   </html>


Form Submission
---------------
what causes a button to be submitted? submit button? hitting enter? button?
Where is the Form submitted?
what is submitted?
action attribute
method attribute


Types of Inputs
---------------
textarea, password, check box, selectbox, radio buttons, email
provide note about: date?, range?, number?


Form Validation with JavaScript
-------------------------------
submit event
preventDefault or maybe stopPropagation?
