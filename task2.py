class ZeroError(Exception):
    def __init__(self, txt):
        self.txt = txt


number_1 = int(input('Введите делимое: '))
number_2 = int(input('Введите делитель:  '))

try:
    if number_2 == 0:
        raise ZeroError('Ошибка! Делитель равен 0')
except ZeroError as error:
    print(error)
else:
    result_1 = number_1 / number_2
    print(f'Результат деления: {result_1}')
