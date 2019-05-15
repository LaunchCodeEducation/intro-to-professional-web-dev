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
Which includes a query parameter for *every* field in the form.That is because the
default form submission type is GET. Remember that GET requests do not have a body
to contain the field values.

Key Value Pairs
^^^^^^^^^^^^^^^
When a form is submitted
a key value pair is submitted for each *named* input, with the key being the name and
the value being the value of the input.

Form with two named inputs:

.. sourcecode:: html

   <form action="">
      <label>Username <input type="text" name="username"></label>
      <label>Team Name <input type="text" name="teamName"></label>
      <button>Submit</button>
   </form>

Key value pairs when form is submitted:

::

   username=salina&teamName=Space+Coders

Form Submission using POST
--------------------------
Instead of using GET and query parameters to submit form data, we can use POST.
To submit a form using a POST request, set the ``method`` attribute to ``"POST"``.
Form data submitted via POST will be contained in the HTTP message body. Using POST is a
more secure way to send form data.

   .. sourcecode:: html

      <form action="" method="POST">
         <label>Username <input type="text" name="username"></label>
         <label>Team Name <input type="text" name="teamName"></label>
         <button>Submit</button>
      </form>

.. admonition:: Try It!

   #. Open `this form using POST <https://form-post--launchcode.repl.co/>`_ in a browser.
   #. Open the network tab of the developer tools
   #. Check "Persist Logs" in the network tab
   #. Enter data into the inputs
   #. Click Submit button

   TODO:: replace post action page with something we control

   **Network Tab After Form Submitted**

   TODO: screen shot of network tab and maybe the browser

.. note::

   POST form submissions are not really secure unless you are using ``https``.


Form Validation with JavaScript
-------------------------------
Validating form inputs *before* submitting the form can make the user experience much smoother.
Some input types have built in browser validation for basic formats such as numbers and email addresses.
We can use event handlers to perform more complex validation on form input values.

TODO: example using code in this https://repl.it/@launchcode/form-validation

TODO: try it  link?

submit event
preventDefault to stop form from submitting normally


Check Your Understanding
------------------------
TODO:...
