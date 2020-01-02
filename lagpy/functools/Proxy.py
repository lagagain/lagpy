import operator

class ProxyOptException:
    def __init__(self, opt:str):
        self.opt = opt
    def __str__(self):
        return "<ProxyOptException Can't find {} operator>".format(self.opt)

class Proxy:
    __handler = None
    def __init__(self, handler:object):
        self.__handler = handler
    @classmethod
    def Cproxy(clz, opt:str, default_handler = None):
        def _handler(self, *args, **kwargs):
            handler = getattr(self.__handler, opt, default_handler if default_handler else clz.__defaultOpt)
            return handler(*args, **kwargs)
        return _handler
    def __defaultOpt(self, opt:str, *args, **kwargs):
        raise ProxyOptException(opt)

for opt in operator.__dict__.keys():
    if opt in ["__name__"]:continue
    setattr(Proxy, opt, Proxy.Cproxy(opt))
