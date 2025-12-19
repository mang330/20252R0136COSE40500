class Node:
    def __init__(self, value, nxt=None):
        self.value = value
        self.next = nxt

class LinkedList:
    def __init__(self):
        self.head = None

    def push_front(self, value):
        self.head = Node(value, self.head)

    def to_list(self):
        out = []
        cur = self.head
        while cur:
            out.append(cur.value)
            cur = cur.next
        return out

if __name__ == "__main__":
    ll = LinkedList()
    ll.push_front(3); ll.push_front(2); ll.push_front(1)
    print(ll.to_list())
