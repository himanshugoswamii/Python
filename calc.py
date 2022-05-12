while True:
    print("1 is Addition")
    print("2 is Subraction")
    print("3 is Multiplication")
    print("4 is Division")
    print("5 is Remainder")
    print("6 is Exit")
    
    x=int(input("enter a number = "))
    y=int(input("enter a number = "))
    choice=int(input("Enter your choice = "))
    if choice==1:
        add= x+y
        print("the Addition is ",add)
    elif choice==2:
        sub= x-y
        print("the Subraction is ",sub)
    elif choice==3:
        mult= x*y
        print("the Multiplication is ",mult)
    elif choice==4:
        div= x/y
        print("the Division is ",div)
    elif choice==5:
        rem= x%y
        print("the Remainder is ",rem)
    elif choice==6:
        print("break")    
    else:
        print("Invalid Input")            
                