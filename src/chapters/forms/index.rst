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
how to define a text input, hint that more types will follow
inputs inside of a form are submitted together in the same request
name attributes are used to identify each data input in the form
label is used to visually label the inputs


Form Submission
---------------
what causes a button to be submitted? submit button? hitting enter? button?
Where is the Form submitted?
action attribute
method attribute


More Input Elements
-------------------
textarea, password, check box, selectbox, radio buttons, email

Form Validation with JavaScript
-------------------------------
submit event
preventDefault or maybe stopPropagation?
