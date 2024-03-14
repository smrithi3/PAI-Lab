print("Nim game!!\nWe have 12 sticks")

def player_turn(sticks):
    while True:
        take = int(input("How many sticks would you like to take? (1-3): "))
        if 1 <= take <= 3 and take <= sticks:
            return take
        print("Invalid input.")

def comp_turn(sticks):
    take = sticks % 4
    if take == 0:
        take = 1
    return take

sticks = 12
while sticks > 0:
    player_take = player_turn(sticks)
    sticks -= player_take
    print(f'You took {player_take} sticks. {sticks} sticks remaining.')
    if sticks <= 0:
        print("You win!")
        break

    comp_take = comp_turn(sticks)
    sticks -= comp_take
    print(f'Computer took {comp_take} sticks. {sticks} sticks remaining.')
    if sticks <= 0:
        print("Computer wins!")
