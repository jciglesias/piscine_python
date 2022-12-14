def ft_reduce(function_to_apply, iterable):
    """Apply function of two arguments cumulatively.
    Args:
    function_to_apply: a function taking an iterable.
    iterable: an iterable object (list, tuple, iterator).
    Return:
    A value, of same type of elements in the iterable parameter.
    None if the iterable can not be used by the function.
    """
    try:
        tmp = iterable[0]
        for x in range(1, len(iterable), 1):
            tmp = function_to_apply(tmp, iterable[x])
        return tmp
    except Exception as e:
        return None