Django Form Helpers
===================

I think we can all agree that Django's forms framework is pretty spiffy.  This app aims to make it even easier to render and style forms.

Over time I've accumulated a number of miscellaneous snippets and utilities for working with forms.   Right now these snippets are buried inside a few different projects.  I intend to (finally) centralize these snippets into `form_helpers` to make maintenance easier and so I don't have to copy & paste anymore :)

**Note:** I had previously named this project 'django-form-utils', after which I discovered there already existed an app called [django-form-utils](https://launchpad.net/django-form-utils).  For the time being, I've simply renamed mine to 'form-helpers'.  Depending on time/motivation, I might eventually contribute `form_helpers` to `form_helpers`.

Usage
=====

Add 'form_helpers' to `INSTALLED_APPS`. Then, {% load form_helpers %} in your templates and go nuts.

Status
======

** May 4, 2010:** added setup.py for installation via pip; tweaked render_field decorator to actually accept a template name (as documented)

**June 8, 2009:** Renamed codebase to avoid name collisions with [django-form-utils](https://launchpad.net/django-form-utils)

**May 21, 2009:** Currently importing some templatetags from older projects, refactoring and testing with Django 1.0.  The templatetags should not be considered stable at this point.

**Questions or Bugs?** [Send me a message](http://github.com/inbox/new/kylefox) via github.