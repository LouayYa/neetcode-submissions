class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ""
        for ch in s:
            if ch.isalnum():
                clean = clean + ch.lower()
        
        l, r = 0, len(clean) - 1
            
        while l < r:  
            if (clean[l] == clean[r]):
                l += 1
                r -= 1
            else:
                return False
        
        return True

        # use .isalnum() to ignore non alphanumeric characters
        # use .lower() to convert characters to lower-case    