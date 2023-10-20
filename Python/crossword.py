def mainsearch():
    with open("Book1.csv","r") as file1:
        listy=[]
        for line in file1.readlines():
            currentlist=line.strip().split(",")
            listy.append(currentlist)
    def search(uiword,letters):#parker helped with this function
        lettertosearchfor=uiword[0]
        for i in range(len(letters)):
            for j in range(len(letters[i])):
                if lettertosearchfor == letters[i][j]:
                    x=horiz(i,j,uiword)
                    if x is not None: #checks type of varible loves the word None
                        print(f"{uiword} is at ({i},{j}")
                    elif horiz2(i,j,uiword) is not None:
                        print(f"{uiword} is at ({i},{j}")
                    elif vert(i,j,uiword) is not None:
                        print(f"{uiword} is at ({i},{j}")
                    elif vert2(i,j,uiword) is not None:
                        print(f"{uiword} is at ({i},{j}")
                    elif diag(i,j,uiword) is not None:
                        print(f"{uiword} is at ({i},{j}")
                    elif diag2(i,j,uiword) is not None:
                        print(f"{uiword} is at ({i},{j}")
                    elif diag3(i,j,uiword) is not None:
                        print(f"{uiword} is at ({i},{j}")
                    elif diag4(i,j,uiword) is not None:
                        print(f"{uiword} is at ({i},{j}")
    def horiz(i,j,hword):#parker helped with this function
        # i = row , j = collium
        found = True
        for k in range(len(hword)):
            if j+k < len(listy[i]):
                if hword[k] == listy[i][j+k]:#to change direction j+k
                    pass
                else:
                    found = False
                    break
            else:
                found = False
                break
        if found == True:
            print("Found the word!")
            return i , j
    def horiz2(i,j,h2word):
        # i = row , j = collium
        found = True
        for k in range(len(h2word)):
            if (j-k) >=0:
                if h2word[k] == listy[i][j-k]:#to change direction j-k
                    pass
                else:
                    found = False
                    break
            else:
                found = False
                break
        if found == True:
            print("Found the word!")
            return i , j
    def vert(i,j,vword):
        # i = row , j = collium
        found = True
        for k in range(len(vword)):
            if (i-k)>=0:
                if vword[k] == listy[i-k][j]:#to change direction i-k
                    pass
                else:
                    found = False
                    break
            else:
                found = False
                break
        if found == True:
            print("Found the word!")
            return i , j
    def vert2(i,j,v2word):
        # i = row , j = collium
        found = True
        for k in range(len(v2word)):
            if (i+k)<(len(listy)):
                if v2word[k] == listy[i+k][j]:#to change direction i+k
                    pass
                else:
                    found = False
                    break
            else:
                found = False
                break
        if found == True:
            print("Found the word!")
            return i , j
    def diag(i,j,dword):
        # i = row , j = collium
        found = True
        for k in range(len(dword)):
            if (i+k)<(len(listy)) and (j+k)<(len(listy[i])):
                if dword[k] == listy[i+k][j+k]:
                    pass
                else:
                    found = False
                    break
            else:
                found = False
                break
        if found == True:
            print("Found the word!")
            return i , j
    def diag2(i,j,d2word):
        # i = row , j = collium
        found = True
        for k in range(len(d2word)):
            if (i-k)>=0 and (j-k)>=0:
                if d2word[k] == listy[i-k][j-k]:
                    pass
                else:
                    found = False
                    break
            else:
                found = False
                break
        if found == True:
            print("Found the word!")
            return i , j
    def diag3(i,j,d3word):
        # i = row , j = collium
        found = True
        for k in range(len(d3word)):
            if (i+k)<(len(listy)) and (j-k)>=0:
                if d3word[k] == listy[i+k][j-k]:
                    pass
                else:
                    found = False
                    break
            else:
                found = False
                break
        if found == True:
            print("Found the word!")
            return i , j
    def diag4(i,j,d4word):
        # i = row , j = collium
        found = True
        for k in range(len(d4word)):
            if (i-k)>=0 and (j+k)<(len(listy)):
                if d4word[k] == listy[i-k][j+k]:
                    pass
                else:
                    found = False
                    break
            else:
                found = False
                break
        if found == True:
            print("Found the word!")
            return i , j
        #TODO:use a loop to match the rest of the word
        #Look to the right of the first found letter.
        #Looking for the letter too the right of the found letter.
        #After found 2nd letter repeat.
        #After word is found let the program keep running.
        #Search from left to right to check for the word
        #Repeat unitl reach end of puzzle
        #a,b,c,c,a,t,a,b,c
    #bogglesearch(i,j,uiword[1],letters)
    # def bogglesearch(i,j,nextletter,letters):
    #     for row in range(i-1,i+2):
    #         for column in range(j-1,j+2):
    #             if nextletter == letters[row][column]:
    #                 print("Found the next letter!")d]
    #                 return row,column
    search("binary",listy)
    search("COMPUTERSCIENCE",listy)
    search("DECIMAL",listy)
    search("HEXADECIMAL",listy)
    search("JUPYTER",listy)
    search("MATPLOTLIB",listy)
    search("NOTEBOOK",listy)
    search("OCTAL",listy)
    search("PANDAS",listy)
    search("POWERSHELL",listy)
mainsearch()