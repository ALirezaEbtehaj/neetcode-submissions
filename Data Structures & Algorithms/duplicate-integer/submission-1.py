class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a = set()
        x = len(nums)
        for i in range (0,x):
            if nums[i] in a:
                return True
            else:
                a.add(nums[i])
        return False