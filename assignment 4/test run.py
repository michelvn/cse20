possible_attacks = {'sneak_attack': 1, 'slash': 2, 'ice_storm': 3, 'fire_storm': 3, 'whirlwind': 3, 'earthquake': 2, 'double_hit': 4, 'tornado': 4, 'wait': 0}
attacks = {'fire_storm': 3, 'double_hit': 4, 'earthquake': 2, 'ice_storm': 3}
attacks2 = {'fire_storm': 3, 'double_hit': 4, 'earthquake': 2, 'ice_storm': 3}
hp1 = 20
hp2 = 20

atk_list = list(attacks.keys())
sort_list = []
for attack in sorted(atk_list):
    sort_list.append(attack)

print(sort_list)

#for attack in sort_list:
    #attacks[]

atk_list2 = list(attacks2.keys())
sort_list2 = []
for attack in sorted(atk_list2):
    sort_list2.append(attack)

#hardcode key for sorting?
# self.possible_attacks = {'sneak_attack': 1, 'slash': 2, 'ice_storm': 3, 'fire_storm': 3, 'whirlwind': 3, 'earthquake': 2, 'double_hit': 4, 'tornado': 4, 'wait': 0}
list_key = ['double_hit', 'tornado', 'fire_storm', 'ice_storm', 'whirlwind', 'earthquake', 'slash', 'sneak_attack', 'wait']
empty = []

for attack in list_key:
    if attack in monster1.attacks.keys():
        empty.append(attack)
    
print(empty)

#for x in range (0, 3):
    #hp2 = hp2 - attacks[atk_list(x)]
    #hp1 = hp1 - attacks2[atk_list2(x)]
  #  print(hp2, hp1)