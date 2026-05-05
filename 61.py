from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    if not head or not head.next or k == 0:
        return head

    length = 1
    last = head
    while last.next:
        last = last.next
        length += 1

    k = k % length 
    if k == 0:
        return head
    
    new_tail = head 
    for _ in range(length - k - 1):
        new_tail = new_tail.next

    new_head = new_tail.next
    new_tail.next = None
    last.next = head

    return new_head