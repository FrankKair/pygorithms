class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        lo = 0
        hi = len(s)-1
        while lo < hi:
            temp = s[lo]
            s[lo] = s[hi]
            s[hi] = temp
            lo += 1
            hi -= 1
        return ''.join(s)
