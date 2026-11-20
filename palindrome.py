def check(str):
    rev=""
    for i in str:
        rev = i + rev
    if rev==str:
        return print("Palindrome")
    else:
        return print("Not Palindrome")
check(input("Enter a String:"))
