Here are the instructions for installing grok from github for Python 2.7 and for Python 3.3

I like to install in /usr/local

     $cd /usr/local

First get the zopache.grokproject from github

    $wget --no-check-certificate https://github.com/clozinski/grok.install/archive/master.zip

Unzip it. 

    $unzip master.zip

Move it to a better location.

    $mv grok.install-master grok

Enter the directory.

   $ cd grok

In a moment we will run the bootstrap command.  This creates the buildout command which will actually create eveyrthing.  Python can be py7thon2.7  I usually do this in a virtualenv.  make sure that you have the most recent versin of virtualenv

   $ easy_install -U virtualenv

Crete a Virtual Environment.
     $virtualenv -p python2.7  virt

Start your Virtual Environment.
      $#source virt/bin/activate.csh

Make sure that you nave the newest version of setuptools
     $easy_install -U setuptools

Bootstrap the buildout environment::

    $ python bootstrap.py

and run the buildout command::

    $ bin/buildout
    [lots of stuff will be downloaded and installed here]
    While waiting read the next paragraph. 

Note that if you have more than one sandbox for a Zope-based web
application, it will probably make sense to share the eggs between the
different sandboxes.  You can tell zc.buildout to use a central eggs
directory by creating ``~/.buildout/default.cfg`` with the following
contents::

    [buildout]
    eggs-directory = /home/bruno/buildout-eggs


Domanin Name and IP address
==========================
Don't forget to change the domain name and 
port in etc/debug.ini and etc/deploy.ini
Then rerun bin/buildout



Running the demo applications
-----------------------------

You can start Zope with the demo applications installed with the
following command:

    $ bin/paster serve parts/etc/deploy.ini

If you now connect to port 8080 and log in with username 'grok',
password 'grok', you should be able to add the grok-based applications
(such as grokwiki) from the menu.

Running a Production Server
__________________________
bin/daemon will starta a production server.  I believe it calls
    bin/paster serve parts/etc/deploy.ini


Chaning the Password
--------------------
You can run bin/zpasswd to create a new password file.  this will create 
some zdml which defines a new pricinpal.  Copy that zcmo into etc/site.zcml.in and run bin/buildout again. There is already one principal in site.zcml.in.  You probably want to delete the default grok principal and replace it with the new 
one you generated. 


Running the tests
-----------------

Grok's tests are easily run by executing the test runner that's
installed in the ``bin`` directory::

    $ bin/test

The Directory Structure
________________________
You can read more about the directory structure of a buildout here:
http://www.buildout.org/en/latest/docs/dirstruct.html

