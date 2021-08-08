LaunchCode Curriculum Site Template
===================================

This repository is a template for LaunchCode curriculum module sites to be hosted via GitHub Pages, either under `@LaunchCodeEducation`_ or `@LaunchCoderGirl`_.

.. replit:: js
   :slug: control-flow-type-error
   :linenos:

   const input = require('readline-sync');

   let animals = [{name: 'cat'}, {name: 'dog'}];
   let index = Number(input.question("Enter index of animal:"));

   try {
      console.log('animal at index:', animals[index].name);
   } catch(err) {
      console.log("We caught a TypeError, but our program continues to run!");
      console.log("You tried to access an animal at index:", index);
   }

   console.log("the code goes on...");
      
To set up a new curriculum module, see the `curriculum docs`_.

.. _@LaunchCodeEducation: https://github.com/launchcodeeducation
.. _@LaunchCoderGirl: https://github.com/LaunchCoderGirlSTL
.. _curriculum docs: https://education.launchcode.org/curriculum-docs/
