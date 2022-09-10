num=5
for row in range(num,0,-1):
    print()
    for col in range(0,num-row):
        print(end=" ")
        for col in range(row,0,-1):
            print("*",end="")
            
