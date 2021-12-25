============================
Simple HealthChecks Wrapper
============================

.. image:: https://img.shields.io/pypi/v/healthchecks-wrapper.svg
        :target: https://pypi.org/project/healthchecks-wrapper

.. image:: https://readthedocs.org/projects/healthchecks-wrapper/badge/?version=latest
    :target: https://healthchecks-wrapper.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

Context manager around service provided by `healthchecks.io <https://healthchecks.io/>`_ for easy use. 

* Free software: MIT license

Features
--------
* Zero requirements outside the standard library
* Easily report the status of your python jobs
* Reports exceptions to HealthChecks as meta data



Getting started
---------------
Make a free account with at `healthchecks.io <https://healthchecks.io/>`_ and create a check. You need to copy the url of the check endpoint. 

Install the dependencies

::

  pip install healthchecks-wrapper

Use it in your job

::

  from healthchecks_wrapper import HealthCheck

  with HealthCheck(valid_ping_url):
    # Your job
      ...

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
