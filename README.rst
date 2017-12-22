======
pyWype
======
.. image:: https://img.shields.io/badge/License-MIT-yellow.svg
  :target: https://opensource.org/licenses/MIT

Python utility to securely wipe storage drives and partitions in Linux.
-----------------------------------------------------------------------------
** THIS SOFTWARE WILL IRRECOVERABLY WIPE DATA FROM YOUR DRIVE. USE CAUTION **

Requirements
------------
pyWype is tested to run in Python 2.7 and Python 3.4 on Linux.

In Linux, install pv_ via your package manager:

.. _pv: http://www.ivarch.com/programs/pv.shtml

+------------------+--------------+
|apt               |yum           |
+==================+==============+
|apt-get install -y|dnf install -y|
|pv 	           |pv            |
+------------------+--------------+

Install Python requirements:
::
    pip install -r requirements.txt

Usage
-----

TODO
----
- [ ] Add quit at any time option
- [ ] Support multiple drive wipes?
- [ ] Unit tests & integration with Travis-CI_

.. _Travis-CI: https://travis-ci.com

Change Log
----------
.. -CHANGELOG: https://github.com/marshki/pyWype/blob/master/CHANGELOG.rst

LICENSE
-------
LICENSE_

.. -LICENSE: https://github.com/marshki/pyWype/blob/master/LICENSE
