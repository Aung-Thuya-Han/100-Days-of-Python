import random
from hangman_art import stages
from hangman_words import word_list

cum_choice = random.choice(word_list)
print(cum_choice)
placeholder = ""

for word in cum_choice:
    placeholder += "_"

print(f"Word to guess: {placeholder}")

display = ""
lives = 6
guessed_letters = []

while display != cum_choice:

    display = ""
    user_guess = input("Enter your guess: ")

    for letter in cum_choice:
        if letter in guessed_letters:
            display += letter
        elif user_guess == letter:
            display += user_guess
            guessed_letters.append(letter)
            print(f"Correct! {lives} lives left.")
            print(stages[lives])
        else:
            display += "_"

    print(display)

    if  user_guess not in cum_choice:
        lives -= 1
        if lives == 0:
            print("No more lives left. You Lose!")
            print(stages[lives])
            break
        else:
            print(f"Wrong! {lives} lives left")
            print(stages[lives])
            print(display)


