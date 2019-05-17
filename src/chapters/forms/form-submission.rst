Form Submission
===============

.. index:: ! form submission

The purpose of a form is to collect data input by the user. As we learned in the previous
chapter, the web is made up of a serious of HTTP requests and responses. A
**form submission** is when the values in a form are sent in an HTTP request to a server.

Trigger Form Submission
-----------------------
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

   Open `this form <https://form-default--launchcode.repl.co/>`_ in a browser.
   Input values into the inputs, click the Submit button, then notice what happens to the
   address bar.

   .. sourcecode:: html
      :linenos:

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
               <label>Team Name <input type="text" name="team"></label>
               <button>Submit</button>
            </form>
         </body>
      </html>

   **Output**

   .. figure:: figures/default-form.png
      :alt: Browser screen shot showing form with two text inputs and a submit button. Both inputs have text values.

   **Output After Form Submitted**

   .. figure:: figures/default-form-submitted.png
      :alt: Browser screen shot showing form after it has been submitted. The URL has queryString showing.

   Edit code in this `source code repl.it <https://repl.it/@launchcode/form-default>`_.

Notice in the above example that the browser address has changed to
``https://form-default--launchcode.repl.co/?username=salina&team=Space+Coders``.
Which includes a query parameter for *every* field in the form.That is because the
default form submission type is GET. Remember that GET requests do not have a body
to contain the field values.

.. note::

   You may have noticed that the space character between ``"Space Coders"`` was turned
   into a ``+``. That is because some characters can NOT allowed to be in a URL. The browser
   automatically replaces those invalid characters.

Key Value Pairs
^^^^^^^^^^^^^^^
When a form is submitted
a key value pair is submitted for each *named* input, with the key being the name and
the value being the value of the input.

Form with two named inputs:

.. sourcecode:: html

   <form action="">
      <label>Username <input type="text" name="username"></label>
      <label>Team Name <input type="text" name="team"></label>
      <button>Submit</button>
   </form>

Key value pairs when form is submitted:

::

   username=salina&team=Space+Coders


Check Your Understanding
------------------------

.. todo:: do these
