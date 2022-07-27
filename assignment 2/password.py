#Michel Nguyen
#CSE 20, assignment 2 (problem 2 - passphrase check)
#Prof. Larrabee, winter 2020

def palindrome(first_word):
    if first_word.isalpha() == True:
        pass
    else:
        return False

    length_word = len(first_word)
    half = length_word // 2

    for x in range(0, half):
        a = int(ord(first_word[half - 1]))
        b = int(ord(first_word[-half + x]))
        if a + 32 == b:
            return True
        elif a - 32 == b:
            return True
        elif a == b + 32:
            return True
        elif a == b - 32:
            return True
        elif a == b:
            return True
        else:
            return False

def integer(second_word):
    if second_word.isdecimal() == True:
        pass
    else:
        return False
    if len(second_word) >= 4:
        return True
    else:
        return False

def special(third_word):
    #is NOT condition: valid if word fails all tests
    beginning = third_word[0]
    if beginning != '@' and beginning[0] != '$' and beginning[0] != '%' and beginning[0] != '^' and beginning[0] != '&':
        return False
    else:
        pass
   
    end = third_word[-1]
    if end != ',' and end != '.' and end != '?' and end != '!':
        return False
    else:
        pass
    
    middle = third_word[1:4]
    if middle.isalpha() == False:
        return False
    elif middle.isalpha() == True:
        pass
    
    if len(third_word) != 5:
        return False
    elif len(third_word) == 5:
        pass

    #if all conditions met:
    return True


if __name__ == '__main__':

    user_input = input()
    passphrase_split = user_input.split()
    condition_count = 0

    #check first word
    first_word = passphrase_split[0]
    if palindrome(first_word) == True:
        condition_count = condition_count + 1
    else:
        pass

    #check second word
    second_word = passphrase_split[1]
    if integer(second_word) == True:
        condition_count = condition_count + 1
    else:
        pass


    #check third word
    #if passphrase_split[2] meets these conditions:
    third_word = str(passphrase_split[2])
    if special(third_word) == True:
        condition_count = condition_count + 1
    else:
        pass

    #final check for all conditions met
    if condition_count == 3:
        print('valid')
    else:
        print('invalid')