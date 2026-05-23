xontrib-brace-expansion
=======================
|VERSION|

.. |VERSION| image:: https://img.shields.io/pypi/v/xontrib-brace-expansion
   :target: https://pypi.org/project/xontrib-brace-expansion

Implements Bash-style brace expansion:

.. code:: console

   @ echo a{d,c,b}e
   ade ace abe

.. code:: console

   @ echo /usr/{ucb/{ex,edit},lib/{ex?.?*,how_ex}}
   /usr/ucb/ex /usr/ucb/edit /usr/lib/ex?.?* /usr/lib/how_ex

See also:

* https://facelessuser.github.io/bracex/
* https://www.gnu.org/software/bash/manual/html_node/Brace-Expansion.html

Usage
-----

.. code-block :: console

    xpip install xontrib-brace-expansion
    xontrib load brace_expansion
