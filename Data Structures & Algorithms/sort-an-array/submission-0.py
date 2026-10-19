class Solution:
    def mergeSort(self, arr: List[int]):
        size = len(arr)
        if size <= 1:
            return

        middle = size // 2

        left, right = arr[:middle], arr[middle:]

        self.mergeSort(left)
        self.mergeSort(right)
        self.merge(left,right,arr)
    
    def merge(self, left: List[int],right: List[int], arr: List[int]):
        leftSize = len(left)
        rightSize = len(right)

        i,l,r =0,0,0
        while (l < leftSize and r < rightSize):
            if left[l] <= right[r]:
                arr[i] = left[l]
                l += 1
            else:
                arr[i] = right[r]
                r += 1
            
            i += 1
        
        while l < leftSize:
            arr[i] = left[l]
            l+=1
            i+=1
        
        while r < rightSize:
            arr[i] = right[r]
            r += 1
            i += 1

        

    def sortArray(self, nums: List[int]) -> List[int]:
        self.mergeSort(nums)
        return nums
