import pytest


def test_check_age_format(human_info):
    human = human_info
    assert isinstance(human.age, int), 'Age is not an integer'


def test_check_gender_format(human_info):
    human = human_info
    assert isinstance(human.gender, str), 'Gender is not a string'


def test_check_name_format(human_info):
    human = human_info
    assert isinstance(human._Human__name, str), 'Name is not a string'


def test_validate_gender(human_info):
    human = human_info
    available_gender = ['male', 'famel']
    assert human.gender.lower() in available_gender, 'Name of gender is wrong'


def test_grow_function_increment_age(human_info):
    human = human_info
    new_age = human.age + 1
    if new_age < human._Human__age_limit:
        human.grow()
        assert human.age == new_age, "Age should be incremented by 1"


def test_grow_function_status_alive(human_info):
    human = human_info
    new_age = human.age + 1
    if new_age < human._Human__age_limit:
        human.grow()
        assert human._Human__status == "alive", "Status should be 'alive'"


def test_grow_function_status_dead(human_info):
    human = human_info
    if human.age >= human._Human__age_limit:
        human.grow()
        assert human._Human__status == "dead", "If age is more than or equal to 100, status should be 'dead'"


def test_age_limit(human_info_more_100_year):
    human = human_info_more_100_year
    assert human.age <= human._Human__age_limit and human.age > 0, "Age should be more than 0 and less than or equal to 100"


def test_is_alive_exception(human_info):
    human = human_info
    human._Human__status = "dead"
    with pytest.raises(Exception) as exc_info:
        human._Human__is_alive()
    assert str(exc_info.value) == (f"{human._Human__name} is already dead...")


def test_change_gender_exception(human_info):
    human = human_info

    with pytest.raises(Exception) as exc_info:
        human.change_gender('male')

    assert str(exc_info.value) == (f"{human._Human__name} already has gender '{human.gender}'")
