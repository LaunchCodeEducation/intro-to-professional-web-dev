Requests
========

.. index::
   single: HTTP; request

HTTP requests must conform to the structure outlined by the `World Wide Web Consortium (W3C) <https://www.w3.org/>`_. We'll discuss the most important and most commonly-used aspects of HTTP request structure.

A generic HTTP request looks like this:

::

   GET /blog/ HTTP/1.1
   Host: www.launchcode.org
   User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:67.0) Gecko/20100101 Firefox/67.0
   Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
   Accept-Language: en-US,en;q=0.5
   Accept-Encoding: gzip, deflate, br
   DNT: 1
   Connection: keep-alive
   Upgrade-Insecure-Requests: 1
   Cache-Control: max-age=0

   Request Body

The structure has these components:

.. index::
   single: HTTP; request method
   single: HTTP; request headers

#. **Request line:** The first line is the request line. It specifies the **request method**, path, and HTTP version being used.
#. **Request headers:** From line 2 until the first blank line, **request headers** are included as a series of key-value pairs, one per line.
#. **Blank line:** This signifies the end of the request headers.
#. **Request body (Optional):** Below the blank line, the request body takes up the remainder of the HTTP request. 


Request Methods
---------------

The request line is minimal. We have already discussed the path, which specifies the resource being requested. The first part of the request line, the request method, is new to us.

A **request method** specifies the type of action to be carried out on the requested resource. HTTP defines `8 methods <https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol#Request_methods>`_, of which we will only need to use 2: ``GET`` and ``POST``.

The ``GET`` Method
^^^^^^^^^^^^^^^^^^

.. index::
   single: HTTP; GET

Using the ``GET`` method tells the server that we want to simply *retrieve* the resource. This is the most commonly used method. It is used for requests for HTML pages, CSS and JS files, and images. When you click on a link in a web page, you are triggering a ``GET`` request for the linked page.

``GET`` requests generally do not have a body, since they are *asking* rather than *sending* for information.

.. admonition:: Example

   ``GET`` requests are usually used for:

   - Loading a page after typing an address into the browser's address bar
   - Conducting a search via a search engine
   - Loading a page after clicking on a link

The ``POST`` Method
^^^^^^^^^^^^^^^^^^^

.. index::
   single: HTTP; POST

Using the ``POST`` method tells the server that we want to *create* new data on the server. As you will learn in the next chapter, ``POST`` is used when submitting a form. 

``POST`` requests usually have a body, which contains data that the server processes and stores in some fashion.

.. admonition:: Example

   Some common situations that use ``POST`` are:

   - Signing into a web site
   - Sending an email via a web-based email client
   - Making an online purchase

Headers
-------

There are `quite a few request headers <https://en.wikipedia.org/wiki/List_of_HTTP_header_fields#Request_fields>`_, but only a few will be useful to us.

.. list-table:: Common HTTP Request Headers
   :header-rows: 1

   * - Header
     - Purpose
     - Example
   * - ``Host``
     - The domain name or IP address of the server the request should be sent to.
     - ``www.launchcode.org``
   * - ``User-Agent``
     - Information about the client (usually a browser) making the request. The example is for a version of Firefox on a Mac.
     - ``Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:67.0) Gecko/20100101 Firefox/67.0``
   * - ``Accept``
     - The types of data that the client is willing to accept in the response body.
     - ``text/html,image/jpeg``
   * - ``Content-Type``
     - The type of data included in the request body. Usually only used for ``POST`` requests.
     - ``application/json,application/xml``

Body
----

The optional request body may contain any data whatsoever, though it often includes form data submitted via a ``POST`` request. For example, when signing into a web site, the request body will contain your username and password. We will later learn that it can contain other data formats such as XML and JSON.

As mentioned above, ``GET`` requests generally do *not* have a body.

Check Your Understanding
------------------------
   
.. admonition:: Question

   Visit `Wikipedia's article on HTTP request headers <https://en.wikipedia.org/wiki/List_of_HTTP_header_fields#Request_fields>`_. Which request header is used to set cookies? (Cookies are small pieces of data related to your interaction with a web site.)
