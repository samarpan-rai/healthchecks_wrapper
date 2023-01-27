import asyncio
import pytest
from healthchecks_wrapper import HealthCheck


@pytest.mark.asyncio
async def test_when_body_returns_no_error_then_no_error_should_be_raised(
    valid_ping_url,
):
    try:
        async with HealthCheck(valid_ping_url):
            await asyncio.sleep(0.01)
            print("Hello world")
    except Exception:
        pytest.fail("Error raised")


@pytest.mark.asyncio
async def test_when_explicit_suppress_exception_is_disabled_then_pass_through_exception(
    valid_ping_url,
):
    with pytest.raises(RuntimeError):
        async with HealthCheck(valid_ping_url, suppress_exceptions=False):
            raise RuntimeError


@pytest.mark.asyncio
async def test_when_implicit_suppress_exception_is_disabled_then_pass_through_exception(
    valid_ping_url,
):
    with pytest.raises(RuntimeError):
        async with HealthCheck(valid_ping_url):
            raise RuntimeError


@pytest.mark.asyncio
async def test_when_suppress_exception_is_enabled_then_do_not_pass_through_exception(
    valid_ping_url,
):
    try:
        async with HealthCheck(valid_ping_url, suppress_exceptions=True):
            raise RuntimeError(
                "test_when_suppress_exception_is_enabled_then_do_not_pass_through_exception"
            )
    except RuntimeError:
        pytest.fail("Error not suppressed")


@pytest.mark.asyncio
async def test_when_bad_url_is_provided_then_raise_exception():
    with pytest.raises(ValueError):
        async with HealthCheck("https://thiisbad"):
            print("Nothing to suspect")


@pytest.mark.asyncio
async def test_when_no_url_is_provided_then_raise_exception():
    with pytest.raises(ValueError):
        async with HealthCheck(""):
            print("Nothing to suspect")


@pytest.mark.asyncio
async def test_sleep_and_print(valid_ping_url):
    async with HealthCheck(valid_ping_url):
        await asyncio.sleep(0.1)
        print("Test complete")
