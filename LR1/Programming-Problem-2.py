filename = input("Enter the file NAME and FORMAT!\n(name.format): ")

file = open(filename, 'r')

linecount = 0
for line in file:
    linecount = linecount + 1
    
print("\n",filename,"has",linecount,"lines")

while True:
    numline = 0
    num = int(input("\nEnter a LINE NUMBER [0] to quit: "))
    if num >=1 and num <= linecount:
        file = open(filename, 'r')
        for lines in file:
            numline = numline + 1
            if numline == num:
                print(num,":",lines)
    elif num == 0:
        break
    
    else:
        if num!= linecount:
            print("\nLINE NUMBER is not available! Please input a number less than",linecount)
