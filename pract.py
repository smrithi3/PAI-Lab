def nim():
    rows = [1, 3, 5, 7]  # Initial number of matchsticks in each row

    while any(rows):
        for i, sticks in enumerate(rows):
            print(f"Row {i+1}: {'| ' * sticks}")
        
        row = int(input("Choose a row (1-4): ")) - 1
        num_sticks = int(input("How many matchsticks do you want to take? "))

        if 1 <= num_sticks <= rows[row]:
            rows[row] -= num_sticks
        else:
            print("Invalid input. Please choose a valid number of matchsticks.")
            continue

        if all(sticks == 0 for sticks in rows):
            print("You win!")
            break

        ai_row = next((i for i, sticks in enumerate(rows) if sticks), None)
        ai_num_sticks = rows[ai_row] if ai_row is not None else 0
        rows[ai_row] -= ai_num_sticks
        print(f"The AI takes {ai_num_sticks} matchsticks from row {ai_row + 1}.")

        if all(sticks == 0 for sticks in rows):
            print("AI wins!")
            break

# Run the game
nim()
