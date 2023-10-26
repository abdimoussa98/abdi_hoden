class MergeSort(object):
    def merge(self, listOne, listTwo):
      print("merge function entered")

      idxOne = 0
      idxTwo = 0
      list = []
      while idxOne <= (len(listOne)-1) and idxTwo <= (len(listTwo)-1):
        if (listOne[idxOne] < listTwo[idxTwo]):
          list.append(listOne[idxOne])
          idxOne+=1
        elif (listTwo[idxTwo] < listOne[idxOne]):
          list.append(listTwo[idxTwo])
          idxTwo+=1
        else:
          list.append(listOne[idxOne])
          idxOne+=1
          list.append(listTwo[idxTwo])
          idxTwo+=1
      while idxOne <= (len(listOne)-1):
        list.append(listOne[idxOne])
        idxOne+=1
      while idxTwo <= (len(listTwo)-1):
        list.append(listTwo[idxTwo])
        idxTwo+=1
      return list

    def mergeSort(self, list):
      start = 0
      middle = len(list) // 2 # 1

      if len(list) == 1:
        return list
      # if len(list) == 2:
      #   return self.merge([list[0]], [list[1]])
      # if len(list) < 2: return list
      # middle = len(list) // 2

      l_arr = self.mergeSort(list[start:middle]) # middle is exclusive
      r_arr = self.mergeSort(list[middle:]) # middle is inclusive
      print("l_arr",l_arr)
      print("r_arr",r_arr)
      return self.merge(l_arr, r_arr)

### 8 (286)  (8 286)
### 2 (8 286) 2 (8 286)
## 2 3 (8 286) 2 (3 8 286)
# 1 2 3 (4 5 6 7 8 9 10)

# list = [8,286]
# print(list[0:1])
# print(list[:0])
# sortedList= MergeSort().mergeSort(list)
# print("sortedList",sortedList)
# # print(len(sortedList))


def mergesort(nums):
  #base case:
  if len(nums) <= 1: return nums

  mid = len(nums) // 2
  l, r = mergesort(nums[:mid]), mergesort(nums[mid:])
  i = j = k = 0

  while i < len(l) and j < len(r):
    if l[i] < r[j]:
      nums[k] = l[i]
      i += 1
    else:
      nums[k] = r[j]
      j += 1
    k += 1

  while i < len(l):
    nums[k] = l[i]
    i += 1
    k += 1
  while j < len(r):
    nums[k] = r[j]
    j += 1
    k += 1
  return nums


print(mergesort([3, 2, 1, 5]))
