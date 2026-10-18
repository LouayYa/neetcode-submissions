class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = collections.defaultdict()
        majority = len(nums) // 2
        res = 0

        for n in nums:
            if n in counts:
                counts[n] = counts.get(n,0) + 1
            else:
                counts[n] = 1
            
            if counts.get(n,0) > majority:
                res = n
        
        return res
         