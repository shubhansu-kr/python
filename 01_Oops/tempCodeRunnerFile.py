class First: 
    def __init__(self) -> None:
        super(First, self).__init__()
        print('Constructor First')
    def displayA(): 
        print("Instance Method First")

class Second: 
    def __init__(self) -> None:
        super(Second, self).__init__()
        print('Constructor Second')
    def displayC(): 
        print('Instance Second')

class THird(Second, First): 
    def __init__(self) -> None:
        super(THird, self).__init__()
        print("Constructor THird")
    def displayB():
        print("Instance Method THird")

# If the derived class does not have a constructor, the base class 
# constructor which is inherited by the derived class is called.
b = THird()

# IF both class has their own constructor, only derived class constructor 
# is called
# To call the constructor of base class super is used 

# Now to initialise the members of the class 

# Super init will call the init function of the first class and if the first
# arg class does not have any init function, it will look for another class 

