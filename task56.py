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


def write_to_file(path1):
    tmp_line = input("Введите ФИО и телефон: ")
    with open('phones.txt', "a") as file1:
        file1.write(tmp_line + "\n")


def search_file(path1, search_input):
    with open('phones.txt', "r") as file1:
        lst_1 = file1.readlines()
        flag1 = False
        result = "\n"
        for line in lst_1:
            if search_input in line:
                result = result + line
                flag1 = True
        if not flag1:
            result = "Извините, такой записи нет\n"
    return result


def show_all(path1):
    with open('phones.txt', "r") as file1:
        return file1.read()


def del_line(path1, what_to_del):
    search_file(path1, what_to_del)
    pass


def edit_line(path1, what_to_edit):
    search_file(path1, what_to_edit)
    pass



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
            print(result)
        elif a == '3':
            result = show_all(os.getcwd())
            print(result)
        elif a == '4':
            to_search = input("Что вы хотите удалить? ")
            result = search_file(os.getcwd(), to_search)
        elif a == '5':
            result = show_all(os.getcwd())
            print(result)


get_user_intention()
