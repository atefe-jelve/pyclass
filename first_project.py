import sqlite3
def search_contact(action_code):
    conn = sqlite3.connect('contact_phone.db')
    cursor = conn.cursor()
    name_contact = (input('enter your name you want :\n'))
    num_contact = int(input('enter your phone number you want :\n'))
    search_query = f'select * from contact where name =="{name_contact}" or tel_number == {num_contact}'
    cursor.execute(search_query)
    result = cursor.fetchall()
    print(result)
    conn.close()


def add_contact(action_code):
    name_contact = (input('enter your name you want add:\n'))
    family_contact = (input('enter your family you want add:\n'))
    num_contact = int(input('enter your phone number you want add :\n'))
    conn = sqlite3.connect('contact_phone.db')
    cursor = conn.cursor()
    add_query = f'insert into contact (name,family,tel_number) values ("{name_contact}","{family_contact}",{num_contact})'
    cursor.execute(add_query)
    conn.commit()
    conn.close()

def update_contact(action_code):
    name_contact = (input('enter your name you want update:\n'))
    new_name = (input('enter new name :\n'))
    new_family = (input('enter new family :\n'))
    new_num = int(input('enter new phone number :\n'))
    conn = sqlite3.connect('contact_phone.db')
    cursor = conn.cursor()
    update_query = f'update contact set name = "{new_name}" , family = "{new_family}" , tel_number={new_num} where name =="{name_contact}" ;'
    cursor.execute(update_query)
    conn.commit()
    conn.close()

def delete_contact(action_code):
    name_contact = (input('enter your name you want delete:\n'))
    num_contact = int(input('enter your phone number you want :\n'))
    conn = sqlite3.connect('contact_phone.db')
    cursor = conn.cursor()
    delete_query = f'delete from contact where name =="{name_contact}" and tel_number == {num_contact}'
    cursor.execute(delete_query)
    conn.commit()
    conn.close()

i = 'y'
while i =='y':
    i = input('if you want close program enter "n" or for continue enter "y": \t\t ')
    action_code = int(input('enter number 1 for search contact  \n number 2 for add contact: \n number 3 for edit contact: \n number 4 for delete contact:\n'))
    if action_code == 1:
        search_contact(action_code)
    elif action_code == 2:
        add_contact(action_code)
    elif action_code == 3:
        update_contact(action_code)
    elif action_code == 4:
        delete_contact(action_code)
