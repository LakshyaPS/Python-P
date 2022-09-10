num=int(input("enter the number of rows you want"))
for i in range(1,num+1):
    for j in range(num-i):
        print(end=' ')
    for j in range(i):
        print("*",end=' ')
    print()
for i in range(num-1,0,-1):
    for j in range(num-i,0,-1):
        print(end=' ')
    for j in range(i):
        print("*",end=' ')
    print()


'''
string=input("enter the word")
length=len(string)
for row in range(length):
    for col in range(row+1):
        print(string[col],end="")
    print()
'''
 
