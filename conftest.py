import os
import platform
import random
import allure
import pytest


def _should_fail() -> bool:
    mode = os.environ.get("TESTS_SUCCESS", "random")
    if mode == "always":
        return False
    if mode == "never":
        return True
    return random.random() < 0.1


@pytest.fixture(autouse=True)
def _tests_success_gate():
    mode = os.environ.get("TESTS_SUCCESS", "random")
    if mode == "broken":
        raise RuntimeError("Broken by TESTS_SUCCESS=broken")
    os_label = os.environ.get("TESTS_OS", platform.system().lower())
    allure.dynamic.label("os", os_label)
    yield
