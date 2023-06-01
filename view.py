def greetings():
    print('Добро пожаловать в Телефонный справочник!')


def farewell():
    print('Вы закончили работу со справочником. До свидания!')


def show_menu():
    main_menu = ['1: Показать все контакты',
                 '2: Найти контакт',
                 '3: Добавить новый контакт',
                 '4: Изменить контакт',
                 '5: Удалить контакт',
                 '6: Очистить справочник',
                 '7: Выйти из приложения']
    print()
    print(*main_menu)


def show_contacts(pb: list):
    if not pb:
        print('\n' + 'Контакты не найдены.')
    else:
        print('\n' + 'Найдены следующие контакты:')
        for i in pb:
            print(i)


def confirm_adding(answer: bool, contact: str):
    if answer:
        print(f'Контакт {contact.title()} успешно добавлен в Справочник.')
    else:
        print(f'Произошла ошибка. Контакт {contact.title()} не добавлен. Повторите попытку.')


def confirm_deleting(answer: bool, contact: str):
    if answer:
        print(f'Контакт {contact.title()} успешно удален из Справочника.')
    else:
        print(f'Произошла ошибка. Контакт {contact.title()} не удален. Повторите попытку.')


def confirm_changing(answer: bool, contact_old: str, contact_new: str):
    if answer:
        print(f'Контакт {contact_old.title()} успешно заменен на {contact_new.title()}.')
    else:
        print(f'Произошла ошибка. Контакт {contact_old.title()} не изменен.')


def confirm_phone_book_clearing(answer: bool):
    if answer:
        print('Справочник успешно очищен.')
    else:
        print('Произошла ошибка. Справочник не очищен.')



def ask_contact_data(request: str):
    if request == 'to_delete':
        print('\n' + 'Последовательно введите данные контакта, который хотите удалить. '
              '(При необходимости сначала воспользуйтесь поиском)')
    elif request == 'to_change':
        print('\n' + 'Последовательно введите данные контакта, который хотите изменить. '
              '(При необходимости сначала воспользуйтесь поиском)')
    else:
        print('\n' + 'Последовательно введите новые данные контакта.')


def invalid_command():
    print('Выберите корректную команду: ')