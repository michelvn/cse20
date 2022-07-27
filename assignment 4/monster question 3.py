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
       pass #your code here
   def remove_attack(self, attack_name):
       pass #your code here
   def win_fight(self):
       pass #your code here
   def lose_fight(self):
       pass #your code here
 
def monster_fight(monster1, monster2):
   pass #your code here
 
class Ghost(Monster):
   def win_fight(self):
       pass #your code here
   def lose_fight(self):
       pass #your code here
 
class Dragon(Monster):
   def win_fight(self):
       pass #your code here
   def lose_fight(self):
       pass #your code here