xontrib-brace-expansion
=======================
|VERSION|

.. |VERSION| image:: https://img.shields.io/pypi/v/xontrib-brace-expansion
   :target: https://pypi.org/project/xontrib-brace-expansion

Implements simple brace expansion:

.. code:: console

   @ echo a{d,c,b}e
   ade ace abe

Nested expansion is not supported:

.. code:: console

   @ echo /usr/{ucb/{ex,edit},lib/{ex?.?*,how_ex}}
   SyntaxError: Unmatched "}" at line 1, column 16

See also:

* https://www.gnu.org/software/bash/manual/html_node/Brace-Expansion.html

Usage
-----

.. code-block :: console

    xpip install xontrib-brace-expansion
    xontrib load brace_expansion
