import view, model

def start():
    model.check_phone_book()
    view.greetings()
    while True:
        view.menu()
        answer = input('Введите команду: ')
        if answer =='1':
            data = model.get_data()
            view.show_contacts(data)
        elif answer == '2':
            contact = [input('Введите Фамилию контакта: '), input('Введите Имя контакта: '), input('Введите Телефон контакта: ')]
            res = model.add_contact(contact)
            if res:
                view.success(res)

