# # class RotateImage(object):
# #     def rotateLayer(self, matrix, top, bottom, left, right ): 
# #         for i in range(right - left):
# #             # move bottom-left to top-left
# #             temp = matrix[top][left + i] #store the top-left in temp, so we only have 1 temp var
# #             matrix[top][left + i] = matrix[bottom - i][left]

# #             # move bottom-right to bottom-left
# #             matrix[bottom - i][left] = matrix[bottom][right - i]

# #             # move top-right to bottom-right
# #             matrix[bottom][right - i] = matrix[top + i][right]

# #             # move top-left to top-right
# #             matrix[top + i][right] = temp

# #     def rotate(self, matrix):
# #         size = len(matrix)

# #         left = 0
# #         right = size - 1
# #         top = 0
# #         bottom = size - 1

# #         while(top < bottom and left < right):
# #             self.rotateLayer(matrix, top, bottom, left, right)
# #             top += 1
# #             bottom -= 1
# #             left += 1
# #             right -= 1

# # class ContainsDuplicate(object):
# #     def containsDuplicate(self, nums):
# #         """
# #         :type nums: List[int]
# #         :rtype: bool
# #         """
# #         values = {}
# #         for i, val in enumerate(nums):
# #             if(val in values):
# #               return True
# #             values.setdefault(val, 1)



# # # https://leetcode.com/problems/design-hashset/
# # class MyHashSet(object):
# #     def __init__(self):
# #       self.myList = [-1] * 1000000

# #     def getHashIndex(self, value):
# #       # get hash index that is unique to value
# #       return hash(value) % 1000000

# #     def add(self, key):
# #         """
# #         :type key: int
# #         :rtype: None
# #         """
# #         if not self.contains(key):
# #           idx = self.getHashIndex(key)
# #           self.myList[idx] = key

# #     def remove(self, key):
# #         """
# #         :type key: int
# #         :rtype: None
# #         """
# #         if self.contains(key):
# #           idx = self.getHashIndex(key)
# #           self.myList[idx] = -1

# #     def contains(self, key):
# #         """
# #         :type key: int
# #         :rtype: bool
# #         """
# #         idx = self.getHashIndex(key)
# #         if self.myList[idx] == key:
# #           return True
# #         return False



# # # Your MyHashSet object will be instantiated and called as such:
# # # obj = MyHashSet()
# # # obj.add(key)
# # # obj.remove(key)
# # # param_3 = obj.contains(key)


# #     def char_frequency(self, str1):
# #             dict = {}
# #             for n in str1:
# #                 keys = dict.keys()
# #                 if n in keys:
# #                     dict[n] += 1
# #                 else:
# #                     dict[n] = 1
# #             return dict
# #     def groupAnagrams(self, strs):
# #         dict = {}
# #         for str in strs:
# #             char_array = list(str)
# #             frequency_map = frozenset(self.char_frequency(char_array).items())
# #             if frequency_map in dict:
# #                  dict.setdefault(frequency_map, dict[frequency_map].append(str))
# #             else:
# #                  dict.setdefault(frequency_map, [str])

# #         return dict.values()          



# # # INSERTION SORT: To order a list of elements in ascending order, the Insertion Sort
# # # algorithm requires the following operations:

# # # Begin with a list of unsorted elements.
# # # Iterate through the list of unsorted elements, from the first item to last.
# # # The current element is compared to the elements in all preceding positions to the left in each step.
# # # If the current element is less than any of the previously listed elements, it is moved one position to the left.

# # # https://leetcode.com/problems/find-target-indices-after-sorting-array/

# # def findTargetIndices(nums, target):
# #     """
# #     :type nums: List[int]
# #     :type target: int
# #     :rtype: List[int]
# #     """

# #     #our goal is to sort nums in ascending order, we can do this in anyway
# #     def our_sort(nums):
# #       for idx in range(len(nums)):
# #         currentUnsortedElement = nums[idx]
# #         sortedIdx = idx - 1
# #         while sortedIdx >= 0 and currentUnsortedElement < nums[sortedIdx]:
# #           nums[sortedIdx + 1] = nums[sortedIdx] # move sorted value to the right
# #           sortedIdx-=1
# #         nums[sortedIdx + 1] = currentUnsortedElement # finally insert currentUnsorted element        
# #       return nums

# #     sorted_arr = our_sort(nums)
# #     targets = []

# #     for i in range(len(sorted_arr)):
# #       if sorted_arr[i] == target:
# #         targets.append(i)

# #     return targets


# # class MergeSort(object):
# #     def merge(self, listOne, listTwo):
# #       print("merge function entered")

