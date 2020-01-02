from .Callable import CallableWrapper

class Environment:
    """
    >>> def puts(s:str, *args, **kwargs):
    ...     print(s, *args, **kwargs)
    ...     return s
    >>>
    >>> Env = Environment # alias
    >>> env = Env()
    >>> # env(puts,"Hello", end="") \
    >>> # (puts, 'World.') # Output: Hello, World
    >>>
    >>> ###########
    >>> env.get("a", 100)
    100
    >>> env.set("a", [1,2,3,4,5,6])
    [1, 2, 3, 4, 5, 6]
    >>> env.a
    [1, 2, 3, 4, 5, 6]
    >>> env.get("a")(sum)
    21
    >>> env["a"](sum)
    21
    >>> ###########
    >>> env.set("get", 100)
    100
    >>> env.get
    100
    >>> #env.get("a", 100) # can't
    >>>
    """
    def __getitem__(self, key:str):
        return self.__getattr__(key)

    def __setitem__(self, key:str, value):
        setattr(self, key, value)
        return CallableWrapper.new(value)

    def __getattr__(self, key: str, default = None):
        if key in self.__dict__: return CallableWrapper.new(self.__dict__[key])
        else: return CallableWrapper.new(default)

    def get(self, key, default = None):
        return self.__getattr__(key, default)

    def set(self, key, value):
        setattr(self, key, value)
        return CallableWrapper.new(value)

    def set_(self, value, key:str):
        return self.set(key, value)

    def __call__(env, f,  *args, **kwargs):
        f(env, *args, **kwargs)
        return env

    @staticmethod
    def WrapFun(f, *args, **kwargs):
        def _f(env,*args, **kwargs):
            return f(*args, **kwargs)
        return _f

if __name__ == "__main__":
    import doctest
    doctest.testmod()
