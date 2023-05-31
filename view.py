import controller
import model 

def menu():
    while True:
        print('\nМЕНЮ')
        print('1 - Показать все контакты')
        print('2 - Добавить новый контакт')
        print('3 - Поиск контакта')
        print('4 - Изменить существующую запись')
        print('5 - Удалить запись')
        print('6 - Закрыть программу\n')
        n = сhecking_the_number(input('Выберите пункт меню: '))

        if n == 1:
            print(controller.get_data)

        elif n == 2:
            name = input('Введите имя: ')
            surname = input('Введите фамилию: ')
            number = input('Введите номер телефона: ')
            controller.add_contact(name, surname, number)
        elif n == 3:
            search = input('Введите фамилию: ')
            print(controller.find_contact(surname=search))
            search = input('Введите имя: ')
            print(controller.find_contact(name=search))
            search = input('Введите номер  телефона: ')
            print(controller.find_contact(number=search))

        elif n == 4:
            print('1. Найти номер по фамилии.')
            print('2. Найти номер по имени.')
            print('3. Поиск по номеру телефона.')
            change = controller.change_contact(input('Введите номер пункта: '))
            if change == 1:
                search = input('Введите фамилию: ')
                controller.find_contact(surname=search)
                user_id = input('Введите id записи: ')
                new_number = input('Введите новый номер телефона: ')
                controller.change_contact(id=user_id, new_number=new_number)

            elif change == 2:
                search = input('Введите имя: ')
                controller.find_contact(name=search)
                user_id = input('Введите id записи: ')
                new_number = input('Введите новый номер телефона: ')
                controller.change_contact(id=user_id, new_number=new_number)

            elif change == 3:
                search = input('Введите номер телефона: ')
                controller.find_contact(number=search)
                user_id = input('Введите id записи: ')
                new_number = input('Введите новый номер телефона: ')
                controller.change_contact(id=user_id, new_number=new_number)

            else:
                print('\nТакого пункта меню не существует.\nВведите цифру, соответствующую пункту меню.')

        elif n == 5:
            print('1. Найти номер по фамилии.')
            print('2. Найти номер по имени.')
            print('3. Поиск по номеру телефона.')
            deleting = сhecking_the_number(input('Введите номер пункта: '))

            if deleting == 1:
                search = input('Введите фамилию: ')
                print(controller.find_contact(surname=search))
                user_id = input('Введите id записи: ')
                controller.delete_contact(id=user_id)

            elif deleting == 2:
                search = input('Введите имя: ')
                print(controller.find_contact(name=search))
                user_id = input('Введите id записи: ')
                controller.delete_contact(id=user_id)

            elif deleting == 3:
                search = input('Введите номер телефона: ')
                print(controller.find_contact(number=search))
                user_id = input('Введите id записи: ')
                new_number = input('Введите новый номер телефона: ')
                controller.delete_contact(id=user_id)

            else:
                print('\nТакого пункта меню не существует.\nВведите цифру, соответствующую пункту меню.')

        elif n == 6:
            print('Завершение!')
            break
        
        else:
            print('\nТакого пункта меню не существует.\nВведите цифру, соответствующую пункту меню.')


def сhecking_the_number(num):
    while num.isdigit() != True:
        num = input('Введите соответствующий пункт меню: ')
    return int(num)

