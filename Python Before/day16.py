#match case statement
x = int(input("Enter the value of x "))
match x:
    case 0:
        print("x is zero")
    
    case 4:
        print("x is four")
    
    case _ if x != 90:
        print(x, "x is not equal to 90")
    
    case _ if x != 80:
        print(x, "x is not equal to 90")
    case _:
        print(x)