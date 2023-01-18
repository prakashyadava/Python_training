# pyramid pattern 
a = int(input("Enter number of rows : "))
temp = a-1
for i in range(1,a+1):
    print(" "*(temp),'* '*i)
    temp -=1
