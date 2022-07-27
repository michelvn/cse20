#Michel Nguyen
#CSE 20, assignment 2 (problem 3 - writing a multiples list)
#Prof. Larrabee, winter 2020

#for some number input_2, list all its multiples up to input_2 * input_1

input_1 = int(input())
input_2 = int(input())

list = []

for x in range(1, input_1+1):
    list.append(x*input_2)

print(list)