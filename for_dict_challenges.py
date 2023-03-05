# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]
lst = [a['first_name'] for a in students]
s = set(lst)
for b in s:
    print(f'{b}: {lst.count(b)}')

# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]
lst = [a['first_name'] for a in students]
lst1 = [lst.count(a) for a in lst]
d = {lst1[i]: lst[i] for i in range(len(lst))}
print(f'Самое частое имя среди учеников: {d[max(lst1)]}')


# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]
for j in range(len(school_students)):
    lst = [a['first_name'] for a in school_students[j]]
    lst1 = [lst.count(a) for a in lst]
    d1 = {lst1[i]: lst[i] for i in range(len(lst))}
    print(f'Самое частое имя в классе {j + 1}: {d1[max(lst1)]}')


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2в', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}
for i, d in enumerate(school):
    x = 0
    y = 0
    for j, n in enumerate(d['students']):
        if is_male[n['first_name']]:
            x += 1
        else:
            y += 1
    else:
        z = d['class']
        print(f'Класс: {z} девочки {y}, мальчики {x}')





# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}
L1 = []
L2 = []
for i, d in enumerate(school):
    lst = []
    for j, n in enumerate(d['students']):
        if is_male[n['first_name']]:
            lst.append(1)
        else:
            lst.append(0)
    else:
        L1.append(lst.count(1))
        L2.append(lst.count(0))
else:
    a = school[L1.index(max(L1))]['class']
    print(f'Больше всего мальчиков в классе {a}')
    b = school[L2.index(max(L2))]['class']
    print(f'Больше всего девочек в классе {b}')
