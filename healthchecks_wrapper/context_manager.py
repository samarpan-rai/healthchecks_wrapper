"""Main module."""
import asyncio
import traceback
import socket
from functools import partial
from urllib.request import urlopen
from .functions import is_invalid_url

# Constants required by HealthChecks.io

JOB_START_POST_FIX = "/start"
JOB_END_POST_FIX = ""
JOB_FAILURE_PATH = "/fail"

TIMEOUT = 10


class HealthCheck:
    def __init__(self, health_check_url, suppress_exceptions=False):
        """Wrapper around HealthChecks.io to log job status

        Args:
            health_check_url (str): A valid url to send request
            suppress_exceptions (bool, optional): [description]. Defaults to False.
        """
        if is_invalid_url(health_check_url):
            raise ValueError("Invalid URL provided : {}".format(health_check_url))
        self.health_check_url = health_check_url
        self.suppress_exceptions = suppress_exceptions

    def __enter__(self):
        return self.send_request(JOB_START_POST_FIX)

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if exc_type is None:
            self.send_request(JOB_END_POST_FIX)
        else:
            stack_trace = "".join(
                traceback.format_exception(exc_type, exc_value, exc_traceback)
            )
            payload = stack_trace.encode("utf-8")
            self.send_request(JOB_FAILURE_PATH, payload)
        return self.suppress_exceptions

    def send_request(self, post_fix, text_message=None):
        try:
            urlopen(self.health_check_url + post_fix, timeout=10, data=text_message)
        except socket.error as e:
            print("Ping failed: %s" % e)

    async def send_request_async(self, post_fix, payload=None):
        try:
            pfunc = partial(
                urlopen, self.health_check_url + post_fix, timeout=TIMEOUT, data=payload
            )
            await asyncio.get_event_loop().run_in_executor(None, pfunc)
        except socket.error as e:
            print("Ping failed: %s" % e)

    async def __aenter__(self):
        await self.send_request_async(JOB_START_POST_FIX)
        return self

    async def __aexit__(self, exc_type, exc_value, exc_traceback):
        if exc_type is None:
            await self.send_request_async(JOB_END_POST_FIX)
        else:
            stack_trace = "".join(
                traceback.format_exception(exc_type, exc_value, exc_traceback)
            )
            payload = stack_trace.encode("utf-8")
            await self.send_request_async(JOB_FAILURE_PATH, payload)
        return self.suppress_exceptions
