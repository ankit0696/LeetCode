class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        occur = {}
        for num in nums:
            occur[num] = 0
        for num in nums:
            if occur[num] != 0:
                return True
            occur[num]=1
        return False
