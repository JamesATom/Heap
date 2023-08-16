# import random number generator
from random import randrange
# import heap class
from min_heap import MinHeap 

# make an instance of MinHeap
min_heap = MinHeap()

# populate min_heap with descending numbers
descending_nums = [n for n in range(10001, 1, -1)]
print("ADDING!")
for el in descending_nums:
  min_heap.add(el)

print("REMOVING!")
# remove minimum until min_heap is empty
min_heap.retrieve_min()


# import heap class
# from min_heap import MinHeap 

# # make an instance of MinHeap
# min_heap = MinHeap()

# # set internal list for testing purposes...
# min_heap.heap_list = [None, 10, 13, 21, 61, 22, 23, 99]
# min_heap.count = 7

# while len(min_heap.heap_list) != 1:
#   print(min_heap.heap_list)
#   min_heap.retrieve_min()
