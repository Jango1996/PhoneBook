def check_phone_book():
    pb = open('phone-book.txt', 'a', encoding='utf-8')
    pb.close()


def get_data():
    with open('phone-book.txt', 'r', encoding='utf-8') as pb:
        return [i for i in pb.read().splitlines()] if pb else 'Phone-book is empty'


def add_contact(contact: str):
    with open('phone-book.txt', 'a', encoding='utf-8') as pb:
        pb.write(contact.title() + '\n')
    with open('phone-book.txt', 'r', encoding='utf-8') as pb:
        return str(pb.read().splitlines()[-1]) == contact.title()


def find_contact(request: str):
    with open('phone-book.txt', 'r', encoding='utf-8') as pb:
        for i in pb.read().splitlines():
            for j in i.split():
                if request.lower() == j.lower():
                    return i
        return f'Sorry, contact not found'


def delete_contact(contact: str):
    pb_list = []
    with open('phone-book.txt', 'r', encoding='utf-8') as pb:
        for i in pb.read().splitlines():
            if i.lower() != contact.lower():
                pb_list.append(i)
    clear_phone_book()
    for i in pb_list:
        add_contact(i)


def change_contact(old_contact: str, new_contact: str):
    add_contact(new_contact)
    delete_contact(old_contact)


def clear_phone_book():
    with open('phone-book.txt', 'w', encoding='utf-8') as pb:
        pb.write('')
