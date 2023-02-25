while(True):
    print("Welcome to MyCalculator")
    print("\n\nSelect an option to perform operation")
    print("\n1:Addition")
    print("2:Subtraction")
    print("3:Multiplication")
    print("4:Divison")
    print("5:Exit")

    c=input("Enter your choice :")

    if (c=="1"):
        x=float(input("Enter a number :"))
        y=float(input("Enter a number :"))
        print(f"\n\n{x}+{y}={x+y}")
        print("\n\n=====================================")

    elif(c=="2"):
        x=float(input("Enter a number :"))
        y=float(input("Enter a number :"))
        print(f"\n\n{x}-{y}={x-y}")
        print("\n\n=====================================")

    elif(c=="3"):
        x=float(input("Enter a number :"))
        y=float(input("Enter a number :"))
        print(f"\n\n{x}*{y}={x*y}")
        print("\n\n=====================================")

    elif(c=="4"):
        x=float(input("Enter a number :"))
        y=float(input("Enter a number :"))
        print(f"\n\n{x}/{y}={x/y}")
        print("\n\n=====================================")

    elif(c=="5"):
        con=input("Do you want to Exit Y/N :")
        if (con.lower()=="y"):
            break
        elif (con.lower()=="n"):
            continue
        else :
            print("Invalid input")

input("press<enter> to close")

        
            