# #       idxOne = 0
# #       idxTwo = 0
# #       list = []
# #       while idxOne <= (len(listOne)-1) and idxTwo <= (len(listTwo)-1):
# #         if (listOne[idxOne] < listTwo[idxTwo]):
# #           list.append(listOne[idxOne])
# #           idxOne+=1
# #         elif (listTwo[idxTwo] < listOne[idxOne]):
# #           list.append(listTwo[idxTwo])
# #           idxTwo+=1
# #         else:
# #           list.append(listOne[idxOne])
# #           idxOne+=1
# #           list.append(listTwo[idxTwo])
# #           idxTwo+=1
# #       while idxOne <= (len(listOne)-1):
# #         list.append(listOne[idxOne])
# #         idxOne+=1
# #       while idxTwo <= (len(listTwo)-1):
# #         list.append(listTwo[idxTwo])
# #         idxTwo+=1
# #       return list

# #     def mergeSort(self, list):
# #       start = 0
# #       middle = len(list) // 2 # 1

# #       if len(list) == 1:
# #         return list
# #       # if len(list) == 2:
# #       #   return self.merge([list[0]], [list[1]])
# #       # if len(list) < 2: return list
# #       # middle = len(list) // 2

# #       l_arr = self.mergeSort(list[start:middle]) # middle is exclusive
# #       r_arr = self.mergeSort(list[middle:]) # middle is inclusive
# #       print("l_arr",l_arr)
# #       print("r_arr",r_arr)
# #       return self.merge(l_arr, r_arr)

# # ### 8 (286)  (8 286)
# # ### 2 (8 286) 2 (8 286)
# # ## 2 3 (8 286) 2 (3 8 286)
# # # 1 2 3 (4 5 6 7 8 9 10)

# # # list = [8,286]
# # # print(list[0:1])
# # # print(list[:0])
# # # sortedList= MergeSort().mergeSort(list)
# # # print("sortedList",sortedList)
# # # # print(len(sortedList))


# # def mergesort(nums):
# #   #base case:
# #   if len(nums) <= 1: return nums

# #   mid = len(nums) // 2
# #   l, r = mergesort(nums[:mid]), mergesort(nums[mid:])
# #   i = j = k = 0

# #   while i < len(l) and j < len(r):
# #     if l[i] < r[j]:
# #       nums[k] = l[i]
# #       i += 1
# #     else:
# #       nums[k] = r[j]
# #       j += 1
# #     k += 1

# #   while i < len(l):
# #     nums[k] = l[i]
# #     i += 1
# #     k += 1
# #   while j < len(r):
# #     nums[k] = r[j]
# #     j += 1
# #     k += 1
# #   return nums


# # print(mergesort([3, 2, 1, 5]))

# # https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

# # https://leetcode.com/problems/two-sum/

# # def betterTwoSum(nums, target):
# #   for inx, num in enumerate(nums):
# #             expectedNum = target - num
# #             remainingNums = nums[inx+1:]
# #             if expectedNum in remainingNums: #n
# #                 return [inx, (inx+1 + remainingNums.index(expectedNum))] # n

# # def bestTwoSum(nums, target):
# #   differences = {} # O(n) space

# #   for i, n in enumerate(nums):
# #     k = target - n
# #     if k in differences: # 1
# #       return [differences[k], i]
# #     differences[n] = i
# # from typing import Counter


# # def findIndices(nums, indexDifference, valueDifference):
# #     """
# #     :type nums: List[int]
# #     :type indexDifference: int
# #     :type valueDifference: int
# #     :rtype: List[int]
# #     """
# #     counts = {}
# #     for idx, num in enumerate(nums):
# #         if counts.__contains__((idx, num)):
# #             print("here")
# #             return [idx, counts[(idx, num)][0]]
# #         else:
# #             counts.setdefault((idx + indexDifference, num + valueDifference ), (idx, num))
# #             counts.setdefault((abs(idx - indexDifference), abs(num - valueDifference) ), (idx, num))
# #             counts.setdefault((abs(idx - indexDifference)+ valueDifference ), (idx, num))
# #             counts.setdefault((idx + indexDifference, num , abs(num - valueDifference) ), (idx, num))






# # print(findIndices([5,1,4,1] , 3 , 4))


# # Input: s = "100011001", k = 3
# # Output: "11001"
# # Explanation: There are 7 beautiful substrings in this example:
# # 1. The substring "100011001".
# # 2. The substring "100011001".
# # 3. The substring "100011001".
# # 4. The substring "100011001".
# # 5. The substring "100011001".
# # 6. The substring "100011001".
# # 7. The substring "100011001".
# # The length of the shortest beautiful substring is 5.
# # The lexicographically smallest beautiful substring with length 5 is the substring "11001".

