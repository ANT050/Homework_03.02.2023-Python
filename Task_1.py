import numpy as np
import matplotlib.pyplot as plt


#Функция вычисления математического выражения
def f(x):
    return -12*x**4*np.sin(np.cos(x)) - 18*x**3 + 5*x**2 + 10*x - 30

# Функция проверки на правильность ввода значений диапазона
def checking_input():
    while True:
        try:
            min_value = float(
                input("\n\033[32mВведите минимальное значение диапазона min_value: \033[0m"))
            max_value = float(
                input("\033[32mВведите максимальное значение диапазона max_value: \033[0m"))
            if min_value >= max_value:
                raise ValueError("Проверьте правильность ввода")
            return min_value, max_value
        except ValueError:
            print("\n\033[31mПроверьте правильность ввода: min_value должно быть меньше max_value\n"
                  "и значения должны быть числом!!!\033[0m")

# Нахождение корней в выбранном диапазоне (используется метод деления пополам)
def finding_roots(f, min_value, max_value, accuracy_root_search=1e-5):
    mid_point = (min_value + max_value) / 2
    mid_value = f(mid_point)
    if abs(mid_value) < accuracy_root_search:
        return mid_point
    elif f(min_value) * mid_value < 0:
        return finding_roots(f, min_value, mid_point, accuracy_root_search)
    else:
        return finding_roots(f, mid_point, max_value, accuracy_root_search)

# Функция получения списка уникальных корней
def get_roots(f, min_value, max_value):
    roots = []
    x = np.linspace(min_value, max_value)
    y = f(x)
    for i in range(len(y) - 1):
        if y[i] * y[i+1] < 0:
            root = finding_roots(f, x[i], x[i+1])
            roots.append(root)
    return np.unique(roots)

# Функция вывод результата(корней) в консоль
def plot_function(f, min_value, max_value):
    roots = get_roots(f, min_value, max_value)
    rounded_roots = [round(root, 2) for root in roots]
    print("\n\033[33mПолученные корни:\033[0m", rounded_roots)
    return roots

#Функция нахождения интервалов, на которых функция возрастает
def increasing_intervals(f, min_value, max_value, step=0.01):
    inc_int = []
    current_interval = [min_value, min_value]
    previous_value = f(min_value)
    for x in np.arange(min_value + step, max_value, step):
        current_value = f(x)
        if current_value > previous_value:
            current_interval[1] = x
        else:
            if current_interval[1] - current_interval[0] > step:
                inc_int.append([round(i, 2) for i in current_interval])
            current_interval = [x, x]
        previous_value = current_value
    if current_interval[1] - current_interval[0] > step:
        inc_int.append([round(i, 2) for i in current_interval])
    print("\n\033[33mИнтервалы, на которых функция возрастает: \033[0m[ " + ", ".join(["({}, {})".format(*map(str, interval)) for interval in inc_int]) + " ]")

#Функция нахождения интервалов, на которых функция убывает
def decreasing_intervals(f, min_value, max_value, step=0.01):
    dec_int = []
    current_interval = [min_value, min_value]
    previous_value = f(min_value)
    for x in np.arange(min_value + step, max_value, step):
        current_value = f(x)
        if current_value < previous_value:
            current_interval[1] = x
        else:
            if current_interval[1] - current_interval[0] > step:
                dec_int.append([round(i, 2) for i in current_interval])
            current_interval = [x, x]
        previous_value = current_value
    if current_interval[1] - current_interval[0] > step:
        dec_int.append([round(i, 2) for i in current_interval])
    print("\033[33mИнтервалы, на которых функция убывает: \033[0m[ " + ", ".join(["({}, {})".format(*map(str, interval)) for interval in dec_int]) + " ]")

# Функция определения координат вершины функции f(x)
def vertex_coordinates(x, y):
    vertex = np.argmin(y)
    print("\n\033[33mКоординаты вершины: \033[0m({:.2f}, {:.2f})".format(x[vertex], y[vertex]))
    return vertex

#Функция определения промежутков, на котором f(x) > 0
def positive_intervals(max_value, x, y):
    pos_int = []
    start = None
    for i in range(len(y)):
        if y[i] > 0:
            if start is None:
                start = x[i]
        elif start is not None:
            pos_int.append((start, x[i]))
            start = None
    if start is not None:
        pos_int.append((start, max_value))
    print("\n\033[33mИнтервалы, на которых f(x) > 0: \033[0m", [(round(start, 2), round(end, 2)) for start, end in pos_int])

#Функция определения промежутков, на котором f(x) < 0
def negative_intervals(min_value, x, y):
    neg_int = []
    start = None
    for i in range(len(y)):
        if y[i] < 0:
            if start is None:
                start = x[i]
        elif start is not None:
            neg_int.append((start, x[i]))
            start = None
    if start is not None:
        neg_int.append((start, min_value))
    print("\033[33mИнтервалы, на которых f(x) < 0: \033[0m", [(round(start, 2), round(end, 2)) for start, end in neg_int])

#Функция построения графика
def plotting(x, y, vertex, roots):
  plt.plot(x, y, 'b-')
  plt.plot(x[vertex], y[vertex], 'ro', markersize=5)
  plt.axvline(0, color='black', lw=1)
  plt.axhline(0, color='black', lw=1)
  plt.scatter(roots, np.zeros_like(roots), color='black')
  plt.text(0.55, 0.9, "Черные точки - это корни\nКрасная точка - это вершина", transform=plt.gca().transAxes)
  plt.show()


min_value, max_value = checking_input()
x = np.linspace(min_value, max_value)
y = f(x)

roots = plot_function(f, min_value, max_value)
vertex = vertex_coordinates(x, y)

increasing_intervals(f, min_value, max_value)
decreasing_intervals(f, min_value, max_value)
positive_intervals(max_value, x, y)
negative_intervals(min_value, x, y)
plotting(x, y, vertex, roots)




