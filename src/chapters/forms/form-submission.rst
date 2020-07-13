Form Submission
===============

.. index::
   single: form; submission

Forms collect data input by the user. As we learned in the previous
chapter, communication on the web occurs via a series of HTTP requests and responses. A
**form submission** is an HTTP request sent to the server containing the values
in a form.

Trigger Form Submission
-----------------------

A form submission is triggered by clicking a button inside the form. A submit button can be
an ``input`` element with ``type=submit`` or a ``button`` element. Both button types are
in the below example.

.. sourcecode:: html
   :linenos:

   <form>
      <label>Username <input type="text" name="username"></label>
      <!-- clicking either of these will cause a form submission -->
      <input type="submit"/>
      <button>Submit</button>
   </form>

When a form is submitted, an HTTP request is sent to the location set in the ``action``
attribute of the ``<form>`` tag.

If the action attribute is not present or is empty, then the form will submit to the URL
of the current page.

.. admonition:: Try It!

   Open `this form <https://form-default--launchcode.repl.co/>`_ in a browser.
   Type values into the inputs, click the Submit button, and notice what happens to the
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

   **Output After Submitted**

   .. figure:: figures/default-form-submitted.png
      :alt: Browser screen shot showing form after it has been submitted. The URL has queryString showing.

   `Run it <https://repl.it/@launchcode/form-default>`_.

Notice in the above example that the browser address has changed to:

::

   https://form-default--launchcode.repl.co/?username=salina&team=Space+Coders

The web address is the same as the form we loaded, but now includes a query parameter
for *every* input, with a name, in the form. These parameters are known as the query string parameters.
The form values are submitted via the query string because the default submission type for
forms is GET. In the next section, we will soon learn how to submit form data via POST.

.. note::

   Since spaces are not allowed in URLs, the browser replaces them with ``+``.

Key-value Pairs
^^^^^^^^^^^^^^^

When a form is submitted a key-value pair is created for each named input. The keys
are the values of the ``name`` attributes, and they are paired with the content of the
``value`` attributes.

Form with two named inputs:

.. sourcecode:: html

   <form action="">
      <label>Username <input type="text" name="username"></label>
      <label>Team Name <input type="text" name="team"></label>
      <button>Submit</button>
   </form>

When this form is submitted with the values from the previous example, the query string looks like this:

::

   username=salina&team=Space+Coders


Check Your Understanding
------------------------

.. admonition:: Question

   What must be added to a form to enable submission?

.. admonition:: Question

   By *default*, are HTTP forms submitted with GET or POST?
