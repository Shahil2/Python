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
    while option!=3:
        option=int(input("Select Option\n1.Balance\n2.Withdraw\n3.Exit\n" ))
        if option==1:
            print(f"Balance is : {bal}")
        elif option==2:
            amount = int(input("Enter the Amount:"))
            if bal<amount:
                print("Insufficent Balance")
                break
            bal = bal - amount
            print(f"Withdraw complete Balance {bal}")
        elif option==3:
            break
        else:
            print("Enter a valid option:")
else:
        print("Wrong PIN \nTry again ")

