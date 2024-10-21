from statistics import mean, median, mode

def calcular_estatisticas(numeros):
    try:
        media = mean(numeros)
        mediana = median(numeros)
        moda = mode(numeros)
        
        print(f"Média: {media}")
        print(f"Mediana: {mediana}")
        print(f"Moda: {moda}")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Função para receber a entrada de números do usuário
def entrada_de_numeros():
    while True:
        try:
            # Receber os números separados por espaço
            numeros_str = input("Digite uma lista de números separados por espaço: ")
            # Converter para uma lista de inteiros ou floats
            numeros = [float(x) for x in numeros_str.split()]
            return numeros
        except ValueError:
            print("Por favor, digite apenas números.")

# Exemplo de uso
numeros = entrada_de_numeros()
calcular_estatisticas(numeros)
