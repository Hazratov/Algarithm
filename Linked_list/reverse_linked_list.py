class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None


def reverse(head: Node) -> Node:
    current = head
    prev = None

    while current:
        next_ = current.next
        current.next = prev
        prev = current
        current = next_
    return prev