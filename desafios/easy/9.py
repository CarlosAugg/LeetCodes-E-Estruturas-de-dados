class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):  # Elimina negativos e múltiplos de 10 (exceto 0)
            return False

        reversed_half = 0
        original = x
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10  # Remove o último dígito de x

        return x == reversed_half or x == reversed_half // 10  # Para números de tamanho ímpar
