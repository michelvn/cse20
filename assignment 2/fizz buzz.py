#Michel Nguyen
#CSE 20, assignment 2 (problem 1 - FIZZ BUZZ)
#Prof. Larrabee, winter 2020

int_fizz = int(input())
int_buzz = int(input())

for x in range(1, 21):
    if x % int_fizz == 0 and x % int_buzz == 0:
        print('FIZZBUZZ', end=' ')
    elif x % int_fizz == 0:
        print('FIZZ', end=' ')
    elif x % int_buzz == 0:
        print('BUZZ', end=' ')
    else:
        print(x, end=' ')