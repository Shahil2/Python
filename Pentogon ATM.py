print("Welcome to Pentagon ATM \nInsert your Card")
pin = int(input("Enter the pin:"))
bal=5000
option=0

if pin==1234:
    print("Select Language:")
    print("1.English")
    print("2.Malayalam")
    print("3.Hindi")
    lang=int(input())
    option=int(input("Select Option\n1.Balance\n2.Withdraw\n3.Exit\n" ))
    if option==1:
        print(f"Balance is : {bal}")
        print("Thanks for Visiting")
    elif option==2:
        amount = int(input("Enter the Amount:"))
        if amount % 500 != 0:
            print("Error: Amount must be in multiples of 500 (e.g., 500, 1000, 1500).")
        elif bal < amount:
            print("Insufficient Balance")
        else:
            bal = bal - amount
            print(f"Withdraw complete. Remaining Balance: {bal}")
            print("Thanks for Visiting")
    else:
        print("Enter a valid option:")
else:
        print("Wrong PIN \nTry again ")

