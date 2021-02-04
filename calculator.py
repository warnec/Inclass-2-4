
#Colston Warne
#Inclass assignment 1


def add(x,y):
    result = x + y
    return result

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    if y == 0:
        print("The denominator can not be zero!")
        return None
    return x / float(y)

userX = input('Enter the first number: ')
userY = input('Enter the second number: ')
try:
    print("The numbers added = ", add(int(userX), int(userY)))
    print("The numbers subtracted = ", subtract(int(userX), int(userY)))
    print("The numbers multiplied = ", multiply(int(userX), int(userY)))
    print("The numbers divided = ", divide(float(userX), float(userY)))

except ValueError:
    print("You must enter integer values!")