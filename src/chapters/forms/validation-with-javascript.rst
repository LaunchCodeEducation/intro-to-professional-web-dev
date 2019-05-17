Validation with JavaScript
==========================

Validating form inputs *before* submitting the form can make the user experience much
smoother. Some input types have built in browser validation for basic formats such as
numbers and email addresses. We can use event handlers to perform more complex
validation on form input values.


Steps to Add Validation
-----------------------

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


Follow Along as We Add Validation
---------------------------------

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
