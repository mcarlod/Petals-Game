import dice
import random

# introducing the game to the user
print('Petals Around the Rose')
print('----------------------')
print("\nThe name of the game is 'Petals Around the Rose'. The name of the")
print("game is important. The computer will roll five dice and ask you to")
print("guess the score for the roll. The score will always be zero or an")
print("even number. Your mission, should you choose to accept it, is to")
print("work out how the computer calculates the score. If you succeed in")
print("working out the secret and guess correctly three times in a row, you")
print("become a Potentate of the Rose.")

# asks the user if they want to start or not
start = str(input('\nWould you like to play Petals Around the Rose [y|n]? '))

# if user doesn't put y or n, this error message will appear and will ask again
while start != "y" and start != "n":
    print("Please enter either 'y' or 'n'.")
    start = str(input('\nWould you like to play Petals Around the Rose [y|n]? '))    

# when user doesn't want to play, this appears
if start == 'n':
    print('\nNo worries... another time perhaps... :)')
    
# when user wants to play, this appears
elif start == 'y':
    # variables that track if user gets 3 incorrect or correct in a row
    hotstreak = 0
    coldstreak = 0

    # variable to start while loop
    restart = 'y'

    # variable to keep track of rounds and number of correct and wrong attempts
    rounds = 0
    correct = 0
    wrong = 0

    dice_count = [0,0,0,0,0,0,0]
    
    # restart while loop just incase user wants to keep playing after this turn
    while restart != 'n' and restart == 'y':
        # simulates roll of a die
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        die3 = random.randint(1,6)
        die4 = random.randint(1,6)
        die5 = random.randint(1,6)
        dice.display_dice(die1, die2, die3, die4, die5)

        # keeps track of dice roll stats
        roll = [die1, die2, die3, die4, die5]
        
        for index in roll:
            if index == 1:
                dice_count[index] += 1
            elif index == 2:
                dice_count[index] += 1
            elif index == 3:
                dice_count[index] += 1
            elif index == 4:
                dice_count[index] += 1
            elif index == 5:
                dice_count[index] += 1
            elif index == 6:
                dice_count[index] += 1

        # keeps track of score
        score = 0

        if die1 == 3:
            score += 2
        elif die1 == 5:
            score += 4
        else:
            score += 0
        
        if die2 == 3:
            score += 2
        elif die2 == 5:
            score += 4
        else:
            score += 0
        
        if die3 == 3:
            score += 2
        elif die3 == 5:
            score += 4
        else:
            score += 0
        
        if die4 == 3:
            score += 2
        elif die4 == 5:
            score += 4
        else:
            score += 0
        
        if die5 == 3:
            score += 2
        elif die5 == 5:
            score += 4
        else:
            score += 0

        # user input their guess for the roll
        user = int(input('Please enter your guess for the roll: '))
    
        # checks if users input is correct and providing feedback
        if user % 2 != 0:
            print("\nNo sorry, it's", score, "not", str(user) + '.', "The score is always even.")
            coldstreak += 1
            hotstreak = 0
            rounds += 1
            wrong += 1
        elif user % 2 == 0 and user != score:
            print("\nNo sorry, it's", score, "not", str(user) + '.')
            coldstreak += 1
            hotstreak = 0
            rounds += 1
            wrong += 1
        elif user % 2 == 0 and user == score:
            print('\nWell done! You guessed it!')
            coldstreak = 0
            hotstreak += 1
            rounds += 1
            correct += 1

        # incorrect and correct guesses in a row message is displayed
        if hotstreak == 3:
            print('')
            print('\nCongratulations! You have worked out the secret!')
            print("Make sure you don't tell anyone!")
        elif coldstreak == 3:
            print('')
            print('\nHint: The name of the game is important... Petals Around the Rose.')
        
        # asks if they wanna replay
        print('')
        restart = str(input('\nRoll dice again [y|n]? '))
        while restart != 'y' and restart != 'n':
            print("Please enter either 'y' or 'n'.")
            restart = str(input('\nRoll dice again [y|n]? '))

    # game summary
    print('')
    print('\nGame Summary')
    print('============')
    print('\nYou played', rounds,'games:')
    print('  |--> Number of correct guesses:    ', correct)
    print('  |--> Number of incorrect guesses:  ', wrong)
    print('\nDice Roll Stats:')
    print('\nFace Frequency')

    # this will display how frequent a face appeared in *
    index = 0
    while index < len(dice_count):
        for num in dice_count:
            if index > 0:
                print('  ', index, num * '*')
            index += 1
            
    print('\nThanks for playing!')