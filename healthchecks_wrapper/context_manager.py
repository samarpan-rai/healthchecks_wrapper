"""Main module."""
import json
import re
import socket
from io import StringIO
from urllib.request import urlopen

# Shamelessly stolen from Django's url validator https://github.com/django/django/blob/stable/1.3.x/django/core/validators.py#L45
regex = re.compile(
    r"^(?:http|ftp)s?://"  # http:// or https://
    r"(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|"  # domain...
    r"localhost|"  # localhost...
    r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"  # ...or ip
    r"(?::\d+)?"  # optional port
    r"(?:/?|[/?]\S+)$",
    re.IGNORECASE,
)


class HealthCheck:
    def __init__(self, health_check_url, suppress_exceptions=False):
        """Wrapper around HealthChecks.io to log job status

        Args:
            health_check_url (str): A valid url to send request
            suppress_exceptions (bool, optional): [description]. Defaults to False.
        """
        if not regex.match(health_check_url):
            raise ValueError("Invalid URL provided : {}".format(health_check_url))
        self.health_check_url = health_check_url
        self.suppress_exceptions = suppress_exceptions

    def __enter__(self):
        return self.send_request("/start")

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if exc_type is None:
            self.send_request("")
        else:
            top_stack = StringIO()

            top_lines = top_stack.getvalue().strip("\n").split("\n")[:-4]
            top_stack.close()

            full_stack = StringIO()
            full_stack.write("Traceback (most recent call last):\n")
            full_stack.write("\n".join(top_lines))
            full_stack.write("\n")

            full_stack.write("{}: {}".format(exc_type.__name__, str(exc_value)))
            sinfo = full_stack.getvalue().encode("utf-8")
            full_stack.close()

            self.send_request("/fail", sinfo)
        return self.suppress_exceptions

    def send_request(self, post_fix, text_message=None):
        try:
            urlopen(self.health_check_url + post_fix, timeout=10, data=text_message)
        except socket.error as e:
            print("Ping failed: %s" % e)
