"""
Math 560
Project 2
Fall 2020

p2queue.py

Partner 1:Ke Chen
Partner 2:Xunyu Chu
Date:
"""

"""
Queue Class
"""
class Queue:

    """
    Class attributes:
    queue    # The array for the queue.
    front    # The index of the front of the queue.
    rear     # The index ONE PAST the rear of the queue.
    numElems # The number of elements in the queue.
    """

    """
    __init__ function to initialize the Queue.
    Note: intially the size of the queue defaults to 3.
    Note: the queue is initally filled with None values.
    """
    def __init__(self, size=3):
        self.queue = [None for x in range(0,size)]
        self.front = 0
        self.rear = 0
        self.numElems = 0
        return

    """
    __repr__ function to print the stack.
    """
    def __repr__(self):
        s = '[ ' + ', '.join(map(str, self.queue)) + ' ]\n'
        s += ('Front: %d' % self.front) + '\n'
        s += ('Rear: %d' % self.rear) + '\n'
        s += ('numElems: %d' % self.numElems) + '\n'
        return s

    """
    isFull function to check if the queue is full.
    Queue is full when numElems is equal or bigger than length of queue
    """
    def isFull(self):
        ##### IMPLEMENT! #####
        return self.numElems >= len(self.queue)

    """
    isEmpty function to check if the queue is empty.
    Queue is empty when numElems is 0
    """
    def isEmpty(self):
        ##### IMPLEMENT! #####
        return self.numElems == 0

    """
    resize function to resize the queue by doubling its size.
    Note: we also reset the front to index 0.
    """
    def resize(self):
        ##### IMPLEMENT! #####
        temp = self.queue
        #consider the case that rear is bigger than front
        self.queue = [None for x in range(0, 2*len(temp))]
        if(self.rear > self.front) :
            self.queue[0: self.numElems] = \
                temp[self.front : self.front + self.numElems]    
            #mark self.queue[0:0]
        else:
            #consider the case that rear is smaller than front
            #copy the elements which originally behind front to new queue
            self.queue[0:len(temp) - self.front] = \
                temp[self.front : len(temp)]
            self.queue[len(temp) - self.front : \
                       len(temp) - self.front + self.rear] = temp[0 : self.rear]
        self.front = 0
        self.rear = self.numElems
        return

    """
    push function to push a value into the rear of the queue.
    """
    def push(self, val):
        ##### IMPLEMENT! #####
        #verify the case that queue is not full
        if(self.isFull()):
            self.resize()
            #push
        self.queue[self.rear] = val
        self.rear = (self.rear + 1) % len(self.queue)
        self.numElems += 1
        return

    """
    pop function to pop the value from the front of the queue.
    """
    def pop(self):
        ##### IMPLEMENT! #####
        #verify the case queue is not empty
        if(self.isEmpty()):
            return None
        #pop
        temp = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % len(self.queue)
        self.numElems -= 1
        return temp

# a = Queue(4)
# for i in range(0,4):
#     a.push(i)
# print(a.__repr__())
# a.pop()
# a.pop()
# a.push(5)
# a.push(6)
# a.push(7)
# print(a.__repr__())
# for i in range(0,a.numElems):
#     print(a.pop())
