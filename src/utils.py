from abc import ABC, abstractmethod
import json
from src.vacancy import Vacancy


class Saver(ABC):
    """Абстрактный класс для сохранения файла в разном виде"""
    @abstractmethod
    def add_vacancy(self, vacancy):
        """Добавление вакансии"""
        pass

    @abstractmethod
    def get_vacancy(self):
        """Получение вакансии"""
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy):
        """Удаление вакансии"""
        pass


class JSONSaver(Saver):
    """Класс для сохранения файла в JSON и работы с ним"""
    vacancies_count = 0

    def __init__(self):
        """Инициализация"""
        self.vacancies_count = 0

    def add_vacancy(self, vacancy: Vacancy):
        """Добавление вакансии"""
        try:
            with open('data/vacancies.json', "r", encoding="utf-8") as json_file:
                file_data = json.loads(json_file.read())
            file_data.append(vacancy)
            with open('data/vacancies.json', 'w', encoding="utf-8") as f:
                json.dump(file_data, f, ensure_ascii=False)
            self.vacancies_count += 1
        except (FileNotFoundError, ValueError):
            with open('data/vacancies.json', 'a+', encoding="utf-8") as f:
                json.dump([vacancy], f, ensure_ascii=False)
            self.vacancies_count += 1

    def get_vacancy(self):
        """Получение вакансии"""
        pass

    def delete_vacancy(self, vacancy: Vacancy):
        """Удаление вакансии"""
        try:
            with open('data/vacancies.json', 'r') as json_data:
                data = json.load(json_data)
            nd = [i for i in data if i["vacancy_id"] != vacancy.vacancy_id]
            with open('data/vacancies.json', 'w') as outfile:
                json.dump(nd, outfile)
            self.vacancies_count -= 1
        except (FileNotFoundError, ValueError):
            print('Возможны проблемы с файлом!')
