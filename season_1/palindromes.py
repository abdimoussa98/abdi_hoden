# https://leetcode.com/problems/valid-palindrome/ 
def isPalindrome(s) :
    # A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all 
    # non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

    # Given a string s, return true if it is a palindrome, or false otherwise.
    # 0-9 ord(48-57); A-Z ord(65-90)
    # Input: s = "race car"
    # abba  racecar 

    def isAlphaNum(c):
      val = ord(c)

      if (48 <= val and val <= 57) or (65 <= val and val <= 90):
        return True
      return False

    s=s.upper()
    l, r = 0, len(s) - 1
    while l <= r:

      while l < r and not isAlphaNum(s[l]):
        l += 1

      while l < r and not isAlphaNum(s[r]):
        r -= 1

      if s[l].upper() != s[r].upper(): 
        return False

      print(s[l], s[r])

      l += 1
      r -= 1
    return True

s = "abca"
print(isPalindrome(s))

# Given a string s, return true if the s can be palindrome after deleting at most one character from it.

# Example 1:

# Input: s = "aba"
# Output: true
# Example 2:

# Input: s = "abca"
# Output: true
# Explanation: You could delete the character 'c'.
# Example 3:

# Input: s = "abc"
# Output: false

def isPalindrome(s) :
      # A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all 
      # non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

      # Given a string s, return true if it is a palindrome, or false otherwise.
      # 0-9 ord(48-57); A-Z ord(65-90)
      # Input: s = "race car"
      # abba  racecar 

    count = 0
    l, r = 0, len(s) - 1
    while l <= r :

        if s[l] != s[r]:

            if count < 1 and s[r-1] == s[l]:
                r-=1  
                count+=1
            elif count < 1 and s[l+1] == s[r]:
                l+=1
                count+=1
            # 
            else:
                return False
        l += 1
        r -= 1
    return True
s = "abca" #"atbbga"
print(len("abboa"))
print(isPalindrome(s))

class Solution:
  def validPalindrome(self, s: str) -> bool:

      def isValid(l, r):
          while l < r:
              if s[l] != s[r]: return False
              l += 1
              r -= 1
          return True

      l, r = 0, len(s) - 1
      mistake = False
      while l < r:
          if s[l] != s[r]:
              if not mistake:
                  return isValid(l + 1, r) or isValid(l, r - 1)
              else:
                  return False
          l += 1
          r -= 1
      return True

