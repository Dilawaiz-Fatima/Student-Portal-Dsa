import datetime

class Events:
    def __init__(self, work, enddate):
        self.startdate="Date : "+ str(datetime.datetime.now())
        self.obj =work
        self.enddate = enddate
class que:
    def __init__(self,capacity):
        self.front = self.rear = 0
        self.capacity = capacity
        self._queue = _queue = [(self.capacity)]
    def queueEnqueue(self, data):
        # check queue is full or not
        if self.capacity == self.rear:
            print("\n\t\t\t5 Events Are Going Already, No More Events Can Be Added \n")
            return
        # insert element at the rear
        else:
            self._queue[self.rear] = data
            self.rear += 1
        return
    def queueDequeue(self):
        # if queue is empty
        if self.front == self.rear:
            print("\nNo Events Entered To Remove \n")
            return
        # shift all the elements from index 2 till rear
        # to the right by one
        else:
            i = 0
            while i < self.rear - 1:
                self._queue[i] = self._queue[i + 1]
                i += 1
            if (self.rear < self.capacity):
                self._queue[i] = 0 
            # decrement rear
            self.rear -= 1
    def queueDisplay(self):
        if self.front == self.rear:
            print("\nNo Events To Show\n")
            return
        # traverse front to rear and print elements
        i = self.front
        while i < self.rear:
            print(" Event : "+ self._queue[i].obj)
            print("Added on : "+self._queue[i].startdate)
            print("Deadline : "+self._queue[i].enddate)
            i += 1
    def queueFront(self):
        if self.front == self.rear:
            print("\nNo Event To Show\n")
            return
        print(" Event : "+ self._queue[self.front].obj)
        print("Added on : "+self._queue[self.front].startdate)
        print("Deadline : "+self._queue[self.front].enddate)