<a id="return"></a>

<center>

# Знакомство с языком Python (семинары)

## Урок 11. Jupyter Notebook и несколько слов об аналитике

</center>


<u>***Задача***</u>

f(x) = -12*x**4*sin(cos(x)) - 18*x**3+5*x**2 + 10*x - 30

* Определить корни

* Найти интервалы, на которых функция возрастает

* Найти интервалы, на которых функция убывает

* Построить график

* Вычислить вершину

* Определить промежутки, на котором f > 0

* Определить промежутки, на котором f < 0

---

**Определение корней:**

Находим корни в диапазоне, который указывает пользователь в консоли (от min_value до max_value). Используется метода деления пополам. На вход функция finding_roots принимает функцию f(x), min_value и max_value и требуемую точность accuracy_root_search, чем меньше значение accuracy_root_search, тем точнее будет возвращаемый корень.В функции get_roots определяем уникальные корни функции f(x) в интервале, который указывает пользователь в консоли (от min_value до max_value). Функция plot_function выводит полученный результат, форматируя его.

**Результат:**

<img src="images\roots.jpg" height="86" width="506"/>

---

**Нахождение интервалов, на которых функция возрастает и убывает:**

*increasing_intervals* - находит интервалы, в которых функция f(x) возрастает.

*decreasing_intervals* - находит интервалы, в которых функция f(x) убывает.

Обе функции на вход принимают функцию f(x), интервал, который указывает пользователь в консоли (от min_value до max_value) и аргумент step (по умолчанию 0.01), который определяет размер шага, который используется для вычисления функции. Метод arange используется для перебора диапазона значений между значениями min_value и max_value с шагом step.

**Результат:**

<img src="images\ascen_descen.jpg" height="112" width="965"/>

---

**Вычисление вершины:**

*vertex_coordinates* - нахождение вершины функции f(x). Функция np.argmin возвращает индекс минимального значения в массиве, который соответствует y-координате вершины. Координата x вершины определяется с использованием этого индекса в массиве x.

**Результат:**

<img src="images\top.jpg" height="87" width="462"/>

---

**Определить промежутки, на котором f > 0, f < 0:**

*positive_intervals* - функция определения промежутков, на котором f > 0. Начало положительного интервала - когда в функции f(x) найдено положительное значение. Конец положительного интервала - следующее отрицательное значение в функции f(x) или окончание интервала, где последнее значение все еще положительное.

*negative_intervals* - функция определения промежутков, на котором f < 0. Начало отрицательного интервала - когда в функции f(x) найдено отрицательное значение. Конец отрицательного интервала - следующее положительное значение в функции f(x) или окончание интервала, где последнее значение все еще отрицательное.

**Результат:**

<img src="images\more_less.jpg" height="109" width="788"/>

---

**Построение графика:**

*plotting* - функция для построения графика функции f(x). Для построения графика используется библиотека Matplotlib. Красная точка - вершина функции f(x). Черные точки - корни функции f(x).

**Результат:**

<img src="images\chart.jpg" height="816" width="1012"/>

---

:point_right: [Перейти к решению]( "Открыть")

---

:point_right: [Вначало](#return "Вернуться вначало")