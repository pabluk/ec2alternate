============
ec2alternate
============

:author: Pablo SEMINARIO
:version: 0.1

A simple command to alternate two EC2 instances.

ec2alternate provides simple commands to alternate two Amazon EC2 instances
and always point to the last ip address.

You can find more information at https://github.com/pabluk/ec2alternate

Requirements
------------

ec2admin has a easily-met set of requirements.

* Python 2.5+
* boto 2.0+

and only needed to run tests

* mock 0.8.0+

Available commands
------------------

Show instance id and status::

    $ ec2alternate status
    Instance:i-2362e830 running
    Instance:i-5483c012 stopped

Start all ec2 instances at same time::

    $ ec2alternate start
    Instance:i-2362e830 running
    Instance:i-5483c012 running

Stop all ec2 instances at same time::

    $ ec2alternate stop
    Instance:i-2362e830 stopped
    Instance:i-5483c012 stopped

Restart all ec2 instances at same time::

    $ ec2alternate restart
    Instance:i-2362e830 running
    Instance:i-5483c012 running

