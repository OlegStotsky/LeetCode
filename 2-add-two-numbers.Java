/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
  public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
      int carry = 0;
      ListNode head = null;
      ListNode curAns = head;
      
      while (l1 != null || l2 != null) {
          int firstVal = l1 == null ? 0 : l1.val;
          int secondVal = l2 == null ? 0 : l2.val;
          int sum = firstVal + secondVal + carry;
          carry = sum / 10;
          
          ListNode next = new ListNode(sum % 10);
          if (head == null) {
              head = next;
              curAns = next;
          } else {
              curAns.next = next;
              curAns = next;
          }
          
          if (l1 != null) l1 = l1.next;
          if (l2 != null)  l2 = l2.next;
      }
      
      if (carry != 0) {
          curAns.next = new ListNode(carry);
      }
      
      return head;
  }
}