from ast import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counted_nums = []
        for i in nums:
            if i not in counted_nums:
                if nums.count(i) > len(nums) / 2:
                    return i
                else:
                    counted_nums.append(i)

    def majorityElement2(self, nums: List[int]) -> int:
        # The intuition behind this approach is that if an element occurs more than n/2 times in the array (where n is the size of the array), 
        # it will always occupy the middle position when the array is sorted. 
        # Therefore, we can sort the array and return the element at index n/2.
        nums.sort()
        n = len(nums)
        return nums[n//2]
    
    def majorityElement3(self, nums: List[int]) -> int:
        # The intuition behind the Moore's Voting Algorithm is based on the fact that if there is a majority element in an array, 
        # it will always remain in the lead, even after encountering other elements.
        count = 0
        candidate = 0

        for num in nums:
            if count == 0:
                candidate = num

            if num == candidate:
                count += 1
            else:
                count -= 1

        return candidate