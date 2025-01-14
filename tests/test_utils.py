from src.utils import JSONSaver


def test_add_vacancy(vacancy_1):
    json_saver = JSONSaver()
    assert json_saver.vacancies_count == 0
    vacancy = vacancy_1.vacancy_dict()
    json_saver.add_vacancy(vacancy)
    assert json_saver.vacancies_count == 1


def test_delete_vacancy(vacancy_1, vacancy_2):
    json_saver = JSONSaver()
    assert json_saver.vacancies_count == 0
    vacancy = vacancy_1.vacancy_dict()
    vacancy2 = vacancy_2.vacancy_dict()
    json_saver.add_vacancy(vacancy)
    json_saver.add_vacancy(vacancy2)
    assert json_saver.vacancies_count == 2
    json_saver.delete_vacancy(vacancy_2)
    assert json_saver.vacancies_count == 1
