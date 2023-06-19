from typing import List, Union

"""
Домашнее задание №1
Функции и структуры данных
"""


def check_integer_type(
        num: Union[int, float],
) -> None:
    if not isinstance(num, int):
        raise ValueError("На вход принимаются только целые числа (int) ")


def is_prime(
        num: int,
) -> bool:
    if num in (0, 1,):
        return False

    possible_denominator = range(2, num)
    for den in possible_denominator:
        if num % den == 0:
            return False

    return True


def power_numbers(*args) -> Union[None, List[int]]:
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    filter(check_integer_type, args)
    return [num ** 2 for num in args]


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def filter_numbers(
        num_list: List[int],
        filter_type: str,
) -> Union[None, List[int]]:
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    available_types = [ODD, EVEN, PRIME]
    if filter_type not in available_types:
        raise ValueError(f"Указан неверный return_type. Введите один вариант из списка: {available_types}")

    filter(check_integer_type, num_list)

    if filter_type == ODD:
        return [num for num in num_list if num % 2 == 1]
    elif filter_type == EVEN:
        return [num for num in num_list if num % 2 == 0]
    elif filter_type == PRIME:
        return [num for num in num_list if is_prime(num)]
