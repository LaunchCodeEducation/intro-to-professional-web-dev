Studio: Fetch & JSON
====================

Requirements

* Make a request to astronauts API https://api.education.launchcode.org/astronauts
* Use HTML template to add each astronaut to web page


Example JSON

.. sourcecode:: js
   :linenos:

   {
        "id": 5,
        "active": false,
        "firstName": "Sally",
        "lastName": "Ride",
        "skills": [
            "Physicist", "Astrophysics"
        ],
        "hoursInSpace": 343,
        "picture": "sally-ride.jpg"
    }

Example HTML created for each astronaut. Notice the CSS classes used.

.. sourcecode:: html
   :linenos:

   <div class="astronaut">
      <div class="bio">
         <h3>Mae Jemison</h3>
         <ul>
         <li>Hours in space: 190</li>
         <li>Active: false</li>
         <li>Skills: Physician, Chemical Engineer</li>
         </ul>
      </div>
      <img class="avatar" src="images/mae-jemison.jpg">
   </div>

.. figure:: figures/studio-example-page.png
       :alt: Screen shot showing what result of studio should look like.

       Example of what resulting page should look like.
