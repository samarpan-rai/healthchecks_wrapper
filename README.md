# Simple HealthChecks Wrapper


[<img src="https://img.shields.io/pypi/v/healthchecks-wrapper.svg">](https://pypi.org/project/healthchecks-wrapper)
[<img src="https://readthedocs.org/projects/healthchecks-wrapper/badge/?version=latest">](https://healthchecks-wrapper.readthedocs.io/en/latest/?badge=latest)
[![buy me a coffee](https://img.shields.io/badge/If%20you%20like%20it-Buy%20me%20a%20coffee-orange.svg?style=for-the-badge)](https://www.buymeacoffee.com/samarpanrai)
Context manager around service provided by [healthchecks.io](https://healthchecks.io/) for easy use in your code.

### Features

* Zero requirements outside the standard library
* Easily report the status of your python jobs
* Reports exceptions to HealthChecks as meta data

### Getting started
Make a free account with at [healthchecks.io](https://healthchecks.io/) and create a check. You need to copy the url of the check endpoint.

Install the library

```bash
pip install healthchecks-wrapper
```

Use it in your code

```python
from healthchecks_wrapper import HealthCheck
valid_ping_url = "https://hc-ping.com/b2b308a5-765c-4136-8d0a-2ff0b906e3ee"  # Replace with your job url

with HealthCheck(valid_ping_url):
    # Do your job
    ...
```


[![buy me a coffee](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/samarpanrai)

### Credits

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

[Cookiecutter](https://github.com/audreyr/cookiecutter)
[audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage)
