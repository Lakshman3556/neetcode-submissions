class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        d1=ListNode(0,head)
        s=d1
        f=d1
        for _ in range(n+1):
            f=f.next
        while f:
            s=s.next
            f=f.next
        s.next=s.next.next
        return d1.next       
