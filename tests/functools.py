import unittest
from lagpy.functools.Proxy import Proxy
from lagpy.functools.Callable import CallableMeta, CallableWrapper, Callable

class TestProxy(unittest.TestCase):
    def testInt(self):
        for i in range(-10, 10):
            self.assertEqual(Proxy(i), i)
            self.assertEqual(Proxy(i + 5), i + 5)
            self.assertEqual(Proxy(i - 5), i - 5)
            self.assertEqual(Proxy(i / 2), i / 2)
            self.assertEqual(Proxy(i * 10), i * 10)


class TestCallableMeta(unittest.TestCase):
    pass

class TestCallable(unittest.TestCase):
    def testInherited(self):
        self.assertTrue(issubclass(CallableWrapper, Callable))
        self.assertTrue(isinstance(CallableWrapper(1), Callable)) # int
        self.assertTrue(isinstance(CallableWrapper(1.0), Callable)) # float
        self.assertTrue(isinstance(CallableWrapper("hello"), Callable)) # string
        self.assertTrue(isinstance(CallableWrapper(True), Callable)) # bool
        self.assertTrue(isinstance(CallableWrapper([1,2,3,4]), Callable)) # list
        self.assertTrue(isinstance(CallableWrapper((1,2,3,4,)), Callable)) # tuple
        self.assertTrue(isinstance(CallableWrapper({1,2,3,4,5,}), Callable)) # set
        self.assertTrue(isinstance(CallableWrapper({1:1,2:2,3:3,4:4,}), Callable)) # dict
        self.assertTrue(isinstance(CallableWrapper(None), Callable)) # None
        self.assertTrue(isinstance(CallableWrapper(lambda :None), Callable)) # function
        self.assertTrue(isinstance(CallableWrapper(type), Callable)) # type
        ### CallableWrapper.new
        self.assertTrue(isinstance(CallableWrapper.new(1), Callable)) # int
        self.assertTrue(isinstance(CallableWrapper.new(1.0), Callable)) # float
        self.assertTrue(isinstance(CallableWrapper.new("hello"), Callable)) # string
        self.assertTrue(isinstance(CallableWrapper.new(True), Callable)) # bool
        self.assertTrue(isinstance(CallableWrapper.new([1,2,3,4]), Callable)) # list
        self.assertTrue(isinstance(CallableWrapper.new((1,2,3,4,)), Callable)) # tuple
        self.assertTrue(isinstance(CallableWrapper.new({1,2,3,4,5,}), Callable)) # set
        self.assertTrue(isinstance(CallableWrapper.new({1:1,2:2,3:3,4:4,}), Callable)) # dict
        self.assertTrue(isinstance(CallableWrapper.new(None), Callable)) # None
        self.assertTrue(isinstance(CallableWrapper.new(lambda :None), Callable)) # function
        # self.assertTrue(isinstance(CallableWrapper.new(int), Callable)) # type


class TestCallableWrapper(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
