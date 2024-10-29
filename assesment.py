# 1. Two Sum (1-leetcode)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}

        for i, num in enumerate(nums):
            val = target - num

            if val in res:
                return[res[val],i]
            
            res[num] = i
#2. Remove Element (27-leetcode)

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k = k + 1

        return k
    

#3. Next Permutations (31-leetcode)

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2
        while i >=0 and nums[i] >= nums[i+1]:
            i -= 1

        if i >=0:
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            
            nums[i],nums[j] = nums[j],nums[i]

        l = i + 1
        r = len(nums) - 1
        while l < r:
            nums[l],nums[r] = nums[r],nums[l]
            l = l + 1
            r = r - 1
# 4. Find First and Last Position of Element in a sorted Array(34-leetcode)

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = []
        for i in range(len(nums)):
            if nums[i] == target:
                res.append(i)

        if res:
            if len(res) == 1:
                return [res[0],res[0]]
            return [res[0],res[-1]]
        return [-1,-1]