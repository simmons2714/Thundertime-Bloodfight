import stats,story

def chat_who(list_item, player_name):
    function_dict = {
        'durga': chat_durga, 
        'ekene': chat_ekene,
        'keala': chat_keala,
        'ailbe': chat_ailbe,
        'yaxkin': chat_yaxkin,
        'moran': chat_moran,
        'billie': chat_billie,
        'ilkay': chat_ilkay,
        'sree': chat_sree
        }
    func = list_item.lower()
    return function_dict[func](player_name)

def chat_durga(player_name):
    stats.update_relationship('Durga', 0)
    story.borderprint("As the player approaches Durga, the captain of the mining ship, they find her meticulously overseeing the ship's operations. Her stern expression softens as she notices the player's presence. With a nod, she gestures for them to speak.")
    
    story.delay_print(f'{player_name}: Approaches Durga with a respectful nod Captain Durga, mind if I have a moment?')

    chatting = True
    while chatting:
        question = questionary.select(
            'Durga: Glances up from her work, her expression stoic "Make it quick. We\'ve got a lot to do."',
            choices = [
                'Ask about her past adventures',
                'Express admiration for her leadership',
                'Share a personal story of determination',
                'Discuss the challenges ahead',
                'Stop talking'
            ]
        ).ask()

        if question == 'Ask about her past adventures':
            stats.update_relationship('Durga', 1)
            story.delay_print(f'{player_name}: I\'ve heard tales of your past adventures, Captain. The daring missions, the close calls. Care to share any of those experiences?')
            story.delay_print('Durga: Pauses, a flicker of nostalgia in her eyes You want to hear about the old days, huh? Well, I suppose I\'ve had my fair share of challenges out there in the black. It\'s a harsh universe, but it\'s also full of wonder. What do you want to know?')
        elif question == 'Express admiration for her leadership':
            stats.update_relationship('Durga', -1)
            story.delay_print(f'{player_name}: I must say, Captain, your leadership skills are impressive. The way you command respect from the crew and guide us through the dangers of space is remarkable.')
            story.delay_print('Durga: Arches an eyebrow, looking unimpressed Save the flattery. I\'m not interested in empty words. I need a crew that can back up their talk with action.')
            chatting = False
            break
        elif question == 'Share a personal story of determination':
            stats.update_relationship('Durga', 0)
            story.delay_print(f'{player_name}: You know, I haven\'t always had an easy path. There were times when I thought I might give up, but I kept pushing forward. Determination is what brought me here, standing before you now.')
            story.delay_print('Durga: \x1B[3mNods, her expression softening slightly\x1B[0m I respect determination. It\'s a quality that can get you far in this line of work. Keep that fire burning, and you might just prove yourself."')
        elif quesiton == ' Discuss the challenges ahead':
            stats.update_relationship('Durga', 2)
            story.delay_print(f'{player_name}: I\'ve been thinking about the challenges we might face in the Nexus Rift. It\'s uncharted territory, and we\'ll need to be prepared for anything.')
            story.delay_print('Durga: \x1B[3mListens intently\x1B[0m You\'re right. The Nexus Rift is uncharted and unpredictable. But that\'s why we\'re here - to explore and adapt. Just remember, talk is cheap. I\'m more interested in seeing how you handle yourself when the going gets tough.')
        elif question == 'Stop talking':
            chatting = False
        else:
            continue

def chat_ekene(player_name):
    stats.update_relationship('Ekene', 0)
    story.borderprint('As the player approaches Ekene, the Navigator of the ship, they find them studying star charts and celestial navigation. With a warm smile, Ekene welcomes the player.')
    
    chatting = True
    while chatting:
        question = questionary.select(
            'Ekene: Ah, greetings! You must be the new crew member. I\'m Ekene, the Navigator. What brings you here?',
            choices = [
                'Ask about their mysterious past',
                'Discuss their thoughts on space exploration',
                'Share a personal fascination with the cosmos',
                'Seek advice on navigating through dangerous space',
                'Stop talking'
            ]
        ).ask()

def chat_keala(player_name):
    stats.update_relationship('Keala', 0)
    print('chatted keala')

def chat_ailbe(player_name):
    stats.update_relationship('Ailbe', 0)
    print('chatted ailbe')

def chat_yaxkin(player_name):
    stats.update_relationship('Yaxkin', 0)
    print('chatted yaxkin')

def chat_moran(player_name):
    stats.update_relationship('Moran', 0)
    print('chatted moran')

def chat_billie(player_name):
    stats.update_relationship('Billie', 0)
    print('chatted billie')

def chat_ilkay(player_name):
    stats.update_relationship('İlkay', 0)
    print('chatted İlkay')

def chat_sree(player_name):
    stats.update_relationship('Sree', 0)
    print('chatted sree')