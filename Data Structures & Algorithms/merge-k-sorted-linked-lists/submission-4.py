# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        while len(lists) > 1:
            merged = []
            for ii in range(0, len(lists), 2):
                a = lists[ii]
                b = lists[ii+1] if ii + 1 < len(lists) else None
                merged.append(self.mergeLists(a, b))
            lists = merged
        return lists[0] if len(lists) > 0 else None

    def mergeLists(self, a: Optional[ListNode], b: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, None)
        tail = dummy
        while a and b:
            if a.val < b.val:
                tail.next = a
                a = a.next
            else:
                tail.next = b
                b = b.next
            tail = tail.next
        if a: tail.next = a
        elif b: tail.next = b
        return dummy.next


        