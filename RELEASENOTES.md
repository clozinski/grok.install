grok.install is a cousin of grokproject.  grok.install just does a very simple installation.  To change passwords, domain names, and ip addresses you have to edit finfiles.  grokproject asks lots of questions simplifying the process for the end user, but making maintenance much harder. 

Really grok.install is a precursor to grokproject.  grok.install is a huge step towards upgrading grokproject. If anyone wants to I invite them to now upgrade grokproject.

grok.install evolved from grok.  You can actually download a current version of grok and it runs and compiles in Python 3 and 2. But grok and grok.install are on very different trajectories, so I felt no need to keep one as a fork of the other.  


I can't say that grok.install is perfect.  But it installs  for me, and I know of no known problems.  Moreover if you have a problem, other than on windows, I am happy to fix it quickly. 

Three  things I would like to do.  Configure fanstatic, so that it server grokwiki/iki.css and make it compile under Python 3.  In general grok works under PYthon 3, but just not for me.  Add support for favicons. 




grok.intall egg
===============
I do not see a reason to turn grok.install into an egg, but if someone wants one, let me know and I am happy to do it. 



Notes on Grok
===============
grok.install is good, but now I want to fix other parts of grok.  
I need to write to the people with pull authority if they will accept my 
pull requests. 

We should remove grokwiki from grok.  It belongs in grok.install.

grokgui lost its nice grok icon.  

package grok should no longer refer to grokproject 
