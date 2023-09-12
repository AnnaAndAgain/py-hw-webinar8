# Задача 55.
# Создать телефонный справочник с возможностью импорта и экспорта данных
# в формате .txt. Фамилия, имя, отчество, номер телефона - данные,
# которые должны находиться в файле.
# Программа должна выводить данные
# Программа должна сохранять данные в текстовом файле
# Пользователь может ввести одну из характеристик для поиска определенной записи
# (Например имя или фамилию человека)
# Использование функций. Ваша программа не должна быть линейной

# Задача 38.
# Дополнить телефонный справочник возможностью изменения и удаления данных. Пользователь также может ввести
# имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных

import os


# генерация сообщения об ошибке -- использую его в нескольких функциях, не хочу хардкодить в каждой с опечатками
def error_message():
    return "Извините, такой записи нет\n"


# запись в файл
def write_to_file(path1):
    tmp_line = input("Введите ФИО и телефон: ")
    with open('phones.txt', "a") as file1:
        file1.write(tmp_line + "\n")


# поиск по файлу -- переделала, чтобы возвращал списки
def search_file(path1, search_input):
    with open('phones.txt', "r") as file1:
        lst_1 = file1.readlines()
        flag1 = False
        result = []
        for line in lst_1:
            if search_input in line:
                result.append(line)
                flag1 = True
        if not flag1:
            result.append(error_message())
    return result


# вывод всего файла
def show_all(path1):
    with open('phones.txt', "r") as file1:
        return file1.read()


# удаление по точной строке
def del_line_from_file(path1, str_to_del):
    tmp_list = []

    # выгружаю файл в список
    with open('phones.txt', "r") as file1:
        tmp_list = file1.readlines()
        # print(tmp_list)

    # нахожу индекс нужной строки в списке и удаляю ее из списка
    tmp_index = tmp_list.index(str_to_del)
    tmp_list.pop(tmp_index)
    # print(tmp_list)

    # записываю новый список в файл
    with open('phones.txt', "w") as file1:
        file1.writelines(tmp_list)
        print("Строка успешно удалена\n")


# правка по точной строке
def edit_line(path1, str_to_edit):
    tmp_list = []

    #запрашиваю, на что меняем
    new_str = input("Введите данные, на которые нужно поменять текущие (строку целиком: ФИО и номер телефона): ")

    # выгружаю файл в список
    with open('phones.txt', "r") as file1:
        tmp_list = file1.readlines()
        # print(tmp_list)

    # нахожу индекс нужной строки в списке и удаляю ее из списка
    tmp_index = tmp_list.index(str_to_edit)
    tmp_list[tmp_index] = new_str
    # print(tmp_list)

    # записываю новый список в файл
    with open('phones.txt', "w") as file1:
        file1.writelines(tmp_list)
        print("Строка успешно изменена\n")


# выбор конкретной строки, которую пользователь хочет удалить или изменить, и вызов соответствующей процедуры
def check_user_request(path1, what_to_find, what_to_do):
    # ищем строки с введенными пользователем символами
    lines_to_edit = search_file(path1, what_to_find)
    # обрабатываем случай, когда запрошенной информации в файле нет (сообщение об ошибке, возврат в меню)
    if lines_to_edit[0] == error_message():
        print(lines_to_edit[0])
        return

    # просим выбрать одну конкретную строку и подтвердить удаление/изменение
    print(f"Выберите номер строки, которую хотите {what_to_do}:")
    a = None
    for i in range(len(lines_to_edit)):
        print(f"{i}. {lines_to_edit[i]}", end="")
    print(f"{len(lines_to_edit)}. Не хочу ничего {what_to_do}.")
    a = int(input())

    if a == len(lines_to_edit):
        return
    elif 0 <= a < len(lines_to_edit):
        print(f"Вы уверены, что хотите {what_to_do} строку ниже?\n"
              f"{lines_to_edit[a]}"
              f"Если уверены, нажмите Y.")
        # вызываем, собственно, удаление или правку
        if input("").upper() == 'Y':
            if what_to_do == "удалить":
                # интуитивно хочется для выбора между удалением и правкой завести отдельную переменную int, с кодами
                # каждого действия, но по сути она будет просто дублировать эти строки, так что пользуюсь строками
                del_line_from_file(os.getcwd(), lines_to_edit[a])
            elif what_to_do == "изменить":
                edit_line(os.getcwd(), lines_to_edit[a])
        return


# меню пользоателя
def get_user_intention():
    txt_zapros = "Введите номер команды, которую хотите выполнить.\n" \
                 "1. Записать новые данные в файл\n" \
                 "2. Найти и вывести конкретную запись в файле\n" \
                 "3. Вывести весь файл\n" \
                 "4. Удалить запись\n" \
                 "5. Изменить запись\n" \
                 "6. Выйти из программы\n"
    a = None
    while a != '6':
        a = input(txt_zapros)
        if a == '1':
            write_to_file(os.getcwd())
        elif a == '2':
            to_search = input("Что ищем? ")
            result = search_file(os.getcwd(), to_search)
            print(*result)
        elif a == '3':
            result = show_all(os.getcwd())
            print(result)
            print()
        elif a == '4':
            to_search = input("Что вы хотите удалить? ")
            check_user_request(os.getcwd(), to_search, "удалить")
        elif a == '5':
            to_search = input("Что вы хотите изменить? ")
            check_user_request(os.getcwd(), to_search, "изменить")


get_user_intention()
