# Alphabets pattern 
inp = int(input("Enter the number of rows: "))
cnt = 65
temp2 = inp-1
for i in range(1,inp+1):
    print(" "*(temp2),end="")
    for j in range(0,i):
        print(chr(cnt),end=" ")
        cnt+=1
    print()
    temp2 -=1
