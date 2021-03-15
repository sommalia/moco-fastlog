Moco Fastlog
============

Moco fastlog  is a simple helper script to create activities
directly via the command line.

Requirements
------------

* click
* moco-wrapper Version 0.9.0 or above

Installation
------------

Install the requirements via pip

.. code-block:: shell

    $ pip install -r requirements.txt

Usage and Setup
----------------

Before you can use this script you have to export two environment
vars for authentication.

.. code-block:: shell

    $ export MOCO_FASTLOG_API_KEY=abcdefghijkl

Your can find your Api token in your moco user profile.

Also you will have to export your moco-Subdomain. For example if your
moco-Domain ist *example.mocoapp.com* we export the following environment
variable.

.. code-block:: shell

    $ export MOCO_FASTLOG_DOMAIN="example"

After we exported these values we can start our script.

.. code-block:: shell

    $ python3 iflog.py


You will be presented with a list of projects. Select the one your want
to log time for.

::

    [0] First Customer => My first Project
    [1] Second Customer => My second Project
    [2] Third Customer => My third Project
    > Which Project would you like to log time on?: 1
    Project "My second Project" selected

After selecting the project we also have to select the project task.

::

    [0] Development
    [1] Other
    > Which Task would you like to log time on?: 0
    Create Activity for Project "My second Project", Task "Development".

Now we enter the final information for our new activity, description and the
time we want to log.

::

    > Activity Description: Fastlog setup
    > Activity Time (Enter in Hours, 0.5 for 30m): 0.5
    Time logged successfully

Loading authentication info from config file
--------------------------------------------

As an alternative to setting environment variables you can also load your api key and domain from a .json config file.
The file holds the same variables we would otherwise set as environment vars.

.. code-block:: javascript

    {
        "api_key" : "REPLACE_ME",
        "domain": "REPLACE_ME"
    }

After you have created the config file, invoke the script like this.

.. code-block:: shell

    $ python iflog.py --config /path/to/my/configfile.json




