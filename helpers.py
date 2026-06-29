import os
import random


def _should_fail() -> bool:
    mode = os.environ.get("TESTS_SUCCESS", "random")
    if mode == "always":
        return False
    if mode == "never":
        return True
    return random.random() < 0.2
