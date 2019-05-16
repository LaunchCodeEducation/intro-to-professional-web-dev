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


Form Validation with JavaScript
-------------------------------
Validating form inputs *before* submitting the form can make the user experience much
smoother. Some input types have built in browser validation for basic formats such as
numbers and email addresses. We can use event handlers to perform more complex
validation on form input values.

**To add validation using JavaScript:**

1. Add an event handler for the ``window`` *load* event
2. Add an event handler for the ``form`` *submit* event
3. Check the input values

   a. If the values are valid, allow the form submission
   b. If the values are NOT valid, inform the user and STOP form submission

.. admonition:: Example

   Let's start this by showing an ``alert`` box when the form *submit* event is
   triggered.

   .. sourcecode:: html
      :linenos:

      <html>
         <head>
            <title>Form Validation</title>
            <style>
               label {display: block;}
               body {padding: 25px;}
            </style>
         </head>
         <script>
            window.addEventListener("load", function() {
               let form = document.querySelector("form");
               form.addEventListener("submit", function(event) {
                  alert("submit clicked");
               });
            });
         </script>
         <body>
            <form method="POST" action="https://www.w3schools.com/action_page.php">
               <label>Username <input type="text" name="username"></label>
               <label>Team Name <input type="text" name="team"></label>
               <button>Submit</button>
            </form>
         </body>
      </html>

**Follow Along as We Add Validation**

Use `this repl.it <https://repl.it/@launchcode/form-validation>`_ to add validation to
the above example.

To validate what the user has typed, we can get a reference to the ``input`` elements in
the DOM and check ``input.value``. Let's change the *submit* event handler to alert
the value of the username input. We are going to use
``document.querySelector("input[name=username]")``, which uses an *attribute selector* to
select the ``<input>`` that has ``name="username"``.

.. sourcecode:: html
   :linenos:

   <script>
      window.addEventListener("load", function() {
         let form = document.querySelector("form");
         form.addEventListener("submit", function(event) {
            let usernameInput = document.querySelector("input[name=username]");
            // alert the current value found in the username input
            alert("username: " + usernameInput.value);
         });
      });
   </script>

Now that we know how to get the value of an input, we can add *conditional statements*.
Let's add code that opens an alert box if *either* input values are *empty*.

.. sourcecode:: html
   :linenos:

   <script>
      window.addEventListener("load", function() {
         let form = document.querySelector("form");
         form.addEventListener("submit", function(event) {
            let usernameInput = document.querySelector("input[name=username]");
            let teamName = document.querySelector("input[name=team]");
            if (usernameInput.value === "" || teamName.value === "") {
               alert("All fields are required!");
            }
         });
      });
   </script>

We are making progress. Now if you click *Submit* with one or both of the inputs empty,
then an alert message appears telling you that both inputs are required.

.. index:: ! preventDefault

But we want to prevent the form submission from happening until all
inputs have valid values. We can use the ``event`` parameter and
``event.preventDefault()`` to stop the form submission. ``event.preventDefault()``
prevents default browser functionality from happening, like form submission happening
when ``<button>`` tags are clicked.

.. sourcecode:: html
   :linenos:

   <script>
      window.addEventListener("load", function() {
         let form = document.querySelector("form");
         form.addEventListener("submit", function(event) {
            let usernameInput = document.querySelector("input[name=username]");
            let teamName = document.querySelector("input[name=team]");
            if (usernameInput.value === "" || teamName.value === "") {
               alert("All fields are required!");
               // stop the form submission
               event.preventDefault();
            }
         });
      });
   </script>

.. todo:: try it using this example app? https://repl.it/@launchcode/form-validation-breakfast-menu

.. todo:: remove references to we3schools submission page


Check Your Understanding
------------------------

.. todo:: do these
