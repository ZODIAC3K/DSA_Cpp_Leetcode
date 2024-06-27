class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxArea = 0

        while(left < right):
            leftTowerHeight = height[left]
            rightTowerHeight = height[right]
            minTowerHeight = min(leftTowerHeight, rightTowerHeight)
            maxArea = max(maxArea, minTowerHeight*(right - left) )
            if(leftTowerHeight < rightTowerHeight):
                left += 1
            else:
                right -= 1
        
        return maxArea
        