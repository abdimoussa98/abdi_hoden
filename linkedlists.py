# to consolidate our topics, let's just organize files by data structure

from typing import Optional
from typing import List

class ListNode():
  def __init__(self, val = 0, next = None) -> None:
    self.val = val
    self.next = next

def arr_to_linked_list(arr): # we can use this function to create our linked list as needed
  dummy_head = ListNode()
  endOfList = dummy_head
  
  for x in arr:
    node = ListNode()
    node.val = x
    endOfList.next = node
    endOfList = node
  return dummy_head.next


######################### LINKED LIST EASY PROBLEMS: #######################################

# 1) https://leetcode.com/problems/reverse-linked-list/
# Given the head of a singly linked list, reverse the list, and return the reversed list.
def reverseList(self, head):
  prev = None
  curr = head
  next = None

  while curr is not None:
    next = curr.next
    curr.next = prev

    prev = curr
    curr = next

  return prev

# 2) https://leetcode.com/problems/merge-two-sorted-lists/
# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

def mergeTwoLists(list1, list2):
  dummy_head = ListNode()
  curr = dummy_head

  while list1 and list2:
    if list1.val < list2.val:
      curr.next = list1
      list1 = list1.next
    else:
      curr.next = list2
      list2 = list2.next
    
    curr = curr.next

  curr.next = list1 if list1 else list2
  return dummy_head.next

class Solution:
  def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
      if not list1 and not list2:
          return list1
      if not list1 or not list2:
          return list1 if not list2 else list2 # dumb null checks
      
      seek, target = (list1, list2) if list1.val < list2.val else (list2, list1)
      head = seek
      while seek and target:
          while seek.next and seek.next.val < target.val:
              seek = seek.next
          seek.next, target = target, seek.next
          seek = seek.next
      return head

# https://leetcode.com/problems/merge-two-sorted-lists/solutions/1826705/python-without-recursion-or-dummy/
def betterMergeTwoLists(self, list1, list2):
  # inserting list2 into list1
  # loop through while list1 has next
  # check for which current node val is larger
    # if list1 val is larger increment list1 curr
    # if list2 val is larger insert list2 curr after list1 curr
  # after loop add the rest of list2 into list 1
  if list1.val < list2.val:
    curr = list1
    list1 = list1.next
  else:
    curr = list2
    list2 = list2.next
  
  while list1 is not None and list2 is not None:
    if list2.val > list1.val:
      curr.next = list1
      
    elif list1.val > list2.val: 
      curr = list2
      curr.next = list1

    

  
    
# https://leetcode.com/problems/linked-list-cycle/
# Given head, the head of a linked list, determine if the linked list has a cycle in it.

# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

# Return true if there is a cycle in the linked list. Otherwise, return false.
def hasCycle(self, head):
  pass


########################## LINKED LIST MEDIUM PROBLEMS: #######################################
# https://leetcode.com/problems/reorder-list/
# You are given the head of a singly linked-list. The list can be represented as:

# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:

# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.



def reorderList(self, head):
  pass



# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Given the head of a linked list, remove the nth node from the end of the list and return its head.
def removeNthFromEnd(self, head, n):
  pass



# https://leetcode.com/problems/add-two-numbers/
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
def addTwoNumbers(self, l1, l2):
  pass

# https://leetcode.com/problems/find-the-duplicate-number/
# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
# There is only one repeated number in nums, return this repeated number.
# You must solve the problem without modifying the array nums and uses only constant extra space.

def findDuplicate(self, nums):
  pass

# https://leetcode.com/problems/lru-cache/
# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

# Implement the LRUCache class:

# LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
# int get(int key) Return the value of the key if the key exists, otherwise return -1.
# void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
# The functions get and put must each run in O(1) average time complexity.
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

class LRUCache:

  def __init__(self, capacity: int):
    pass
  
  
  def get(self, key: int) -> int:
    pass
  
  
  def put(self, key: int, value: int) -> None:
    pass


# https://leetcode.com/problems/copy-list-with-random-pointer/
# A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

# Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

# For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

# Return the head of the copied linked list.

# The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

# val: an integer representing Node.val
# random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
# Your code will only be given the head of the original linked list.

class Node:
  def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
      self.val = int(x)
      self.next = next
      self.random = random

def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
  pass


########################## LINKED LIST HARD PROBLEMS: #######################################

#  https://leetcode.com/problems/merge-k-sorted-lists/
# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
# Merge all the linked-lists into one sorted linked-list and return it.
def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
  pass

# https://leetcode.com/problems/reverse-nodes-in-k-group/
# Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

# You may not alter the values in the list's nodes, only nodes themselves may be changed.
def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
  pass



