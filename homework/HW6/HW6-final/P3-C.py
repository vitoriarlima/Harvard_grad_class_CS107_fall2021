import matplotlib.pyplot as plt
from P3 import NaivePriorityQueue, HeapPriorityQueue, PythonHeapPriorityQueue, timeit

ns=(10, 20, 50, 100, 200, 500)


import matplotlib.pyplot as plt
plt.figure(figsize=(7,7))
plt.title("Plot of performance comparison between three priority queues implementations")
plt.plot(ns, timeit(pqclass = NaivePriorityQueue), label = 'Naive priority queue')
plt.plot(ns, timeit(pqclass = HeapPriorityQueue), label = 'Heap priority queue')
plt.plot(ns, timeit(pqclass = PythonHeapPriorityQueue), label = 'Python Heap priority queue')
plt.xlabel("Number of Lists Merged (ranges from 0 to 500)")
plt.ylabel("Elapsed time in seconds")
plt.legend()
plt.draw()
plt.savefig('P3-C.png')
plt.show()

