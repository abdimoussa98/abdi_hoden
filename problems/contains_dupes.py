class ContainsDuplicate(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        values = {}
        for i, val in enumerate(nums):
            if(val in values):
              return True
            values.setdefault(val, 1)

