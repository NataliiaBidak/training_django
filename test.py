for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
         print(n, 'is a prime number')

# >>> def f(ham: str, eggs: str = 'eggs') -> str:
# ...     print("Annotations:", f.__annotations__)
# ...     print("Arguments:", ham, eggs)
# ...     return ham + ' and ' + eggs
# ...
# >>> f('spam')
# Annotations: {'ham': <class 'str'>, 'return': <class 'str'>, 'eggs': <class 'str'>}
# Arguments: spam eggs
# 'spam and eggs'

class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

for cls in [B,C,D]:
    try:
        raise cls()
    except C:
        print("C")
    except D:
        print("D")
    except B:
        print("B")