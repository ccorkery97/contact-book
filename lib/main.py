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

db.drop_tables(models)
db.create_tables(models)

conor = Contact(first_name = 'Conor', number = '123-456-7890')
conor.save()



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
            show_contact_info(choice_c)


def show_contact_info(contact_choice):
    leave = ''
    while leave != 'back':
        print(f"-----{contact_choice}-----")
        for contact in Contact.select():
                if contact_choice == contact.first_name:
                    print(contact.number)
                    print(contact.email)
                    print(contact.address)
                    print("--------------------")
        choice_i = input()
        if choice_i == 'back':
            leave = 'back'



main_menu()