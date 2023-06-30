# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1 - открыть файл
# 2 - сохранить файл
# 3 - показать всю телефонную книжку
# 4 - найти контакт
# 6 - изменить контакт
# 7 - удалить контакт
# 8 - выход



def open_create_file():
    data = open('телефонная_книга.txt','a')
    data.close()

def save_file():
    first_name = input("Введите имя для сохранения: ")
    second_name = input("Введите фамилию для сохранения: ")
    middle_name = input("Введите отчество для сохранения: ")
    phone_number = int(input("Введите номер для сохранения: "))
    with open('телефонная_книга.txt', 'a', encoding='utf-8') as date:
        date.write(f"{first_name} {second_name} {middle_name} {phone_number}\n")
        print("Файл сохранен.")

def find_contact():
    name = input("Введите имя контакта для поиска: ")
    with open('телефонная_книга.txt', 'r', encoding='utf-8') as date:
        contacts = date.read()
        if name in contacts:
            print("Контакт найден:")
        else:
            print("Контакт не найден")

def edit_contact():
    name = input("Введите имя контакта для редактирования: ")
    new_number = input("Введите новый контакт: ")
    with open('телефонная_книга.txt', 'r', encoding='utf-8') as date:
        contacts = date.read()
    if name in contacts:
        updated_contacts = contacts.replace(name,new_number)
        with open('телефонная_книга.txt', 'w', encoding='utf-8') as date:
            date.write(updated_contacts)
        print("Контакт успешно отредактирован.")
    else:
        print("Контакт не найден.")

def delete_contact():
    name = input("Введите имя контакта для удаления: ")
    with open('телефонная_книга.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()

    updated_lines = [line for line in lines if name not in line]

    with open('телефонная_книга.txt', 'w', encoding='utf-8') as file:
        file.writelines(updated_lines)

    if len(lines) != len(updated_lines):
        print("Контакт успешно удален.")
    else:
        print("Контакт не найден.")

def main():
    while True:
        print("Телефонная_книга:")
        print("1. Открыть файл(создать)")
        print("2. Сохранить контакт")
        print("3. Найти контакт")
        print("4. Изменить контакт")
        print("5. Удалить контакт")
        print("6. Выход")

        choice = input("Выберите пункт меню: ")

        if choice == "1":
            open_create_file()
        elif choice == "2":
            save_file()
        elif choice == "3":
            find_contact()
        elif choice == "4":
            edit_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Выход из программы.")
            break
        else:
            print("Некорректный выбор. Повторите попытку.")

main()