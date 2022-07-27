'''
Michel Nguyen
CSE 20, assignment 1 (problem 1 - cost of baked goods)
Larrabee, winter 2020
'''

#cost = hourly wage * hours of work + ingredients

print('Cost of baked goods - a calculator')
print('To create baked goods, one needs to pay for labor, ingredients, and time.\n')

hours = (float(input('How many hours are spent baking? ')))
baker = (float(input('What is the cost per hour of hiring a baker? $')))
ingredients = (float(input('How much is spent on ingredients? $')))


paytime = hours * baker

total = round(paytime + ingredients, 1)

print()
print('The total cost for baking is $', total, '0', '.\n', sep='')

'''
end program
'''