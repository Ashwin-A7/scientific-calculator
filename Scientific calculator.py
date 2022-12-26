import math
while(True):
    print(" _______________________________")
    print("|        **CALCULATOR**       |")
    print("|                               |")
    print("|  1.ADD                        |")
    print("|  2.SUBTRACT                   |")
    print("|  3.MULTIPLY                   |")
    print("|  4.DIVIDE                     |")
    print("|  5.MOD                        |")
    print("|  6.SQUARE ROOT                |")
    print("|  7.EXPONENT                   |")
    print("|  8.SINE                       |")
    print("|  9.COSINE                     |")
    print("|  10.TANGENT                   |")
    print("|  11.CONVERT RADIAN TO DEGREE  |")
    print("|  12.CONVERT DEGREE TO RADIAN  |")
    print("|  13.EXIT                      |")
    print("|_______________________________|")
    opt=int(input("Please Enter The Number From Above Table: "))
    if(opt==1):
        print("ENTER TWO NUMBERS")
        a=int(input())
        b=int(input())
        print("ADDITION:-",(a+b))
    elif(opt==2):
        print("ENTER TWO NUMBERS")
        a=int(input())
        b=int(input())
        c=a-b
        print("SUBTRACTION:-",c)
    elif(opt==3):
        print("ENTER TWO NUMBERS")
        a=int(input())
        b=int(input())
        c=a*b
        print("MULTIPLICATION:-",c)
    elif(opt==4):
        print("ENTER TWO NUMBERS")
        a=int(input())
        b=int(input())
        c=a/b
        print("DIVISION:-",c)
    elif(opt==5):
        print("ENTER TWO NUMBERS")
        a=int(input())
        b=int(input())
        c=a%b
        print("MODULUS:-",c)
    elif(opt==6):
        print("ENTER THE NUMBERS")
        a=int(input())
        print("SQUARE ROOT:-",(math.sqrt(a)))
    elif(opt==7):
        a=int(input("ENTER THE BASE "))
        b=int(input("ENTER THE POWER "))
        print(a,"TO THE POWER OF",b,"=",(a**b))
    elif(opt==8):
        print("ENTER THE ANGLE")
        a=int(input())
        print("SINE OF",a,"=",(math.sin(a)))
    elif(opt==9):
        print("ENTER THE ANGLE")
        a=int(input())
        print("COSINE OF",a,"=",(math.cos(a)))
    elif(opt==10):
        print("ENTER THE ANGLE")
        a=int(input())
        print("TANGENT OF",a,"=",(math.tan(a)))
    elif(opt==11):
        print("ENTER THE ANGLE IN DEGREE")
        a=int(input())
        print("RADIAN =",(math.radians(a)))
    elif(opt==12):
        print("ENTER THE ANGLE IN RADIAN")
        a=int(input())
        print("DEGREE =",(math.degrees(a)))
    elif(opt==13):
        print("**THANK YOU FOR USING MY CALCULATOR**")
        break
    else:
        print("Invalid, Please Enter The opt Between 1-13")
