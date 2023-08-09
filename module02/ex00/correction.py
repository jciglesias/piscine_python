from functools import reduce
from ft_reduce import ft_reduce
from ft_map import ft_map
from ft_filter import ft_filter

function = lambda x: x + 1
iterable = [1, 2, 3]
print(f"{ft_map(function_to_apply = None, iterable = iterable)}")
#  Should print "< generator object at hexa_adress>" 
try:
    print(f"{list(ft_map(function_to_apply = None, iterable = iterable))}")
except Exception as e:
    print(e)
# Error

print(f"{ft_filter(function_to_apply = None, iterable = iterable)}")
# Should print < generator object at hexa_adress>

try:
    list(ft_filter(function_to_apply = None, iterable = iterable))
except Exception as e:
    print(e)

try:
    ft_reduce(None, iterable = iterable)
except Exception as e:
    print(e)
try:
    ft_reduce(function, None)
except Exception as e:
    print(e)
print(list(ft_map(lambda x: x + 2, [])))
# you should get [].
print(list(ft_map(lambda x: x + 2, [1])))
# you should get [3].
print(list(ft_map(lambda x: x ** 2, [1, 2, 3, 4, 5])))
# you should get [1, 4, 9, 16, 25].)
print(list(ft_filter(lambda x: x <= 1, [])))
# you should get [].
print(ft_reduce((lambda x, y: x + y), [1]))
# you should get 1.
print(ft_reduce((lambda x, y: x * y), [1, 2, 3, 4]))
# you should get 24.