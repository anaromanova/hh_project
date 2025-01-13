from abc import ABC, abstractmethod
from src.hh import Vacancy
import json


class Work_With_Vacancies(ABC):

    @abstractmethod
    def vacancies_to_file(self, vacancies):
        pass

    @abstractmethod
    def vacancies_from_file(self):
        pass

    @abstractmethod
    def delete_info_from_vacancies(self):
        pass


class Vacancies_To_JSON(Work_With_Vacancies):

    def vacancies_to_file(self, vacancies):
        with open('data/vacancies.json', 'w') as f:
            json.dump(vacancies, f)

