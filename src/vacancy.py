class Vacancy:
    """Класс для вакансий"""

    def __init__(self, name, vacancy_id, salary, description):
        """Инициализация"""
        self.name = name
        self.vacancy_id = vacancy_id
        self.__salary = salary
        self.description = description

    @property
    def salary(self) -> float:
        """Выдать приватные атрибуты"""
        return self.__salary

    @salary.setter
    def salary(self, value) -> None:
        """Поменять зарплату"""
        if value <= 0 or value is None:
            print('Зарплата не указана или равна 0')
        self.__salary = value

    def vacancy_dict(self) -> dict:
        """Выдать словарь с вакансией"""
        return {'name': self.name, 'vacancy_id': self.vacancy_id, 'salary': self.salary, 'description': self.description}

    def compare_salaries(self, other) -> str:
        """Сравнение зарплат"""
        if type(other) is self.__class__:
            if self.__salary > other.__salary:
                return f'У {self.vacancy_id} зарплата больше'
            elif self.__salary < other.__salary:
                return f'У {other.vacancy_id} зарплата больше'
            else:
                return 'У вакансий одинаковые зарплаты'
        else:
            raise ValueError('Это не сравнение вакансий!')
