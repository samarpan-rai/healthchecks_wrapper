"""Main module."""
import json
from contextlib import ContextDecorator
from io import StringIO

import requests


class HealthCheck(ContextDecorator):
    def send_request(self, post_fix, additional_data):
        if not additional_data:
            requests.get(self.url + post_fix, timeout=10)
        else:
            if type(additional_data) is dict:
                additional_data = json.dumps(additional_data)
            requests.post(self.url + post_fix, timeout=10, data=additional_data)

    def __init__(self, health_check_url):
        self.url = health_check_url

    def __enter__(self):
        return self.send_request("/start", None)

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if exc_type is None:
            self.send_request("", None)
        else:
            top_stack = StringIO()

            top_lines = top_stack.getvalue().strip("\n").split("\n")[:-4]
            top_stack.close()

            full_stack = StringIO()
            full_stack.write("Traceback (most recent call last):\n")
            full_stack.write("\n".join(top_lines))
            full_stack.write("\n")

            full_stack.write("{}: {}".format(exc_type.__name__, str(exc_value)))
            sinfo = full_stack.getvalue()
            full_stack.close()

            self.send_request("/fail", sinfo)
        return True
