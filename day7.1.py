import random
from hangmanwords import word_list
from hangmanart import stages,logo
lives = 0


print(logo)
chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for letters in range(word_length):
    placeholder += '-'

print(placeholder)


game_over = False
correct_letters = []

while not game_over:
    display = ""
    print(f"***************************************{lives}/6 LIVES LEFT***********************************")
    user_input = input("Guess the letter in the word:\n").lower()

    if user_input in correct_letters:
        print(f"You've already Guessed {user_input}")

    correct_guess = False

    for char in chosen_word:
        if char == user_input:
            display += char
            correct_letters.append(char)
        elif char in correct_letters:
            display += char
        else:
            display += '-'


    print(display)



    if user_input not in chosen_word:
        lives += 1
        print(f"You guessed{user_input}, that's not in the word. you lose a life")
        if lives >= 6:
            game_over = True
            print(f"**************************It was :{chosen_word} -- You lose**************************")

    if '-' not in display:
        game_over = True
        print("********************************You win**********************************")
    print(stages[lives])