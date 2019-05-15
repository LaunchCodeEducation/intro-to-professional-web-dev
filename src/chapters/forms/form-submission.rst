Form Submission
===============

.. index:: ! form submission

The purpose of a form is to collect data input by the user. As we learned in the previous
chapter, the web is made up of a serious of HTTP requests and responses. A **form submission** is when the values in a
form are sent in an HTTP request to a server.

A form submission is triggered by clicking a button inside the form. The buttons can be
``input`` elements or ``button`` elements.

.. sourcecode:: html

   <form>
      <label>Username <input type="text" name="username"></label>
      <!-- clicking either of these will cause a form submission -->
      <input type="submit"/>
      <button>Submit</button>
   </form>

Where do form submissions go when they are submitted?
The answer is the ``action`` attribute on the ``<form>`` tag. The ``action`` attribute
is the destination that the form submission request will be sent to.

If the ``action`` attribute is not present or has the value empty string, then ``action``
is set to the address of the current page.

.. admonition:: Try It!

   Load this form on `repl.it <https://form-default--launchcode.repl.co/>`_.
   Input values into the inputs, click the Submit button, then notice what happens to the
   address bar.

   .. sourcecode:: html

      <html>
         <head>
            <title>Form Example</title>
            <style>
               body { padding: 25px;}
            </style>
         </head>
         <body>
            <form action="">
               <label>Username <input type="text" name="username"></label>
               <label>Team Name <input type="text" name="teamName"></label>
               <button>Submit</button>
            </form>
         </body>
      </html>

   **Output**

   .. figure:: figures/default-form.png
      :alt: todo...

   **Output After Form Submitted**

   .. figure:: figures/default-form-submitted.png
      :alt: todo...

   Edit code in this `source code repl.it <https://repl.it/@launchcode/form-default>`_.

Notice in the above example that the browser address has changed to
``https://form-default--launchcode.repl.co/?username=salina&teamName=Space+Coders``.
Which includes a query parameter for each field on the form. This is because the
default form submission type is GET.

Something about wanting to use POST
Example using POST
https://www.w3schools.com/action_page.php

What is submitted?
- key values


Form Validation with JavaScript
-------------------------------
submit event
preventDefault to stop form from submitting normally


Check Your Understanding
------------------------
TODO:...
