import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        av = sys.argv
        av.reverse()
        av.pop()
        av = [x for x in av if x != '']
        for i in range(len(av)):
            av[i] = av[i][::-1].swapcase()
        print(*av)
    else:
        print("Usage: python3 exec.py <Arg> ...")