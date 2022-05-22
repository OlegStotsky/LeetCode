class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_node = ListNode(-1)
        
        if head is None:
            return None
        
        first_node = head
        new_head = head if head.next is None else head.next
        
        while first_node is not None:
            next_node = first_node.next
            if next_node is not None:
                tmp = next_node.next
                prev_node.next = next_node
                next_node.next = first_node
                prev_node = first_node
                first_node = tmp
                prev_node.next = None
            else:
                prev_node.next = first_node
                first_node = None
        
        return new_head
