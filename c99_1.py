import os, shutil

#src = input("Enter Source Directory: ")
#dest = input("Enter Destination Directory: ")

src = "C://Users/Saaheer/Desktop/Programming/New"
dest = "C://Users/Saaheer/Desktop/Programming/Backup"
    
or item in os.listdir(src):
    name, ext = os.path.splitext(item)
    
    if ext=="":
        for item1 in os.listdir(src + '/' + item):
            if not os.path.exists(dest + '/' + item):
                os.mkdir(dest + '/' + item)
                
            shutil.copy(src + "/" + item + '/' + item1, dest + "/" + item + '/' + item1)
    else:
        shutil.copy(src + "/" + item, dest + "/" + item)
