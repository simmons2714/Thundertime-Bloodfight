import json

def add_to_inventory(adding_item):
    filepath = 'sav1.json'
    with open(filepath, 'r') as fp:
        information = json.load(fp)

    
    #information.update({'Inventory': test_list})
    #information.update({'Inventory': []})
    information.setdefault('Inventory', []).append(adding_item)

    with open(filepath, 'w') as fp:
        json.dump(information, fp, indent=4)