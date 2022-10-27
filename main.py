import random
from replit import clear
# import word list
from hangman_words import word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6

# import logo
from hangman_art import logo, stages
print(logo)

#create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    clear()
# if user entered a letter they've already guessed, print the letter and notify
    if guess in display:
        print(f'You have already guessed {guess}')
    # check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    # if user is wrong.
    if guess not in chosen_word:
        # if the letter is not in the chosen word, print out the letter and notify
        print(f'You guessed {guess}, that is not in word. You lose a life')
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose. \n")
            print(f"The word was {chosen_word}")

    # join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    # import ascii art
    print(stages[lives])