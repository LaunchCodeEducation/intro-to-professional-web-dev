Studio: HTTP and Forms
======================

Introduction
------------

This chapter taught you that forms submit data in HTTP requests. This studio uses form and HTTP concepts to build a *search engine selector*, that is, a search form that allows a user to choose which search engine they would like to use. It will look like this:

.. figure:: figures/search-engine-selector.png
   :alt: A form with a text input and radio buttons corresponding to various search engines.

   The search engine selector that we will build.

Most search engines work the same way. The have a single text input, and they submit data using a ``GET`` request. Additionally, many of the most popular search engines also use the same name for the search parameter, ``q``. 

.. admonition:: Try It!

   Use 2-3 different search engines to search for the same term. On the results page, look at the URL. Did the search happen via ``GET`` or ``POST``? If a ``GET`` request was made, what is the name of the parameter containing your search term?

   *Note:* You may have to copy/paste the URL into a text editor to find the search parameter. Some engines add other parameters to the URL, causing it to extend past the end of the browser's address bar.

.. note:: We remarked previously that most forms use ``POST`` because they cause data to be changed on the server. A web search only *retrieves* data. It does not change data. Therefore it's safe to use a ``GET`` request for searches.

The fact that most search engines use the name ``q`` for their search boxes will allow us to easily create a form that is capable of sending a search request to several search engines.

The form will send a request with query parameter ``q`` to the selected engine. Since this request looks essentially the same as requests coming from the search engine's own form (for examle, at `google.com <https://google.com>`_) it will give us back the results the same as if we had searched via those sites. 

Getting Started
---------------

Fork the `starter code for this studio <https://repl.it/@launchcode/Forms-Studio>`_, which has some basic HTML to get you started. 

Create Form Inputs
------------------

Let's build out the form. We will need some data for the search engines we want to work with.

.. list-table:: Search Engine Options
   :header-rows: 1

   * - Label
     - Value
     - Searh URL
   * - Google
     - ``google``
     - https://www.google.com/search
   * - DuckDuckGo
     - ``duckDuckGo``
     - https://duckduckgo.com/
   * - Bing
     - ``bing``
     - https://www.bing.com/search
   * - Ask
     - ``ask``
     - https://www.ask.com/web

- Create a text input within the form and set its ``name`` attribute to the value ``q``.
- Create a radio group with one radio button for each search engine. Recall that radio buttons with the same ``name`` are grouped, so use the same value for this attribute, ``"engine"``, on each radio button.
- Create a ``label`` element for each radio button.

Finally, add a submit button to the form and set it's ``value`` to ``"Go!"``. 

.. admonition:: Question

   How is the ``value`` attribute of a submit button used?

Submit Event Handler
--------------------

Pop quiz:

.. admonition:: Question

   What happens if you try to submit the form at this point? Why? 

.. admonition:: Question

   Which HTTP method will be used when submitting the form? 

We now have a form with inputs that has nowhere to send its data. The ``action`` attribute determines where a form submits data, but we can't set the ``action`` attribute on the form in our HTML. Our form needs to submit data to a different site based on the selected search engine. 

To make this happen, we need to set the value of the form's ``action`` *after* the user hits the submit button, but *before* the form request is sent. Forms trigger a ``submit`` event at precisely this moment. Therefore, we can create an event handler to solve this problem. Our handler will:

#. Retrieve the selected value from the radio group.
#. Use this value to determine the ``action`` URL, based on the selected search engine.
#. Set the ``action`` attribute of the form.

Create and Register the Handler
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Within the ``<script>`` element near the top of the file, create a function named ``setSearchEngine``. We will code this function later, so for now just add a ``console.log`` statement so we can see when it runs.

Near the bottom of the ``<script>`` element is the stub:

.. sourcecode:: js
   :linenos:

   window.addEventListener('load', function(){
        // TODO: register the handler
    });

Replace the TODO with code to add ``setSearchEngine`` as a handler to the form's ``submit`` event. You will first need to get the form element using one of the DOM methods.

.. note:: The event handler can be added only after the form has been built, so we do so by adding a ``load`` event handler to the ``window``. This ensures that the event is registered *after* the page has loaded.

Before moving on, make sure the code you just wrote works. Submit the form and look for a message in the console to verify that ``setSearchEngine`` ran.

Set the ``action``
^^^^^^^^^^^^^^^^^^

Our event handler now runs when the form is submitted, but it doesn't do anything. We would like it to set the ``action`` on the form based on the user's choice of search engine.

Add code to ``setSearchEngine`` to get the selected radio button element, using ``document.querySelector``. The selector you'll need is a little complicated, so we'll give it to you here:

::

   input[name=engine]:checked

This compound CSS selector combines an *attribute* selector with a *pseudo selector*. The attribute selector ``input[name=engine]`` matches all ``input`` elements with the attribute ``name`` equal to ``"engine"``. The pseudo selector ``:checked`` specifies that we only want the selected element from that group of matches. Combined, the selector gives us the selected element in the radio group.

Once you have the selected radio button, get it's value using ``.value``. The value tells us which search engine the user has chosen.

At this stage, we could use a large ``if``/``else if``/``else`` statement to determine the URL for the selected search engine.

::

   let actionURL;

   if (engine === "google") {
      actionURL = "https://www.google.com/";
   } else if (engine === "bing") {
      actionURL = "https://duckduckgo.com/";
   }

   // ... and so on ...

This is ugly and inefficient. A better approach is to create an object to store the engine values and URLs as key/value pairs. For a single engine, the object would look like:

.. sourcecode:: js
   :linenos:

   let actions = {
      "google": "https://www.google.com/"    
   };

Add this to your code, and fill it out to include the other three engines.

Now, you can get the action URL using ``action``, bracket notation,  and the value of the selected radio button. Once you have the action URL, find the form element and set its action using ``setAttribute``.

If everything went well, your search engine selector page should now work! If not, that's okay. Switch to debugging mode and figure out what needs fixing.

Bonus Missions
--------------

#. Add validation to your submit handler to make sure that the user has both selected a search engine and entered a (non-empty) search term.
#. Add some CSS rules to your page to make it look nice.
