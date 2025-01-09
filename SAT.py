def add(*args):
    a=0
    for i in args:
        a+=i
    return a

def subtract(a,b):
    return a - b

def tubmi(a):
    for i in range(2,a):
        if a%i==0:
            return False
    return True



def sqrt(a, b):
    """2ta son kiriting. \n1-sonni 2-sonidagi ildizini topib beradi"""
    ildiz = a**(1/b)
    return ildiz
    

def pow(a, b):
    return a**b

def floor(a):
    """Float son kiriting"""
    a=int(a)
    return a

def ceil(a):
    """Float son kiriting"""

    b = int(a)+1
    return a
print(subtract(6,3))