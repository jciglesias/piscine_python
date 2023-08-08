from functools import reduce
from ft_reduce import ft_reduce
from ft_map import ft_map
from ft_filter import ft_filter

x = [1, 2, 3, 4, 5]
print("Example1\nft:  ", ft_map(lambda dum: dum + 1, x))
print("std: ", map(lambda dum: dum + 1, x))
# Output:
# <generator object ft_map at 0x7f708faab7b0> # The adress will be different
print("ft:  ", list(ft_map(lambda t: t + 1, x)))
print("std: ", list(map(lambda t: t + 1, x)))
# Output:
# [2, 3, 4, 5, 6]
# Example 2:
print("\nExample2\nft:  ", ft_filter(lambda dum: not (dum % 2), x))
print("std: ", filter(lambda dum: not (dum % 2), x))
# Output:
# <generator object ft_filter at 0x7f709c777d00> # The adress will be different
print("ft:  ", list(ft_filter(lambda dum: not (dum % 2), x)))
print("std: ", list(filter(lambda dum: not (dum % 2), x)))
# Output:
# [2, 4]
# Example 3:
lst = ['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
print("\nExample3\nft:  ", ft_reduce(lambda u, v: u + v, lst))
print("std: ", reduce(lambda u, v: u + v, lst))
# Output:
# "Hello world"

function = lambda x: x + 1
iterable = [1, 2, 3]
print(ft_map(function_to_apply = None, iterable = iterable))
#  Should print "< generator object at hexa_adress>" 
print(list(ft_map(function_to_apply = None, iterable = iterable)))

# Error