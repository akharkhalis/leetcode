l1 = [1,2,4]
l2 = [1,3,4]


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        new_node = ListNode(0)
        result_node = new_node
        while True:

            if not l2:
                result_node.next = l1
                break
            if not l1:
                result_node.next = l2
                break

            if l1.val > l2.val:
                result_node.next = ListNode(l2.val)
                l2 = l2.next
            else:
                result_node.next = ListNode(l1.val)
                l1 = l1.next
            result_node = result_node.next

        return new_node.next

print (mergeTwoLists(l1, l2))