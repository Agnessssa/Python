# создание словаря с цветами смешариков
color = {
    "Лосяш": "шафрановый",
    "Копатыч": "коричневый"
}
# создание словаря с сериями лосяша
mult1 = {
    "Лосяш1": "Герой Плутона",
    "Лосяш2": "Бабочка",
    "Лосяш3": "Долгая рыбалка"
}
# создание словаря с сериями копатыча
mult2 = {
    "Копатыч1": "Долгая рыбалка",
    "Копатыч2": "Кулинария",
    "Копатыч3": "Танцор Диско"
}
# создание словаря с любимыми фразами смешариков
phrase = {
    "Лосяш": "",
    "Копатыч": ""
}
# добавление любимой фразы лосяша
phrase["Лосяш"] = "Феноменально!"
# добавление любимой фразы копатыча
phrase["Копатыч"] = "Укуси меня пчела!"
# удаление серии Герой Плутона
del mult1["Лосяш1"]
# замена цвета Копатыча
color["Копатыч"] = "Светло-коричневый"
# значение словаря с сериями Лосяша
mult1 = set(mult1.values())
# значение словаря с сериями Копатыча
mult2 = set(mult2.values())
# получение общей серии и Лосяша, и Копатыча
# ввод имени нового смешарика
a = input("Имя смешарика:")
# ввод цвета нового смешарика
color10 = input("Цвет:")
# ввод серии нового смешарика
mult20 = input("Серия:")
# ввод любимой фразы нового смешарика
phrase30 = input("Фраза:")
# создание соваря про нового смешарика
new_dict = (
    [
        [a, color10],
        [a, mult20],
        [a, phrase30]
    ]
)
# создание нового множества
new = {}
# значения цветов Лосяша и Копатыча
new = color.keys()
color_new = color.values()
mult_new = dict(zip(mult1.values(), mult2.values()))
phrase_new = phrase.values()
# вывод количества смешариков
print(len(new) + len(a.split()))
# вывод любимых фраз Лосяша и Копатыча
print(phrase.values())
# вывод общей серии
print(mult)
# вывод характеристик нового смешарика
print(new_dict)





