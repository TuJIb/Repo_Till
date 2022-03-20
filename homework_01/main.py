"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*numbers, power=2):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    result = [number ** power for number in numbers]
    return result


# filter types
ODD = "odd"     #не четные
EVEN = "even"   #четные
PRIME = "prime" #простые

def is_odd(number):
    return number % 2 != 0
def is_even(number):
    return number % 2 == 0
def is_prime(number):
    dl = 2
    while dl * dl <= number and number % dl != 0:
        dl += 1
    return dl * dl > number

def filter_numbers(numbers, type_data):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    if type_data == "even":
        #result = [number for number in numbers if number % 2 == 0]
        return (list(filter(is_even, numbers)))
    elif type_data == "odd":
        #result = [number for number in numbers if number % 2 != 0]
        return (list(filter(is_odd, numbers)))
    elif type_data == "prime":
        return (list(filter(is_prime, numbers)))





def main():
    result = power_numbers(1, 2, 5, 7)
    print(f'(1, 2, 5, 7) to power 2 = {result}')

    result = filter_numbers([2, 3, 4, 5], ODD)
    print(f'result [2, 3, 4, 5] {ODD} = {result}')

    result = filter_numbers([2, 3, 4, 5], EVEN)
    print(f'result [2, 3, 4, 5] {EVEN} = {result}')

    result = filter_numbers([2, 3, 4, 5], PRIME)
    print(f'result [2, 3, 4, 5] {PRIME} = {result}')

if __name__ == '__main__':
    main()