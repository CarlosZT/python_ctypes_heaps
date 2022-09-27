from cProfile import label
from os import getcwd
from ctypes import c_int, CDLL, POINTER

import numpy as np
import matplotlib.pyplot as plt
import timeit




#Heap Class
class Heap():
    #Constructor/Initializer. It gets the size of the array to represent the tree (Default is 3)
    def __init__(self, size=3) -> None:
        #Set the path for the library
        path = getcwd() + "\\Heap Class\\heap.so"
        path = path.replace('\\', '/')

        #Load the heap.c library and define the argument types por each function
        self.libc = CDLL(path)
        self.libc.insert.argtypes = [POINTER(c_int), c_int, c_int]
        self.libc.delete_first.argtypes = [POINTER(c_int), POINTER(c_int)]
        self.libc.heapsort.argtypes = [POINTER(c_int), c_int]
        self.libc.reverse.argtypes = [POINTER(c_int), c_int]

        #Creates the array (C array of int) and initialize the element counter value
        d = []*(size+1)
        self.heap = (c_int * (size + 1))(*d)
        self.reserved = size
        self.size = 0
        self.e_count = c_int(0)

        self.queue_mode = 'max_first'
        
        #Execute the insertion operation, only if there's an element within the array and this one is not full
    def insert(self, element:int):
        if self.size < self.reserved:
            self.size += 1
            self.e_count.value = self.size
            self.libc.insert(self.heap, c_int(element), self.e_count)
        else:
            print('Couldn\'t insert element. Heap is full.')

        #Execute the heap sort algorithm
    def heapsort(self):
        if self.size > 2:
            self.libc.heapsort(self.heap, c_int(self.size), self.e_count)

        
        #Delete the root (max value) of the tree
    def delete_first(self):
        if self.size > 0:
            self.libc.delete_first(self.heap, self.e_count)

        self.size = self.e_count.value


    def priority_queue(self, type='max_first'):
        """
        Input
        type: String.
        'max_first' will bring to top the largest values.
        'min_first' will bring to top the smallest values.
        """

        if type != 'min_first' and type != 'max_first':
            print("Queue mode not allowed")
            return

        
        if self.size > 2:
            self.libc.heapsort(self.heap, self.e_count)

        if  type == 'min_first':
            self.queue_mode = type
        elif type== 'max_first':
            self.queue_mode = type
            self.libc.reverse(self.heap, self.e_count)

    def queue_next(self):
        if self.size > 0:
            self.libc.delete_first(self.heap, self.e_count)
            
            self.size = self.e_count.value
            if self.queue_mode=='min_first':
                
                self.libc.heapsort(self.heap, self.e_count)

        else:
            print("Needed any element in queue")


# #Size of the input 
# size = 10

# #Create a new object of the Heap class
# myheap = Heap(size)

# #Creating elements
# elements = np.arange(1, size + 1, 1)

def insert_h(myheap, elements):
    #Inserting elements
    print(elements.shape)
    for e in elements:
        myheap.insert(e)

def queue_mngr(myheap):
    myheap.queue_next()



n_exec = 1
y_ins = []
y_que = []
x = []

for i in range(6):
    size = 10**i
    x.append(size)
    elements = np.arange(1, size + 1, 1)
    myheap = Heap(size)

    result_ins = timeit.timeit(stmt='insert_h(myheap, elements)', globals=globals(), number=n_exec)
    ins_time = result_ins/n_exec
    #print(f'Heap insert: {ins_time}')
    y_ins.append(ins_time)
    print(ins_time)
    
    myheap.priority_queue('min_first')

    result_que_min = timeit.timeit(stmt='queue_mngr(myheap)', globals=globals(), number=n_exec)
    que_min_time = result_que_min/n_exec
    #print(f'Queue: {que_min_time}')
    y_que.append(que_min_time)

    

plt.title(f'Heaps')
plt.plot(x, y_ins, label='Insertion')
plt.plot(x, y_que, label='Priority Queues')
plt.xlabel('Input (n)')
plt.ylabel('Approx. time (s)')
plt.xscale('log')
plt.legend(loc='best')
plt.show()

    