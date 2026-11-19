str=input("Enter a String:")
str1=""
for i in str:
    if i not in str1:
       str1= str1+i
print(str1)
# for i in str:
#     if i in str1:
#         pass
#     else:
#        str1= str1+i
# print(str1)