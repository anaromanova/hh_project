class Vacancy:
    """
           Класс для вакансий
           """

    def __init__(self, name, vacancy_id, salary, description):
        self.name = name
        self.vacancy_id = vacancy_id
        self.__salary = salary
        self.description = description

    @property
    def salary(self) -> float:
        return self.__salary

    @salary.setter
    def salary(self, value) -> None:
        if value <= 0 or value is None:
            print('Зарплата не указана или равна 0')
        self.__salary = value

    def compare_salaries(self, other) -> str:
        if type(other) is self.__class__:
            if self.__salary > other.__salary:
                return f'У {self.vacancy_id} зарплата больше'
            elif self.__salary < other.__salary:
                return f'У{other.vacancy_id} зарплата больше'
            else:
                return 'У вакансий одинаковые зарплаты'
        else:
            raise ValueError('Это не сравнение вакансий!')







test = HH(1)
test.load_vacancies('Авито Сбербанк разработчик')
var = test.vacancies
print(var)