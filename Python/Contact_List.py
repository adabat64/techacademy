people_dict = {'tom' : ['tom@tom&jerry.com', 503739739], 'jerry' : ['jerry@tom&jerry.com', 503739739]}
print people_dict


def main_menu():
    questions = True
    while questions == True:
        answer = raw_input('Main Menu: Press "S" to search for a name in your Contact List, press "A" to add a new name to your Contact List: ').lower()
        if answer == 's':
            questions = False
            name_search()

        elif answer == 'a':
            questions = True
            new_name = raw_input('Add a new name: ')
            new_email = raw_input('Add an email for ' +new_name+ ': ')
            new_phone = raw_input('Add a phone number for ' +new_name+ ': ')
            people_dict[new_name]=new_email, new_phone

            print new_name + ' was added to your contacts list. Here is your updated Contacts List: '
            for names in sorted(people_dict.iterkeys()):
                print "%s: %s" % (names, people_dict[names])

        else:
            print ("I didn't quite catch that.")
            questions = True


def name_search():
    search_again = True
    while search_again == True :

        name = raw_input('Who are you looking for? ').lower()
        search_people(name)

        search_question = raw_input('Do you want to search for another name? y/n ')

        if search_question == 'y' :
            search_again = True

        elif search_question == 'n':

            search_again = False
            main_menu()

        else:
            print ("I didn't quite catch that.")
            search_again = False
            main_menu()

def search_people(name):
    try :
        people_name = people_dict[name]
        print 'Name: ' +name.capitalize()
        print 'email: ' +people_name[0]
        print 'Phone Number: ' +people_name[1]
    except :
        print 'That name does not exist. '



main_menu()
