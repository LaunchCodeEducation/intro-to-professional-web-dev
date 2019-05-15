Studio: Making Headlines
========================

Getting Ready: Developer Tools
------------------------------

As you've learned, debugging code is an essential part of coding. When it comes to working with web pages, browser developer tools are indispensable.

This studio requires you to use Firefox's developer tools. In particular, you should be able to:

- Open dev tools
- Inspect an HTML element
- Modify an element's HTML
- Explain the difference between the content displayed when using *View Source* and what's in the *Inspector* tab

.. note:: The `full documentation <https://developer.mozilla.org/en-US/docs/Tools>`_ for Firefox's developer tools covers these items, and much more.

Studio
------

Pick a news site (`The New York Times <https://www.nytimes.com/>`_, for example), and use your browser's developer tools to modify one of the main articles to use a picture and text of your choosing.

Have fun with this (see our example below), but be respectful of others and avoid overtly critical political or social commentary.

.. figure:: figures/making-headlines-sample.png
   :alt: A screenshot of the New York Times website, with a fake article announcing an astronaut apprenticeship program at LaunchCode.

   A Sample Fake Article

.. warning:: 
   
   When linking to an image, pay attention to the protocol, either ``http`` or ``https``, of the site you are modifying, and of the image you are including. You can find the protocol at the beginning of the image URL.

   If the site you are modifying was loaded over ``https`` and your image uses ``http`` then the image may not load properly. You should try to add ``s`` to the image protocol, and if that doesn't work, look for another image or modify a site that uses ``http``.

.. tip:: 

   If you want to use an image of your own that is not already available via the internet, here's how:

   - Upload the photo to a Dropbox account
   - View the photo on `Dropbox <https://www.dropbox.com/>`_ and select *Share*, then *Get link*, then *Go to link*
   - You should now be viewing the image within Dropbox. If the URL contains ``?dl=0``, remove it. Add ``?raw=1`` to the end of the URL in the location bar of your browser and hit *Enter*. The URL should look something like this:

      ::
      
         https://www.dropbox.com/sc/qc3htnhv7fb3i2x/AAC5OzECOyBynstMDWawCZhxa?raw=1
      
   - Copy the URL of the loaded image. You can use this URL within any HTML that you're editing.

Resources
---------

* `Using Firefox's Page Inspector <https://developer.mozilla.org/en-US/docs/Tools/Page_Inspector>`_
* `Firefox DevTools Documentation <https://developer.mozilla.org/en-US/docs/Tools>`_
