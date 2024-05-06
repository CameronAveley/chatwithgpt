
import random

def play_game():
    score = 0
    
    while True:
        player_number = int(input("Enter your player number (1, 2, or 3): "))
        if player_number == 1:
            # Player 1's turn
            print("Player 1 rolls...")
            dice_roll = random.randint(1, 6)
            print("You rolled a", dice_roll)
            if dice_roll == 1:
                print("Bust!")
            elif dice_roll == 2 or dice_roll == 3:
                # Player 1 keeps rolling
                score += dice_roll
                print("You rolled a", dice_roll)
                if score >= 15:
                    print("Bust!")
                    return score
        elif player_number == 2:
            # Player 2's turn
            print("Player 2 rolls...")
            dice_roll = random.randint(1, 6)
            print("You rolled a", dice_roll)
            if dice_roll == 1:
                print("Bust!")
            elif dice_roll == 2 or dice_roll == 3:
                # Player 2 keeps rolling
                score += dice_roll
                print("You rolled a", dice_roll)
                if score >= 15:
                    print("Bust!")
                    return score
        elif player_number == 3:
            # Player 3's turn
            print("Player 3 rolls...")
            dice_roll = random.randint(1, 6)
            print("You rolled a", dice_roll)
            if dice_roll == 1:
                print("Bust!")
            elif dice_roll == 2 or dice_roll == 3:
                # Player 3 keeps rolling
                score += dice_roll
                print("You rolled a", dice_roll)
                if score >= 15:
                    print("Bust!")
                    return score
        else:
            print("Invalid player number. Please enter 1, 2 or 3.")
        
    # End of game
    print("Player", winner(score), "wins!")
    
def winner(score):
    if score >= 15:
        return "Bust!"
    elif score > 21:
        return "Blackjack!"
    else:
        return "Bust!"

play_game()
