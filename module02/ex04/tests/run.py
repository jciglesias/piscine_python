import my_minipack.logger
import my_minipack.loading
import time

if __name__ == "__main__":
    machine = my_minipack.logger.CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()
    machine.make_coffee()
    machine.add_water(70)
    tmp = range(100, 200)
    ret = 0;
    for i in my_minipack.loading.ft_progress(tmp):
        ret += (i + 3) % 5;
        time.sleep(0.01);
    print();
    print(ret);