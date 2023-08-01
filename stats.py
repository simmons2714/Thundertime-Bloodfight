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

def update_relationship(noun_name, value):
    filepath = 'sav1.json'
    with open(filepath, 'r') as fp:
        information = json.load(fp)

    # Check if "Relationships" key exists in the JSON data
    relationships = information.get('Relationships', {})

    # Get the current value for the NPC, or set it to 0 if it doesn't exist yet
    current_value = relationships.get(noun_name, 0)

    # Update the NPC's value in the "Relationships" dict
    new_value = current_value + value
    relationships[noun_name] = new_value

    # Update the "Relationships" key in the main JSON data
    information['Relationships'] = relationships

    with open(filepath, 'w') as fp:
        json.dump(information, fp, indent=4)
