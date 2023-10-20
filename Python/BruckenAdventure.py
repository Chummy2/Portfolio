from turtle import pu
from webbrowser import get


firstAchivement=1
secondAchivement=1
thirdAchivement=1
fourthAchivement=1
fifthAchivement=1
i=0
l=0
a=0
#loop that resets for the ending 
while l==0:
    winnerwinner=[]#A list to get the good ending
    #used for when you continue to sleep and lose and will ask if they wanna to play again if yes then it keeps going other wise it goes back to the beginning screen
    while i==0:
        #used for the main menu so you can check achivements
        while a==0:
            start=input("Type Play to start or type Achivements to check what achivements you've unlocked. ")
            if start==("Achivements"):
                choose=input("Type 1,2,3,4,5 to check what achivements you've unlocked ")
                if choose==("1"):
                    if firstAchivement==1:
                        print("(?????????????)(Locked)Hint(Sleepyhead)")
                    elif firstAchivement==2:
                        print("(Seems like you overslept)(Unlocked)")
                if choose==("2"):
                    if secondAchivement==1:
                        print("(?????????????)(Locked)Hint(did you forget something?)")
                    elif secondAchivement==2:
                        print("(dude you had time)(Unlocked)")
                if choose==("3"):
                    if thirdAchivement==1:
                        print("(?????????????)(Locked)Hint(dirty boy)")
                    elif thirdAchivement==2:
                        print("(thats nasty)(Unlocked)")
                if choose==("4"):
                    if fourthAchivement==1:
                        print("(?????????????)(Locked)Hint(can brushing your teeth go wrong?)")
                    elif fourthAchivement==2:
                        print("(Bro how can't you brush correctly???)(Unlocked)")
            elif start==("Play"):
                print("You wake up and look at the clock and see thats its 7:30")
                print("you bus leaves at 7:35")
                a=1
        getup=input("Should you start getting ready for school?(y/n) ")
        if getup==("y"):
            i=1
        elif getup==("n"):
            print("You overslept and missed the bus.")
            print("GAME OVER")
            print("Achivement 1 unlocked")
            winnerwinner.append("nosleep")#added to the good ending list
            i=1
            firstAchivement=2
            playagain=input("Would you like to continue?)(y/n) ")
            if playagain==("y"):
                i=0
            elif playagain==("n"):
                i=0
                a=0

    print("You get out of bed and start getting ready" )
    putonclothes=input("you look around and dont see any underware. Should you try to find some?(y/n) ")
    if putonclothes==("n"):
        print("Achivement 2 Unlocked")
        print("You decide that you dont have the time to find your underware so you continue getting dressed the rest of the way")
        secondAchivement=2
    elif putonclothes==("y"):
        winnerwinner.append("clothes")
        print("You look around and find some some underware under your bed. You're not really sure how clean these are but you continue to put them on")
        print("You get the rest of you clothes on and go to the bathroom to finish getting ready")
    print("You go to the bathroom to finish getting ready")
    shower=input("you think to your self, should you take a shower?(y/n) ")
    if shower==("n"):
        print("Achivement 3 Unlocked")
        thirdAchivement=2
        print("You decided to skip the shower and continue your day")
    elif shower==("y"):
        print("You get in the shower and continue your day.")
        winnerwinner.append("shower1")
    print("your really low on time but then you remeber you still need to brush your teeth.")
    brush=input("Should you brush your teeth?(y/n) ")
    if brush==("n"):
        print("Achivement 4 Unlocked")
        fourthAchivement==2
        print("you decide to skip brushing and start to get your shoes on")
    elif brush==("y"):
        winnerwinner.append("brush1")
        print("You decide that its worth brushing your teeth and afterwards start to get your shoes on")
    #if lengh does not equal 4 you will get the bad ending
    if len(winnerwinner) != 3:
        print("you get outside and notice the bus hasnt even came....")
        print("Seems like you had time to get ready")
        print("You win I guess...")
        print("Maybe get a better ending?")
        #if you do everything right you get the good ending
    elif len(winnerwinner) == 3:
        print("Right when you get outside the bus is closing its door and is about to drive away")
        print("You make a mad dash to the bus and start screaming for it.")
        print("right when you are about to give up the bus stops again and opens its door.")
        print("You Win")
        print("Achivement 5 Unlocked")
        fifthAchivement==2
    #checks if you want to play again and if yoy say yes it restarts from the beginning
    again=input("do you want to play again? (y/n)")
    if again==("n"):
        l=1
    elif again==("y"):
        a=0
        l=0
        i=0
    
        
        
    
    
        
