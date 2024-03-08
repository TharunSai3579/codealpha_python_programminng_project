import random
import hangman_stages
def choose_words():
    words=["python","program","handsome","strawberry","sky","universe","ironman","car","house","family","krishna","pawan kalyan"]
    return random.choices(words)

print("Lets Play Hangman!!")
print("You have 5 lives so try to guess the word within 5 attempts! Good luck!!")
lives=5
word=choose_words()
display=[]
for i in range(len(word)):
    display += '_'
print(display)
game_over=False
while not game_over:
    guessed_letter=input("Guess a letter from the word: ").lower()
    for position in range(len(word)):
        letter=word[position]
        if letter==guessed_letter:
            display[position]=guessed_letter
    print(display)
    if guessed_letter not in word:
        lives-=1
        if lives==0:
            game_over=True
            print("You lost the game...!!!")
            print("the word is: ",word)
    if '_' not in display:
        game_over=True
        print("congratulations you won the game..:)")  
    print(hangman_stages.stages[lives]) 