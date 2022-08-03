"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Отредактировать функцию month_to_season, которая принимает номер месяца,
таким образом, чтобы она возвращала название сезона, к которому относится
этот месяц

ПРИМЕРЫ
--------------------------------------------------------------------------------
- month_to_season(12) -> 'Зима'
- month_to_season(4) -> 'Весна'
- month_to_season(7) -> 'Лето'
- month_to_season(9) -> 'Осень'
"""


def month_to_season(month: int) -> str:
    """Возвращает сезон по его номеру

    :param month: номер сезона
    :type month: int

    :return: название сезона, например "зима"
    :rtype: str
    """


    if month == 12:
        return 'Зима'
    elif month == 4:
        return 'Весна'
    elif month == 7:
        return 'Лето'
    elif month == 9:
        return 'Осень'



if __name__ == '__main__':
    month_number = int(input('Введите номер месяца: '))
    print(f'Сезон: {month_to_season(month_number)}')
