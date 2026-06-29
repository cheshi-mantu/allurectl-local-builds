import os
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
def _layer():
    allure.dynamic.label("layer", "api")
