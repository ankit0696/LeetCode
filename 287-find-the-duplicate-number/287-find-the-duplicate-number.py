class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        count = {}
        for ele in nums:
            if ele in count:
                count[ele] += 1
            else:
                count[ele] = 1
                
        for ele in count:
            if count[ele] > 1:
                return ele
        