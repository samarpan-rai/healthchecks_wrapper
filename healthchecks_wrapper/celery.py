import logging
import sys
import traceback

from healthchecks_wrapper.api import send_request
from healthchecks_wrapper.api import JOB_START_POST_FIX
from healthchecks_wrapper.api import JOB_END_POST_FIX
from healthchecks_wrapper.api import JOB_FAILURE_PATH

logger = logging.getLogger(__name__)

try:
    import celery
except ImportError:
    logger.error("Cannot use the healthchecks_wrapper.celery without celery installed")
    sys.exit(1)


class HealthCheckTaskBase(celery.Task):
    """Base class to use for celery tasks to report status to healthchecks.io

    Attributes:
        health_check_url (str): A valid url to send request
        health_check_retry_as_failure (bool, optional): If True, a retry will be
            reported as a failure. Defaults to False.

    """

    health_check_url = None
    health_check_retry_as_failure = False

    def __init__(self):
        super().__init__()
        if self.health_check_url is None:
            raise ValueError("health_check_url must be set")

    def before_start(self, task_id, args, kwargs):
        send_request(self.health_check_url + JOB_START_POST_FIX)
        return super().before_start(task_id, args, kwargs)

    def on_success(self, retval, task_id, args, kwargs):
        send_request(self.health_check_url + JOB_END_POST_FIX)
        return super().on_success(retval, task_id, args, kwargs)

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        stack_trace = "".join(traceback.format_exception(exc))
        payload = stack_trace.encode("utf-8")
        send_request(self.health_check_url + JOB_FAILURE_PATH, payload)
        return super().on_failure(exc, task_id, args, kwargs, einfo)

    def on_retry(self, exc, task_id, args, kwargs, einfo):
        if self.health_check_retry_as_failure:
            stack_trace = "".join(traceback.format_exception(exc))
            payload = stack_trace.encode("utf-8")
            send_request(self.health_check_url + JOB_FAILURE_PATH, payload)
        return super().on_retry(exc, task_id, args, kwargs, einfo)
