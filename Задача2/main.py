    # импорт библиотеки
    import json


    # создание главной функции
    def inspect_func(input_file_way, output_file_way):
        # открытие входного файла
        with open(input_file_way, 'r') as input_file:
            # создание словаря для функций
            func_dict = {}
            # бегаю по строчкам во входном файле
            for line in input_file.readlines():
                # нахожу строки, где объявляются функции
                if len(line) >= 3 and line[:3] == 'def':
                    # создаю копию строки, где все разделители заменяю на пробелы
                    new_line = ''
                    # отрезаю def
                    line = line[3:]
                    # бегаю посимвольно
                    for i in range(len(line)):
                        # если символ - не разделитель
                        if line[i] not in list('()=,:'):
                            # добавляю его
                            new_line += line[i]
                        # иначе
                        else:
                            # добавляю пробел
                            new_line += ' '
                    # разбиваю на отдельные слова
                    line_arr = new_line.split()
                    # первое слово - название функции
                    func = line_arr[0]
                    # отрезаю название функции
                    line_arr = line_arr[1:]
                    # добавляю эту функцию
                    func_dict[func] = {'args': [], 'kwargs': {}}
                    # пробегаюсь дальше по индексам
                    for arg_idx in range(len(line_arr)):
                        # если первые символы - не кавычки или цифры, значит это arg
                        if line_arr[arg_idx][0] not in list('0123456789\'\"'):
                            # добавляю его в список функции
                            func_dict[func]['args'].append(line_arr[arg_idx])
                        # иначе это kwarg
                        else:
                            # в словаре добавляю поле с названием arg и значением kwarg (kwarg всегда сразу после соответствующего arg, поэтому можно просто отнять 1 от индекса)
                            func_dict[func]['kwargs'][line_arr[arg_idx - 1]] = line_arr[arg_idx]
        # открываю выходной файл
        with open(output_file_way, 'w') as output_file:
            # записываю в него словарь
            json.dump(func_dict, output_file, indent=4)


    # вызываю главную функцию
    inspect_func('input.txt', 'output.json')
