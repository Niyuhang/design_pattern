def foo(a):
    print(a)
    return 3

print(foo(3))
def foo2(a, b):
    print(a, b)
from unittest import mock

foo = mock.Mock(side_effect=foo2)
print(foo(20, 30))
