"""
Hangman
"""

max_attempts = 6
failed_attempts = 0
answer = "better"
answer_list = list(answer)
player_guess = []
wrong_guesses = []

for letter in answer_list:
    player_guess.append('_')

while failed_attempts < max_attempts:
    print(f"Attempts remaining {failed_attempts}/{max_attempts}")
    print(' '.join(player_guess))
    letter = input("Guess a letter: ").lower()
    matching_letters = answer_list.count(letter)

    if matching_letters == 0:
        if letter in wrong_guesses:
            print(f"{letter} has already been guessed and is NOT in the word")
        else:
            wrong_guesses.append(letter)
            failed_attempts += 1
    else:
        if letter in player_guess:
            print(f"{letter} has already been guessed and is in the word")
        else:
            for index, answer_letter in enumerate(answer_list):
                if answer_letter == letter:
                    player_guess[index] = letter
    if player_guess.count('_') == 0:
        break

if failed_attempts == max_attempts:
    print("Ran out of attempts you lose")
    print(answer)
    print(''.join(player_guess))
else:
    print("you guessed the word!")
    print(''.join(player_guess))
    