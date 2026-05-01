class Solution:
    def search(self, nums: List[int], target: int) -> int:

        nums.sort()
        l, h = 0, len(nums)-1
        found_index = -1
        while l <= h:
            mid = (l + h) // 2
            guess = nums[mid]
            if guess == target:
                found_index = mid
                break
            elif guess > target:
                h = mid-1
            elif guess < target:
                l = mid + 1

        return found_index
                