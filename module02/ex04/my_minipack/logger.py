import time
from random import randint
import os

def log(fn):
    def inner(*args, **kwargs):
        action = {
            "start_machine": "Start Machine",
            "boil_water": "Boil Water",
            "make_coffee": "Make Coffee",
            "add_water": "Add Water"
        }
        init_time = time.perf_counter_ns()
        ret = fn(*args, **kwargs)
        exec_time = (time.perf_counter_ns() - init_time) / 1000000
        time_mesure = "s" if exec_time > 999 else "ms"
        if exec_time > 999: exec_time = exec_time / 1000
        fs = open("machine.log", "a")
        fs.write('({})Running: {:19}[ exec-time = {:.3f} {} ]\n'.format(os.environ["USER"], action[fn.__name__], exec_time, time_mesure))
        fs.close()
        return ret
    return inner

class CoffeeMachine():
    
    water_level = 100
    
    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
        return False
    
    @log
    def boil_water(self):
        return "boiling..."
    
    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")
    
    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")