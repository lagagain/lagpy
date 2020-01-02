from .Proxy import Proxy


class CallableMeta(type):
    """
    A MetaClass, and implement the method __call__ of Callable Class
    """
    def __call__(defineclz, *args, **kargs):
        """
        # Callable Class
        Accept a function and arguments(include keyword arguments)
        which will pass args to the function.
        You can get back the value by giving None replace function.
        """
        class __callableClass:
            def __call__(self, f = None, *args, **kargs):
                """
                Accept(function, *args, **kargs)
                it will return a new Callable object with
                function(*args, **args).

                if function is None, it just return result of function(*args, **args).
                """
                if f == None: return self
                result = f(self, *args, **kargs)
                return CallableWrapper.new(result)
        class __defineclz(defineclz, __callableClass):
            """just inherit __callableClass, but other behaviors are same as defineclz"""
            pass
        instance = __defineclz.__new__(__defineclz, *args, **kargs)
        __defineclz.__init__(instance, *args, **kargs)
        return instance


class Callable(metaclass = CallableMeta):
    """
    ```
    >>> class CallableList(list, Callable):
    ...     pass
    ...
    >>> l = CallableList([1,2,3,4,5,6])
    >>> l
    [1, 2, 3, 4, 5, 6]
    >>> l(sum)
    21
    >>>
    ```
    """
    pass

class CallableWrapper(Proxy, Callable):
    """
    Inherit Proxy and Callable, so using isinstance(obj, Proxy) or
    isinstance(obj, Callable) is posibile.

    This class will wrap the value you giving.  When it call, accept A
    function and other args, then it will put the wrap to first
    position and call function.  Last, it return result with
    CallableWrapper again.

    You can get the original wrap value using call with None replace
    function.

    ```
    >>> l = CallableWrapper([1,2,3,4,5,6])
    >>> l(sum)
    21
    >>> l = CallableWrapper.new([1,2,3,4,5,6])
    >>> l
    [1, 2, 3, 4, 5, 6]
    >>> l(sum)
    21
    >>>
    ```
    """
    def __init__(self, wrap, *args, **kargs):
        self.wrap = wrap
        super().__init__(wrap, *args, **kargs)
    def __call__(self, f=None, *args, **kargs):
        if f == None:
            return self.wrap
        result = f(self.wrap, *args, **kargs)
        __callable = CallableWrapper.__genClass(result)
        return __callable(result, *args, **kargs)
    @staticmethod
    def new(wrap, *args, **kargs):
        """
        The obj with using CallableWrapper.new are almost same like
        origianl itself, and only some type not, like None, NoneType, function....
        """
        __callable = CallableWrapper.__genClass(wrap)
        return __callable(wrap, *args, **kargs)
    @staticmethod
    def __genClass(wrap, *args, **kargs):
        try:
            class __callable(type(wrap), Callable):
                pass
            return __callable
        except TypeError as e:
            return CallableWrapper

if __name__ == "__main__":
    import doctest
    doctest.testmod()
