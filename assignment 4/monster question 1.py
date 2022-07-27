class Monster:
    def __init__(self, name, hp = 20):
        self.exp = 0
        self.name = name
        self.type = 'Normal'
        self.max_hp = hp
        self.current_hp = self.max_hp
        self.attacks = {'wait': 0}
        self.possible_attacks = {'sneak_attack': 1, 'slash': 2, 'ice_storm': 3, 'fire_storm': 3, 'whirlwind': 3, 'earthquake': 2, 'double_hit': 4, 'tornado': 4, 'wait': 0}

    def add_attack(self, attack_name):

        if attack_name not in self.possible_attacks:
            return False
        
        elif attack_name in self.possible_attacks:

            if attack_name not in self.attacks:

                if len(self.attacks) < 4:
                    self.attacks[attack_name] = self.possible_attacks[attack_name]
                    return True
                
                elif len(self.attacks) == 4:
                    if 'wait' in self.attacks:
                        del self.attacks['wait']

                    elif 'wait' not in self.attacks:
                        min_val = min(self.attacks.values())
                        #value (points) of current weakest attack already in dict 
                        weakest_atk = 0
                
                        for attack in self.attacks:

                            if self.attacks.get(attack, 00) == min_val:
                            #if this key has the value of the min_val:

                                if weakest_atk != 0:
                                #if there is already a weakest attack:

                                    if attack < weakest_atk:
                                    #if current attack is less than weakest_atk alphabetically, weakest_atk is updated
                                        weakest_atk = attack

                                    elif weakest_atk < attack:
                                        pass

                                elif weakest_atk == 0:
                                #if there is no weakest attack, set weakest attack
                                    weakest_atk = attack
                        
                            elif self.attacks.get(attack, 00) != min_val:
                                pass
                    
                        del self.attacks[weakest_atk]
                        
                    self.attacks[attack_name] = self.possible_attacks[attack_name]
                    return True
                
            elif attack in self.attacks:
                return False

    def remove_attack(self, attack_name):
        if attack_name not in self.possible_attacks:
        #is this a valid attack?
            return False
        
        elif attack_name not in self.attacks:
        #is this a learned attack?
            return False

        elif attack_name in self.attacks:
            del self.attacks[attack_name]
        
            if len(self.attacks) == 0:
                self.attacks['wait'] = self.possible_attacks['wait']
            
            return True