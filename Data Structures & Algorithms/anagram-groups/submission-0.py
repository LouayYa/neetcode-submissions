class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # mapping character count --> anagram list

        for s in strs:
            count = [0] * 26 # a - z

            for c in s:
                count[ord(c) - ord("a")] += 1
            
            res[tuple(count)].append(s) # turn array into tuple so it can be used as a key

        return list(res.values())


        