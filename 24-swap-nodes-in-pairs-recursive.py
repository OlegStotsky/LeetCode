class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        next_node = head.next
        if next_node != None:
            head.next = self.swapPairs(next_node.next)
            next_node.next = head
            return next_node
        return head
