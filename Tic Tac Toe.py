board=[' ' for x in range(10)]
def insertletter(letter,pos):
    board[pos]=letter
def designboard(board):
    print('   |   |   ')
    print(' '+board[1]+' | '+board[2]+' | '+board[3]+' ')
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(' '+board[4]+' | '+board[5]+' | '+board[6]+' ')
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(' '+board[7]+' | '+board[8]+' | '+board[9]+' ')
    print('   |   |   ')
def spaceIsfree(pos):
    return board[pos]==' '
def isboardfull(board):
    if board.count(' ')>1:
        return False
    else:
        return True
def getwinner(b,l):
    return ((b[1]==l and b[2]==l and b[3]==l) or
    (b[4]==l and b[5]==l and b[6]==l) or
    (b[7]==l and b[8]==l and b[9]==l) or
    (b[1]==l and b[4]==l and b[7]==l) or
    (b[2]==l and b[5]==l and b[8]==l) or
    (b[3]==l and b[6]==l and b[9]==l) or
    (b[1]==l and b[5]==l and b[9]==l) or
    (b[3]==l and b[5]==l and b[7]==l))
def playermove():
    run=True
    while run:
        move=input('Enter the position')
        try:
            move=int(move)
            if (move>0 and move<10):
                if spaceIsfree(move):
                    run=False;
                    insertletter('X',move)
                else:
                    print('Space is not free')
            else:
                print('Enter a number between 1 to 9')
        except:
            print('Enter a number')
def computermove():
    possiblemove=[x for x , letter in enumerate(board) if letter==' ' and x!=0]
    move=0
    for let in ['O' , 'X']:
        for i in possiblemove:
            copyboard=board[:]
            copyboard[i]=let
            if getwinner(copyboard,let):
                move=i
                return move
    cornersopen=[]
    for i in possiblemove:
        if i in [1,3,7,9]:
            cornersopen.append(i)
        if len(cornersopen)>0 :
            move=selectrandom(cornersopen)
            return move
    if 5 in possiblemove:
        move=5
        return move
    edgeopen=[]
    for i in possiblemove:
        if i in [2,4,6,8]:
            edgeopen.append(i)
        if len(edgeopen)>0:
            move=selectrandom(edgeopen)
            return move
def selectrandom(li):
    import random
    ln=len(li)
    r=random.randrange(0,ln)
    return li[r]
def main():
    print('Welcome to the game')
    designboard(board)
    while not(isboardfull(board)):
        if not(getwinner(board , 'O')):
            playermove()
            designboard(board)
        else:
            print('You loose the game')
        if not(getwinner(board , 'X')):
              move = computermove()
              if move == 0:
                print(" ")
              else:
                insertletter('O' , move)
                print('computer placed an o on position' , move , ':')
                designboard(board)
        else:
            print("you win!")
            break
        if isboardfull(board):
            print("Tie game")
while True:
    x = input("Do you want to play again? (y/n)")
    if x.lower() == 'y':
        board = [' ' for x in range(10)]
        print('--------------------')
        main()
    else:
        break







    if isboardfull(board):
        print("Tie the game")
