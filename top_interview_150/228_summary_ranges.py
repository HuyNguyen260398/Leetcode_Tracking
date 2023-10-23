from ast import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return nums

        range_list = []
        start = nums[0]

        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] != 1:
                if start == nums[i-1]:
                    range_list.append(f"{start}")
                else:
                    range_list.append(f"{start}->{nums[i-1]}")
                start = nums[i]

        if start == nums[-1]:
            range_list.append(f"{start}")
        else:
            range_list.append(f"{start}->{nums[-1]}")

        return range_list
    
    def summaryRanges2(self, nums: List[int]) -> List[str]:
        result = []

        start, end = 0, 0  # using 2 pointer for the index

        while start < len(nums) and end < len(nums):
            if (end+1) < len(nums) and nums[end] + 1 == nums[end+1]: # check for range
                end += 1 # increase the end pointer if still in range
            else:
                if nums[start] == nums[end]: # check if the range only have one item
                    result.append(str(nums[start]))
                    start += 1
                    end += 1
                else:
                    result.append(str(nums[start]) + '->' + str(nums[end]))
                    end += 1
                    start = end
        
        return result