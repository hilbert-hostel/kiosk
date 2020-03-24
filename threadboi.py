from threading import *

class Td(Thread):
    def setAction(self,action):
        self.action = action
    def run(self):
        self.action()
'''
def lol():
    for x in range(5):
        print("Yeah boi by",current_thread().getName())

t1 = Td()
t1.setAction(lol)
t1.start()
#t1.join()
print("Return to", current_thread().getName())
'''