# # https://leetcode.com/problems/shortest-and-lexicographically-smallest-beautiful-string/description/
# # https://www.youtube.com/watch?v=q7bEQMv9TFQ
# # def shortestBeautifulSubstring(s, k):
# #     """
# #     :type s: str
# #     :type k: int
# #     :rtype: str
# #     """
# #     smallest = s 
# #     for i in range(len(s)):
# #       for j in range(len(s)):
# #         subString = s[:j+1]
# #         free = Counter(subString)
# #         if len(subString) < len(smallest) and free["1"] ==  k:
# #           return subString

# # https://leetcode.com/problems/valid-palindrome/ 
# # def isPalindrome(s) :
# #     # A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all 
# #     # non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# #     # Given a string s, return true if it is a palindrome, or false otherwise.
# #     # 0-9 ord(48-57); A-Z ord(65-90)
# #     # Input: s = "race car"
# #     # abba  racecar 

# #     def isAlphaNum(c):
# #       val = ord(c)

# #       if (48 <= val and val <= 57) or (65 <= val and val <= 90):
# #         return True
# #       return False

# #     s=s.upper()
# #     l, r = 0, len(s) - 1
# #     while l <= r:

# #       while l < r and not isAlphaNum(s[l]):
# #         l += 1

# #       while l < r and not isAlphaNum(s[r]):
# #         r -= 1

# #       if s[l].upper() != s[r].upper(): 
# #         return False

# #       print(s[l], s[r])

# #       l += 1
# #       r -= 1
# #     return True

# # s = "abca"
# # print(isPalindrome(s))

# # Given a string s, return true if the s can be palindrome after deleting at most one character from it.

# # Example 1:

# # Input: s = "aba"
# # Output: true
# # Example 2:

# # Input: s = "abca"
# # Output: true
# # Explanation: You could delete the character 'c'.
# # Example 3:

# # Input: s = "abc"
# # Output: false

# # def isPalindrome(s) :
# #       # A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all 
# #       # non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# #       # Given a string s, return true if it is a palindrome, or false otherwise.
# #       # 0-9 ord(48-57); A-Z ord(65-90)
# #       # Input: s = "race car"
# #       # abba  racecar 

# #     count = 0
# #     l, r = 0, len(s) - 1
# #     while l <= r :

# #         if s[l] != s[r]:

# #             if count < 1 and s[r-1] == s[l]:
# #                 r-=1  
# #                 count+=1
# #             elif count < 1 and s[l+1] == s[r]:
# #                 l+=1
# #                 count+=1
# #             # 
# #             else:
# #                 return False
# #         l += 1
# #         r -= 1
# #     return True
# # s = "abca" #"atbbga"
# # print(len("abboa"))
# # print(isPalindrome(s))


# # class Solution:
# #   def validPalindrome(self, s: str) -> bool:

# #       def isValid(l, r):
# #           while l < r:
# #               if s[l] != s[r]: return False
# #               l += 1
# #               r -= 1
# #           return True

# #       l, r = 0, len(s) - 1
# #       mistake = False
# #       while l < r:
# #           if s[l] != s[r]:
# #               if not mistake:
# #                   return isValid(l + 1, r) or isValid(l, r - 1)
# #               else:
# #                   return False
# #           l += 1
# #           r -= 1
# #       return True

# # 1) https://leetcode.com/problems/reverse-linked-list/
# # Given the head of a singly linked list, reverse the list, and return the reversed list.

# class ListNode:
#   val=0
#   next=0
#   def __init__(self, val=0, next=None):
#       self.val = val
#       self.next = next

# class Solution:
#   def reverseList(head):
#     prev = None
#     curr = head
#     next = None

#     while curr is not None:
#       next = curr.next
#       curr.next = prev

#       prev = curr
#       curr = next

#     return prev 


#   def arr_to_linked_list(arr):
#     dummy_head = ListNode()
#     endOfList = dummy_head

#     for x in arr:
#       node = ListNode()
#       node.val = x
#       endOfList.next = node
#       endOfList = node
#     return dummy_head.next


# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# head_of_linkedList = Solution.arr_to_linked_list(arr)
# curr = Solution.reverseList(head_of_linkedList)
# # curr = head_of_linkedList


# while curr is not None: # expected 3, 2, 1
#   print(curr.val)
#   curr = curr.next


# # print(Solution.reverseList(linkedList))


# # 2) https://leetcode.com/problems/merge-two-sorted-lists/
# # 3) https://leetcode.com/problems/reorder-list/

