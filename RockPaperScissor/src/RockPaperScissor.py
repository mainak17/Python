import random as rd 
my_win = 0 #initialize user wins
comp_win = 0#initialize computer wins

def getChoice():#function that takes input from user
    print("### Rock Paper Scissor ###")
    choice = input("Enter Your Choice : ")
    choice  = choice.lower()
    return choice
def displayScore() :#function that displays result
    print("Score : Player = %d Computer = %d"%(my_win,comp_win))

option = ["rock","paper","scissor"]#choices of list to choose from
rounds = int(input("Enter Number of Rounds : "))#input the number of rounds

for i in range(0,rounds) :   
    my_choice = getChoice()
    comp_choice = rd.choice(option)
    print("Computer Choice : ",comp_choice)
    #different choice combinations
    if comp_choice == my_choice :
        print("Match Draw...Try Again...")
    elif comp_choice == "rock" and my_choice =="paper" :
        print("Player Wins..")
        my_win+=1
    elif comp_choice == "rock" and my_choice =="scissor" :
        print("Computer Wins..")
        comp_win+=1
    elif comp_choice == "paper" and my_choice =="rock" :
        print("Computer Wins..")
        comp_win+=1
    elif comp_choice == "paper" and my_choice =="scissor" :
        print("Player Wins..")
        my_win+=1
    elif comp_choice == "scissor" and my_choice =="rock" :
        print("Player Wins..")
        my_win+=1
    elif comp_choice == "scissor" and my_choice =="paper" :
        print("Computer Wins..")
        comp_win+=1

    displayScore()#display the current score
if(comp_win > my_win):#condition for computer wins
    print("Computer Wins...Better Luck Next Time...")
elif(comp_win < my_win):#condition for user wins
    print("Player Wins...Good Job...")
else :#condition for draw
    print("Match Draw...")        
print("##################################################")
