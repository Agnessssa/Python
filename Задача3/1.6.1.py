# импорт библиотеки для работы с папками
from pathlib import Path

# создание корневой папки
Path("love_and_piece").mkdir(exist_ok=True)
# открытие исходного файла
with open('Толстой Лев. Война и мир. Книга 1 - royallib.ru.txt', mode='r', encoding='cp1251') as main_file:
    # ввод счетчика абзацев
    number_of_paragraph = 0
    # завод строчной переменной, где будет храниться текст из абзаца
    paragraph_str = "."
    # начало цикла, где будет происходить проверка по абзацу посимвольно
    while paragraph_str != "":
        # читка абзаца в строку
        paragraph_str = main_file.readline()
        # проверка, не пустой ли он
        if paragraph_str not in ("\n", ""):
            # если не пуст, увеличение счетчика
            number_of_paragraph += 1
            # создание папки абзаца
            Path("love_and_piece/{}".format(number_of_paragraph)).mkdir(exist_ok=True)
            # счетчик для предложений
            number_of_sentence = 1
            # вывод длины абзаца
            size_of_paragraph = len(paragraph_str)
            # контейнер для символов предложения
            sentence = ""
            # проверка посимвольно
            for i in range(size_of_paragraph):
                # чтение символа
                char = paragraph_str[i]
                # добавление символа к строке
                sentence += char
                # проверка, не знак препинания ли это и есть ли следующий символ
                if char in ("!", "?", ".") and i < size_of_paragraph - 1:
                    # если после знака препинания пробел - это конец предложения
                    if paragraph_str[i + 1] == " ":
                        # завод файла для предложения
                        with open("love_and_piece/{}/{}.txt".format(number_of_paragraph, number_of_sentence),
                                  "w") as sentence_file:
                            # запись в него предложения
                            sentence_file.write(sentence)
                        # увеличение счетчика
                        number_of_sentence += 1
                        # обнуление буфера
                        sentence = ""
                    # если после препинания переход на новую строку - это конец абзаца
                    elif paragraph_str[i + 1] == "\n":
                        # завод файла для предложения
                        with open("love_and_piece/{}/{}.txt".format(number_of_paragraph, number_of_sentence),
                                  "w") as sentence_file:
                            # запись в него предложения
                            sentence_file.write(sentence)
                        # обрывание цикла, так как абзац прочтен
                        break
                # если дошли до конца и там не было знака препинания - аналогично
                elif i == size_of_paragraph - 1:
                    # создание файла для предложения
                    with open("love_and_piece/{}/{}.txt".format(number_of_paragraph, number_of_sentence),
                              "w") as sentence_file:
                        # запись в него предложение
                        sentence_file.write(sentence)