import random

options = ['rock','paper','scissors']

user_choise = None
computer_choise = random.choice(options)


while user_choise not in options:
    print('Please type one of the option')
    user_choise = input('rock,paper or scissors: ').lower()
    
print('Your choise is: ' + user_choise)
print('the computer choise is: ' + computer_choise )

if user_choise == computer_choise:
    print('tie')
elif user_choise == 'rock':
    if computer_choise == 'paper':
        print('The computer won')
    else:
        print('You won')
elif user_choise == 'paper':
    if computer_choise == 'rock':
        print('You won')
    else:
        print('The computer won')
else:
    if computer_choise == 'rock':
        print('The computer won')
    else:
        print('You won')