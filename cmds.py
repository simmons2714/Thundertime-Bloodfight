import stats
import json
import story

def first_choice():
    choosing = True
    while choosing:
        usr_input = input('What would you like to do? ')
        usr_input.lower()
        if usr_input in ('look', 'l', 'accept', 'find', 'join', 'help', 'h', '1', '2', '3', 'inv', 'i', 'stats', 's'):
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
            if usr_input == 'accept' or usr_input == '1':
                stats.usr_choices('accept the tournament invite')
                story.story_path1_accept()
                
            if usr_input == 'find' or usr_input == '2':
                stats.usr_choices('find a ship')
                story.story_path1_find()
            if usr_input == 'join' or usr_input == '3':
                stats.usr_choices('join Kōnane')
                story.story_path1_join()
            if usr_input == 'help' or usr_input == 'h':
                choosing = True
                print("l or look for a description of your soundings.\ni or inv for a description of the items in your inventory.\ns or stats for your current stats.\n1 for the first story choice.\n2 for the second story choice. \n3 for the third story choice.\nh or help to print this message again. ")
        else:
            print("Invalid choice. Try again. Valid options are: 'look', 'accept', 'find', 'join', 'help', '1', '2', '3', 'inv', 'stats'")

def find_path1_choice():
    choosing = True
    while choosing:
        usr_input = input("So I see you've decided to join Durga and find a ship. There are a few things you can do before you make your trip to the Outer Rim. You have the option to chat it up with the crew, attempt to study magic, or skip to the Outer Rim. What will you do? ")
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
    
    for j in nest_dict:
        for k1 in j.keys():
            print(k1)

    inv_desc = True
    while inv_desc:
        count = 0
        item_not_found = 0
        usr_input = input('Which item would you like to know about? ')
        usr_input.lower()
        for i in nest_dict:
            for k, v in i.items():
                count += 1
                if k == usr_input:
                    item_found = v
                else:
                    item_not_found += 1

        if item_not_found == count:
            print('Item not in inventory')
        else:
            print(item_found)

        still_looking = True
        while still_looking:
            usr_quit = input('Keep looking? ')
            usr_quit.lower()
            if usr_quit in ('no', 'n', 'quit', 'q', 'yes', 'y'):
                if usr_quit == 'n' or usr_quit == 'no' or usr_quit == 'q' or usr_quit == 'quit': 
                    inv_desc = False
                    still_looking = False
                else:
                    still_looking = False
                    continue
            else:
                print('invalid input')
        
    f.close()

def look():
    return 0