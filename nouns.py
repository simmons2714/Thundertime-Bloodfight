import json

def create_noun(thing_name, thing_desc):
    things_dict = {
        thing_name : thing_desc
    }

    # Serializing json
    json_object = json.dumps(things_dict, indent=4)

    # Writing to sample.json
    with open("nouns.json", "w") as outfile:
        outfile.write(json_object)

def add_noun(thing_name, thing_desc):
    filepath = 'nouns.json'
    with open(filepath, 'r') as fp:
        information = json.load(fp)

    information.update({thing_name:thing_desc})

    with open(filepath, 'w') as fp:
        json.dump(information, fp, indent=4)

def remove_noun(thing_name):
    filepath = 'nouns.json'
    with open(filepath, 'r') as fp:
        information = json.load(fp)

    information.pop(thing_name)

    with open(filepath, 'w') as fp:
        json.dump(information, fp, indent=4)