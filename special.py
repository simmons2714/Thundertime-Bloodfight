def assign_stats():
    special_stat_loop = True
    inital_stats = 40
    usr_int = 0
    strength = 0
    perception = 0
    endurance = 0
    charisma = 0
    intelligence = 0
    agility = 0
    luck = 0
    while special_stat_loop:
        if inital_stats <= 0:
            strength += 0
            special_stat_loop = False
            break
        else:
            while strength < 11:
                usr_int = int(input("Strength: "))
                if usr_int < 0 or usr_int > 10:
                    print('Please enter a value between -1 and 11')
                    continue
                else:
                    if usr_int > inital_stats and inital_stats == 0:
                        print('Out of stat points allocating the rest as zero.')
                        strength += 0
                        break
                    elif usr_int > inital_stats and inital_stats > 0:
                        print(f'Stat points left: {inital_stats}. Please enter a value between zero and {inital_stats}.')
                        continue
                    else:
                        strength += usr_int
                        inital_stats -= usr_int
                        break

        if inital_stats <= 0:
            perception += 0
            special_stat_loop = False
            break
        else:
            while perception < 11:
                usr_int = int(input("Perception: "))
                if usr_int < 0 or usr_int > 10:
                    print('Please enter a value between -1 and 11')
                    continue
                else:
                    if usr_int > inital_stats and inital_stats == 0:
                        print('Out of stat points allocating the rest as zero.')
                        perception += 0
                        break
                    elif usr_int > inital_stats and inital_stats > 0:
                        print(f'Stat points left: {inital_stats}. Please enter a value between zero and {inital_stats}.')
                        continue
                    else:
                        perception += usr_int
                        inital_stats -= usr_int
                        break

        if inital_stats <= 0:
            endurance += 0
            special_stat_loop = False
            break
        else:
            while endurance < 11:
                usr_int = int(input("Endurance: "))
                if usr_int < 0 or usr_int > 10:
                    print('Please enter a value between -1 and 11')
                    continue
                else:
                    if usr_int > inital_stats and inital_stats == 0:
                        print('Out of stat points allocating the rest as zero.')
                        perception += 0
                        break
                    elif usr_int > inital_stats and inital_stats > 0:
                        print(f'Stat points left: {inital_stats}. Please enter a value between zero and {inital_stats}.')
                        continue
                    else:
                        endurance += usr_int
                        inital_stats -= usr_int
                        break

        if inital_stats <= 0:
            charisma += 0
            special_stat_loop = False
            break
        else:
            while charisma < 11:
                usr_int = int(input("Charisma: "))
                if usr_int < 0 or usr_int > 10:
                    print('Please enter a value between -1 and 11')
                    continue
                else:
                    if usr_int > inital_stats and inital_stats == 0:
                        print('Out of stat points allocating the rest as zero.')
                        charisma += 0
                        break
                    elif usr_int > inital_stats and inital_stats > 0:
                        print(f'Stat points left: {inital_stats}. Please enter a value between zero and {inital_stats}.')
                        continue
                    else:
                        charisma += usr_int
                        inital_stats -= usr_int
                        break

        if inital_stats <= 0:
            intelligence += 0
            special_stat_loop = False
            break
        else:
            while intelligence < 11:
                usr_int = int(input("Intelligence: "))
                if usr_int < 0 or usr_int > 10:
                    print('Please enter a value between -1 and 11')
                    continue
                else:
                    if usr_int > inital_stats and inital_stats == 0:
                        print('Out of stat points allocating the rest as zero.')
                        intelligence += 0
                        break
                    elif usr_int > inital_stats and inital_stats > 0:
                        print(f'Stat points left: {inital_stats}. Please enter a value between zero and {inital_stats}.')
                        continue
                    else:
                        intelligence += usr_int
                        inital_stats -= usr_int
                        break

        if inital_stats <= 0:
            agility += 0
            special_stat_loop = False
            break
        else:
            while agility < 11:
                usr_int = int(input("Agility: "))
                if usr_int < 0 or usr_int > 10:
                    print('Please enter a value between -1 and 11')
                    continue
                else:
                    if usr_int > inital_stats and inital_stats == 0:
                        print('Out of stat points allocating the rest as zero.')
                        agility += 0
                        break
                    elif usr_int > inital_stats and inital_stats > 0:
                        print(f'Stat points left: {inital_stats}. Please enter a value between zero and {inital_stats}.')
                        continue
                    else:
                        agility += usr_int
                        inital_stats -= usr_int
                        break

        if inital_stats <= 0:
            luck += 0
            special_stat_loop = False
            break
        else:
            while luck < 11:
                usr_int = int(input("Luck: "))
                if usr_int < 0 or usr_int > 10:
                    print('Please enter a value between -1 and 11')
                    continue
                else:
                    if usr_int > inital_stats and inital_stats == 0:
                        print('Out of stat points allocating the rest as zero.')
                        luck += 0
                        break
                    elif usr_int > inital_stats and inital_stats > 0:
                        print(f'Stat points left: {inital_stats}. Please enter a value between zero and {inital_stats}.')
                        continue
                    else:
                        luck += usr_int
                        inital_stats -= usr_int
                        break
        if inital_stats > 0:
            print(f'You have unspent stat points. {inital_stats}')
            usr_int = 0
            continue
        else:
            special_stat_loop = False
    return strength, perception, endurance, charisma, intelligence, agility, luck
