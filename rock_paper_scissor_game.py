import random

print("=" * 45)
print("     🎮 WELCOME TO ROCK PAPER SCISSORS 🎮")
print("=" * 45)
print("Instructions:")
print("Enter:")
print("  r --> Rock")
print("  p --> Paper")
print("  s --> Scissors")
print("=" * 45)

user_score = 0
computer_score = 0

choices = {
    "r": "Rock",
    "p": "Paper",
    "s": "Scissors"
}

while True:
    user = input("\nEnter your choice (r/p/s): ").lower()

    if user not in choices:
        print("❌ Invalid choice! Please enter r, p, or s.")
        continue

    computer = random.choice(["r", "p", "s"])

    print(f"\nYou chose      : {choices[user]}")
    print(f"Computer chose : {choices[computer]}")

    if user == computer:
        print("🤝 It's a Draw!")

    elif (user == "r" and computer == "s"):
        print("🎉 You Win this round!")
        user_score += 1

    elif (user == "p" and computer == "r"):
        print("🎉 You Win this round!") 
        user_score += 1

    elif (user == "s" and computer == "p"):
        print("🎉 You Win this round!")   
        user_score += 1

    else:
        print("😔 Computer Wins this round!")
        computer_score += 1

    print("\n--------- Score Board ---------")
    print(f"You      : {user_score}")
    print(f"Computer : {computer_score}")
    print("-------------------------------")

    play_again = input("\nDo you want to play another round? (y/n): ").lower()

    if play_again != "y":
        break

print("\n========== FINAL SCORE ==========")
print(f"Your Score     : {user_score}")
print(f"Computer Score : {computer_score}")

if user_score > computer_score:
    print("🏆 Congratulations! You won the game.")
elif computer_score > user_score:
    print("💻 Computer won the game.")
else:
    print("🤝 The game ended in a Draw.")

print("\nThanks for playing! 😊")