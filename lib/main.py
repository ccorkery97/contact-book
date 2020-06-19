from peewee import *


db = PostgresqlDatabase('contacts', user='postgres', password='', host='localhost', port=5432)

db.connect()

class BaseModel(Model):
    class Meta:
        database = db

class Contact(BaseModel):
    first_name = CharField()
    last_name = CharField(default=" ")
    number = CharField()
    email = CharField(default=" ")
    address = CharField(default=" ")

models = [Contact]

db.create_tables(models)

#conor = Contact(first_name = 'Conor', number = '123-456-7890')
#conor.save()
#
#bud = Contact(first_name = 'Bud', number = '453-210-2342', email = 'bud@bud.com', address = '1111 bud lane, budtown FL')
#bud.save()



def main_menu():
    leave = ''
    while leave != 'Exit':
        print('------ Main Menu ------')
        print('Contact List')
        print('Add Contact')
        print('Exit')
        print('-----------------------')
        choice = input()
        if choice == 'Contact List':
            show_contact_list()
        elif choice == 'Exit':
            leave = 'Exit'
        elif choice == 'Add Contact':
            add_contact()


def show_contact_list():
    back = ''
    while back != 'menu':
        print('----- Contact List -----')
        for contact in Contact.select():
            print(contact.first_name)
        print('------------------------')
        choice_c = input('You can go back to menu or type one of the names to see more: ')
        if choice_c == 'menu':
            back = 'menu'
        else:
            back = show_contact_info(choice_c)


def show_contact_info(contact_choice):
    leave = ''
    while leave != 'back':
        print(f"-----{contact_choice}-----")
        for contact in Contact.select().where(Contact.first_name == contact_choice):
                print(contact.number)
                print(contact.email)
                print(contact.address)
                print("--------------------")
        choice_i = input()
        if choice_i == 'back':
            leave = 'back'
        elif choice_i == 'menu':
            leave = 'back'
            return 'menu'
        elif choice_i == 'update':
            update_contact(contact_choice)


def add_contact():
    leave = ''
    while leave != 'menu':
        new_contact_first_name = input('First name: ')
        new_contact_last_name = input('Last name: ')
        new_contact_number = input('number: ')
        new_contact_email = input('email: ')
        new_contact_address = input('address: ')
        new_contact = Contact(first_name = new_contact_first_name, number = new_contact_number, last_name = new_contact_last_name, email = new_contact_email, address = new_contact_address)
        new_contact.save()
        leave = show_contact_info(new_contact_first_name)
        

def update_contact(contact_name):
    update_field = input("What do you want to update? ")
    update_value = input(f"new {update_field}: ")
    for contact in Contact.select().where(Contact.first_name == contact_name):
        if update_field == 'first name':
            contact.first_name = update_value
            contact.save()
        if update_field == 'last name':
            contact.last_name = update_value
            contact.save()
        if update_field == 'number':
            contact.number = update_value
            contact.save()
        if update_field == 'email':
            contact.email = update_value
            contact.save()
        if update_field == 'address':
            contact.address = update_value
            contact.save()







main_menu()

