def reverse_string(str1): 
    rev_str=''
    index =len(str1) #4
    while index>0:
        rev_str=rev_str + str1[index-1]
        index=index-1
    return rev_str

print(reverse_string("1234abcd"))