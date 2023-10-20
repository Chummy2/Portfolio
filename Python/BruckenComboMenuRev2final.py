# pltw 3.1.3
# Simulate someone ordering at a fast food resturant
from ast import Num
from decimal import Rounded
from numbers import Number
total=0
orderinformation=[]
i=0
sandwich=1
drink=1
fries=1
ketchup=0
more=1
#sandwich
#ask user if they would like chicken, beef or tofu 
while i==0:
    
    while sandwich!=("y") or ("n"):
        print("Please type y or n")
        sandwich=input ("Do you want a sandwich(y/n) ")
        if sandwich=="y":
            break
        if sandwich=="n":
            break
    if sandwich=="y":
        
        while sandwich!=("c") or ("b") or ("t"):
            print("Please type c or b or t")
            sandwich=input ("which sandwich would you like: chicken $5.25, beef $6.25, tofu $5.75(c,b,t) ")
            if sandwich=="c":
                break
            if sandwich=="b":
                break
            if sandwich=="t":
                break
    if sandwich=="c":
        orderinformation.append("Chicken Sandwich")  
        total+=5.25
    elif sandwich=="b":
        orderinformation.append("Beef Sandwich")
        total+=6.25
    elif sandwich=="t":
        orderinformation.append("tofu Sandwich")
        total+=5.75
    else:
        print("you did not order a sandwich")
        orderinformation.append("you did not order a sandwich")
        
        
    while drink!=("y") or ("n"):
        print("Please type y or n")
        drink=input ("Do you want a drink(y/n) ")
        if drink=="y":
            break
        if drink=="n":
            break
    if drink=="y":

        while drink!=("s") or ("m") or ("l"):
            print("Please type s or m or l")
            drink=input ("which size? s,m,l ")
            if drink=="s":
                break
            if drink=="m":
                break
            if drink=="l":
                break
    if drink=="s":
        orderinformation.append("small drink")
        total+=1
    if drink=="m":
        orderinformation.append("medium drink")
        total+=1.75
    if drink=="l":
        
        while drink!=("y") or ("n"):
            print("Please type y or n")
            drink=input ("would you like a child size for $.38 more?(y/n) ")
            if drink=="y":
                break
            if drink=="n":
                break
        if drink=="y":
            total+=(2.25+.38)
            orderinformation.append("child drink")
        else:
            total+=2.25
            drink="l"
            orderinformation.append("large drink")
    else:
        print("no drink")
        orderinformation.append("you did not order a drink")
        
    while fries!=("y") or ("n"):
        print("Please type y or n")
        fries=input ("would you like fries(y/n) ")
        if fries=="y":
            break
        if fries=="n":
            break
    if fries=="y":
        
        while fries!=("s") or ("m") or ("l"):
            print("Please type s or m or l")
            fries=input ("which size? s,m,l ")
            if fries=="s":
                break
            if fries=="m":
                break
            if fries=="l":
                break
    if fries=="s":
        
        while fries!=("y") or ("n"):
            print("Please type y or n")
            fries=input ("would you like to mega size it?(y/n) ")
            if fries=="y":
                break
            if fries=="n":
                break
        if fries=="y":
            total==2.0
            orderinformation.append("large fry")
        else:
            orderinformation.append("small fry")
            total+=1.00
    elif fries=="m":
                total+=1.50
                orderinformation.append("medium fry")
    elif fries=="l":
                total+=2.0
                orderinformation.append("large fry")
    else:
        print("no fries")
        orderinformation.append("you did not order a frys")
        
    while ketchup!=("y") or ("n"):
            print("Please type y or n")
            ketchup=input("would you like ketchup(y/n) ")
            if ketchup==("y"):
                break
            if ketchup==("n"):
                break
            ketchup=0
    if ketchup==("y"):
        while ketchup.isnumeric:
            print("Please type a number")
            ketchup=int(input("How many "))
            if ketchup<=10:
                break
            if ketchup>=0:
                break
    orderinformation.append(ketchup)
    ketchup*=.25
    total+=ketchup
    if sandwich!="n" and drink!="n" and fries!="n":
        total-=1
    if ketchup==("n"):
        orderinformation.append(0)
    while more!=("y") or ("n"):
            print("Please type y or n")
            more=input("Do you want more food?(y/n) ")
            if more==("y"):
                break  
            if more==("n"):
                i=1
                break

#checkout
print("You order a",orderinformation[0])
print("You order a",orderinformation[1])
print("You order a",orderinformation[2])
print("You order",orderinformation[3],"ketchup")
print("subtotal $"+("%.2f" % (round(total,2))))
print("total $"+("%.2f" % (((round(total+total*0.07,2))))))
#https://www.w3schools.com/python/ref_func_round.asp
#https://stackoverflow.com/questions/19986662/rounding-a-number-in-python-but-keeping-ending-zeros
