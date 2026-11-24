str=input("Enter a String:")
rev=""
for i in str:
    rev = i + rev
if rev==str:
    print("Palindrome")
else:
    print("Not Palindrome")
