=======================
django-country-dialcode
=======================


This Django application provides Dial Code and Country data to reuse in a django application.


Installation
============

Install Django-Country-Dialcode::

    python setup.py install


Dependencies
------------

See requirements.txt file


Settings
========

in your settings.py file::

INSTALLED_APPS = INSTALLED_APPS + ('country_dialcode',)


Usage
=====

In your models add the following ::

    dialcode = models.ForeignKey(Prefix, verbose_name=_("Destination"), null=True,
                               blank=True, help_text=_("Select Prefix"))


Contributing
============

If you've found a bug, implemented/improved a feature and think it is useful 
then please consider contributing. Patches, pull requests or just suggestions 
are welcome!

Source code: http://github.com/Star2Billing/django-country-dialcode


If you don’t like Github and Git you’re welcome to send regular patches.

Bug tracker: https://github.com/Star2Billing/django-country-dialcode/issues


Documentation
=============

Documentation is available on 'Read the Docs':
http://django-country-dialcode.readthedocs.org


License
=======

Copyright (c) 2012 Star2Billing S.L. <info@star2billing.com>

django-country-dialcode is licensed under MIT, see `MIT-LICENSE.txt`.


Credit
======

Django-country-dialcode is a Star2Billing-Sponsored Community Project, for more information visit 
http://www.star2billing.com  or email us at info@star2billing.com


    
    
