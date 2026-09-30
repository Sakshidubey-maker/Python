class Pro:
    # constructor-function inside the class
    def __init__(self):
        self.pin=""
        self.balance=0
        self.menu()


# constructor(special function)->superpower automatically called when an object is created
    def menu(self):
        user_input=input("hii how can i help you: "
                         "1.Press 1 to create pin\n"
                         "2.Press 2 to change pin\n"
                         "3.Press 3 to check balance\n"
                         "4.Press 4 to withdraw\n"
                         "5.Press 5 to deposit\n"
                         "6.Press 6 to exit\n")
        if user_input=='1':
            # create pin
            self.create_pin()
        elif user_input=='2':
            #  change pin
            pass
        elif user_input=='3':
            # check balance
            pass
        elif user_input=='4':   
            # withdraw
            pass
        elif user_input=='5':
            # deposit
            pass
        elif user_input=='6':
            exit()
        else:
            print("invalid input")
            self.menu()

    def create_pin(self):
        user_pin=input("enter your pin")
        self.pin=user_pin
        user_balance=int(input("enter balance"))
        self.balance=user_balance
        print("pin created successfully")      
  


obj=Pro()
# print(type(obj))
# print(obj.pin)
# print(obj.balance)2

