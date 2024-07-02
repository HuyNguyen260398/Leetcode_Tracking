class Solution:
    def canJump(self, nums: list[int]) -> bool:
        current_gas = 0
        for new_gas in nums:
            if current_gas < 0:
                return False
            elif current_gas < new_gas:
                current_gas = new_gas
            current_gas -= 1
        return True