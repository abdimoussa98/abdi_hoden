from linkedlists import ListNode, arr_to_linked_list
from typing import Optional

list1, list2 = arr_to_linked_list([1,2,4]), arr_to_linked_list([1,3,4])

def mergeTwoLists(list1, list2):
  dummy_head = ListNode()
  curr = dummy_head

  while list1 and list2:
    if list1.val < list2.val:
      curr.next = list1
      list1 = list1.next
      curr = curr.next
    else:
      curr.next = list1
      list1 = list1.next
      curr = curr.next

  curr.next = list1 if list1 else list2
  return dummy_head.next

sol = mergeTwoLists(list1, list2)

while sol:
  print(sol.val)
  sol = sol.next






