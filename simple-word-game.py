import random
import time

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board']
word = random.choice(words)
turns = 12
name = str(input("What is your name? "))
guesses = ""

print(f"Good luck, {name}!")
time.sleep(1)
print("Game starts in 3")
time.sleep(1)
print("Game starts in 2")
time.sleep(1)
print("Game starts in 1")
time.sleep(1)

while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_", end=" ")
            failed += 1
    if failed == 0:
        print("\nCongratulations! You won!")
        break
    guess = input("\nGuess a character: ").lower()
    guesses += guess + " "
    print(f"used letters: {guesses}")
    if guess not in word:
        turns -= 1
        print(f"Wrong! You have {turns} turns left.")
        if turns == 0:
            print("Sorry, you lost. The word was:", word)
            break