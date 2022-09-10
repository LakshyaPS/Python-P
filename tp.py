num=int(input("enter the number of rows you want::"))
for row in range(1,num+1):
    for col in range(num-row):
        print(end=' ')
    for col in range(1,row+1):
        print('*',end=' ')
    print()
for row in range(num-1,0,-1):
    for col in range(num-row,0,-1):
        print(end=' ')
    for col in range(row):
        print('*',end=' ')
    print()
num=int(input("enter the number of rows you want::")) 
for row in range(1,num+1):
    for col in range(1,row+1):
        print("*",end=' ')
    print()
for row in range(num-1,0,-1):
    for col in range(row):
        print("*",end=' ')
    print()
string=input("enter the word")
length=len(string)
for row in range(length):
    for col in range(row+1):
        print(string[col],end="")
    print()
 

