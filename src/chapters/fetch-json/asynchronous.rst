Asynchronous and Promises
=========================
.. index:: ! asynchronous

.. index:: ! AJAX

.. index::
   single: AJAX; Asynchronous JavaScript and XML

In order to fully explain how the ``fetch`` function works, we need to define
and talk about the terms **asynchronous** and **synchronous**.

    Asynchronous: Not simultaneous or concurrent in time.

    Synchronous: Simultaneous or concurrent in time.

When fetching data in JavaScript, the HTTP requests are asynchronous. In brief, that 
means when an HTTP request is sent, we don't know exactly when a response will be 
received by the browser. Remember that HTTP requests are sent to an address, then a 
response is sent. That process takes a variable amount of time depending on network 
speed, the address location, and response size.

.. note::

   These requests are also called **AJAX requests** (Asynchronous JavaScript and XML). 
   The XML part of AJAX refers to a data format that was popular before JSON.


Response Handlers
-----------------
Browsers can't stop everything and wait for a response to an HTTP request. Browsers 
have to render HTML, interact with the user, and run JavaScript. To keep these 
processes running seamlessly, without any noticeable pauses, the browser relies on 
events.

This is where ``.then()`` and the response handler function come in. The browser 
provides us with a way to handle the response whenever it is received.


Promises and the ``then`` Function
----------------------------------
.. index:: ! promise

.. index::
   single: asynchronous; promise

Let's look again at a simple ``fetch`` example. Notice on line 1 that ``then`` is 
called on the value returned from ``fetch``.

.. sourcecode:: js
   :linenos:

   fetch('https://api.education.launchcode.org/weather').then( function(response) {
      console.log(response);
   } );

To make it clearer, let's capture the value returned by ``fetch`` in a variable 
named ``promise``.

.. sourcecode:: js
   :linenos:

   const promise = fetch('https://api.education.launchcode.org/weather');
   promise.then( function(response) {
      console.log(response);
   } );

``fetch`` returns an instance of the ``Promise`` class. The **Promise** class represents
a future event that will eventually occur. In the above example, ``promise`` represents
the eventual response from the HTTP request to ``https://api.education.launchcode.org/weather``.

A promise can be fulfilled or rejected. When a promise is fulfilled, data is passed 
to the response handler function. The ``then`` method of a promise defines what will 
happen when the promise is fulfilled. When a promise is rejected, an error reason is 
provided.

The above example can be translated to these steps

#. Make an HTTP request to ``https://api.education.launchcode.org/weather``
#. When the response is received, THEN run the response handler function (passing in response data)
#. In the response handler function, console log the ``response`` object

More Promises
-------------
Promises are used for more than HTTP requests. A promise can represent any future event.
The ``response`` object has a ``json()`` function that will return the JSON data in the
response. The ``json()`` function returns a promise that represents the future result 
of turning the response data into JSON.

The below example involves two promises. One promise on line 1 that represents the 
fetch request and a second on line 3 that represents the response data being turned 
into JSON.

Finally on line 5, the JSON data can be logged.

.. sourcecode:: js
   :linenos:

   const promise = fetch('https://api.education.launchcode.org/weather');
   promise.then( function(response) {
      const jsonPromise = response.json();
      jsonPromise.then( function(json) {
         console.log("temp", json.temp);
      });
   } );

.. tip::

   Promises can be a hard concept to understand. Focus on the examples and the theory will
   make sense in time.


Check Your Understanding
-------------------------

.. admonition:: Question

   True or False, we know exactly when an asynchronous request will return?


.. admonition:: Question

   True or False, a Promise can represent any future event?

.. admonition:: Question

   True or False, ``then`` is a method of the ``Promise`` class that allows us to run code
   after an event is completed?
