def reverse(str):
    # str1=""
    # i=len(str)
    # while i!=0:
    #     str1=str1+str[i-1]
    #     i=i-1
    # return str1
    rev=""
    for i in str:
        rev=i+rev
    return rev

print(reverse(input("Enter a String:")))
# str=input("Enter a String")