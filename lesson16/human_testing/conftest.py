import pytest

from lesson16.human import Human

@pytest.fixture()
def human_info():
    info_about_human = Human(name='Tom', age=99, gender='male')
    return info_about_human

@pytest.fixture()
def human_info_more_100_year():
    info_about_human = Human(name='Bob', age=100, gender='male')
    return info_about_human

@pytest.fixture()
def check_negative_value_in_the_year():
    info_about_human = Human(name='Bob', age=-1, gender='male')