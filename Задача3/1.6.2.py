# импорт библиотеки для работы с папками
from pathlib import Path

# задание корневой папки
root = "love_and_piece"
# завод файла, куда будет все записываться
with open("war_and_peace.txt", "w") as main_file:
    # счетчик абзацев
    number_of_paragraph = 0
    # проверка по абзацам
    while True:
        # увеличение счетчика
        number_of_paragraph += 1
        # путь к папке абзаца
        directory = root + "/{}".format(number_of_paragraph)
        # если такой нет
        if not Path(directory).exists():
            # то и кина не будет(обрывание))
            break
        # иначе - заводим буфер для абзаца
        paragraph_str = ""
        # счетчик предложений
        number_of_sentence = 0
        # проверка по предложениям
        while True:
            # увеличение счетчика
            number_of_sentence += 1
            # прописываем путь к файлу предложения
            way_to_file = directory + "/{}.txt".format(number_of_sentence)
            # если такого нет
            if not Path(way_to_file).exists():
                # кина опять не будет(обрывание))
                break
            # иначе открывам файл
            with open(way_to_file, "r", encoding='cp1251') as sentence_file:
                # убираем текст из него и кладем в буфер
                paragraph_str += sentence_file.read()
        # в главный файл запись абзаца
        main_file.write(paragraph_str + "\n\n")