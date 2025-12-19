from algorithm.bubble_sort import bubble_sort
from algorithm.binary_search import binary_search
from data_structure.stack import Stack
from data_structure.queue import Queue
from math.gcd_lcm import gcd, lcm

def run():
    assert bubble_sort([3,2,1]) == [1,2,3]
    assert binary_search([1,2,3,4], 3) == 2
    s = Stack(); s.push(1); s.push(2); assert s.pop() == 2
    q = Queue(); q.enqueue(5); q.enqueue(6); assert q.dequeue() == 5
    assert gcd(24, 18) == 6
    assert lcm(24, 18) == 72
    print("All basic tests passed.")

if __name__ == "__main__":
    run()
