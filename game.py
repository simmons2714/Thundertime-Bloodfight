from art import *
from textwrap import wrap
import sys, time

#my modules
import stats
import inv
import cmds
import special
import story

#story.into_story()


player_name = input('What is your name? ')

strength, perception, endurance, charisma, intelligence, agility, luck = special.assign_stats()
stat_check = True

while stat_check:
    print(f'Strength: {strength}, Perception: {perception}, Endurance: {endurance}, Charisma: {charisma}, Intelligence: {intelligence}, Agility: {agility}, Luck: {luck}')
    usr_input = input("Are you okay with these stats? ")
    usr_input.lower()
    if usr_input in ('y', 'n', 'yes', 'no', 'ye'):
        if(usr_input == 'n' or usr_input == 'no'):
            strength, perception, endurance, charisma, intelligence, agility, luck = special.assign_stats()
        else:
            stat_check = False
            break
    else:
        print('Invalid choice. Try again.')

stats.save_stats(player_name,strength, perception, endurance, charisma, intelligence, agility, luck)
inv.add_to_inventory({'flyer': "You are cordially invited to participate in the most prestigious event of the galaxy!\nThe Cosmic Tournament\nUncover the Secrets of the Nexus Rift and Prove Your Magical Prowess\nLocation: Nexus Rift Arena, Astral Citadel\nDear <Person Name Here>,\nWe are pleased to extend an exclusive invitation to you on behalf of the renowned Magical Academy. You have been recognized as one of the most promising mages, and we believe that you have what it takes to compete in the Cosmic Tournament.\nPrepare to embark on an extraordinary journey, where magic and space converge in a spectacle unlike any other. The Nexus Rift, a mystical anomaly that intertwines realms, will serve as the battleground for this legendary event. It is within this enigmatic gateway that you will unlock the true extent of your magical abilities and uncover the untold secrets of the universe.\nThe Cosmic Tournament is a rare opportunity to showcase your skills, engage with fellow enchanters from across the galaxy, and forge lasting alliances. Engross yourself in thrilling challenges, navigate treacherous puzzles, and face formidable opponents on your path to victory.\nRemember, the fate of the galaxy hangs in the balance. Dark forces threaten to disrupt the harmonious coexistence of magic and technology. It is up to you, the chosen ones, to restore order and safeguard the Nexus Rift from impending doom.\nJoin us, and let your name be etched into the annals of history as a champion of the Cosmic Tournament!\nTo confirm your participation, kindly reply to this invitation at your earliest convenience. Upon acceptance, further instructions will be provided regarding travel arrangements and tournament regulations.\nMay your spells be powerful, your resolve unyielding, and your destiny entwined with the stars!\nYours magically,\nThe Starfire Corporation"})
cmds.first_choice()
