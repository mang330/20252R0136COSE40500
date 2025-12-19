from collections import deque

class Queue:
    def __init__(self):
        self._q = deque()

    def enqueue(self, x):
        self._q.append(x)

    def dequeue(self):
        if not self._q:
            raise IndexError("dequeue from empty queue")
        return self._q.popleft()

    def is_empty(self):
        return len(self._q) == 0

    def __len__(self):
        return len(self._q)

if __name__ == "__main__":
    q = Queue()
    q.enqueue(1); q.enqueue(2)
    print(q.dequeue())
