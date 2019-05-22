POST Form Submission
====================


Form Submission Using POST
--------------------------
Instead of using GET and query parameters to submit form data, we can use POST.
To submit a form using a POST request, set the form's ``method`` attribute to ``"POST"``.
Form data submitted via POST will be submitted in the body of the HTTP request.
Data submitted by GET request is less secure than POST because GET request URLs
and the query parameters are cached and logged, possibly leaking sensitive data.

.. admonition:: Example

   Form with ``method="POST"``

   .. sourcecode:: html

      <form action="" method="POST">
         <label>Username <input type="text" name="username"></label>
         <label>Team Name <input type="text" name="team"></label>
         <button>Submit</button>
      </form>


Send Form Submission to a Server
--------------------------------
The ``action`` and ``method`` attributes allows us to choose where the form request will be
sent and what type of request will be sent. How do we configure what happens in response to
a form submission?

.. index:: ! form handler

**Form handlers** are web servers that receive and respond to a form submission. Form
handlers are usually separate web pages or applications that receive, inspect,
do something with the form values, and then finally respond. For this unit we are
going to use form handlers that have already been created for us.

.. admonition:: Example

   When submitted this form will send a POST request to a certain form handler defined by
   ``action`` attribute.

   .. sourcecode:: html

      <form action="https://www.w3schools.com/action_page.php" method="POST">
         <label>Username <input type="text" name="username"></label>
         <label>Team Name <input type="text" name="team"></label>
         <button>Submit</button>
      </form>

.. admonition:: Try It!

   #. Open `this form using POST <https://form-post--launchcode.repl.co/>`_ in a browser.
   #. Open the network tab of the developer tools
   #. Check "Persist Logs" in the network tab
   #. Enter data into the inputs
   #. Click Submit button

   **Network Tab After Form Submitted**

   TODO: screen shot of network tab and maybe the browser

   TODO:: remove w3schools from example (requires we have something setup)

.. warning::

   Using POST for form submissions adds a very low level of security.
   Using `HTTPS <https://en.wikipedia.org/wiki/HTTPS>`_ instead of HTTP
   adds a higher level of security. Configuring HTTPS is beyond the
   scope of this class.


Check Your Understanding
------------------------

.. admonition:: Question

   What attribute on ``<form>`` determines if the form is submitted with GET or POST?

.. admonition:: Question

   What attribute on ``<form>`` determines *where* the request is sent?

.. admonition:: Question

   What do *form handlers* do with form submissions?
