class StoreMashines:

    def __init__(self, name, price, quantity, number, *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.numb = number
        self.my_store_full = []
        self.my_store = []
        self.my_unit = {'Модель устройства': self.name, 'Цена за единицу': self.price, 'Количество': self.quantity}

    def __str__(self):
        return f'{self.name} цена {self.price} количество {self.quantity}'

    def reception(self):

        try:
            unit = input(f'Введите наименование: ')
            unit_p = int(input(f'Введите цену за едицу: '))
            unit_q = int(input(f'Введите количество: '))
            unique = {'Модель устройства': unit, 'Цена за единицу': unit_p, 'Количество': unit_q}
            self.my_unit.update(unique)
            self.my_store.append(self.my_unit)
            print(f'Текущий список -\n {self.my_store}')
        except:
            return f'Ошибка ввода данных'

        print(f'Для выхода наберите - "Exit" или для продолжения нажмите - "Enter"')
        q = input(f'>>> ')
        if q == 'Exit' or q == 'EXIT' or q == 'exit':
            self.my_store_full.append(self.my_store)
            print(f'Весь склад -\n {self.my_store_full}')
            return f'Выход'
        else:
            return StoreMashines.reception(self)


class Printer(StoreMashines):
    def to_print(self):
        return f'Принтеры {self.numb}'


class Scanner(StoreMashines):
    def to_scan(self):
        return f'Сканеры {self.numb}'


class Copier(StoreMashines):
    def to_copier(self):
        return f'МФУ  {self.numb}'


unit_1 = Printer('Samsung', 5000, 2, 12)
unit_2 = Scanner('Minolta', 8000, 6, 15)
unit_3 = Copier('Xerox', 6000, 1, 10)
print(unit_1.reception())
print(unit_2.reception())
print(unit_3.reception())
print(unit_1.to_print())
print(unit_3.to_copier())

