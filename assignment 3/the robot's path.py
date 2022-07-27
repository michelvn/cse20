#Michel Nguyen
#CSE 20, assignment 3 (problem 1 - The robot's path)
#Prof. Larrabee, winter 2020

def check_valid_input(coordinates):
    
    for x in range(0, num_of_directions):

        #check for two inputs (direction + number of steps)
        if len(direction_list[x]) == 2:
            pass

        else:
            return False

        #check if direction is valid
        if direction_list[x][0] == 'L' or direction_list[x][0] == 'R' or direction_list[x][0] == 'U' or direction_list[x][0] == 'D':
            pass

        else:
            return False

        #check if number of steps is valid
        if (direction_list[x][1]).isdigit() == True:
            pass
        
        else:
            return False

def update_coordinates(coordinates):

    for x in range(0, num_of_directions):
    #add or subtract from x or y axis

        if direction_list[x][0] == 'L':
            coordinates[0] = int(coordinates[0]) - int(direction_list[x][1])
    
        elif direction_list[x][0] == 'R':
            coordinates[0] = int(coordinates[0]) + int(direction_list[x][1])
        
        elif direction_list[x][0] == 'U':
            coordinates[1] = int(coordinates[1]) + int(direction_list[x][1])
        
        elif direction_list[x][0] == 'D':
            coordinates[1] = int(coordinates[1]) - int(direction_list[x][1])
        
def theRoundTrip(coordinates):
    
    if coordinates == [0, 0]:
        return True

    else:
        return False

########

direction_input = input()

direction_list = direction_input.split(', ')

num_of_directions = len(direction_list)

for x in range(0, num_of_directions):
    direction_list[x] = direction_list[x].split(' ')

coordinates = [0, 0]

########

valid_input = check_valid_input(coordinates)

if valid_input != False:
    update_coordinates(coordinates)

    if theRoundTrip(coordinates) == True:
        print('True')
    
    elif theRoundTrip(coordinates) == False:
        print('False')

elif valid_input == False:
    print('bad input')

