def GlobalVar(name: str, val = None):
    globals()[name] = val
    return val

def Void(*expr, **kexpr):
    """
    >>> name = "World"
    >>> hello = lambda name: print("Hello, " + str(name))
    >>> def puts(s:str, *args, **kwargs):
    ...     print(s, *args, **kwargs)
    ...     return s
    >>>
    >>> Void(name) # => None
    >>> Void(hello(name)) # => None.  Output: "Hello, World"
    Hello, World
    >>>

    或是

    >>> Void(
    ...     puts("Hello, ", end=""),
    ...     puts("World.")
    ...    ) # => None.  Output: Hello, World.
    Hello, World.
    >>> Void(
    ...    step_1 = puts("Hello, ", end=""),
    ...    step_2 = puts("World")
    ... ) # => None.  Output: Hello, World.
    Hello, World
    >>>
    """
    return None

def Progn(*expr):
    '''
    >>> Progn(print("Hello, ", end=""),
    ...       print("World."),
    ...       "Hello, World")
    Hello, World.
    'Hello, World'
    >>>
    '''
    if expr: return expr[-1]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
