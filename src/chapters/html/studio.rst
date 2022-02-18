Studio: Making Headlines
========================

Studio Setup
------------

In this course, we will mostly use Firefox as our browser. 
If you haven't installed Firefox, you can get it from `Mozilla <https://www.mozilla.org/en-US/firefox/new/>`_. 
Other browsers have good developer tools as well (Chrome, in particular) but we're going to stick with Firefox. 
If you are more comfortable with another browser, you'll find that most of the developer tools functionality exists in other browsers' dev tools as well.

Firefox's developer tools contain a lot of functionality, and we will only begin to touch on it here, 
learning more of its functionality later in the unit. In this class, we'll learn about the tools available for working with HTML elements

Getting Ready: Developer Tools
------------------------------

As you've learned, debugging is an essential part of coding. When it comes to debugging web pages, browser developer tools are indispensable.

This studio requires you to use Firefox's developer tools. In particular, you should be able to:

- Open Firefox's dev tools
- Inspect an HTML element
- Modify an element's HTML
- Explain the difference between the content displayed when using *View Source* and what you see in the *Inspector* tab

.. note:: The `full documentation <https://developer.mozilla.org/en-US/docs/Tools>`_ for Firefox's developer tools covers these items, and much more.

Studio
------

Pick a news site (`The New York Times <https://www.nytimes.com/>`_, for example), and use your browser's developer tools to modify one of the main articles to use a picture and text of your choosing.

Have fun with this, but be respectful of others and avoid overtly critical political or social commentary.

You might do something like this:

.. figure:: figures/making-headlines-screenshot.png
   :alt: A screenshot of the New York Times website, with a fake article announcing an astronaut apprenticeship program at LaunchCode.

   A Sample Fake Article

Image URLs
^^^^^^^^^^

When linking to an image, pay attention to the protocol of both the site you are modifying and of the image you are including. The protocol will be either ``http`` or ``https``.

If the site loads over ``https`` and your image uses ``http`` then the image may not load properly due to browser security restrictions. You should try to add ``s`` to the image protocol, and if that doesn't work, look for another image.

Resources
---------

* `Using Firefox's Page Inspector <https://developer.mozilla.org/en-US/docs/Tools/Page_Inspector>`_
* `Firefox DevTools Documentation <https://developer.mozilla.org/en-US/docs/Tools>`_

Bonus Mission
-------------

Try adding your own image! If you want to use an image of your own that is not already available via the internet, here's how:

- Upload the photo to a `Dropbox <https://www.dropbox.com/>`_ account. You can use Dropbox Basic for this!
- View the photo on Dropbox and select *Share*, then *Get link*, then *Go to link*
- You should now be viewing the image on the Dropbox site. If the URL contains ``?dl=0``, remove it. Add ``?raw=1`` to the end of the URL in the location bar of your browser and hit *Enter*. The URL should look something like this:

::

   https://www.dropbox.com/sc/qc3htnhv7fb3i2x/AAC5OzECOyBynstMDWawCZhxa?raw=1

- Copy the URL of the loaded image. You can use this URL within any HTML.
