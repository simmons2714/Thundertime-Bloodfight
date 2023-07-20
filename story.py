from art import *
from textwrap import wrap
import sys, time
import questionary

import nouns
import cmds

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.01)

def borderprint(sentence):
    width = 100
    print('+-' + '-' * width + '-+')
    for line in wrap(sentence, width):
        print('| {0:^{1}} |'.format(line, width))
    print('+-' + '-'*(width) + '-+')

def into_story():
    print(f"\033[1mYou are cordially invited to participate in the most prestigious event of the galaxy!\033[0m")
    tprint("The Cosmic Tournament")
    print("Uncover the Secrets of the Nexus Rift and Prove Your Magical Prowess")
    print('Location: Nexus Rift Arena, Astral Citadel')
    print("Dear <Person Name Here>,")

    tourn_sentence1 = "We are pleased to extend an exclusive invitation to you on behalf of the renowned Magical Academy. You have been recognized as one of the most promising mages, and we believe that you have what it takes to compete in the Cosmic Tournament.\n"
    tourn_sentence2 = 'Prepare to embark on an extraordinary journey, where magic and space converge in a spectacle unlike any other. The Nexus Rift, a mystical anomaly that intertwines realms, will serve as the battleground for this legendary event. It is within this enigmatic gateway that you will unlock the true extent of your magical abilities and uncover the untold secrets of the universe.\n'
    tourn_sentence3 = 'The Cosmic Tournament is a rare opportunity to showcase your skills, engage with fellow enchanters from across the galaxy, and forge lasting alliances. Engross yourself in thrilling challenges, navigate treacherous puzzles, and face formidable opponents on your path to victory.\n'
    tourn_sentence4 = 'Remember, the fate of the galaxy hangs in the balance. Dark forces threaten to disrupt the harmonious coexistence of magic and technology. It is up to you, the chosen ones, to restore order and safeguard the Nexus Rift from impending doom.\n'
    tourn_sentence5 = 'Join us, and let your name be etched into the annals of history as a champion of the Cosmic Tournament!\n'
    tourn_sentence6 = 'To confirm your participation, kindly reply to this invitation at your earliest convenience. Upon acceptance, further instructions will be provided regarding travel arrangements and tournament regulations.\n'
    tourn_sentence7 = 'May your spells be powerful, your resolve unyielding, and your destiny entwined with the stars!\n'

    borderprint(tourn_sentence1)

    read = questionary.confirm("Continue reading?").ask()

    if read:
        borderprint(tourn_sentence2)
        borderprint(tourn_sentence3)
        borderprint(tourn_sentence4)
        borderprint(tourn_sentence5)
        borderprint(tourn_sentence6)
        borderprint(tourn_sentence7)
        print('Yours magically,')
        tprint("The Starfire Corporation")

    nouns.create_noun('konane', "Kōnane was born into a world plagued by a cyberpunk dystopia, where the power dynamics were firmly controlled by a few influential corporations. In this oppressive society, access to space travel was restricted, limited only to these corporations and daring pirates who had managed to steal ships. Growing up in the depths of this dystopia, Kōnane witnessed the exploitation and suppression of those who possessed natural access to magic. The corporations recognized the potential of magic as a valuable resource, and those born with innate magical abilities were seen as valuable commodities to be exploited for profit. Despite the oppressive regime, Kōnane's thirst for knowledge and rebellion against the status quo led them on a path of discovery. Through secretive encounters with underground factions and their own relentless pursuit of knowledge, Kōnane uncovered the existence of the Nexus Rift—a phenomenon that could potentially unlock the full extent of magical abilities. Recognizing the potential of the Nexus Rift as a source of liberation, Kōnane devoted themselves to uncovering its secrets and harnessing its power. They became a skilled mage, acquiring mastery over various magical disciplines and developing a deep understanding of the balance between magic and technology. In their travels, Kōnane encountered individuals from all walks of life, witnessing firsthand the suffering caused by the exploitation of magic and the limitations imposed on space travel. The knowledge to learn magic had been deliberately kept hidden from the public to maintain control and prevent uprisings against the oppressive regime. Realizing the need for change, Kōnane became an advocate for empowering individuals to harness their magical abilities. They believed that by uncovering the secrets of the Nexus Rift and granting access to magic for all, a revolution against the corporate tyranny could be sparked. When Kōnane encounters the player, they see potential and an opportunity for change. While understanding the risks and dangers involved, Kōnane guides the player on their journey through the Nexus Rift, empowering them to explore the universe and discover the magic hidden within. They become a mentor and ally, imparting their knowledge and assisting the player in their quest to challenge the oppressive forces that seek to exploit magical abilities.")

    print(f"Kōnane: ",end='')
    delay_print("Hold up, pal! I noticed you didn't respond to that tournament flyer. What's the deal?\n")
    delay_print("Player: Yeah, I saw it, but I'm not interested in some fancy tournament. I've got my own plans.\n")
    delay_print("Kōnane: I understand your skepticism, but you've got to look beyond the surface. The tournament is more than just a showcase of power. It's an opportunity to challenge the status quo and uncover the truth they want to keep hidden.\n")
    delay_print("Player: What truth? I thought the tournament was just a way to find naturally gifted mages to exploit them.\n")
    delay_print("Kōnane: You're not entirely wrong. The tournament and the academy were indeed designed to discover gifted individuals, but we can turn that to our advantage. The powers that be want to exploit magic for their own gain, but we can learn to wield it for our liberation.\n")
    delay_print("Player: How?\n")
    delay_print("Kōnane: By embracing the magic within you. The universe is vast, and beyond their reach lies the chance to learn magic on your own terms. We can break free from their control, but it won't be easy. It starts with the tournament. It's a stepping stone to something greater.\n")
    delay_print("Player: I never considered it that way. Maybe I should give it a second thought.\n")
    delay_print("Kōnane: I'm glad to hear that. The tournament can be a gateway to discovering your true potential and finding allies who share our vision. If you decide to participate, seek me out. I can provide guidance and help you navigate the challenges ahead. Together, we can uncover the hidden truths and reshape our world.\n")

    print()
    borderprint("Accept the Tournament Invitation: This choice sets you on a path to explore your magical abilities, uncover the secrets of the Nexus Rift, and challenge the exploitation of magic by corporations.")
    borderprint("Find a Ship: You choose to focus on acquiring a ship to explore the hidden realms beyond the control of the corporations. This choice sets you on a quest to find a vessel, gather resources, and establish a foothold in the universe, allowing you to learn magic on your own terms.")
    borderprint("Join Kōnane's Underground Movement: You decide to align yourself with Kōnane and their underground movement aimed at liberating magic from the corporations' grasp. This choice involves working closely with Kōnane, carrying out missions, and gathering allies to challenge the oppressive regime and expose the truth behind the exploitation of magic.")
    #print("Accept the Tournament Invitation: This choice sets you on a path to explore your magical abilities, uncover the secrets of the Nexus Rift, and challenge the exploitation of magic by corporations.")
    #print("Seek Out a Ship: You choose to focus on acquiring a ship to explore the hidden realms beyond the control of the corporations. This choice sets you on a quest to find a vessel, gather resources, and establish a foothold in the universe, allowing you to learn magic on your own terms.")
    #print("Join Kōnane's Underground Movement: You decide to align yourself with Kōnane and their underground movement aimed at liberating magic from the corporations' grasp. This choice involves working closely with Kōnane, carrying out missions, and gathering allies to challenge the oppressive regime and expose the truth behind the exploitation of magic.")
    print()

    story_choices_list = ['Accept the invite', 'Find a ship', 'Join Kōnane']
    return story_choices_list


