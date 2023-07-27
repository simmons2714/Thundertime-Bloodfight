import stats

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
    stats.set_or_update_relationship('Durga', 0)
    print('chatted durga')

def chat_ekene(player_name):
    stats.set_or_update_relationship('Ekene', 0)
    print('chatted ekene')

def chat_keala(player_name):
    stats.set_or_update_relationship('Keala', 0)
    print('chatted keala')

def chat_ailbe(player_name):
    stats.set_or_update_relationship('Ailbe', 0)
    print('chatted ailbe')

def chat_yaxkin(player_name):
    stats.set_or_update_relationship('Yaxkin', 0)
    print('chatted yaxkin')

def chat_moran(player_name):
    stats.set_or_update_relationship('Moran', 0)
    print('chatted moran')

def chat_billie(player_name):
    stats.set_or_update_relationship('Billie', 0)
    print('chatted billie')

def chat_ilkay(player_name):
    stats.set_or_update_relationship('İlkay', 0)
    print('chatted İlkay')

def chat_sree(player_name):
    stats.set_or_update_relationship('Sree', 0)
    print('chatted sree')
