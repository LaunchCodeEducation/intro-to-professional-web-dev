POST Form Submission
====================


Form Submission using POST
--------------------------
Instead of using GET and query parameters to submit form data, we can use POST.
To submit a form using a POST request, set the ``method`` attribute to ``"POST"``.
Form data submitted via POST will be contained in the HTTP message body. Using POST is a
more secure way to send form data.

   .. sourcecode:: html

      <form action="" method="POST">
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

   TODO:: replace post action page with something we control

   **Network Tab After Form Submitted**

   TODO: screen shot of network tab and maybe the browser

.. note::

   POST form submissions are not really secure unless you are using
   `HTTPS <https://en.wikipedia.org/wiki/HTTPS>`_.
   Configuring HTTPS is beyond the scope of this class, but it's important to
   know the protocol exists.



Check Your Understanding
------------------------

.. todo:: do these
