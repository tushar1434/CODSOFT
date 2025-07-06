import random

# Score tracking
user_score = 0
computer_score = 0

while True:
    # User input
    user = input("Choose rock, paper, or scissors (or 'exit' to stop): ").lower()

    if user == 'exit':
        break

    # Check valid input
    if user not in ['rock', 'paper', 'scissors']:
        print("Invalid input, try again.\n")
        continue

    # Computer choice
    computer = random.choice(['rock', 'paper', 'scissors'])

    print(f"You chose: {user}")
    print(f"Computer chose: {computer}")

    # Game logic
    if user == computer:
        print("It's a tie!\n")
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        print("You win!\n")
        user_score += 1
    else:
        print("Computer wins!\n")
        computer_score += 1

    # Show current score
    print(f"Score: You = {user_score}, Computer = {computer_score}\n")

print("\nGame Over!")
print(f"Final Score: You = {user_score}, Computer = {computer_score}")