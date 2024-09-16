{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "intro-markdown"
      },
      "source": [
        "# Análise Estatística da Lista de Valores\n",
        "\n",
        "Neste notebook, analisaremos a seguinte lista de números:\n",
        "\n",
        "```python\n",
        "valores = [4, 6, 3, 4, 5, 8, 4, 2]\n",
        "```\n",
        "\n",
        "Calcularemos as seguintes informações:\n",
        "1. Valor máximo\n",
        "2. Valor mínimo\n",
        "3. Média aritmética dos valores\n",
        "4. Mediana dos valores\n",
        "5. Desvio padrão dos valores"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "8DyF0FHS0brG"
      },
      "outputs": [],
      "source": [
        "import math\n",
        "\n",
        "valores = [4, 6, 3, 4, 5, 8, 4, 2]\n",
        "\n",
        "def getMaxValue(array):\n",
        "    maxValue = None\n",
        "    for value in array:\n",
        "        if maxValue == None:\n",
        "            maxValue = value\n",
        "        elif maxValue < value:\n",
        "            maxValue = value\n",
        "    return maxValue\n",
        "\n",
        "def getMinValue(array):\n",
        "    minValue = None\n",
        "    for value in array:\n",
        "        if minValue == None:\n",
        "            minValue = value\n",
        "        elif minValue > value:\n",
        "            minValue = value\n",
        "    return minValue\n",
        "\n",
        "def getAvgValue(array):\n",
        "    avgValue = 0\n",
        "    for value in array:\n",
        "        avgValue += value\n",
        "    return avgValue / len(array)\n",
        "\n",
        "def getMedianValue(array):\n",
        "    array.sort()\n",
        "    if (len(array) + 1) % 2 == 0:\n",
        "        return array[((len(array) + 1) // 2) - 1]\n",
        "    else:\n",
        "        nPosition = len(array) // 2\n",
        "        firstElement = array[nPosition - 1]\n",
        "        secondElement = array[nPosition]\n",
        "        return getAvgValue([firstElement, secondElement])\n",
        "\n",
        "def getStandardDeviation(array, sample=False):\n",
        "    avg = getAvgValue(array)\n",
        "    length = len(array)\n",
        "    squaredSum = 0\n",
        "    for value in array:\n",
        "        difference = value - avg\n",
        "        squaredSum += difference ** 2\n",
        "    \n",
        "    if sample:\n",
        "        variance = squaredSum / (length - 1)\n",
        "    else:\n",
        "        variance = squaredSum / length\n",
        "    \n",
        "    return math.sqrt(variance)\n",
        "\n",
        "# Calculando e imprimindo os resultados\n",
        "print(f\"1. Valor máximo: {getMaxValue(valores)}\")\n",
        "print(f\"2. Valor mínimo: {getMinValue(valores)}\")\n",
        "print(f\"3. Média aritmética: {getAvgValue(valores):.2f}\")\n",
        "print(f\"4. Mediana: {getMedianValue(valores)}\")\n",
        "print(f\"5. Desvio padrão: {getStandardDeviation(valores):.3f}\")"
      ]
    }
  ]
}
