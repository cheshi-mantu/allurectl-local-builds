import allure
from conftest import _should_fail

@allure.suite("Second steps")
@allure.story("smoking pytest and assertions with allure report")
@allure.feature("tuple assertion")
@allure.title("Assert a tuple and test will fail")
def test_failing():
    with allure.step("Assert tuple 1,2,3 versus tuple 1,2,3"):
        assert not _should_fail(), "Failure due to reason ODD"

@allure.suite("Second steps")
@allure.story("smoking pytest and assertions with allure report")
@allure.feature("tuple assertion")
@allure.title("Assert a string and test will fail")
def test_failing_strings():
    with allure.step("Assert string 'tra-tata' versus string 'trata-ta'"):
        assert not _should_fail(), "Failure due to reason ODD"

@allure.suite("Second steps")
@allure.story("smoking pytest and assertions with allure report")
@allure.feature("in assertion")
@allure.title("Assert a string and test will fail")
def test_failing_strings():
    with allure.step("Assert 1 is in the list [1,2,3]"):
        assert not _should_fail(), "Failure due to reason ODD"