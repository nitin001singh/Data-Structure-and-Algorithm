# Brute Force

# Tc : O(N^3)
# Sc : O(1)


# import sys
# class Solution:
#     def maximumSubArray(self, nums):
#         maxSum = -sys.maxsize-1
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)+1):                
#                 sumTotal = 0
#                 for k in range(i, j):
#                     sumTotal += nums[k]
                    
#                 maxSum = max(maxSum, sumTotal)
#         return maxSum
                
            
    
# result = Solution().maximumSubArray([-2,1,-3,4,-1,2,1,-5,4])
# print(result)


# Better Approach

# Tc : O(N^2)
# Sc : O(1)


# import sys
# class Solution:
#     def maximumSubArray(self, nums):
#         maxSum = -sys.maxsize-1
#         for i in range(len(nums)):
#             sumTotal = 0            
#             for j in range(i, len(nums)):                
#                 sumTotal += nums[j]            
#                 maxSum = max(maxSum, sumTotal)
#         return maxSum
                
            
    
# result = Solution().maximumSubArray([-2,1,-3,4,-1,2,1,-5,4])
# print(result)

# Optimize

# TC : O(N)
# SC : O(1)

import sys
class Solution:
    def maximumSubArray(self, nums):
        maxSum = -sys.maxsize - 1
        tempSum = 0
        tempStart = 0
        start = -1
        end = -1

        for index in range(len(nums)):
            if tempSum == 0:
                tempStart = index
                
            tempSum += nums[index]

            if tempSum > maxSum:
                maxSum = tempSum
                start = tempStart
                end = index

            if tempSum < 0:
                tempSum = 0

        return maxSum, nums[start:end+1]
            
    
result = Solution().maximumSubArray([-2,1,-3,4,-1,2,1,-5,4])
print("Max Sum:", result[0])
print("Subarray:", result[1])