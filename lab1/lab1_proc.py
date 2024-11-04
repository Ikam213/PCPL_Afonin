import math
import sys

def get_coef(index, prompt):
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
    return coef

def get_roots(a, b, c):
    roots_list = []
    D = b**2 - 4*a*c
    if D == 0:
        if -b/(2*a) > 0:
            root1 = math.sqrt(-b/(2*a))
            root2 = -root1
            roots_list.append(root1)
            roots_list.append(root2)
        elif (a != 0) and (b == 0):
            root1 = 0
            roots_list.append(root1)
    if D > 0:
        buf1 = (-b - math.sqrt(D))/(2*a)
        buf2 = (-b + math.sqrt(D))/(2*a)
        if buf1 > 0:
            root1 = math.sqrt(buf1)
            root2 = -root1
            roots_list.append(root1)
            roots_list.append(root2)
        elif buf1 == 0:
            root1 = 0
            roots_list.append(root1)
        if buf2 > 0:
            root3 = math.sqrt(buf2)
            root4 = -root3
            roots_list.append(root3)
            roots_list.append(root4)
        elif buf2 == 0:
            root3 = 0
            roots_list.append(root3)
    return roots_list

def main():
    a = get_coef(1, "Введите коэффициент a:")
    b = get_coef(1, "Введите коэффициент a:")
    c = get_coef(1, "Введите коэффициент a:")
    roots = get_roots(a, b, c)
    len_roots = len(roots)
    if len_roots == 0:
        print('Корней нет')
    elif len_roots == 1:
        print('Один корень: {}'.format(roots[0]))
    elif len_roots == 2:
        print('Два корня: {} и {}'.format(roots[0], \
            roots[1]))
    elif len_roots == 3:
        print('Три корня: {} и {} и {}'.format(roots[0], roots[1], roots[2]))
    else:
        print('Четыре корня: {} и {} и {} и {}'.format(roots[0], roots[1], \
        roots[2], roots[3]))

if __name__ == "__main__":
    main()