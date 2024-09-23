import random
import words
import stages
user_list=[]
guessed_list=[]
lives=6
generated_word=random.choice(words.words_list)
for i in range(len(generated_word)):
    user_list+='_'
game_over=False
while not game_over:
    char=input("Guess a letter:").lower()
    if char in guessed_list:
        print(f"{char} already guessed")
        continue
    guessed_list.append(char)
    for pos in range(len(generated_word)):
        if generated_word[pos]==char:
            user_list[pos]=char
    print(" ".join(user_list))
    if '_' not in user_list:
        game_over=True
        print("HEY YOU WON !!!!!")
    if char not in generated_word:
        lives-=1
        print(stages.stages_list[lives])
        if lives==0:
            game_over=True
            print("YOU LOST !!!")
            print(f"WORD : {generated_word}")
            print(f"WORD : {generated_word}")






