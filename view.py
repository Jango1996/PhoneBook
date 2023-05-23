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
            print(model.show_contacts)

        elif n == 2:

        elif n == 3:

        elif n == 4:

        elif n == 5:

        elif n == 6:
            print('Завершение!')
            break
        
        else:
            print('\nТакого пункта меню не существует.\nВведите цифру, соответствующую пункту меню.')


def сhecking_the_number(num):
    while num.isdigit() != True:
        num = input('Введите соответствующий пункт меню: ')
    return int(num)

