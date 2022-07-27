class Monster:
    def __init__(self, name, hp = 20):
        self.exp = 0
        self.name = name
        self.type = 'Normal'
        self.max_hp = hp
        self.current_hp = self.max_hp
        self.attacks = {'wait': 0}
        self.possible_attacks = {'sneak_attack': 1, 'slash': 2, 'ice_storm': 3, 'fire_storm': 3, 'whirlwind': 3, 'earthquake': 2, 'double_hit': 4, 'tornado': 4, 'wait': 0}

    def win_fight(self):
        self.exp = self.exp + 5
        self.current_hp = self.max_hp

    def lose_fight(self):
        self.exp = self.exp + 1
        self.current_hp = self.max_hp

def monster_fight(monster1, monster2):

    atk_dict1 = monster1.attacks
    atk_dict2 = monster2.attacks

    #sort
    atk_list1 = list(monster1.attacks.keys())
    atk_list2 = list(monster2.attacks.keys())
    list_key = ['double_hit', 'tornado', 'fire_storm', 'ice_storm', 'whirlwind', 'earthquake', 'slash', 'sneak_attack', 'wait']
    sorted_atk1 = []
    sorted_atk2 = []

    for attack in list_key:
        if attack in atk_list1:
            sorted_atk1.append(attack)

    for attack in list_key:
        if attack in atk_list2:
            sorted_atk2.append(attack)
    
    #battle

    rnd1 = 0
    rnd2 = 0
    x = 0
    moves1 = []
    moves2 = []

    while monster1.current_hp > 0 and monster2.current_hp > 0:

        monster2.current_hp = monster2.current_hp - atk_dict1[sorted_atk1[x]]
        rnd1 = rnd1 + 1
        moves1.append(attack)

        if monster1.current_hp <= 0:

            monster2.win_fight()
            monster1.lose_fight()
            return (rnd2), monster2.name, moves2
            
        elif monster2.current_hp <= 0:

            monster1.win_fight()
            monster2.lose_fight()
            return (rnd1), monster1.name, moves1

        monster1.current_hp = monster1.current_hp - atk_dict2[sorted_atk2[x]]
        rnd2 = rnd2 + 1
        moves2.append(attack)

        if monster1.current_hp <= 0:

            monster2.win_fight()
            monster1.lose_fight()
            return (rnd2), monster2.name, moves2
                    
        elif monster2.current_hp <= 0:

            monster1.win_fight()
            monster2.lose_fight()
            return (rnd1), monster1.name, moves1

        if x < 3:
            x = x + 1
        
        elif x == 3:
            x = 0

    if monster1.attacks == {'wait': 0} and monster2.attacks == {'wait': 0}:
        return -1, None, None

#####

monster1 = Monster('One')
monster2 = Monster('Two')

monster1.attacks = {'fire_storm': 3, 'double_hit': 4, 'earthquake': 2, 'ice_storm': 3}
monster2.attacks = {'sneak_attack': 1, 'slash': 2, 'whirlwind': 3, 'double_hit': 4}

list1 = list(monster1.attacks.keys())

list2 = list(monster2.attacks.keys())

print(monster_fight(monster1, monster2))