import pytest
from src.vacancy import Vacancy


@pytest.fixture
def vacancy_1() -> Vacancy:
    return Vacancy({
        "name": "Junior Python Developer",
        "alternate_url": "https://hh.ru/vacancy/105338726",
        "salary": {"from": 0},
        "snippet": {"responsibility": "Требования: опыт работы от 2 лет..."}
    })


@pytest.fixture
def vacancy_2() -> Vacancy:
    return Vacancy({
        "name": "Junior Python Developer",
        "alternate_url": "https://hh.ru/vacancy/105338543",
        "salary": {"from": 10000},
        "snippet": {"responsibility": "Требования: опыт работы от 1 лет..."}
    })

@pytest.fixture
def vacancy_3() -> Vacancy:
    return Vacancy({"name": "Go Developer",
            "alternate_url": "<https://hh.ru/vacancy/123567>",
            "salary": {"from": 150000},
            "snippet": {"responsibility": "Требования: опыт работы от 3 лет..."}
    })


@pytest.fixture
def vacancies_list_1(vacancy_1, vacancy_2):
    return [vacancy_1, vacancy_2]
