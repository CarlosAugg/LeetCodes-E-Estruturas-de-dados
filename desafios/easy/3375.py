class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # Se k não está em nums, verificamos se é possível
        if any(num < k for num in nums):
            return -1
        
        # Encontrar os valores únicos maiores que k em ordem decrescente
        unique_values = sorted(set(num for num in nums if num > k), reverse=True)
        
        # Cada valor único representa uma operação
        return len(unique_values)""