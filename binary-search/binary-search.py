class Solution:
    def search(self, nums: List[int], target: int) -> int:
        end = len(nums)-1
        start = 0
        
        while start <= end:
            mid = start + (end-start)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
                
        return -1