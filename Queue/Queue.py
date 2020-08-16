class Queue:
    
    #Creating the queue
    def __init__(self):
        self.queue = list()
      
    #Enqueue
    def addToQueue(self, data):
        if data not in self.queue:
            self.queue.insert(0 ,data)
            return True
        else:
            return False
    
    #Dequeue
    def removeFromQueue(self):
        if len(self.queue) > 0:
            return self.queue.pop()
        return ("No elemenst in the queue")
    
    #Determining the size of the queue
    def size(self):
        return len(self.queue)
    
TheQueue = Queue()
TheQueue.addToQueue(3)
TheQueue.addToQueue(9)
TheQueue.addToQueue(6)
TheQueue.addToQueue(20)

print(TheQueue.size())
