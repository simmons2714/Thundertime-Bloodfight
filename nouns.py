import json

def add_noun(thing_name, thing_desc):
    things_dict = {
        thing_name : thing_desc
    }

    # Serializing json
    json_object = json.dumps(things_dict, indent=4)

    # Writing to sample.json
    with open("nouns.json", "w") as outfile:
        outfile.write(json_object)