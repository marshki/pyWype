======
pyWype
======
.. image:: https://api.codacy.com/project/badge/Grade/78a1649abd3144369e66326394211ea3    
  :target: https://www.codacy.com/app/marshki/pyWype?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=marshki/pyWype&amp;utm_campaign=Badge_Grade

.. image:: https://img.shields.io/badge/Made%20with-Python-1f425f.svg
   :target: https://www.python.org/

.. image:: https://img.shields.io/badge/License-MIT-blue.svg
   :target: https://lbesson.mit-license.org/

.. image:: https://badges.frapsoft.com/os/v3/open-source.svg?v=103
   :target: https://github.com/ellerbrock/open-source-badges

Securely wipe storage drives and partitions 
-----------------------------------------------------------------------------
Disk-wiping utility for GNU/Linux, written in Python 2 & 3. 

**THIS SOFTWARE WILL IRRECOVERABLY WIPE DATA FROM YOUR DRIVE. USE CAUTION.**

Requirements
------------
pyWype is tested to run in Python 2.7 and Python 3.4 on GNU/Linux. 

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
