import typing

from src.parser import HeadHunterAPI
from unittest.mock import patch



# @patch('requests.get')
# def test_parser_api(mock_get: typing.Any) -> None:
#     """Функция тестирует HeadHunterAPI from src.parser"""
#     mock_get.return_value.json['items'].return_value = {'id': '115259163', 'premium': False, 'name': 'Android-разработчик', 'department': None, 'has_test': True, 'response_letter_required': False,
#                                                'area': {'id': '1', 'name': 'Москва', 'url': 'https://api.hh.ru/areas/1'}, 'salary': None, 'type': {'id': 'open', 'name': 'Открытая'}, 'address': None, 'response_url': None,
#                                                'sort_point_distance': None, 'published_at': '2025-01-10T15:39:21+0300', 'created_at': '2025-01-10T15:39:21+0300',
#                                                'archived': False, 'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=115259163', 'show_logo_in_search': None, 'insider_interview': None,
#                                                'url': 'https://api.hh.ru/vacancies/115259163?host=hh.ru', 'alternate_url': 'https://hh.ru/vacancy/115259163', 'relations': [],
#                                                'employer': {'id': '9301808', 'name': 'Сбер Бизнес Софт', 'url': 'https://api.hh.ru/employers/9301808', 'alternate_url': 'https://hh.ru/employer/9301808',
#                                                             'logo_urls': {'original': 'https://img.hhcdn.ru/employer-logo-original/1267826.png', '90': 'https://img.hhcdn.ru/employer-logo/6691622.png',
#                                                                           '240': 'https://img.hhcdn.ru/employer-logo/6691623.png'}, 'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=9301808',
#                                                             'accredited_it_employer': True, 'trusted': True},
#                                                'snippet': {'requirement': 'Опыт разработки под Android от 2 лет (Android Studio, Gradle). Опыт разработки на Kotlin. Уверенное знание Android SDK, знание разницы...',
#                                                            'responsibility': 'Разработка сложных программных продуктов. Поддержка и модернизация существующих решений.\
#                                                                               Участие в развитии продукта. Участие во всём процессе разработки - от проектирования...'},
#                                                'contacts': None, 'schedule': {'id': 'remote', 'name': 'Удаленная работа'}, 'working_days': [], 'working_time_intervals': [], 'working_time_modes': [],
#                                                'accept_temporary': False, 'fly_in_fly_out_duration': [], 'work_format':
#                                                    [{'id': 'ON_SITE', 'name': 'На\xa0месте работодателя'},{'id': 'REMOTE', 'name': 'Удалённо'}],
#                                                'working_hours': [{'id': 'HOURS_8', 'name': '8\xa0часов'}], 'work_schedule_by_days': [{'id': 'FIVE_ON_TWO_OFF', 'name': '5/2'}],
#                                                'night_shifts': False, 'professional_roles': [{'id': '96', 'name': 'Программист, разработчик'}], 'accept_incomplete_resumes': False,
#                                                'experience': {'id': 'between3And6', 'name': 'От 3 до 6 лет'}, 'employment': {'id': 'full', 'name': 'Полная занятость'},
#                                                'employment_form': {'id': 'FULL', 'name': 'Полная'}, 'internship': False, 'adv_response_url': None, 'is_adv_vacancy': False, 'adv_context': None}
#
#     hh_api = HeadHunterAPI()
#     assert (hh_api.get_vacancies("Авито Сбербанк разработчик") == {'id': '115259163', 'premium': False, 'name': 'Android-разработчик', 'department': None, 'has_test': True, 'response_letter_required': False,
#                                                'area': {'id': '1', 'name': 'Москва', 'url': 'https://api.hh.ru/areas/1'}, 'salary': None, 'type': {'id': 'open', 'name': 'Открытая'}, 'address': None, 'response_url': None,
#                                                'sort_point_distance': None, 'published_at': '2025-01-10T15:39:21+0300', 'created_at': '2025-01-10T15:39:21+0300',
#                                                'archived': False, 'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=115259163', 'show_logo_in_search': None, 'insider_interview': None,
#                                                'url': 'https://api.hh.ru/vacancies/115259163?host=hh.ru', 'alternate_url': 'https://hh.ru/vacancy/115259163', 'relations': [],
#                                                'employer': {'id': '9301808', 'name': 'Сбер Бизнес Софт', 'url': 'https://api.hh.ru/employers/9301808', 'alternate_url': 'https://hh.ru/employer/9301808',
#                                                             'logo_urls': {'original': 'https://img.hhcdn.ru/employer-logo-original/1267826.png', '90': 'https://img.hhcdn.ru/employer-logo/6691622.png',
#                                                                           '240': 'https://img.hhcdn.ru/employer-logo/6691623.png'}, 'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=9301808',
#                                                             'accredited_it_employer': True, 'trusted': True},
#                                                'snippet': {'requirement': 'Опыт разработки под Android от 2 лет (Android Studio, Gradle). Опыт разработки на Kotlin. Уверенное знание Android SDK, знание разницы...',
#                                                            'responsibility': 'Разработка сложных программных продуктов. Поддержка и модернизация существующих решений.\
#                                                                               Участие в развитии продукта. Участие во всём процессе разработки - от проектирования...'},
#                                                'contacts': None, 'schedule': {'id': 'remote', 'name': 'Удаленная работа'}, 'working_days': [], 'working_time_intervals': [], 'working_time_modes': [],
#                                                'accept_temporary': False, 'fly_in_fly_out_duration': [], 'work_format':
#                                                    [{'id': 'ON_SITE', 'name': 'На\xa0месте работодателя'},{'id': 'REMOTE', 'name': 'Удалённо'}],
#                                                'working_hours': [{'id': 'HOURS_8', 'name': '8\xa0часов'}], 'work_schedule_by_days': [{'id': 'FIVE_ON_TWO_OFF', 'name': '5/2'}],
#                                                'night_shifts': False, 'professional_roles': [{'id': '96', 'name': 'Программист, разработчик'}], 'accept_incomplete_resumes': False,
#                                                'experience': {'id': 'between3And6', 'name': 'От 3 до 6 лет'}, 'employment': {'id': 'full', 'name': 'Полная занятость'},
#                                                'employment_form': {'id': 'FULL', 'name': 'Полная'}, 'internship': False, 'adv_response_url': None, 'is_adv_vacancy': False, 'adv_context': None})
