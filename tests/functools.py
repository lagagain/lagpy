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
    pass

class TestCallableWrapper(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
