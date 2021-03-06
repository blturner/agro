AGRO
====

Aggregates personal online activity with plug-in based architecture.

Agro is a small, streamlined, simple feed/activity aggregator. The (released) feature set is simple, but with the ability to write your own plugins, the possibilities are endless. If you do write a plug-in, let me know and I'll include it in a source repo here.

BUILT-IN
--------

Twitter, flickr, last.fm and delicious. 

INSTALL
-------

Check the [settings](http://code.google.com/p/agroapp/wiki/Settings) wiki page on how to 'install' agro.
[Default sources require](http://code.google.com/p/django-tagging/).

************

CHANGELOG
=========
09/08/2008
----------

Can now use signed calls to get non-public data, original_secret, etc from non-CC licensed photos!
Set up an API_Key, and [visit this page.](http://camronflanders.com/agro/flickr_token_gen/)

08/19/2008
----------

Command line arguments!

The ability to update only certain sources was added a while back, but now we can force update.  
[see the wiki page](http://code.google.com/p/agroapp/wiki/retrievePy "retrievePy")

08/07/2008
----------

Can now aggregate for multiple accounts on every plugin!

08/05/2008
----------

Template tags added.
2 template tags have been added.
[see the wiki page.](http://code.google.com/p/agroapp/wiki/TemplateTags)

*************

_agro is developed on django trunk and is inspired by jellyroll (from Jacob Kaplan-Moss)._

