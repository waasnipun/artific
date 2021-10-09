=======
artific
=======


.. image:: https://img.shields.io/pypi/v/artific.svg
        :target: https://pypi.python.org/pypi/artific

.. image:: https://img.shields.io/travis/waasnipun/artific.svg
        :target: https://travis-ci.com/waasnipun/artific

.. image:: https://readthedocs.org/projects/artific-doc/badge/?version=latest
        :target: https://artific-doc.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status




Python libray for efficient algorithms


* Free software: MIT license
* Documentation: https://artific-doc.readthedocs.io.


Features
--------
* Lists, arrays and trees
    * Sorting
        * **Bubblesort** - *For each pair of indices, swap the items if out of order.*
        * **Mergesort** - *Sort the first and second half of the list separately, then merge the sorted lists.*
        * **Heapsort** - *Convert the list into a heap, keep removing the largest element from the heap and adding it to the end of the list.*
        * **Insertionsort** - *Determine where the current item belongs in the list of sorted ones, and insert it there.*
        * **Quicksort** - *Divide list into two, with all items on the first list coming before all items on the second list.; then sort the two lists. Often the method of choice.*
        * **Selection sort** - *Pick the smallest of the remaining elements, add it to the end of the sorted list.*
        * **Pigeonhole sort.** - *Fill an empty array with all elements of an array to be sorted, in order.*
        * **Binary tree sort.** - *Sort of a binary tree, incremental, similar to insertion sort.*
Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
