str=input("Enter a string:")
print(str)
if str.isalpha():
    print("Only Alphabet")

elif str.isdigit():
    print("Only Numbers")

elif str.isalnum():
    print("Both")
else:
    print("Other Characters")