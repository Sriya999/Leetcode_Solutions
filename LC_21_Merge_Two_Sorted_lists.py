from typing import Optional  # Import Optional at the top of the file

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to serve as the start of the merged list
        dummy = ListNode()
        current = dummy

        # Traverse both lists and merge them
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # If one of the lists is not empty, append it to the merged list
        if list1:
            current.next = list1
        elif list2:
            current.next = list2

        # Return the head of the merged list (skipping the dummy node)
        return dummy.next

# Helper function to convert a list to a linked list
def list_to_linked_list(lst):
    dummy = ListNode()
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

# Helper function to convert a linked list to a list
def linked_list_to_list(node):
    lst = []
    while node:
        lst.append(node.val)
        node = node.next
    return lst

# Example usage:
solution = Solution()
list1 = list_to_linked_list([1, 2, 4])
list2 = list_to_linked_list([1, 3, 4])
merged_list = solution.mergeTwoLists(list1, list2)
print(linked_list_to_list(merged_list))  # Output: [1, 1, 2, 3, 4, 4]