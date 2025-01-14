import pytest
from src.vacancy import Vacancy


@pytest.fixture
def vacancy_1():
    return Vacancy("Python Developer",
                   "<https://hh.ru/vacancy/123456>",
                   150000,
                   "Требования: опыт работы от 3 лет...")


@pytest.fixture
def vacancy_2():
    return Vacancy("Senior Go Developer",
                   "<https://hh.ru/vacancy/123321>",
                   350000,
                   "Требования: опыт работы от 6 лет...")

@pytest.fixture
def vacancy_3():
    return Vacancy("Go Developer",
                   "<https://hh.ru/vacancy/123567>",
                   150000,
                   "Требования: опыт работы от 3 лет...")