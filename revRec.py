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
