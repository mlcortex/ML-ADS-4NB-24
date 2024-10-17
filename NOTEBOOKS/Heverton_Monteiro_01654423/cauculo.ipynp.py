from statistics import mean, median, mode
from typing import List, Union

def calcular_estatisticas(lista: List[float]) -> dict:
    """Calcula a média, mediana e moda de uma lista de números.

    Args:
        lista: Uma lista de números.

    Returns:
        Um dicionário contendo a média, mediana e moda da lista.
    """

    try:
        media = mean(lista)
        mediana = median(lista)
        moda = mode(lista)
    except StatisticsError:
        moda = "Sem moda única (ou seja, mais de um valor tem a mesma frequência máxima)."

    return {
        'média': media,
        'mediana': mediana,
        'moda': moda
    }

# Exemplo de uso:
lista_numeros: List[float] = [1, 2, 3, 4, 4, 5, 5, 5, 6]
resultado = calcular_estatisticas(lista_numeros)

print(f"Média: {resultado['média']}")
print(f"Mediana: {resultado['mediana']}")
print(f"Moda: {resultado['moda']}")