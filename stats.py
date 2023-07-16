import json

def save_stats(player_name, strength, perception, endurance, charisma, intelligence, agility, luck):
    stats_dict ={
        'player_name': player_name,
        'special' : {
            'Strength': strength,
            'Perception': perception,
            'Endurance': endurance,
            'Charisma': charisma,
            'Intelligence': intelligence,
            'Agility': agility,
            'Luck': luck
        }
    }

    # Serializing json
    json_object = json.dumps(stats_dict, indent=4)

    # Writing to sample.json
    with open("sav1.json", "w") as outfile:
        outfile.write(json_object)

def usr_choices(choice):
    filepath = 'sav1.json'
    with open(filepath, 'r') as fp:
        information = json.load(fp)

    information.setdefault('User Choices', []).append(choice)

    with open(filepath, 'w') as fp:
        json.dump(information, fp, indent=4)
