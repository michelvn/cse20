'''
Michel Nguyen
CSE 20, assignment 1 (problem 3 - file size)
Larrabee, winter 2020
'''

print('File size - a byte conversion tool')
print('Bytes will be converted into kB, mB, or gB depending on size.\n')

byte_input = (input('Enter any number of bytes: '))
print(byte_input, 'bytes is equivalent to ', end='')

#find converted value and print

divide_byte = float(byte_input)
if divide_byte < pow(2, 20):
    divide_byte = divide_byte / pow(2,10)
    print(round(divide_byte), 'kB.\n')
#if bytes are less than 1MB (1024 KB), divide and express in KB

else:
    divide_byte = divide_byte / pow(2, 10)
    #or else bytes must be equal to or greater than 1MB
    
    if divide_byte >= pow(2, 20):

            divide_byte = divide_byte / pow(2, 20)
            print(round(divide_byte), 'gB.\n')
            #if 1024 MB or more, it's at least 1 GB (1024 MB)

    else:
            divide_byte = divide_byte / pow(2, 10)
            print(round(divide_byte), 'mB.\n')
            #or else it must be somewhere between 1 MB and 1023 MB

#print statements for each conversion are inside the conditionals,
#no further action needed 

'''
end program
'''