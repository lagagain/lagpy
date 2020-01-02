from .Proxy import Proxy


class CallableMeta(type):
    def __call__(defineclz, *args, **kargs):
        class __callableClass:
            def __call__(self, f = None, *args, **kargs):
                if f == None: return self
                result = f(self, *args, **kargs)
                return CallableWrapper.new(result)
        class __defineclz(defineclz, __callableClass):
            pass
        instance = __defineclz.__new__(__defineclz, *args, **kargs)
        __defineclz.__init__(instance, *args, **kargs)
        return instance


class Callable(metaclass = CallableMeta):
    pass

class CallableWrapper(Proxy, Callable):
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



''' Example
class CallableList(list, Callable):
    def hello(self):
        print("Hello World")
'''
