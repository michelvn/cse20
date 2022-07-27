#Michel Nguyen
#CSE 20, assignment 3 (problem 2 - Minesweeper)
#Prof. Larrabee, winter 2020

num_of_strings = int(input())
num_of_str_list = []
temp_count = 0
stored_count = 0
max_count = 0
current_string: False


#create list of user input, then join all inputs together for one string
for x in range(0, num_of_strings):
    str_input = str(input())
    num_of_str_list.append(str_input)
    
continuous = ''.join(num_of_str_list)

#search string for '1'
for x in range(0, len(continuous)):

    if continuous[x] == '1':
    #string is true, add to current string counter, store
        current_string = True
        temp_count = temp_count + 1
        stored_count = temp_count

    elif continuous[x] == '0':
    #string is false, store number of '1's and reset current string counter to 0
        current_string = False
        stored_count = temp_count
        temp_count = 0

    if x == len(continuous) and current_string == True:
    #if the end of the string is reached, whatever is in temp_count gets stored
                stored_count = temp_count

    if stored_count > max_count:
    #if the stored length is larger than the current max length, update
        max_count = stored_count
    
print(max_count, end='')