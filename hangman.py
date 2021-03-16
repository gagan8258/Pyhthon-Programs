import random
def hman():
    word=random.choice(["adventure","night","program","computer","science","software"])
    alpha='abcdefghijklmnopqrstuvwxyz'
    guessmade=''
    turn=10
    while(len(word)>1):
        main=''
        missed=0
        for letter in word:
            if letter in guessmade:
                main=main+letter
            else:
                main=main+' '+'_'
        if(main==word):
            print(main)
            print("You win the game")
            break
        print("Guess the word:",main)
        guess=input()
        if guess in alpha:
            guessmade=guessmade+guess
        else:
            print("Please enter the correct letter")
            guess=input()
        if guess not in word:
            turn=turn-1
            if(turn==9):
                print("9 turns are left",end='\n')
                print("---------")
            if(turn==8):
                print("8 turns are left",end='\n')
                print("---------")
                print("    O    ")
            if(turn==7):
                print("7 turns are left",end='\n')
                print("---------")
                print("    O    ")
                print("    |    ")
            if(turn==6):
                print("6 turns are left",end='\n')
                print("---------")
                print("    O    ")
                print("    |    ")
                print("   /     ")
            if(turn==5):
                print("5 turns are left",end='\n')
                print("---------")
                print("    O    ")
                print("    |    ")
                print("   / \   ")
            if(turn==4):
                print("4 turns are left",end='\n')
                print("---------")
                print("  \ O    ")
                print("    |    ")
                print("   / \   ")
            if(turn==3):
                print("3 turns are left",end='\n')
                print("---------")
                print("  \ O /  ")
                print("    |    ")
                print("   / \   ")
            if(turn==2):
                print("2 turns are left",end='\n')
                print("---------")
                print("  \ O / |")
                print("    |    ")
                print("   / \   ")
            if(turn==1):
                print("1 turn is left",end='\n')
                print("---------")
                print("  \ O /_|")
                print("    |    ")
                print("   / \   ")
            if(turn==0):
                print("You loose the game")
                print("---------")
                print("    O_|  ")
                print("   /|\   ")
                print("   / \   ")
name=input("enter your name")
print("Welcome ",name)
print("---------------------")
print("Try to guess the word in less than 10 attempts")
hman()
print()
