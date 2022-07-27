'''
Michel Nguyen
CSE 20, assignment 1 (problem 2 - even flip)
Larrabee, winter 2020
'''

print('Even flip - a number game')
print('For any number, the order of the digits will be reversed, and printed only when even.\n')

user_input = input('Please enter a number greater than 0: ')
length = len(user_input)

print()
print('Total digits in original number: ', length, sep='')
print('New number: ', end='')

#process of finding new number

place_in_number = 1
even_digits = 0
#two counters for number of digits processed and number of even digits

loop_1 = True
loop_2 = True
#arbitrary loop to nest inside for continue/break statements
while loop_1 == loop_2:
    if place_in_number == length + 1:
        print()
        break
        #complete when times looped and total digits match

    else:
        digit = int(user_input) % 10

        #check for even digit and update even digit counter
        if digit == 0 or digit == 2 or digit == 4 or digit == 6 or digit == 8:
            print(digit, end='')
            even_digits = even_digits + 1

        else:
            pass
    
        place_in_number = place_in_number + 1
        user_input = int(user_input) // 10
        #update place in number counter and use floored division to round input to a multiple of 10
    continue

print('Even digits from original number: ', even_digits, '\n', sep='')

'''
end program
'''