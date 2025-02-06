class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d = {}

        for idx, x in enumerate(nums):
            if x in d and abs(idx - d[x] ) <= k:
                    return True
            else:
                d[x] = idx

        return False

#O algoritmo verifica se existe algum número repetido no array nums, mas 
#com a restrição de que os índices dessas ocorrências devem ter uma diferença de, no máximo, k.

#Ele usa um dicionário (d) para armazenar a posição mais recente de cada número visto até o momento.
# Ao percorrer nums, verifica se o número já apareceu antes e se a diferença entre os índices é menor ou igual a k. Se for, retorna True. Caso contrário, atualiza a posição do número no dicionário.

#A complexidade temporal é O(n), pois percorre o array uma única vez, e a complexidade espacial também é O(n), no pior caso, se não houver duplicatas próximas.