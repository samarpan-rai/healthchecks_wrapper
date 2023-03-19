"""Main module."""
import asyncio
import logging
import socket
from functools import partial
from urllib.request import urlopen

TIMEOUT = 10

logger = logging.getLogger(__name__)


def send_request(health_check_url, text_message=None):
    try:
        urlopen(health_check_url, timeout=TIMEOUT, data=text_message)
    except socket.error as e:
        logger.info(f"Ping failed: {e}")


async def asend_request(health_check_url, payload=None):
    try:
        pfunc = partial(
            urlopen,
            health_check_url,
            timeout=TIMEOUT,
            data=payload,
        )
        await asyncio.get_event_loop().run_in_executor(None, pfunc)
    except socket.error as e:
        logger.info(f"Ping failed: {e}")
