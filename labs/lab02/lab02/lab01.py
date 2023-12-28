import sys

class BiquadraticEquation:
    #конструктор класса с коэффициентами по умолчанию
    def __init__(self, a = 0.0, b = 0.0, c = 0.0):
        self.a = a
        self.b = b
        self.c = c
        self.roots = set()
        self.num_roots = 0
    #функция для установки коэффициентов
    def coef_setter(self):
        #пробуем считать из системных атрибутов коэффициенты
        try:
            self.a = float(sys.argv[1])
            self.b = float(sys.argv[2])
            self.c = float(sys.argv[3])
        #считать из системных атрибутов не получилось, значит вводим с клавиатуры
        except:
            while True:
                try:
                    print('Введите коэффициент А: ')
                    self.a = float(input())
                    break
                except:
                    pass
            while True:
                try:
                    print('Введите коэффициент B: ')
                    self.b = float(input())
                    break
                except:
                    pass
            while True:
                try:
                    print('Введите коэффициент C: ')
                    self.c = float(input())
                    break
                except:
                    pass
    #функция вычисления корней
    def calculate_roots(self):
        self.roots = set()
        self.num_roots = 0
        a = self.a
        b = self.b
        c = self.c
        d = b**2 - 4*a*c
        if d == 0:
            t = (-1*b)/(2*a)
            if t == 0:
                self.roots.add(0)
            elif t > 0:
                for j in {(-1)**i*(t**0.5) for i in range(0, 2)}:
                    self.roots.add(j)
        elif d > 0:
            t1 = (-1*b+d**0.5)/(2*a)
            t2 = (-1*b-d**0.5)/(2*a)
            if t1 == 0:
                self.roots.add(0)
            elif t1 > 0:
                for j in {(-1)**i*(t1**0.5) for i in range(0, 2)}:
                    self.roots.add(j)
            if t2 == 0:
                self.roots.add(0)
            elif t2 > 0:
                for j in {(-1)**i*(t2**0.5) for i in range(0, 2)}:
                    self.roots.add(j)
        self.num_roots = len(self.roots)
        if self.num_roots == 0:
            self.solution_exception()
    #функция вывода коэффициентов
    def coef_print(self):
        print('Коэффициент A: {}, Коэффициент B: {}, Коэффициент C: {}'.format(self.a, self.b, self.c))
    #функция вывода корней
    def roots_print(self):
        print('Решения уравнения: ' + ' ,'.join(map(str, self.roots)))
    #функция вывода ошибки при вычислении корней
    def solution_exception(self):
        print('Нет действительных корней')

def main():
    equation = BiquadraticEquation()
    equation.coef_setter()
    equation.calculate_roots()
    equation.roots_print()

if __name__ == '__main__':
    main()