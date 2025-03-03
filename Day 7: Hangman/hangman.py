"""
Hangman
"""

max_attempts = 6
failed_attempts = 0
generated_word = "better"
generated_word_list = list(generated_word)
player_guess = []

for letter in generated_word_list:
    player_guess.append('_')

while failed_attempts < max_attempts:
    print(f"Attempts remaining {failed_attempts}/{max_attempts}")
    print(' '.join(player_guess))
    letter = input("Guess a letter: ")
    count_of_guess = generated_word.count(letter)
    if count_of_guess == 0:
        failed_attempts += 1
    else:
        for i in range(0, count_of_guess):
            first_index_of_guess = generated_word_list.index(letter)
            player_guess[first_index_of_guess] = letter
            generated_word_list[first_index_of_guess] = '_'
    if player_guess.count('_') == 0:
        break

if failed_attempts == max_attempts:
    print("Ran out of attempts you lose")
    print(generated_word)
    print(''.join(player_guess))
else:
    print("you guessed the word!")
    print(''.join(player_guess))
    