Codenode operations
===================
Tools for Codenode site, releases, docs, etc. 
(These tools are incomplete, but a good start in each section)



Setup
-----

1) Create a virtualenv with deps:
    $ virtualenv --no-site-packages codenode-opts_env && pip -E codenode-opts_env install -U boto fabric jinja2 sphinx 


Backend
-------



Deployment of live.codenode.org
===============================


Frontend
--------


Backend
-------
0) cp .skeleton-deploy-environ.sh to deploy-environ.sh and fill in values

1) source deploy-environ.sh #contains all environ variable *not* to be harcoded in source





Release Management
==================


codenode releases
-----------------


Docs
----
cd into "docs" directory and run the Fabric command
"fab" as desribed in the top of the "fabfile.py".



codenode.org website
====================

