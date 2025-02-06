class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        l, r = 0, 0
        _max = 1
        counter = {s[0]: 1}

        while r < len(s) - 1:
            r += 1
            counter[s[r]] = counter.get(s[r], 0) + 1

            while counter[s[r]] > 2:
                counter[s[l]] -= 1
                l += 1
            
            _max = max(_max, r - l + 1)

        return _max

# O algoritmo encontra o maior substring onde cada caractere aparece no máximo duas vezes.

# Ele utiliza a técnica de janela deslizante com dois ponteiros (l e r). Conforme r avança,
# os caracteres são armazenados em um dicionário para contar suas ocorrências. Se um caractere
# aparecer mais que duas vezes, o ponteiro l é movido para reduzir sua frequência.

# Complexidade temporal: O(n), pois percorre s uma única vez.
# Complexidade espacial: O(1), pois o dicionário armazena no máximo 26 caracteres (letras minúsculas).
