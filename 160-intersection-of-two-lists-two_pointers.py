class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        curNode = headA
        aLen = 0
        while curNode is not None:
            aLen += 1
            curNode = curNode.next
        
        curNode = headB
        bLen = 0
        while curNode is not None:
            bLen += 1
            curNode = curNode.next
            
        shorterNode, longerNode = headA, headB
        shorterLen, longerLen = aLen, bLen
        if bLen < aLen:
            shorterNode, longerNode = headB, headA
            shorterLen, longerLen = bLen, aLen
        
        for i in range(0, longerLen - shorterLen):
            longerNode = longerNode.next
            
        while longerNode is not None:
            if longerNode == shorterNode:
                return longerNode
            longerNode, shorterNode = longerNode.next, shorterNode.next
            
        return None
