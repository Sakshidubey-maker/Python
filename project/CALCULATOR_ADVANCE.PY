num1=float(input("enter first no: "))
op=input("enter operator: ")
num2=float(input("enter second no: "))

if op=="+":
    print(num1 + num2)
elif op=="-":
    print(num1 - num2)
elif op=="*":
    print(num1 * num2)
elif op=="/":
    print(num1 / num2)
else:
    print("invalid operator")