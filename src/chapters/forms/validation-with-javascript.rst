Validation with JavaScript
==========================

Validating form inputs *before* submitting the form can make the user experience much
smoother. Some input types have built-in browser validation for basic formats such as
numbers and email addresses. We can use event handlers to perform more complex
validation on form input values.


Form Inputs and the DOM
-----------------------
Before we can validate what the user has typed we need to understand how to use
form inputs with the DOM. Remember that the DOM is a JavaScript representation of
the HTML document. ``<input>`` tags can be selected and referenced like any other
HTML element.

To read the value of an ``input``, we can check the ``value`` attribute. We can
also assign a new value to ``input.value`` which will update the value shown in the input.

.. admonition:: Example

   This example will log the value of an input, update the input's value, and then log it again
   when the button is clicked.

   .. replit:: html
      :slug: dom-input-example
      :linenos:

      <!DOCTYPE html>
      <html>
      <head>
            <title>Check input value with DOM</title>
      </head>
      <body>
         <form>
            <label>Language
               <input type="text" name="language" id="language" value="JavaScript">
            </label>
         </form>
         <button id="update">Update Input Value</button>
         <script>
            let button = document.getElementById("update");
            // add event handler for when button clicked
            button.addEventListener("click", function() {
               let input = document.getElementById("language");
               console.log(input.value);
               // now update the value in the input
               input.value = input.value + " rocks!";
               console.log(input.value);
            });
         </script>
      </body>
      </html>

.. admonition:: Question

   What happens when you click the button multiple times?


Steps to Add Validation
-----------------------

1. Add an event handler for the ``window`` *load* event
2. Within the window's load handler, add an event handlerAdd an event handler for the ``form`` *submit* event
3. Retrieve input values that need to be validated from the DOM.
4. Within the form's submit handler, check the ``input`` values using conditional statements

   a. If the values are valid, allow the form submission
   b. If the values are NOT valid, inform the user and STOP form submission

Each of these steps involves additional details, which we will now break down.

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
            <form method="POST" action="https://handlers.education.launchcode.org/request-parrot">
               <label>Username <input type="text" name="username"></label>
               <label>Team Name <input type="text" name="team"></label>
               <button>Submit</button>
            </form>
         </body>
      </html>


Follow Along as We Add Validation
---------------------------------

Use `this repl.it <https://repl.it/@launchcode/form-validation>`_ and the following instructions
to add validation to the above example.

**Get Reference to Inputs**

To validate what the user has typed, we can get a reference to the ``input`` elements in
the DOM and check the ``value`` property of each. Let's change the *submit* event handler to display the
value of the username input in an ``alert`` box. To do that, we are going to use
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

**Alert the Input Values When Submitted**

Now that we know how to get the value of an input, we can add *conditional statements*.
Let's add code that opens an alert box if *either* input value is *empty*.

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
then an alert message appears telling you that both inputs are required. However, the form is
still submitted even if the data is invalid.

**Prevent Form Submission**

.. index:: ! preventDefault
   single: event; preventDefault

We should prevent the form submission from happening until all
inputs have valid values. We can use the ``event`` parameter and
``event.preventDefault()`` to stop the form submission. ``event.preventDefault()``
prevents default browser functionality from happening, like form submission
when ``<button>`` tags are clicked inside of a form. Remember that *event handler* functions
are passed an ``event`` argument which represents the event that the handler is responding to.

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


Check Your Understanding
------------------------

.. admonition:: Question

   What method on the ``event`` object can be used to stop a form submission?
