import sys
import math

class BiquadraticRoots:
    def __init__ (self):
        self.a = 0
        self.b = 0
        self.c = 0
        self.num_roots = 0
        self.roots_list = []

    def get_coef(self, index, prompt):
        try:
            coef_str = sys.argv[index]
        except:
            print(prompt)
            coef_str = input()
        try:
            coef = float(coef_str)
        except:
            print("Коэффициент должен быть числом")
            sys.exit(0)

    def get_coefs(self):
        self.a = self.get_coef(1, "Введите коэффициент a: ")
        self.b = self.get_coef(2, "Введите коэффициент b: ")
        self.c = self.get_coef(3, "Введите коэффициент c: ")
    
    def calculate_roots(self):
        a = self.a
        b = self.b
        c = self.c
        D = b**2 - 4*a*c
        if D == 0:
            if -b/(2*a) > 0:
                root1 = math.sqrt(-b/(2*a))
                root2 = -root1
                self.num_roots = 2
                self.roots_list.append(root1)
                self.roots_list.append(root2)
            elif (a != 0) and (b == 0):
                root1 = 0
                self.roots_list.append(root1)
        if D > 0:
            buf1 = (-b - math.sqrt(D))/(2*a)
            buf2 = (-b + math.sqrt(D))/(2*a)
            if buf1 > 0:
                root1 = math.sqrt(buf1)
                root2 = -root1
                self.num_roots += 2
                self.roots_list.append(root1)
                self.roots_list.append(root2)
            elif buf1 == 0:
                root1 = 0
                self.num_roots += 1
                self.roots_list.append(root1)
            if buf2 > 0:
                root3 = math.sqrt(buf2)
                root4 = -root3
                self.num_roots += 2
                self.roots_list.append(root3)
                self.roots_list.append(root4)
            elif buf2 == 0:
                root3 = 0
                self.num_roots += 1
                self.roots_list.append(root3)
    
    def print_roots(self):
        if self.num_roots != len(self.roots_list):
            print(('Ошибка. Уравнение содержит {} действительных корней, ' +\
                'но было вычислено {} корней.').format(self.num_roots, len(self.roots_list)))
        else:
            if self.num_roots == 0:
                print('Корней нет')
            elif self.num_roots == 1:
                print('Один корень: {}'.format(self.roots_list[0]))
            elif self.num_roots == 2:
                print('Два корня: {} и {}'.format(self.roots_list[0], \
                    self.roots_list[1]))
            elif self.num_roots == 3:
                print('Три корня: {} и {} и {}'.format(self.roots_list[0], self.roots_list[1], self.roots_list[2]))
            else:
                print('Четыре корня: {} и {} и {} и {}'.format(self.roots_list[0], self.roots_list[1], \
                self.roots_list[2], self.roots_list[3]))

def main():
    r = BiquadraticRoots()
    r.get_coefs()
    r.calculate_roots()
    r.print_roots()

if __name__ == "__main__":
    main()

