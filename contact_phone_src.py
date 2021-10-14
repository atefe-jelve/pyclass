import sqlite3

def search_contact(action_code):
    conn = sqlite3.connect('contact_phone.db')
    cursor = conn.cursor()
    name_contact = (input('enter your name you want :\n\n'))
    num_contact = int(input('enter your phone number you want :\n\n'))
    search_query = f'select contact_id,name,family,tel_number from contact where name like "{name_contact}" or tel_number like {num_contact}'
    cursor.execute(search_query)
    result = cursor.fetchall()
    if len(result) != 0 :
        print('========================================================================')
        print('==========================  result search  =============================')
        print('========================================================================')
        print('========================================================================')
        print(' id      |       name       |        family     |         number        ')
        print('========================================================================\n')
        for row in result:
            print(*row, sep='               ')
    else :
        print('                           the name not saved                           ')
        print('                            please try agin                             \n')
    conn.close()
    print(' ')

def add_contact(action_code):
    print('========================================================================')
    conn = sqlite3.connect('contact_phone.db')
    name_contact = (input('enter your name you want add:\n\n'))
    family_contact = (input('enter your family you want add:\n\n'))
    num_contact = int(input('enter your phone number you want add :\n\n'))
    cursor = conn.cursor()
    add_query = f'insert into contact (name,family,tel_number) values ("{name_contact}","{family_contact}",{num_contact})'
    cursor.execute(add_query)
    conn.commit()
    search_query = f'select contact_id,name,family,tel_number from contact where name == "{name_contact}" and tel_number == {num_contact}'
    cursor.execute(search_query)
    result = cursor.fetchall()
    print('=====================  your contact add to list  =======================')
    print('========================================================================')
    print(' id      |       name       |        family     |         number        ')
    print('========================================================================')
    for row in result:
        print(*row, sep='               ')
    conn.close()
    print('========================================================================\n')
    
def update_contact(action_code):
    print('========================================================================')
    conn = sqlite3.connect('contact_phone.db')
    cursor = conn.cursor()
    name_contact = (input('enter your name you want update:\n\n'))
    search_query = f'select contact_id,name,family,tel_number from contact where name like "{name_contact}"'
    cursor.execute(search_query)
    result = cursor.fetchall()
    if len(result) != 0:
        print('========================================================================')
        print(' id      |       name       |        family     |         number        ')
        print('========================================================================')
        for row in result:
            print(*row, sep='               ')
        update_id = int((input('if you want update contact enter id :\n\n')))
        index_update=((result[0])[0])
        print(' ')
        new_name = (input('enter new name :\n\n'))
        new_family = (input('enter new family :\n\n'))
        new_num = int(input('enter new phone number :\n\n'))
        update_query = f'update contact set name = "{new_name}" , family = "{new_family}" , tel_number={new_num} where contact_id =={update_id} '
        cursor.execute(update_query)
        conn.commit()
        print('======================  your name is update to  ====================')
        search_query = f'select contact_id,name,family,tel_number from contact where contact_id =={update_id}'
        cursor.execute(search_query)
        result = cursor.fetchall()
        print('========================================================================')
        print(' id      |       name       |        family     |         number        ')
        print('========================================================================\n')
        for row in result:
            print(*row, sep='               ')
    else:
        print('                           the name not saved                           ')
        print('                            please try agin                             ')
    conn.close()
    print('========================================================================\n')

def delete_contact(action_code):
    print('========================================================================')
    conn = sqlite3.connect('contact_phone.db')
    cursor = conn.cursor()
    name_contact = (input('enter your name you want delete:\n\n'))
    search_query = f'select contact_id,name,family,tel_number from contact where name like "{name_contact}"'
    cursor.execute(search_query)
    result = cursor.fetchall()
    print('========================================================================')
    print(' id      |       name       |        family     |         number        ')
    print('========================================================================')
    for row in result:
        print(*row, sep='               ')
    print(' ')
    index_delete = (input('enter your id contact you want delete:\n\n'))
    delete_query = f'delete from contact where name =="{name_contact}" and contact_id == {index_delete}'
    cursor.execute(delete_query)
    conn.commit()
    conn.close()
    print('=======================  your name is delete  ==========================')
    print('========================================================================\n')

def show_all_contact(action_code):
    conn = sqlite3.connect('contact_phone.db')
    cursor = conn.cursor()
    show_all = f'select contact_id,name,family,tel_number from contact'
    cursor.execute(show_all)
    result = cursor.fetchall()
    print('====================   result show all contact  ========================')
    print('========================================================================')
    print(' id      |       name       |        family     |         number        ')
    print('========================================================================')
    for row in result:
        print(*row, sep='               ')
    conn.close()
    print('========================================================================\n')

while 1 == 1 :
    print('========================================================================')
    print('======================    list of operation     ========================')
    print('========================================================================')
    print('---------------------- number "1" for search   ------------------------')
    print('---------------------- number "2" for add      ------------------------')
    print('---------------------- number "3" for edit     ------------------------')
    print('---------------------- number "4" for delete   ------------------------')
    print('---------------------- number "5" for show all ------------------------')
    print('========================================================================')
    print('========================================================================')
    action_code = int(input('enter number for action : \n\n'))
    list_action=[1,2,3,4,5]
    if action_code not in list_action:
        print('------- your number you enter is invalid please try again  ----------')
        print('------------------     select between this list    ------------------')
    elif action_code == 1:
        search_contact(action_code)
    elif action_code == 2:
        add_contact(action_code)
    elif action_code == 3:
        update_contact(action_code)
    elif action_code == 4:
        delete_contact(action_code)
    elif action_code == 5:
        show_all_contact(action_code)

