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
