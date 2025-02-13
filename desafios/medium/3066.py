import heapq

class Solution:
    def minOperations(self, nums, k):
        heapq.heapify(nums)
        operations = 0
        
        while len(nums) > 1 and nums[0] < k:
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            heapq.heappush(nums, x * 2 + y)
            operations += 1
        
        return operations if nums[0] >= k else -1

solution = Solution()
print(solution.minOperations([2,11,10,1,3], 10)) 
print(solution.minOperations([1,1,2,4,9], 20))  