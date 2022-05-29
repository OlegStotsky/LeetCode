class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA is None or headB is None:
            return None
        
        visitedNodes = set()
        curNode = headA
        while curNode is not None:
            visitedNodes.add(curNode)
            curNode = curNode.next
        
        curNode = headB
        while curNode is not None:
            if curNode in visitedNodes:
                return curNode
            curNode = curNode.next
        
        return None
