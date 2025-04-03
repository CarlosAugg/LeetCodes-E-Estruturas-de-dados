class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Números negativos nunca são palíndromos por causa do sinal '-'
        if x < 0:
            return False

        # Converte o número para string e o inverte
        return str(x) == str(x)[::-1]
