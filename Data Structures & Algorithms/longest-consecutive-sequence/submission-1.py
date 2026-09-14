class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        consec = set(nums)
        output = 0

        for n in nums:
            if (n-1) not in consec:
                res = 1
                while (n+res) in consec:
                    res += 1
                
                output = max(res,output)
        
        return output

                
