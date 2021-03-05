Moco Fastlog
============

The moco fastlog script is a simple helper script to create activities
directly via the command line.

Requirements
------------

* click
* moco-wrapper Version 0.9.0 or abobe

Installation
------------

Install the requirements via pip

```bash
$ pip -r requirements.txt
```

Usage and Setup
----------------

Before you can use this script you have to export two environment
vars for authentication.

```bash
$ export MOCO_FASTLOG_API_KEY=abcdefghijkl
```

Your can find your Api token in your moco user profile.

Also you will have to export your moco-Subdomain. For example if your
moco-Domnain ist example.mocoapp.com we export the following environment
variable.

```bash
$ export MOCO_FASTLOG_DOMAIN="example"
```

After we exported these values we can start our script.

```bash
python3 iflog.py
```

You will be presented with a list of projects. Select the one your want
to log time for.

```bash
[0] My first Project
[1] My second Project
[2] My third Project
> Which Project would you like to log time on?: 1
Project "My second Project" selected
```

After selecting the project we also have to select the project task.

```bash
[0] Development
[1] Other
> Which Task would you like to log time on?: 0
Create Activity for Project "My second Project", Task "Development".
```

Now we enter the final information for our new activity, description and the
time we want to log.

```bash
> Activity Description: Fastlog setup
> Activity Time (Enter in Hours, 0.5 for 30m): 0.5
Time logged successfully
```

