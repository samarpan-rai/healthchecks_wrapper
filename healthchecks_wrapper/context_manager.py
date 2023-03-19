"""Main module."""
import logging
import traceback

from .api import send_request
from .api import asend_request
from .api import JOB_START_POST_FIX
from .api import JOB_END_POST_FIX
from .api import JOB_FAILURE_PATH

from .functions import is_invalid_url

logger = logging.getLogger(__name__)


class HealthCheck:
    def __init__(self, health_check_url, suppress_exceptions=False):
        """Wrapper around HealthChecks.io to log job status

        Args:
            health_check_url (str): A valid url to send request
            suppress_exceptions (bool, optional): [description]. Defaults to False.
        """
        if is_invalid_url(health_check_url):
            raise ValueError(f"Invalid URL provided : {health_check_url}")
        self.health_check_url = health_check_url
        self.suppress_exceptions = suppress_exceptions

    def __enter__(self):
        return send_request(self.health_check_url + JOB_START_POST_FIX)

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if exc_type is None:
            send_request(self.health_check_url + JOB_END_POST_FIX)
        else:
            stack_trace = "".join(
                traceback.format_exception(exc_type, exc_value, exc_traceback)
            )
            payload = stack_trace.encode("utf-8")
            send_request(self.health_check_url + JOB_FAILURE_PATH, payload)
        return self.suppress_exceptions

    async def __aenter__(self):
        await asend_request(self.health_check_url + JOB_START_POST_FIX)
        return self

    async def __aexit__(self, exc_type, exc_value, exc_traceback):
        if exc_type is None:
            await asend_request(self.health_check_url + JOB_END_POST_FIX)
        else:
            stack_trace = "".join(
                traceback.format_exception(exc_type, exc_value, exc_traceback)
            )
            payload = stack_trace.encode("utf-8")
            await asend_request(self.health_check_url + JOB_FAILURE_PATH, payload)
        return self.suppress_exceptions
