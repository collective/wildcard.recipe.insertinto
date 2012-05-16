Introduction
============

The package is meant to be used to insert text into files via buildout.

Example usage
-------------

Insert text::

  [insertinto]
  recipe = wildcard.recipe.insertinto
  example = ${buildout:directory}/file.conf insert-before "foo" "bar"
  example2 = ${buildout:directory}/file.conf insert-after "foo" "bar"
