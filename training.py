# decorator use for authentication. symbol is @
# def user_is_authenticated():    # This is a placeholder function. In a real application, this would check the user's authentication status.
#     return True





# decorator is a function that takes another function as an argument, and extends the behavior of the latter function without explicitly modifying it.
# def authenticated(func):
#     def wrapper(*args, **kwargs):
#         if not user_is_authenticated():
#             raise Exception("User is not authenticated")
#         return func(*args, **kwargs)
#     return wrapper
def my_decorator(func):
    def wrapper():
        print("Before the function is called.")
        func()
        print("After the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")
    print("Welcome to the world of decorators.")
    
say_hello()
# generator is a function that returns an iterator that produces a sequence of values when iterated over. It allows you to create iterators in a more concise and memory-efficient way compared to using classes with __iter__ and __next__ methods.
# generator is a function that returns value one at a time using yield
def count_up(n):
    for i in range(n):
        yield i 
        
for number in count_up(5):
    print(number)

# lazy iterator ,memory efficient

# list comprehension
# a short and powerful way to create list in one line instead of writing loops ,we write everythings in a single line
number=[]
for i in range(5):
    number.append(i)
print(number)
# even no
odd=[i for i in range(10) if i%2!=0]
print(odd)

#   Q.NO1: price discount 10% discount
prices=[100,200,300]

#   Q.NO2: extract vowel from string
# SLICING
string="hello world"




