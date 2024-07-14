from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # matrix[row][col]
        res = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        while left < right and top < bottom:
            # get every i in the top row (from left to right)
            for i in range(left, right):
                res.append(matrix[top][i])
            
            # shifting top down by 1
            top += 1

            # get every i in the right column (from top to bottom)
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])

            # shifting right to the left
            right -= 1

            # this condition should be tested for understanding
            if not (left < right and top < bottom):
                break

            # get every i in the bottom row (from right to left)
            # -1 means reverse order (right to left)
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])

            # shift the bottom up
            bottom -= 1

            # get every i in the left column (from bottom to top)
            # in reverse order (-1)
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])

            # shift left to right
            left += 1

        return res