def check_phone_book():
    pb = open('phone-book.txt', 'a', encoding='utf-8')
    pb.close()


def get_phone_book():
    with open('phone-book.txt', 'r', encoding='utf-8') as pb:
        return [i for i in pb.read().splitlines()]


def add_contact(contact: str):
    with open('phone-book.txt', 'a', encoding='utf-8') as pb:
        pb.write(contact.title() + '\n')
    with open('phone-book.txt', 'r', encoding='utf-8') as pb:
        return str(pb.read().splitlines()[-1]) == contact.title()


def find_contact(request: str):
    contact_list = []
    with open('phone-book.txt', 'r', encoding='utf-8') as pb:
        for i in pb.read().splitlines():
            for j in i.split():
                if request.lower() == j.lower():
                    contact_list.append(i)
    return contact_list


def delete_contact(contact: str):
    pb_list = []
    with open('phone-book.txt', 'r', encoding='utf-8') as pb:
        for i in pb.read().splitlines():
            if i.lower() != contact.lower():
                pb_list.append(i)
    clear_phone_book()
    return fill_phone_book(pb_list)


def change_contact(old_contact: str, new_contact: str):
    step_1 = add_contact(new_contact)
    step_2 = delete_contact(old_contact)
    return step_1 and step_2


def clear_phone_book():
    with open('phone-book.txt', 'w', encoding='utf-8') as pb:
        pb.write('')
    with open('phone-book.txt', 'r', encoding='utf-8') as pb:
        return len(pb.readlines()) == 0


def fill_phone_book(pb_list: list):
    with open('phone-book.txt', 'a', encoding='utf-8') as pb:
        for i in pb_list:
            pb.write(i + '\n')
    with open('phone-book.txt', 'r', encoding='utf-8') as pb:
        return len(pb.readlines()) == len(pb_list)
