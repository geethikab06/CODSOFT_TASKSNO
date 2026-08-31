import random

user_score = 0
computer_score = 0

print("===== ROCK PAPER SCISSORS =====")
print("1. User vs Computer")
print("2. User vs User")

mode = input("Choose game mode (1/2): ")

while True:

    print("\n--- Choose Your Option ---")
    print("Rock")
    print("Paper")
    print("Scissors")

    # USER VS COMPUTER
    if mode == "1":

        user1 = input("User 1, enter your choice: ").lower()

        choices = ["rock", "paper", "scissors"]
        computer = random.choice(choices)

        print("User 1 chose:", user1)
        print("Computer chose:", computer)

        if user1 not in choices:
            print("Invalid choice!")

        elif user1 == computer:
            print("It's a tie!")

        elif (user1 == "rock" and computer == "scissors") or \
             (user1 == "scissors" and computer == "paper") or \
             (user1 == "paper" and computer == "rock"):

            print("User 1 wins!")
            user_score += 1

        else:
            print("Computer wins!")
            computer_score += 1

        print("User 1 Score:", user_score)
        print("Computer Score:", computer_score)

    # USER VS USER
    elif mode == "2":

        user1 = input("User 1, enter your choice: ").lower()

        user2 = input("User 2, enter your choice: ").lower()

        choices = ["rock", "paper", "scissors"]

        print("User 1 chose:", user1)
        print("User 2 chose:", user2)

        if user1 not in choices or user2 not in choices:
            print("Invalid choice!")

        elif user1 == user2:
            print("It's a tie!")

        elif (user1 == "rock" and user2 == "scissors") or \
             (user1 == "scissors" and user2 == "paper") or \
             (user1 == "paper" and user2 == "rock"):

            print("User 1 wins!")
            user_score += 1

        else:
            print("User 2 wins!")
            computer_score += 1

        print("User 1 Score:", user_score)
        print("User 2 Score:", computer_score)

    else:
        print("Invalid mode!")
        break

    play_again = input("\nPlay another round? (y/n): ").lower()

    if play_again != "y":
        print("\n===== GAME OVER =====")
        break