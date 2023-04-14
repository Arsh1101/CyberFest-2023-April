from faker import Faker
# from faker.providers import internet


# arsh:run -> Arshia, you should run it during the explanation!
# PIP + Hello fakers!
fake = Faker()
# arsh:run
# print("FullName: " + fake.name() + "\n" + "Address: " + fake.address() + "\n" + "Text: " + fake.text())

# I want to do it 10 times!
# arsh:run
# print(list(range(10)))
# The list is a hard concept!
# A 'list' in Python is a list!
# Add, Remove, and etc
# Play with it! 
# arsh:run
'''
This could be documentation!
for index in range(10):
    # Thats a long print!
    # Lets have a variable
    theMessage = "FullName: " + fake.name() + "\n" + "Address: " + fake.address() + "\n" + "Text: " + fake.text()
    # arsh:run
    # print(index + "\n" + theMessage)

    # Ups! But Why!?
    # arsh:run
    # print(type(index))
    # print(type(theMessage))

    # cLass...!?
    # templates to help us explan the world we we need.

    # typs
    # In Python you can go crazy in types but try not get crazy a lot!
    # arsh:run
    # print(str(index) + ".\n" + theMessage + "\n" * 2)
    # Warning: What's going to happen if I mess with the spaces!?

    # If it's a even number I need a fake internet provicer!
    # Warning: It is not a good idea to add packages in the middle of the code.
    # arsh: run
    # from faker.providers import internet
    # fake.add_provider(internet)
    # theOtherMessage = fake.ipv4_private()
    # It is the most werid condition I have evere seen!
    # But you get the idea!
    # arsh:run
    # if (index % 2 == 0 and True) or False:
    #     print(index)
    #     print(theOtherMessage)
    # elif False or (True and index % 2 != 0):
    #     print(index)
    #     print(theMessage)
    # elif False:
    #     pass
    # else:
    #     print("You get the how condtions works right?")

    # Warning: It is not a good ide to define two variables!
    # Warning: It would be a good idea if you define each faker obj
    #   ("What is objec!?") into the condition.

    # ternary operator -> <3
    # arsh:run
    # print(theOtherMessage if index % 2 == 0 else theMessage)

    # Python 3.10
    # arsh: run
    # match index:
    #  case 1:
    #      print("The one!")
    #  case 2:
    #      print("The two!")
    #  case 3,4:
    #      print("What!?")
    #  case _:
    #     # Wow! '_' is so cool! Can I use it in 'for range'?
    #     print('Really!? What do you excpect!?')

    print()
'''


# PIP + Function + Python 3.10:
def createFakes_Fake(number=1):
    pass


def createFakes(number: int) -> str:
    result = ""
    for _ in range(number):
        # The scope, spaces...
        if number == 2:
            continue
        if number == 5:
            break
        result += fake.name() + "\n" + "Address: " + fake.address() + "\n" + fake.text() + "\n---\n"

    else:
        result += "Done!"
    return result

# arsh:run
# print(createFakes_Fake(1))
# print("!" * 6)
# What is 'None'!?

# arsh:run
# print(createFakes(3))
# arsh:run
# print(createFakes(2))
# arsh:run
# print(createFakes(5))

# Lambda (I stole this code from w3schools):
# arsh:run
# twice = lambda b : b * 2
# def myfunc(n):
#   return lambda a : a * n


# myDoubler = myfunc(2)
# print(twice(1))
# print(myDoubler(11))

# Not going to get deep in oop, iheritance, multi-inh, and etc
class NotGoingtoGetDeep:
    pass

# This code is here just to show some stuff!
# like Methods, Decorators, iheritance, __init__, *args, **kwargs. and etc
# *args -> Whats Tuple!?
t = (1,2,3)
# **kwargs -> Whasts Dictionary?
d = {1:"one", 2:"two", 3:"three"}

class MyStr(str):

    def __init__(self, *args, **kwargs):
        super(str, self).__init__(*args, **kwargs)
    

    def wowImMethod(self):
        pass

    # can access to all instances of the class
    @classmethod
    def wowImMethodToo(cls):
        pass


    @staticmethod
    def meToo():
        pass

'''
Decorator Example Developed By Dear ChatGPT:

def log_function(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} called with args={args} and kwargs={kwargs}")
        print(f"Result: {result}")
        return result
    return wrapper

@log_function
def add_numbers(a, b):
    return a + b

result = add_numbers(1, 2)
# Output: Function add_numbers called with args=(1, 2) and kwargs={}
#         Result: 3
'''

# use 'dir' to see whats happening in a class! (Not in a object!)
# the 'len'
# Thank you chatGPT:
#   __str__(self): This method is called when you use the str() function,
#  on an instance of a class, and should return a string representation of the object.
# arsh:run
# obj = NotGoingtoGetDeep()
# print(len(dir(obj)))
# print(dir(obj))
# print()
# obj = MyStr()
# print(len(dir(obj)))
# print(dir(obj))
# print()
# print(dir(obj).index("meToo"))
# print(dir(obj)[dir(obj).index("meToo")])

# lets do a little bit of faking before the end!
# Now we see the input to the __init__
fake = Faker(['it_IT', 'en_US', 'ja_JP'])
for _ in range(10):
    print(fake.name() + " - " + fake.address())