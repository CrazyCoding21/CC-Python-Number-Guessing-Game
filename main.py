import random

number = random.randrange(0, 10)
answer = 0
tries = 3

print('Guess the number game has started! You have 3 tries to guess the number the computer guessed.')

while answer != number:
    answer = input('\nEnter the number:\n')
    if answer.find('-') != -1:
        print('Please enter the number MORE than 0!')
    else:
        if answer.isdigit():
            answer = int(answer)

            if answer > number:
                print('Less!')
                tries -= 1
                if tries == 0:
                    print('You lose! Game Over')
                    quit()
                print('You tries:', tries)
            elif answer < number:
                print('More!')
                tries -= 1
                if tries == 0:
                    print('You lose! Game Over')
                    quit()
                print('You tries:', tries)
            elif answer == number:
                print('You WIN!')
                quit()
            else:
                pass