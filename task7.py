class ComplexNum:
    def __init__(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2

    def __add__(self, other):
        return f'Сумма: {self.num_1 + other.num_1} + {self.num_2 + other.num_2} * i'

    def __mul__(self, other):
        return f'Произведение: {self.num_1 * other.num_1 - (self.num_2 * other.num_2)} ' \
               f'+ {self.num_2 * other.num_1} * i'


num1 = ComplexNum(3, 12)
num2 = ComplexNum(4, 7)
print(num1 + num2)
print(num1 * num2)
