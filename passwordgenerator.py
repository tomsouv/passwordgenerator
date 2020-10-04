'''
Password Generator v1
06/13/2020

Goals for later revisioning:

* Reduce character_set list to one, and maybe look into appending special characters into existing character_set list depending on user input.
* Look into incorporating a cryptographically secure pseudorandom number generator aka CSPRNG for better encryption.
* Build a GUI for program.
'''

import random
import sys

# List that contains no special characters (62 characters total)
character_set_1 = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g',
    'h', 'i', 'j', 'k', 'l', 'm', 'n',
    'o', 'p', 'q', 'r', 's', 't', 'u',
    'v', 'w', 'x', 'y', 'z', 'A', 'B',
    'C', 'D', 'E', 'F', 'G', 'H', 'I',
    'J', 'K', 'L', 'M', 'N', 'O', 'P',
    'Q', 'R', 'S', 'T', 'U', 'V', 'W',
    'X', 'Y', 'Z', '1', '2', '3', '4',
    '5', '6', '7', '8', '9', '0']

# List that contains special characters (74 characters total)
character_set_2 = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g',
    'h', 'i', 'j', 'k', 'l', 'm', 'n',
    'o', 'p', 'q', 'r', 's', 't', 'u',
    'v', 'w', 'x', 'y', 'z', 'A', 'B',
    'C', 'D', 'E', 'F', 'G', 'H', 'I',
    'J', 'K', 'L', 'M', 'N', 'O', 'P',
    'Q', 'R', 'S', 'T', 'U', 'V', 'W',
    'X', 'Y', 'Z', '1', '2', '3', '4',
    '5', '6', '7', '8', '9', '0', '!',
    '@', '#', '$', '%', '^', '&', '*',
    '_', '?', '>', '<']

new_password = []

print('Welcome to my password generator.')

length_of_password = int(input('Enter a number between 8-20\n to generate the length of your new password: '))

if length_of_password in range(8,21):
    special_characters = str(input('Would you like special characters in your generated password?\n (e.g. !@#$%^&*_?><) y/n: '))
    while len(new_password) < length_of_password:
        if special_characters == 'n':
            randomizer = random.randint(0,61)
            new_password.append(character_set_1[randomizer])
            final_password = ''.join(new_password)
        elif special_characters == 'y':
            randomizer = random.randint(0,73)
            new_password.append(character_set_2[randomizer])
            final_password = ''.join(new_password)
        else:
            print('Your input was not valid. Please specify either \'y\' or \'n\' for special characters. Re-run the program to try again. Exiting program now...')
            sys.exit()
else:
    print('Length of generated password must be between 8-20. Re-run the program to try again. Exiting program now...')
    sys.exit()

print(f'Your new password is \"{final_password}\". Enjoy!')
