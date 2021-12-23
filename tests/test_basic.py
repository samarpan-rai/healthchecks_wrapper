#!/usr/bin/env python

"""Tests for `healthchecks_context_manager` package."""

import pytest

from healthchecks_wrapper import HealthCheck


@pytest.fixture
def valid_ping_url():
    return "https://hc-ping.com/b2b308a5-765c-4136-8d0a-2ff0b906e3ee"


def test_when_explicit_suppress_exception_is_disabled_then_pass_through_exception(
    valid_ping_url,
):
    with pytest.raises(RuntimeError):
        with HealthCheck(valid_ping_url, suppress_exceptions=False):
            raise RuntimeError(
                "test_when_explicit_suppress_exception_is_disabled_then_pass_through_exception"
            )


def test_when_implicit_suppress_exception_is_disabled_then_pass_through_exception(
    valid_ping_url,
):
    with pytest.raises(RuntimeError):
        with HealthCheck(valid_ping_url):
            raise RuntimeError(
                "test_when_implicit_suppress_exception_is_disabled_then_pass_through_exception"
            )


def test_when_suppress_exception_is_enabled_then_do_not_pass_through_exception(
    valid_ping_url,
):
    try:
        with HealthCheck(valid_ping_url, suppress_exceptions=True):
            raise RuntimeError(
                "test_when_suppress_exception_is_enabled_then_do_not_pass_through_exception"
            )
    except RuntimeError:
        pytest.fail("Error not supreseed")


def test_when_bad_url_is_provided_then_raise_exception():
    with pytest.raises(ValueError):
        with HealthCheck("https://thiisbad"):
            print("Nothing to suspect")


def test_when_no_url_is_provided_then_raise_exception():
    with pytest.raises(ValueError):
        with HealthCheck(""):
            print("Nothing to suspect")
