#Michel Nguyen
#CSE 20, assignment 3 (problem 2 - minesweeper)
#Prof. Larrabee, winter 2020

def calc_safe_cells(safe_cells, x, y):

#check to see if any row or column needs to be removed from surrounding 8 cells

    if x == 0 or x == int(rows_columns_list[0]) - 1:
    #if the bomb is at the top or bottom, remove 3 surrounding cells
        safe_cells = safe_cells - 3
        top_bottom = True
    
    else:
        top_bottom = False
    
    if y == 0 or y == int(rows_columns_list[1]) - 1:
        if top_bottom == True:
        #if the bomb is on the left or right AND top or bottom, remove 2 more cells (one counts as both the row and column)
            safe_cells = safe_cells - 2
        
        else:
        #if the bomb is on the left or right, remove 3 surrounding cells
            safe_cells = safe_cells - 3

#check for bombs in surrounding cells

    if [x + 1, y] in all_coord_list:
    #middle right
        safe_cells = safe_cells - 1
        
    if [x - 1, y] in all_coord_list:
    #middle left
        safe_cells = safe_cells - 1
        
    if [x, y + 1] in all_coord_list:
    #top middle
        safe_cells = safe_cells - 1
        
    if [x, y - 1] in all_coord_list:
    #bottom middle
        safe_cells = safe_cells - 1
        
    if [x - 1, y - 1] in all_coord_list:
    #top left corner
        safe_cells = safe_cells - 1
        
    if [x + 1, y - 1] in all_coord_list:
    #bottom left corner
        safe_cells = safe_cells - 1
        
    if [x - 1, y + 1] in all_coord_list:
    #top right corner
        safe_cells = safe_cells - 1
        
    if [x + 1, y + 1] in all_coord_list:
    #bottom right corner
        safe_cells = safe_cells - 1
    
    return safe_cells

rows_columns_input = input()
rows_columns_list = rows_columns_input.split(' ')
#list with two items: # of rows and # of columns

num_of_bombs = int(input())

all_coord_list = []
#complete list of all coordinates given

#for number of bombs, repeat ask for input of coordinates
for x in range(0, num_of_bombs):

    coord_input = input()
    coord_pair = [int(coord_input[0]), int(coord_input[2])]
    all_coord_list.append(coord_pair)

all_coord_list.sort()
z = 0
#counter for number of bombs/place in list of num_of_bombs

for x in range (0, int(rows_columns_list[0])):
#in row x:
    
    for y in range (0, int(rows_columns_list[1])):
    #in column y:

        safe_cells = 8
        
        if all_coord_list[z][0] == x and all_coord_list[z][1] == y:
            print('*', end='')
            if z != num_of_bombs - 1:
                z = z + 1
            else:
                pass
            if y == int(rows_columns_list[1]) - 1:
                print()
            
        else:
            cell_value = calc_safe_cells(safe_cells, x, y)
            print(cell_value, end='')

            if y == int(rows_columns_list[1]) - 1:
                print()
                    