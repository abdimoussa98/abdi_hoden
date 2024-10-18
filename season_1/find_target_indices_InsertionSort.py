# INSERTION SORT: To order a list of elements in ascending order, the Insertion Sort
# algorithm requires the following operations:

# Begin with a list of unsorted elements.
# Iterate through the list of unsorted elements, from the first item to last.
# The current element is compared to the elements in all preceding positions to the left in each step.
# If the current element is less than any of the previously listed elements, it is moved one position to the left.

# https://leetcode.com/problems/find-target-indices-after-sorting-array/

def findTargetIndices(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    #our goal is to sort nums in ascending order, we can do this in anyway
    def our_sort(nums):
      for idx in range(len(nums)):
        currentUnsortedElement = nums[idx]
        sortedIdx = idx - 1
        while sortedIdx >= 0 and currentUnsortedElement < nums[sortedIdx]:
          nums[sortedIdx + 1] = nums[sortedIdx] # move sorted value to the right
          sortedIdx-=1
        nums[sortedIdx + 1] = currentUnsortedElement # finally insert currentUnsorted element        
      return nums

    sorted_arr = our_sort(nums)
    targets = []

    for i in range(len(sorted_arr)):
      if sorted_arr[i] == target:
        targets.append(i)

    return targets