.. _strings-exercise-solutions:

Exercise Solutions: Strings
======================================

.. _strings-exercise-solutions1:

Part One
--------

1. Identify the result for each of the following statements:

a. ``'JavaScript'[8] = 'p'``

c. ``"Wonderful".length = 9``

*There's no code snippet for this one, just try it on your own with old-fashioned pen and paper!*

2. The ``length`` method returns how many characters are in a string. However, the method will NOT give us the length of a number. If ``num = 1001``, ``num.length`` returns ``undefined`` rather than 4.

a. Use type conversion to print the length (number of digits) of an integer.

.. sourcecode:: js

		let num = 1001; 

c. What if ``num`` could be EITHER an integer or a decimal?  Add an ``if/else`` statement so your code can handle both cases.  (Hint: Consider the ``indexOf()`` or ``includes()`` string methods).

.. sourcecode:: js
	:linenos:

	if (String(num).includes('.')){
	console.log(String(num).length-1);
	} else {
	console.log(String(num).length);
	}

:ref:`Back to the exercises <exercises-strings>`.

.. _strings-exercise-solutions2:

Part Two
--------

#. Remember, strings are *immutable*. Consider a string that represents a strand of DNA: ``dna = " TCG-TAC-gaC-TAC-CGT-CAG-ACT-TAa-CcA-GTC-cAt-AGA-GCT    "``. There are some typos in the string that we would like to fix:

a. Use the ``trim()`` method to remove the leading and trailing whitespace, and then print the results.	

.. sourcecode:: js
	:linenos:

	let dna = " TCG-TAC-gaC-TAC-CGT-CAG-ACT-TAa-CcA-GTC-cAt-AGA-GCT    ";
	let newString = dna.trim();
	console.log(newString);


c. Note that if you try ``console.log(dna)`` after applying the methods, the original, flawed string is displayed. To fix this, you need to *reassign* the changes back to ``dna``. Apply these fixes to your code so that ``console.log(dna)`` prints the DNA strand in UPPERCASE with no whitespace.

.. sourcecode:: js
	:linenos:

	let dna = " TCG-TAC-gaC-TAC-CGT-CAG-ACT-TAa-CcA-GTC-cAt-AGA-GCT    ";
	dna = dna.trim().toUpperCase();
	console.log(dna);


#. Let's use string methods to do more work on the DNA strand:

a. Replace the sequence ``'GCT'`` with ``'AGG'``, and then print the altered Sstrand.

.. sourcecode:: js
	:linenos:

	dna = dna.replace('GCT','AGG');
	console.log(dna);


c. Use ``slice()`` to print out the fifth set of 3 characters (called a **codon**) from the DNA strand.

.. sourcecode:: js

	console.log(dna.slice(16,19)); 

e. Just for fun, apply methods to ``dna`` and use another template literal to print, ``'taco cat'``.

.. sourcecode:: js

	console.log(`${dna.slice(4,7).toLowerCase()}o ${dna.slice(dna.indexOf('CAT'),dna.indexOf('CAT')+3).toLowerCase()}`);

:ref:`Back to the exercises <exercises-strings>`

.. _strings-exercise-solutions3:

Part Three
----------

1. If we want to turn the string ``'JavaScript'`` into ``'JS'``, we might try ``.remove()``. Unfortunately, there is no such method in JavaScript. However, we can use our cleverness to achieve the same result.	

a. Use string concatenation and two ``slice()`` methods to print ``'JS'`` from ``'JavaScript'``.

.. sourcecode:: js
	:linenos:

	let language = 'JavaScript';
	console.log(language.slice(0,1)+language.slice(4,5));


c. Use bracket notation and a template literal to print, ``"The abbreviation for 'JavaScript' is 'JS'."``

.. sourcecode:: js

	console.log(`The abbreviation for '${language}' is '${initials}'.`)

:ref:`Back to the exercises <exercises-strings>`

