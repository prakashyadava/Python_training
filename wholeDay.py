# pyramid pattern 
a = int(input("Enter number of rows : "))
temp = a-1
for i in range(1,a+1):
    print(" "*(temp),'* '*i)
    temp -=1

s = "I am learning Python"


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

# Format
print("{:5d}".format(12))
print("{:2d}".format(1234))
print("{:8.3f}".format(12.2346))
print("{:05d}".format(12))
print("{:08.36}".format(18.2346))
print("{:^10.3f}".format(12.2346))
print("{:<05d}".format(12))
print("{:>08.3f}".format(12.2346))
print("{:=8.3f}".format(-12.2346))
print("Hello {} your balance is {}".format("Kapil",4563))

# Occurence count 
s = "I am learning python"
s_temp = s.lower()
temp_list = []
for i in range(len(s)):
    if s_temp[i] not in temp_list and s_temp[i]!=' ':
        temp_list.append(s_temp[i])
count = 0
for i in range(len(temp_list)):
    char_temp = temp_list[i]
    for j in range(len(s_temp)):
        if char_temp== s_temp[j]:
            count +=1
    print("Character {} occurs {} times in {}".format(char_temp,count,s))
    count =0    


# dictionary 
d = dict()
d.update({"apple":"red","banana":"yellow"})
print(d["apple"])
l1 = ["India","China","Srilanka"]
l2 = ["Pune","Beijing","Kolambo"]
new_dict = dict(list(zip(l1,l2)))
print(new_dict)

s1 = {1,2,3,4,5,6,7,8}
s2 = {3,4,5,6,7,8,9}
print("Union: ",s1.union(s2))
print("Difference: ",s1.difference(s2))
print("Symmetric Difference: ",s1.symmetric_difference(s2))
print("Intersection: ",s1.intersection(s2))
print("Union: ",s1|s2)
print("Deference: ",s1-s2)
print("Symmetric Difference: ",s1^s2)
print("Intersection: ",s1&s2)


def demo():
    return 2,(1,2,3),"Prakash"
a = demo()
print(a)

def upd_list(lst):
    lst.append(5)


samp_list = [1,2,3,4]
print(samp_list)
upd_list(samp_list)
print(samp_list)


# Factorial using recursion
def fact(n):
    if n==0:
        return 1
    return n* fact(n-1)
print(fact(3))
# Reversing string using recursion
def rev_str(org_str,temp_str,i):
    if i==0:
      
        return temp_str
    temp_str += org_str[i-1]
    i = i-1
    return rev_str(org_str,temp_str,i)
str1 = "Prakash"
str2 = ""
print(rev_str(str1,str2,len(str1)))

l = [1,2,3,4]
l = list(map(lambda x:x**3,l))
print(l)
l = list(filter(lambda x: x%2==0,l))

# file handling
f = open("demo.txt","w")
f.write("This is demo file \n")
f.write("Second line \n")
f.close
with open("demo.txt","a+") as f:
    # line = f.readline()
    # line = f.read()
    # line = f.read(10)
    f.seek(0,0)
    line = f.readlines()
    f.write("Third line\n")
    print(line)
    f.close

f = open("new_demo.txt","w")
for i in range(1,11):
    s = "Hi this is "+str(i)+" line \n"
    f.write(s)
f.close

with open("new_demo.txt","r")as f:
    # f.seek(0,0)
    line = f.readlines()
    # print(line)
    line[3] = "This is new 4 line\n"
    with open("new_demo.txt","w") as fr:
        fr.writelines(line)
        fr.close
    f.close

    
    

