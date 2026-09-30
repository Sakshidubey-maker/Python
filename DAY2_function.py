def say_hii():
    # name=input("name: ")
    print("Hii user !")
# CALL FUNCTION
print("Hope u r doing great !")
say_hii()
print("best wishes!!")

# with parameter
def say_hello(name,age):
    print("hello "+name+" your age is "+str(age))
say_hello("SHYAM",35)
say_hello("hridaya",45)

# using return in function
def cube(num):
    return num*num*num
# print(cube(4))
result=cube(4)
print(result)