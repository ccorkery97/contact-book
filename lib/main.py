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
            for contact in Contact.select():
                if choice_c == contact.first_name:
                    print(contact.first_name)
                    print(contact.number)





main_menu()