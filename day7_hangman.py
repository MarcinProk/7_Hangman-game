import random
from day7_art import stages, logo
from day7_words import word_list

print(logo)
# wybór słowa
chosen_word = random.choice(word_list)
# TEST
# print("TEST: wylosowano słowo:", chosen_word)

# data
lives = 6
display = []
blank = '_'
for letter in chosen_word:
    display.append(blank)
print(display)

# zgadywanie liter
end_of_game = False
while end_of_game is False:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"You have already tried the letter {guess}!")
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = guess
            print(stages[lives])
    if guess not in chosen_word:
        lives -=1
        print(stages[lives])
        print(f"Letter {guess} is not in the word!")
            
    print(display)
    print(f"You have got {lives} lives left!")

    if "_" not in display:
        end_of_game = True
        print("You win!")
    elif lives == 0:
        end_of_game = True 
        print("You lose!")
