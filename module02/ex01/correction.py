from main import what_are_the_vars, doom_printer

obj = what_are_the_vars(None)
doom_printer(obj)
# var_0: None
# end
obj = what_are_the_vars(lambda x: x, function=what_are_the_vars)
doom_printer(obj)
# function: <function what_are_the_vars at 0x...>
# var_0: <function <lambda> at 0x...>
# end
obj = what_are_the_vars(3, var_0=2)
doom_printer(obj)
# ERROR
# end