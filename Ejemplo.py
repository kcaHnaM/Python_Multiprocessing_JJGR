# 

import multiprocessing
import random
import time

class Producer(multiprocessing.Process):

    def __init__(self, queue):
        multiprocessing.Process.__init__(self)
        self.queue = queue

    def run(self):
        for i in range(10):
            item = random.randint(0, 256)
            self.queue.put(item)
            print("Proceso Productor : item %d agregado a la cola %s" % (item, self.name))
            time.sleep(1)
            print("El tamaño de la cola es %s" % self.queue.qsize())

class Consumer(multiprocessing.Process):

    def __init__(self, queue):
        multiprocessing.Process.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            if (self.queue.empty()):
                print("La cola está vacía")
                break
            else:
                time.sleep(2)
                item = self.queue.get()
                print("Proceso Consumidor : item %d quitado de la cola %s" % (item, self.name))
                time.sleep(1)
                print("El tamaño de la cola es %s" % self.queue.qsize())

if __name__ == '__main__':

    queue = multiprocessing.Queue()
    
    process_producer = Producer(queue)
    process_consumer = Consumer(queue)

    process_producer.start()
    process_consumer.start()

    process_producer.join()
    process_consumer.join()