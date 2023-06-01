import view
import model


def start():
    model.check_phone_book()
    view.greetings()
    program_running = True
    while program_running:
        view.show_menu()
        command = input('Выберите задачу: ')
        match command:
            case '1':  # Показать все контакты
                view.show_contacts(model.get_phone_book())
            case '2':  # Найти контакт
                requested_contact = input('Введите фамилию, или имя, или телефон для поиска: ')
                view.show_contacts(model.find_contact(requested_contact))
            case '3':  # Добавить новый контакт
                contact_to_add = get_contact_data()
                view.confirm_adding(model.add_contact(contact_to_add), contact_to_add)
            case '4':  # Изменить контакт
                view.ask_contact_data('to_change')
                contact_to_change = get_contact_data()
                view.ask_contact_data('to_add')
                new_data = get_contact_data()
                view.confirm_changing(model.change_contact(contact_to_change, new_data), contact_to_change, new_data)
            case '5':  # Удалить контакт
                view.ask_contact_data('to_delete')
                contact_to_delete = get_contact_data()
                view.confirm_deleting(model.delete_contact(contact_to_delete), contact_to_delete)
            case '6':  # Очистить справочник
                view.confirm_phone_book_clearing(model.clear_phone_book())
            case '7':  # Выйти из приложения
                view.farewell()
                program_running = False
            case _:  # дефолтный вариант
                view.invalid_command()


def get_contact_data():
    return ' '.join([input('Введите Фамилию контакта: '),
                     input('Введите Имя контакта: '),
                     input('Введите Телефон контакта: ')])