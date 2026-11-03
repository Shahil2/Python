bal = 5000
password=1234
print("Welcome to Pentagon ATM \nInsert your Card")
card=int(input("Insert the Card\nPress 1.Yes 2.No\n"))
if card==1:
    pin = int(input("Enter the pin:"))
    if pin == password:
        lang = int(input("Select Language: 1.English 2.Malayalam 3.Hindi\n"))
        if lang==1:
            option = int(input("Select Option\n1.Balance\n2.Withdraw\n3.Exit\n"))
            if option == 1:
                print(f"Balance is : {bal}")
                print("Thanks for Visiting")
            elif option == 2:
                amount = int(input("Enter the Amount:"))
                if amount % 100 != 0:
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
            print("Select English only ")
    else:
        print("Wrong PIN \nTry again ")

else:
    print("Insert the card properly")

