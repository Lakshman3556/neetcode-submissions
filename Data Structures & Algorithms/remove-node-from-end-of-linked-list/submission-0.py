class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        c = 0
        d = head
        while d.next:
            d = d.next
            c += 1
        r = c - n
        if r < 0:
            return head.next
        t = 0
        d1 = head
        while d1.next:
            if t == r:
                d1.next = d1.next.next
                break
            d1 = d1.next
            t += 1
        return head