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
