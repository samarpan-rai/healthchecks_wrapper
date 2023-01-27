import pytest
from healthchecks_wrapper import HealthCheck


def test_when_body_returns_no_error_then_no_error_should_be_raised(
    valid_ping_url,
):
    try:
        with HealthCheck(valid_ping_url):
            print("Hello world")
    except Exception:
        pytest.fail("Error raised")


def test_when_explicit_suppress_exception_is_disabled_then_pass_through_exception(
    valid_ping_url,
):
    with pytest.raises(RuntimeError):
        with HealthCheck(valid_ping_url, suppress_exceptions=False):
            raise RuntimeError


def test_when_implicit_suppress_exception_is_disabled_then_pass_through_exception(
    valid_ping_url,
):
    with pytest.raises(RuntimeError):
        with HealthCheck(valid_ping_url):
            raise RuntimeError


def test_when_suppress_exception_is_enabled_then_do_not_pass_through_exception(
    valid_ping_url,
):
    try:
        with HealthCheck(valid_ping_url, suppress_exceptions=True):
            raise RuntimeError
    except RuntimeError:
        pytest.fail("Error not suppressed")


def test_when_bad_url_is_provided_then_raise_exception():
    with pytest.raises(ValueError):
        with HealthCheck("https://thiisbad"):
            print("Nothing to suspect")


def test_when_no_url_is_provided_then_raise_exception():
    with pytest.raises(ValueError):
        with HealthCheck(""):
            print("Nothing to suspect")
