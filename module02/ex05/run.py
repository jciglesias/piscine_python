from TinyStatistician import TinyStatistician
import numpy

tstat = TinyStatistician()
a = [1, 42, 300, 10, 59]
b = numpy.ndarray(5, dtype=int, buffer=numpy.array(a))
print(tstat.mean(a))
print(tstat.mean(b))
# Expected result: 82.4
print(tstat.median(a))
print(tstat.median(b))
# Expected result: 42.0
print(tstat.quartiles(a))
print(tstat.quartiles(b))
# Expected result: [10.0, 59.0]
print(tstat.var(a))
print(tstat.var(b))
# Expected result: 12279.439999999999
print(tstat.std(a))
print(tstat.std(b))
# Expected result: 110.81263465868862