def story_path1_find():
    nouns.add_noun('durga', "Durga, renowned as a fearless captain in the unforgiving reaches of space, has a reputation for leading a tight-knit crew aboard her mining ship. Born and raised in the cyberpunk dystopia, Durga witnessed firsthand the corrupt grip of the corporations and the exploitation of magic by the Starfire Corporation. Durga's journey into the mining trade began as a means to escape the suffocating control of the corporations. In the depths of the asteroid fields, she found freedom and a way to carve her own path. Over time, she honed her skills as a resourceful captain, navigating treacherous celestial terrain, and building a crew that shared her vision of independence. Despite her reservations about naturally gifted mages, Durga recognized the potential value of magic in the uncharted realms. However, she had witnessed firsthand the consequences that befell those who drew too much attention. To protect her crew and maintain their freedom, she adopted a strict policy of secrecy, avoiding confrontations with the Starfire Corporation at all costs. Through her resourcefulness and cunning, Durga has managed to maintain a low profile, evading the radar of the powerful corporations. Her ship became a haven for those seeking refuge from the oppressive regime, and she developed a reputation for being fair but unyielding in her determination to protect her crew. Durga's crew respects her leadership, valuing her strong intuition, unwavering principles, and commitment to their safety. They have become a family, bound together by shared goals and a desire for liberation from corporate control. While cautious when it comes to mages, Durga recognizes that the player's desire to explore the hidden realms aligns with her own yearning for freedom. Through the player's actions, they have the chance to prove themselves and earn a place among Durga's trusted crew. As the player's journey unfolds, Durga's steadfastness and resilience will be tested, forcing her to confront her deepest fears and make difficult decisions. Together with the player, she will navigate the challenges of the universe and strive to protect her crew's independence while uncovering the truth behind the exploitation of magic.")
    nouns.remove_noun('konane')

    delay_print("Player: Excuse me, are you Durga? I've heard you're the captain of a mining ship around here.\n")
    delay_print("Durga: Aye, that's me. What's your business with me?\n")
    delay_print("Player: I'm on a quest to explore the hidden realms of the universe, beyond the control of the corporations. I'm seeking a ship to get there. I was wondering if there's any possibility of joining your mining operation and earning my way aboard your vessel.\n")
    delay_print("Durga: Hold on there, friend. I've heard stories about mages like you. Naturally gifted, causing all sorts of trouble, and attracting the unwanted attention of the Starfire Corporation. I can't afford to have my crew and operations in their spotlight.\n")
    delay_print("Player: I understand your concerns, but I assure you I'm not seeking the limelight or trying to draw attention. I have my own reasons for wanting to explore the hidden realms, away from the corporations' grip. I can offer my magical abilities discreetly, for the benefit of the crew and the success of the mission.\n")
    delay_print("Durga: That's a bold claim. The last thing I need is trouble. If I let you on board, it's with the understanding that you keep a low profile, no flashy displays of magic. And if any heat comes our way, you're gone. Understood?\n")
    delay_print("Player: Absolutely, Durga. I appreciate your caution, and I won't jeopardize your crew or your operation. I seek only to contribute and earn my place, using my magic responsibly and discreetly.\n")
    delay_print("Durga: We'll see about that. We've got a dangerous mining operation in the Outer Rim coming up. If you can prove your worth and keep your magic in check, maybe I'll consider letting you join us. But one wrong move, and you're out. Agreed?\n")
    delay_print("Player: Agreed, Durga. I won't let you down. Just give me the chance to show you what I can do.\n")

    cmds.find_path1_choice()

def story_path1_accept():
    return 0

def story_path1_join():
    return 0
