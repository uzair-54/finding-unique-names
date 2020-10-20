def getNames(pathFile):
    f = open(pathFile,"r")      #openning the attendance file

    f1 = f.readlines()          #putting the names in a list
    x = 0
    names = [] 
    while True:

        if f1[x] != "\n":       #checking if there is name or line break
            names.append(f1[x])
        x += 1
        if x == len(f1):        #end the loop when reaches the end of array
            break
    return names                #returning the all the names in a list

def delDuplicate(*lists):
    allNames = []
    
    for i in range(0,len(lists)): 
        
        allNames.append(lists[i])                       #transforming from tuple to array(2d array) 

    finalList = []
    for k in range(0,len(allNames[0])):
    
        finalList.append(allNames[0][k])                # making a list to from the first file

    
    for j in range(1,len(allNames)):
        cnt = 0
        while True:
            
            if allNames[j][cnt] in finalList:           #checking for common names from second file
                cnt += 1
            elif allNames[j][cnt] not in finalList:
               finalList.append(allNames[j][cnt])
               cnt += 1
            if cnt == len(allNames[j]):
                break
    return finalList                                    #returning the final list

f1 = getNames("participants-2020-10-20.txt")            #assuming the file is in the same directory
f2 = getNames("participants-2020-10-20 (1).txt")
f3 = getNames("participants-2020-10-20 (2).txt")
f4 = getNames("participants-2020-10-20 (3).txt")
f5 = getNames("participants-2020-10-20 (4).txt")

l = delDuplicate(f1,f2,f3,f4,f5)
ff = open("finalList.txt","a")
ff.writelines(l)                #writing the names in an txt file
ff.close()

