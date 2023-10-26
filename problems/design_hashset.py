
# https://leetcode.com/problems/design-hashset/
class MyHashSet(object):
    def __init__(self):
      self.myList = [-1] * 1000000

    def getHashIndex(self, value):
      # get hash index that is unique to value
      return hash(value) % 1000000

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        if not self.contains(key):
          idx = self.getHashIndex(key)
          self.myList[idx] = key

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        if self.contains(key):
          idx = self.getHashIndex(key)
          self.myList[idx] = -1

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        idx = self.getHashIndex(key)
        if self.myList[idx] == key:
          return True
        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

          








