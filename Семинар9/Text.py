main_menu = '''\nГлавное меню: 
    1. Открыть файл
    2. Записать файл
    3. Показать контакт
    4. Добавить контакт
    5. Найти контакт
    6. Изменить контакт
    7. Удалить контакт
    8. Выход\n'''

input_choice = 'Выберете пункт меню: '

load_successful = 'Телефонная книга открыта успешно'
save_successful = 'Телефонная книга успешно сохранена'
load_error = 'Телефонная книга пусрта или не открыта'
input_contact = {'name':'Введите имя: ',
                 'phone': 'Введите телефон: ', 
                 'comment':'Введите комментарий: '}

new_contact = 'Введите данные нового контакта: (пустое поле для отмены) '
def new_contact_sucessful(name: str) -> str:
    return f'Контакт {name} успешно добавлен'

cancel_input = 'Отмена ввода'

index_del_contact = 'Введите индекс контакта, который хотите удалить: '

index_modify_contact = 'Введите индекс контакта, который хотите изменить: '

def del_contact(name: str):
    return f'Контакт {name} успешно удалён'

def find_contact(name: str):
    return f"Найден контакт: {name}"


def modify_contact (name: str):
    return f"Контакт {name} успешно изменен"