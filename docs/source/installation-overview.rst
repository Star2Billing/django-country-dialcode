.. _installation-overview:

=====================
Installation overview
=====================

.. _requirements:

requirements
============

A requirements file stores a list of dependencies to be installed for your project/application.

To get started with Django-country-dialcode you must have the following installed:

- python >= 2.4 (programming language)
- Apache / http server with WSGI modules
- Django Framework >= 1.3 (Python based Web framework)


.. _install_requirements:

Install requirements with PIP
=============================

Use PIP to install the dependencies listed in the requirments file,::

    $ pip install -r requirements.txt


.. _configuration:

Configuration
=============

Add ``country_dialcode`` into INSTALLED_APPS in settings.py::

    INSTALLED_APPS = (
        ...
        'country_dialcode',
        ...)


Run following commands to add the models in your database ::

    python manage.py syncdb


