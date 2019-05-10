Exercises: More Functions
==========================

Practice Yer Skills
--------------------

Arrr! Welcome back, swabbie. Ye be almost ready fer yer next task---earning
gold fer yer cap'n.

First, ye need to show what ye've learned.

Complete the Map
^^^^^^^^^^^^^^^^^

Not THAT kinda map, ye rat! Fold that up and do the following:

1. Create an anonymous fucntion and set it equal to a variable. Yer function
   should:

   a. If passed a number, return the tripled value.
   b. If passed a string, return the string "ARRR!"
   c. If NOT passed a number or string, return the data unchanged.
   d. `Build yer function here <https://repl.it/@launchcode/MoreFunctionsExercises02>`__, and be sure to test it.

|

2. Add to yer code! Use yer fuction and the :ref:`map method <map-method>` to
   change the array ``['Elocution', 21, 'Clean teeth', 100]`` as follows:

   a. Triple all the numbers.
   b. Replace the strings with "ARRR!"
   c. Print the new array to confirm yer work.

Raid Yonder Shuttle
--------------------

Shiver me timbers! Ye did well. Yer ready ta join a boarding party.

Ye may still be wonderin' *Why the blazes would I ever use an anonymous
function?* Fer today's mission, o' course! We arrrr going to loot yonder
shuttle, but since it's the 21st century, we need to do better than grappling
hooks and rope.

| Ye arrrr going to hack into the shuttle code and steal supplies. Since the
   LaunchCode TAs keep a sharp eye on the goodies, ye can't just add new
   functions like ``siphonFuel`` or ``lootCargo``. Ye need to be more sneaky.
| Clever.
| Invisible.
| *Anonymous*.

The first mate swiped a copy of the code ye need ta hack:

.. sourcecode:: js
   :linenos:

   function checkFuel(level) {
      if (level > 100000){
         return 'green';
      } else if (level > 50000){
         return 'yellow';
      } else {
         return 'red';
      }
   }

   function holdStatus(arr){
      if (arr.length < 7) {
         return `Spaces available: ${7 - arr.length}`;
      } else if (arr.length > 7){
         return `Over capacity by ${arr.length - 7} items.`
      } else {
         return "Full";
      }
   }

   let fuelLevel = 200000;
   let cargoHold = ['meal kits', 'space suits', 'first-aid kit', 'satellite', 'gold', 'water', 'AE-35 unit'];

   console.log("Fuel level: "+ checkFuel(fuelLevel));
   console.log("Hold status: "+ holdStatus(cargoHold));

Click here to `hack the code <https://repl.it/@launchcode/MoreFunctionsExercises01>`__.

|

1. First, steal some fuel from the shuttle:

   a. Define an anonymous function and set it equal ter a variable with a normal,
      non-suspicious name.  The function needs one parameter, which will be the
      fuel level on the shuttle.
   b. Ye must siphon off fuel without alerting the TAs.  Inside yer function, ye
      want to reduce the fuel level as much as possible WITHOUT changing the
      color returned by the ``checkFuel`` function.
   c. Once ye figure out how much fuel ter pump out, return that value.
   d. Decide where to best place yer function call to gather our new fuel.
   e. Be sure to test yer function! Those bilge rat TAs will notice if they lose
      too much fuel.

|

2. Next, liberate some of that glorious cargo.

   a. Define another anonymous function with an array as a parametarrrrr, and set
      it equal to another innocent variable.
   b. Ye need to swipe two items from the cargo hold.  Choose well. Stealing water
      ain't gonna get us rich.  Put the swag into a new array and return it
      from the function.
   c. The cargo hold has better security than the fuel tanks.  It counts how many
      things are in storage.  Ye need to replace what ye steal with something
      worthless.  The count MUST stay the same, or ye'll get caught and thrown
      into the LaunchCode brig.
   d. Don't get hasty, swabbie! Remember to test yer function.

|

3. Finally, ye need to print a receipt for the accountant. Don't laugh! That
   genius knows MATH and saves us more gold than ye can imagine.

   a. Define a function that takes yer fuel and cargo functions as
      parametarrrrrs.
   b. Use a template literal to print out, ``"Raided _____ kg of fuel from the
      tanks, and stole ____ and ____ from the cargo hold."``
