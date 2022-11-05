# try:
#     print("try block")
#     num1=int(input("Enter the first number:"))
#     num2=int(input("Enter the second number:"))
#     res =num1/num2
# except:
#     print("Except block")
#     print("Number1 is not divisible by zero")
# else:
#     print("Else block")
#     print("output  ",res)

# finally:
#     print("Exceptional handling program")

#-----------------------------------------------------------------

try:
    a=int(input("Enter Your age:"))
    if a<18:
         raise ValueError(a)
except ValueError:
    print(a,"is less than 18")
else:
    print(a,"is allowed")