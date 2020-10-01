import random as rd
import time as t

monster=rd.choice(["Goblins","Slime"])
job=rd.choice(["Hunt"])
weapon="Sword"
magic="Fire"
spell=magic+" Bullet"


def intro():
    print("Hello there!!!")
    t.sleep(0.5)
    print("Welcome to the Fantasy World")
    t.sleep(0.5)
    choice=input("To go to an adventure enter 'Y' : ")
    print("_____________________________________________________________")
    return choice

def play(choice):
    if choice=="Y" or choice=="y":
        global name
        name=input("Enter your name : ")
        t.sleep(0.5)
        print("So",name,"There you go..Time to do some adventure")
        return name
    else:
        print("What are you?? a LOSER!!")
        exit()
    print("_____________________________________________________________")
    
def displayQuest(name):
    t.sleep(0.5)
    print("Now time for a Quest")
    t.sleep(2)
    print("Welcome",name)
    print("Now You wil receive a Quest")
    print("Your Quest is to ",job," ",monster)
    print("_____________________________________________________________")
    
def playQuest():
    global health,reward
    health = 100
    print("Your Primary Weapon is : ",weapon)
    print("Magic Spell is : ",spell)
    print("To use Any Attack name the attack ")
    
    while health>0 :
        attack=input("Enter Attack :  ")
        if attack==weapon:
            health=health-rd.randint(5,20)
        elif attack==spell:
            health=health-rd.randint(20,40)
        else:
            print("You Lost..!!!")
            exit()

        t.sleep(0.5)
        if health < 0:
            health = 0
        print("Enemy health is now ",health)
            
    else:
        t.sleep(0.5)
        print("Congratulations,You Defeated The Eneemy")
        t.sleep(0.5)
        print("Job Completed")
        t.sleep(0.5)
        print("You Earned a reward")
        reward = 50
        t.sleep(0.5)
        print("Your Reward is ",reward)
        
    print("_____________________________________________________________")

ch = "yes"
while ch == "yes" or ch == "y":
    choice=intro()
    name=play(choice)
    displayQuest(name)
    playQuest()
    ch=input("Do you want to play again??(Yes/Y) : ").lower()


