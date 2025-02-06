class Solution:
    def reverseWords(self, s):
        res = ''
        l, r = 0, 0

        while r < len(s):
            if s[r] != '':
                r += 1
            else:
                res += s[l:r][::-1] + ''
                r += 1
                l = r

        res += s[l:r][::-1]
        return res

# O algoritmo inverte cada palavra em s sem alterar a ordem das palavras.

# Ele percorre a string usando dois ponteiros (l e r). Quando encontra um espaço,
# inverte a palavra entre os índices l e r, adiciona ao resultado e avança l para
# o início da próxima palavra. No final, a última palavra é invertida e adicionada.

# Complexidade temporal: O(n), pois percorre a string uma única vez.
# Complexidade espacial: O(n), pois armazena a string invertida.
