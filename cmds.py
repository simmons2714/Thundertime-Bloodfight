import stats
import json
import story
import nouns
import chat
import themes

from simple_term_menu import TerminalMenu

import questionary
from questionary import Style
from questionary import Separator
from questionary import Choice

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
            stats.usr_choices(story_list[0])
            return story_list[0].split(' ')[0]
            break
        elif question == story_list[1]:
            stats.usr_choices(story_list[1])
            return story_list[1].split(' ')[0]
            break
        elif question == story_list[2]:
            stats.usr_choices(story_list[2])
            return story_list[2].split(' ')[0]
            break
        else:
            return 'quit'
            break

def story_chat_choice(chat_list, player_name):
    chat_list.append('Stop chatting')
    chatting = True
    while chatting:
        question = questionary.select(
            'Who would you like to talk to?',
            choices = chat_list,
            style=themes.custom_style_pretty
        ).ask()

        if question in chat_list and question != 'Stop chatting':
            chat.chat_who(question, player_name)
            chat_list.insert(chat_list.index(question), Choice(question, disabled="You've already talked with this person."))
            chat_list.remove(question)

        elif question == 'Stop chatting':
            chatting = False
            break

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