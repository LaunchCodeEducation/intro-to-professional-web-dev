The DOM
=======
.. index:: ! DOM

.. index::
   single: DOM; Document Object Model

You may remember from earlier chapters that classes represent specific entities.
The **Document Object Model (DOM)** is a set of objects that represent the browser and the documents that make up the web page.
The DOM objects are instances of classes that model the structure of the browser, HTML document, HTML elements, element attributes, and CSS.
The below figure depicts the parent-child relationships between the DOM objects that make up a web page.

.. figure:: figures/html-dom-tree.png
   :alt: Figure showing the tree-like relationship between the document of the DOM and HTML elements on the page.

Global DOM Variables
--------------------
.. index::
   pair: variable; global

To utilize the DOM in JavaScript, we need to use the DOM global variables.
In the next section, we will learn more about the DOM global variables, including their type. 
For now, let's get used to the idea of using JavaScript to interact with the DOM.

To start, we are going to use the ``window`` and ``document`` global variables.
As mentioned above, we will go into more detail on these variables and what they are later.

.. admonition:: Example

   Here the ``window`` and ``document`` variables are used to print information about the web page to the browser's console.

   .. sourcecode:: html
      :linenos:

      <!DOCTYPE html>
      <html>
      <head>
            <title>Using DOM Variables</title>
            <script>
               console.log("the page title:", document.title);
               console.log("the protocol:", window.location.protocol);
            </script>
      </head>
      <body>
            contents
      </body>
      </html>

   **Console Output**

   ::

      the page title: Using DOM Variables
      the protocol: https:


Dynamic Web Page Using the DOM
------------------------------
The DOM plays a key part in making web pages dynamic.
Since the DOM is a JavaScript representation of the web page, you can use JavaScript to alter the DOM and consequently, the web page.
The browser will re-render, which is not the same thing as reloading, the web page anytime changes are made via the DOM.

In order to add or edit HTML elements with code, we need to be able to access them.
The method ``document.getElementById`` will search for a matching element and return a reference to it.
We will go into more detail on how this method works in the next section.

.. admonition:: Example

   We can use ``document.getElementById`` and ``element.append`` to add text to a ``<p>`` tag.

   .. sourcecode:: html
      :linenos:

      <!DOCTYPE html>
      <html>
      <head>
            <title>Add content using DOM</title>
      </head>
      <body>
            <p id="main-text">Words about things...</p>
            <script>
               let p = document.getElementById("main-text");
               p.append("More words about things");
               console.log(p.innerHTML);
            </script>
      </body>
      </html>

   **Console Output**

   ::

      Words about things... More words about things

Where to Put the ``<script>``
-----------------------------

In the previous example, notice the ``<script>`` is placed below the ``<p>`` tag in the HTML document.
HTML documents are executed top down, therefore, a ``<script>`` tag must come after any other elements that will be affected by the code inside the ``<script>``.
Later in the chapter, we will learn about another way to handle this.

Check Your Understanding
------------------------

.. admonition:: Question

   What do the DOM objects represent?

   a. Word documents you have downloaded
   b. Directives of memory
   c. The browser window, HTML document, and the elements

.. admonition:: Question

   What is the difference between the document and window variables?
