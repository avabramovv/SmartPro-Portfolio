from classes import StudProjectGraded, Student

projects2 = {
    1: StudProjectGraded(1, 'Какой-то проект', 'Иванов Иван Иванович',
          ['Тег 1', 'Тег 2'], 7, '01.09.2023', '01.06.2027', 'https://ru.wikipedia.org/wiki/Иван', 'Аналатик'),
    2: StudProjectGraded(2, 'Средний проект', 'Владимиров Владимир Владимирович',
          ['Тег 1', 'Тег 2'], 8, '02.09.2023', '02.09.2024', 'https://ru.wikipedia.org/wiki/Владимир', 'Разработчик'),
    3: StudProjectGraded(3, 'Большой проект', 'Петров Пётр Петрович',
          ['Тег 1', 'Тег 2'], 6, '03.09.2023', '03.08.2024', 'https://ru.wikipedia.org/wiki/Пётр', 'Менеджер'),
    4: StudProjectGraded(4, 'Маленький проект', 'Петров Пётр Петрович',
          ['Тег 1', 'Тег 2'], 6, '03.08.2023', '03.06.2025', 'https://ru.wikipedia.org/wiki/Пётр', 'Тестировщик'),
    462: StudProjectGraded(
        462,
        'Доработка системы SmartPro', 
        'Лобок Татьяна Сергеевна',
        ['прикладной', 'RU'], 9,
        '30.06.2024', '31.05.2025',
        'https://smartpro.hse.ru/epp-view/462',
        'Тестировщик')
}

edu_info2 = {
    'fio': 'Антонов Арсений Петрович',
    'specialty': 'Прикладная математика и информатика',
    'level': 'Бакалавриат',
    'course_no': 2
    }

user2 = Student(2, 'user2', 'pass2', edu_info2, projects2)

######################################################################################

projects1 = {
    131: StudProjectGraded(
        131,
        'Популяризация научных исследований среди учащихся школ', 
        'Кожанов Андрей Александрович',
        ['научный', 'прикладной', 'RU'], 10,
        '25.07.2023', '14.11.2023',
        'https://smartpro.hse.ru/epp-view/131',
        'Лектор'),

    462: StudProjectGraded(
        462,
        'Доработка системы SmartPro', 
        'Лобок Татьяна Сергеевна',
        ['прикладной', 'RU'], 8,
        '30.06.2024', '31.05.2025',
        'https://smartpro.hse.ru/epp-view/462',
        'Аналитик'),

    219: StudProjectGraded(
        219,
        'Анализ данных туристского дискурса', 
        'Смольянина Елена Анатольевна',
        ['прикладной', 'RU'], 4,
        '29.09.2023', '25.06.2024',
        'https://smartpro.hse.ru/epp-view/219',
        'Лектор'),
}

edu_info1 = {
    'fio': 'Васечкин Артём Александрович',
    'specialty': 'Прикладной анализ данных',
    'level': 'Бакалавриат',
    'course_no': 1
    }

user1 = Student(1, 'user1', 'pass1', edu_info1, projects1)