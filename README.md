# Simple HealthChecks Wrapper


[<img src="https://img.shields.io/pypi/v/healthchecks-wrapper.svg">](https://pypi.org/project/healthchecks-wrapper)
[<img src="https://readthedocs.org/projects/healthchecks-wrapper/badge/?version=latest">](https://healthchecks-wrapper.readthedocs.io/en/latest/?badge=latest)
[![buy me a coffee](https://img.shields.io/badge/If%20you%20like%20it-Buy%20me%20a%20coffee-orange.svg?style=for-the-badge)](https://www.buymeacoffee.com/samarpanrai)

Context manager around service provided by [healthchecks.io](https://healthchecks.io/) that will ping your check URL for both success and failure (includes stack trace).

### Features

* Zero requirements outside the standard library
* Easily report the status of your python jobs
* Supports both sync and async jobs

### Getting started
Make a free account with at [healthchecks.io](https://healthchecks.io/) and create a check. You need to copy the url of the check endpoint.

Install the library

```bash
pip install healthchecks-wrapper
```

Use it in your code

```python
from healthchecks_wrapper import HealthCheck
import asyncio
valid_ping_url = "https://hc-ping.com/b2b308a5-765c-4136-8d0a-2ff0b906e3ee"  # Replace with your job url

# Sync jobs
with HealthCheck(valid_ping_url):
    # Do your job
    print("hi")

# Async jobs requires a bit more boiler plate code
async def print_hi():
    async with HealthCheck(valid_ping_url):
        # Do your job
        await asyncio.sleep(1) # Read database async
        print("hi")

def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(print_hi())
    loop.close()

main()
```


[![buy me a coffee](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/samarpanrai)

### Credits

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage)
 project template.


