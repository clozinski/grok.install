# Grok Installation Instructions. 

Here are the instructions for installing grok 1.14.1  Released Feb 2016.

## Preparation

  If you are running on an older version of grok, or on an older server, you may want to run grok inside of virtualenv. make sure that you have the most recent versin of virtualenv.

     $ easy_install -U virtualenv

Crete a Virtual Environment.

      $virtualenv -p python2.7  virt

Start your Virtual Environment.

      $source virt/bin/activate.csh

Make sure that you nave the newest version of setuptools

     $easy_install -U setuptools

## Actual Installation Instructinos

I like to install in /usr/local

       $cd /usr/local

First get the grok.install from github

      $wget --no-check-certificate https://github.com/clozinski/grok.install/archive/master.zip

Unzip it. 

      $unzip master.zip

Move it to a better location.

    $mv grok.install-master grok

Enter the directory.

   $ cd grok

Bootstrap the buildout environment:

    $ python bootstrap.py

and run the buildout command:

    $ bin/buildout
    [lots of stuff will be downloaded and installed here]
    While waiting read and execute the next paragraph. 

Note that if you have more than one sandbox for a Zope-based web
application, it will probably make sense to share the eggs between the
different sandboxes.  You can tell zc.buildout to use a central eggs
directory by creating ``~/.buildout/default.cfg`` with the following
contents::

    [buildout]
    eggs-directory = /home/bruno/buildout-eggs

##Domanin Name and IP address
	
Don't forget to change the domain name and 
port in etc/debug.ini and etc/deploy.ini
Then rerun bin/buildout

##Running the tests

Grok's tests are easily run by executing the test runner that's
installed in the ``bin`` directory::

    $ bin/test

##Running the demo applications

You can start Zope with the demo applications installed with the
following command:

    $ bin/paster serve parts/etc/deploy.ini

When it is running it will display a URL.  Copy that URL into your browser
to view the running site.  

UserName:grok
Passowrd:grok

If you now connect to port 8080 and log in with username 'grok',
password 'grok', you should be able to add the grok-based applications
app and grokwiki  from the home page.

##Running a Production Server

bin/daemon will starta a production server.  I believe it calls
    bin/paster serve parts/etc/deploy.ini

##The Directory Structure

You can read more about the directory structure of a buildout here:
http://www.buildout.org/en/latest/docs/dirstruct.html

myapp contains the app.
grokwiki contains the grokwiki egg.