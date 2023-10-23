from ast import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1

        while l < r:
            s = numbers[l] + numbers[r]

            if  s == target:
                return [l+1, r+1]
            # the array is sorted in non-decreasing order
            # if the sum is < target, then increase left
            elif s < target:
                l += 1
            # else if the sum is > target, the decrease right
            else:
                r -= 1