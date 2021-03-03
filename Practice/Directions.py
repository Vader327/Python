dirns = (input("Enter the directions, separated by a space, in lowercase: ")).split()
#dirns = ['n', 'n', 's', 'w', 'w', 'e', 's', 'e', 'w']

for i in range(len(dirns)):    
    try:
        dirn = dirns[i]
        if dirn=="n" and dirns[i+1]=="s":
            del dirns[i:i+2]
        elif dirn=="s" and dirns[i+1]=="n":
            del dirns[i:i+2]
        elif dirn=="e" and dirns[i+1]=="w":
            del dirns[i:i+2]
        elif dirn=="w" and dirns[i+1]=="e":
            del dirns[i:i+2]

    except IndexError:
        pass

print("Directions: " + str(dirns)[1:-1].replace('\'', ''))
