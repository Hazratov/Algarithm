class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None

def findMiddle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def reverse(head: Node) -> Node:
    current = head
    prev = None

    while current:
        next_ = current.next
        current.next = prev
        prev = current
        current = next_
    return prev

def isSame(head1, head2):
    while head1 and head2:
        if head1.val != head2.val:
            return False
        head1 = head1.next
        head2 = head2.next
    return True

def isPalindrome(head: Node) -> bool:
    middle = findMiddle(head)
    middle = reverse(middle)

    return isSame(head, middle)
