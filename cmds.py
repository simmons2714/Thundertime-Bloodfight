import stats
import json
import story
import nouns

from simple_term_menu import TerminalMenu
import questionary

def story_choice(story_list):
    while True:
        question = questionary.select(
            'What would you like to do?',
            choices = [
                f'{story_list[0]}',
                f'{story_list[1]}',
                f'{story_list[2]}',
                'Look around',
                'Check inventory',
                'Check player stats',
                'Quit'
            ]
        ).ask()
        if question == 'Look around':
            look()
            continue
        elif question == 'Check inventory':
            inv()
            continue
        elif question == 'Check player stats':
            get_stats()
            continue
        elif question == story_list[0]:
            stats.usr_choices('accept the tournament invite')
            story.story_path1_accept()
            break
        elif question == story_list[1]:
            stats.usr_choices('find a ship')
            story.story_path1_find()
            break
        elif question == story_list[2]:
            stats.usr_choices('join Kōnane')
            story.story_path1_join()
            break
        else:
            exit()
            


def find_path1_choice():
    choosing = True
    while choosing:
        usr_input = input("So I see you've decided to join Durga and find a ship. There are a few things you can do before you make your trip to the Outer Rim. You have the option to chat it up with the crew, attempt to study magic, or skip to the Outer Rim. What will you do? ")
        usr_input.lower()
        if usr_input in ('look', 'l', 'chat', 'study magic', 'study', 'skip', 'help', 'h', '1', '2', '3', 'inv', 'i', 'stats', 's'):
            choosing = False
            if usr_input == 'stats' or usr_input == 's':
                choosing = True
                get_stats()
            if usr_input == 'inv' or usr_input == 'i':
                choosing = True
                inv()
            if usr_input == 'look' or usr_input == 'l':
                choosing = True
                look()
            if usr_input == 'chat' or usr_input == '1':
                stats.usr_choices('chat up the crew')
                #story.story_path1_accept()
            if usr_input == 'study' or usr_input == '2' or usr_input == 'study magic':
                stats.usr_choices('study magic')
                #story.story_path1_find()
            if usr_input == 'skip' or usr_input == '3':
                stats.usr_choices('skip to Outer Rim')
                #story.story_path1_join()
            if usr_input == 'help' or usr_input == 'h':
                choosing = True
                print("l or look for a description of your soundings.\ni or inv for a description of the items in your inventory.\ns or stats for your current stats.\n1 for the first story choice.\n2 for the second story choice. \n3 for the third story choice.\nh or help to print this message again. ")
        else:
            print("Invalid choice. Try again. Valid options are: 'look', 'accept', 'find', 'join', 'help', '1', '2', '3', 'inv', 'stats'")




def get_stats():
    f = open('sav1.json')
    data = json.load(f)

    nest_dict = data.get('special')

    for k, v in nest_dict.items():
        print(f'{k}: {v}')

    f.close()

def inv():
    f = open('sav1.json')
    data = json.load(f)

    nest_dict = data.get('Inventory')
    
    print('This is what you have in your inventory.')
    for j in nest_dict:
        for k1 in j.keys():
            print(k1)

    options = []
    for i in nest_dict:
        for k, v in i.items():
            options.append(k)

    options.append('Close Inventory')
    
    while True:
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()
        if options[menu_entry_index] == 'Close Inventory':
            break
        else:
            print(nest_dict[menu_entry_index].get(options[menu_entry_index]))
            continue

    f.close()


def look():
    f = open('nouns.json')
    nouns_dict = json.load(f)

    options = []

    for i in nouns_dict.keys():
        options.append(i)

    options.append('Look around me')
    options.append('Stop Looking')
    
    while True:
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()
        if options[menu_entry_index] == 'Stop Looking':
            break
        elif options[menu_entry_index] == 'Look around me':
            for x in nouns_dict.keys():
                    print(x.capitalize())
            continue
        else:
            print(nouns_dict.get(options[menu_entry_index]))
            continue

    f.close()
