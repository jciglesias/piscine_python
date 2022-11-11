import time, timeit

def ft_progress(listy: range):
    total = len(listy)#abs(int((listy.stop - listy.start) / listy.step));
    exce_time = timeit.default_timer();
    for i in range(total):
        p = i / total;
        bar = int(p * 100 / 5)
        print(" " * 100, end = "\r", flush = True);
        print("ETA: {:.2f}s [{:3d}%][{:}{:}{:}] {:}/{:} | elapsed time {:.2f}s".format( total * (timeit.default_timer() - exce_time) / (i + 1), int(p * 100), '=' * bar, ">", " " * (19 - bar), i, total, timeit.default_timer() - exce_time), end = "\r", flush = True);
        yield listy[i];
    print("ETA: {:.2f}s [{:}%][{:}] {:}/{:} | elapsed time {:.2f}s".format(timeit.default_timer() - exce_time, 100, "=" * 20, i + 1, total, timeit.default_timer() - exce_time), end = "", flush = True);

if __name__=="__main__":
    tmp = range(100, 200)
    ret = 0;
    for i in ft_progress(tmp):
        ret += (i + 3) % 5;
        time.sleep(0.01);
    print();
    print(ret);