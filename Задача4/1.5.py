# рандомный выбор слова
from random import choice
# разрешенные буквы
alphabet = "abcdefghijklmnopqrstuvwxyz"
# список слов, из которых рандомно выбирается одно
words_list = ["opera", "avoid", "prime", "angry", "alive", "beach", "berry", "click", "claus"]
# рандомный выбор слова
word = choice(words_list)
# создание пустого списка
user_inputs = []
# присваивание нулевого значения для шага
step = 0
# "пока пользователь не выиграл"
win = False
# цикл:
while True:
    # введение пользователем слова
    user_word = input().lower()
    # условие правильности(5 символов и латиница)
    flag1 = True and len(user_word) == 5
    # для введенного слова:
    for i in user_word:
        # если символы не латиницы
        if not i in alphabet:
            # неправда
            flag1 = False
            # прекращение
            break
    # пока попытки есть и слово соответствует критериям:
    if flag1 and step < 6:
        # отнимается попытка
        step += 1
        # массив с вводами пользователя
        user_inputs.append(user_word)
        # если слово угадано
        if user_word == word:
            # вывод конечной фразы
            print("Вы угадали")
            # изменение значения win
            win = True
            # прекращение
            break
        # иначе:
        else:
            # буквы из введенного слова
            user_letter = set(user_word)
            # буквы из загаданного слова
            word_letter = set(word)
            # для этих букв:
            for i in user_letter:
                # если некоторые из них совпадают в обоих словах:
                if i in word_letter:
                    # выводим их
                    print(i, end=" ")
            # если попытки кончились
            if step == 6:
                # вывод конечной фразы
                print("\nВы не угадали")
            # иначе:
            else:
                # вывод количества оставшихся попыток
                print("\nУ вас осталось такое количество попыток: {}".format(6 - step))
    # если недопустимые символы или длина слова
    else:
        # вывод конечной фразы
        print("Некорректный ввод")
# вывод статистики пользовательского ввода
for i in range(len(user_inputs)):
    # является ли попытка последней
    if i < len(user_inputs) - 1:
        # выводим слова-попытки пользователя
        print(user_inputs[i])
    # если слово было угадано:
    elif win:
        # вывод конечной фразы
        print(user_inputs[i] + " - success")
    # иначе:
    else:
        # выводим слова-попытки пользователя
        print(user_inputs[i])
