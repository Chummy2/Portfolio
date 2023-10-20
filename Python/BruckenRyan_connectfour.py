print("Directions- Pick a column to drop your piece into it. After completing your turn the next player goes. To win you have to get four in a row it can be vertically, diagnolly, and horizontal. ")
Player=1
from CheckInputClass import CheckInput
def printBoard(board):
     for r in range(6):
          print(board[r][0]+"|"+board[r][1]+"|"+board[r][2]+"|"+board[r][3]+"|"+board[r][4]+"|"+board[r][5]+"|"+board[r][6])
          if r==0 or r==1 or r==2 or r==3 or r==4:
               print("-"*13)
#returns a true or false value on whether we can choose that spot
def chooseSpot(r,c,symbol,board):
     #if the spot is open
     if board[r][c] == " ":
          #add the symbol and return true
          board[r][c]=symbol
          return True    
     return False
def catGame(board):
     #check every spot to see if there is something
     for row in range(len(board)):    #range(len(sampleBoard))->[0,1,2]
          for columns in range(len(board[row])):
               if (board[row][columns]) == " ":
                    return False
     print("CAT GAME!")
     return True         #return stop the function and give a value back
def checkForWinners(board):#fully works
     #check horizontally
     for r in range(len(board)):
          #r is the rows and the columns are the same for each row
          if (board[r][0] == board[r][1] and board[r][1] == board[r][2] and board[r][2]== board[r][3]) and board[r][0]!=" ":
               printBoard(board)
               print(f"Player{Player} wins")
               return True
          if (board[r][1] == board[r][2] and board[r][2] == board[r][3] and board[r][3]== board[r][4]) and board[r][1]!=" ":
               printBoard(board)
               print(f"Player{Player} wins")
               return True
          if (board[r][2] == board[r][3] and board[r][3] == board[r][4] and board[r][4]== board[r][5]) and board[r][2]!=" ":
               printBoard(board)
               print(f"Player{Player} wins")
               return True
          if (board[r][3] == board[r][4] and board[r][4] == board[r][5] and board[r][5]== board[r][6]) and board[r][3]!=" ":
               printBoard(board)
               print(f"Player{Player} wins")
               return True
          
     #check vertically
     for c in range(len(board)):
          #r is the rows and the columns are the same for each row
          if (board[0][c] == board[1][c] and board[1][c] == board[2][c] and board[2][c] == board[3][c]) and board[0][c]!=" ":
               printBoard(board)
               print(f"Player{Player} wins")
               return True
          if (board[1][c] == board[2][c] and board[2][c] == board[3][c] and board[3][c] == board[4][c]) and board[1][c]!=" ":
               printBoard(board)
               print(f"Player{Player} wins")
               return True
          if (board[2][c] == board[3][c] and board[3][c] == board[4][c] and board[4][c] == board[5][c]) and board[2][c]!=" ":
               printBoard(board)
               print(f"Player{Player} wins")
               return True
     #check diagonally 
     if (board[0][2] == board[1][1] and board[1][1] == board[2][0]) and board[2][0]!=" ":
          print("Winner winner Turkey dinner!")
          printBoard(board)
          return True
     if (board[0][0] == board[1][1] and board[1][1] == board[2][2]) and board[2][2]!=" ":
          print("Winner winner Turkey dinner!")
          printBoard(board)
          return True

     #hard code
board=[[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "],[" "," "," "," "," "," "," "]]
symbol="X"
r=0
goodc=0
zero=6
one=6
two=6
three=6
four=6
five=6
six=6
seven=6
while symbol!="Q":
     printBoard(board)
     #if the symbol is x
     # then run the code already built
     #else
     # run the computer's code
     #loop until a good spot is chosen
     goodSpot=False
     c=CheckInput.getCorrectInput(["1","2","3","4","5","6","7"],"Col:")
     while not goodSpot:
          bestc=int(c)
          c=bestc-1
          if c==0 and zero>0:
               zero-=1
               r=zero
          if c==1 and one>0:
               one-=1
               r=one
          if c==2 and two>0:
               two-=1
               r=two
          if c==3 and three>0:
               three-=1
               r=three
          if c==4 and four>0:
               four-=1
               r==four
          if c==5 and five>0:
               five-=1
               r=five
          if c==6 and six>0:
               six-=1
               r=six
          if c==7 and seven>0:
               seven=-1
               r=seven
          #if we can NOT choose the spot
          if(0<=c<=6)  and r>=0:
               if (not chooseSpot(r,c,symbol,board)):
                    goodSpot=True
                    if symbol=="X":
                         symbol="O"
                         Player=2
                    elif symbol=="O":
                         symbol="X"
                         Player=1
               else:
                    goodSpot = True

     #check for a winner or CAT
     if catGame(board) or checkForWinners(board):
          symbol="Q"
     #switching our symbols
     if symbol=="X":
          symbol="O"
          Player=2
     elif symbol=="O":
          symbol="X"
          Player=1