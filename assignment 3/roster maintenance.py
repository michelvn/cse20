#Michel Nguyen
#CSE 20, assignment 3 (problem 4 - roster)
#Prof. Larrabee, winter 2020

import sys
class Command:

    def __init__(self, command, name, grade):
    #assign attributes command, name, and grade

        self.command = command
        self.name = name
        self.grade = int(grade)


    def add_grade(self):
    #check for name in roster, and add if not there

        if (user_input.name not in roster) and user_input.grade <= 100:

            roster[user_input.name] = user_input.grade

            print('Added', user_input.name)


        elif (user_input.name in roster) or user_input.grade > 100:

            print('Failed to add', user_input.name)
        

    def update_grade(self):
    #update grade of name given
    
        if (user_input.name in roster) and user_input.grade <= 100:
            roster[user_input.name] = user_input.grade
            print('Updated ', user_input.name, '\'s grade', sep='')

    
        elif (user_input.name not in roster):
            print(user_input.name, 'does not exist in the roster')
    
        elif user_input.grade > 100:
            print('Failed to update ', user_input.name, '\'s grade', sep='')

roster = {}

cmd_input = input()

while cmd_input != 'exit' or cmd_input != 'print':
#if the input is more than one word, we can split it to get the command + name + grade

    list_cmd = cmd_input.split(' ')

    if list_cmd[0] != 'remove':

        user_input = Command(list_cmd[0], list_cmd[1], list_cmd[2])

        if user_input.command == 'add':
            user_input.add_grade()

        if user_input.command == 'update':
            user_input.update_grade()

    if list_cmd[0] == 'remove':
    #remove the specified key from the roster, not the current user_input.name

        if (list_cmd[1] in roster):
            del roster[list_cmd[1]]
            print('Removed', list_cmd[1])

        elif (list_cmd[1] not in roster):
            print(list_cmd[1], 'does not exist in the roster')

    cmd_input = input()
    #loop again

    if cmd_input == 'print':
        for key, val in roster.items():
            print(key, ": ", val, sep='')

        cmd_input = input()

    if cmd_input == 'exit':
        sys.exit()

    else:
        continue
