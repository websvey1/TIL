SIZE = 100
Q = [0]*SIZE
front, rear = -1, -1
def isFull():
    global rear
    return rear == len(Q)-1

def isEmpty():
    global front, rear
    return front == rear

def enQueue(item):
    global rear
    if isFull():
        print("FULL")
    else:
        rear += 1
        # return Q[item]
        Q[rear]= item
def deQueue():
    global front
    if isEmpty():
        print("EMPTY")
    else:
        front += 1
        return Q[front]

def Qpeek():
    if isEmpty():
        print("EMPTY")
    else:
        return Q[front+1]

enQueue(1)
enQueue(2)
enQueue(3)
print(Qpeek())
print(deQueue())
print(deQueue())
print(deQueue())

print(Q)