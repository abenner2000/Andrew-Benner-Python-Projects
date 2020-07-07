import random
import time

d = {1:'water',2:'andrew',3:'flame'}
e = {1:' O',2:' O\n |',3:' O\n |\n |',4:' O\n\|\n |',5:' O\n\|/\n |',6:' O\n\|/\n |\n/',7:' O\n\|/\n |\n/ \ '}

def game_over():
    if input("Play again? (Y/N): ").upper() == 'Y':
        main()
    else:
        print("Thanks for playing!") 

def word_order(word):
    i = 0
    lit = []
    while not len(word) == i:
        a = word[i]
        i += 1
        lit.append(a)
    return lit
        

def main():

    wordindex = random.randint(1,3)
    word = d[wordindex]

    i = 0
    wrong_list = []
    attempt = ['_']*len(word)
    word_guessed = False
    order = word_order(word)
    man = 0

    while not word_guessed:
        x = input("Guess a letter: ").lower()
        while not word_guessed:
            if x in word:
                i = 0
                while not x == word[i]:
                    i += 1
                attempt[i] = x
                print(attempt)
                break
            else:
                man += 1
                wrong_list.append(x)
                print("Wrong letters guessed: ",wrong_list)
                print("__")
                print(" |")
                print(e[man])
                print("\n\n")
                break
                
        if man == 7:
            print("You ran out of tries!")
            print("The answer was: ",word)
            game_over()
            break

        if attempt == order:
            print("You win!")
            print("The answer was: ",word,"!")
            game_over()
            break



main()
    
