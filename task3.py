class ListError(Exception):
    def __init__(self, txt):
        self.txt = txt


list_1 = []

while True:
    user_input = input('Введите число или "ex" для выхода: ')

    if user_input == 'ex':
        break
    try:
        if user_input.isdigit():
            list_1.append(int(user_input))
        elif not user_input.isdigit():
            raise ListError(f'Было введено не число, продолжите ввод данных')
    except ListError as error:
        print(error)

print(list_1)
