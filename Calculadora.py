{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyM1k1rkpeFNJJ1ZYwnwo+VX"
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
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "WgzPU4t0IyhC"
      },
      "outputs": [],
      "source": [
        "print('Calculadora em Phyton. Use +, -, * e / para fazer as operações.\\nEscreva \"sair\" para terminar o programa.\\n')\n",
        "\n",
        "while True:\n",
        " try:\n",
        "  sair = input(\"Digite o primeiro número: \") # input pro primeiro numero e tbm pra fechar o programa caso escreva 'sair'\n",
        "  if sair == \"sair\":\n",
        "   break\n",
        "  n1 = int(sair) # transforma o primeiro número em inteiro se vc não sair\n",
        "  while True:\n",
        "   op = input(\"Digite a operação: \") # negocinho pra não deixar vc digitar algo que não seja uma operação matematica\n",
        "   if op in [\"+\", \"-\", \"*\", \"/\"]: # operações aceitas\n",
        "    break\n",
        "   else:\n",
        "    print(\"Digite uma operação. Use +, -, * ou /.\\n\") # print pra caso vc digite algo que não é uma operação\n",
        "  n2 = int(input(\"Digite o segundo número: \")) # input pro segundo numero\n",
        "\n",
        "  if op == \"+\":       # tabelinha pras operações\n",
        "    result = n1 + n2\n",
        "  elif op == \"-\":\n",
        "    result = n1 - n2\n",
        "  elif op == \"*\":\n",
        "    result = n1 * n2\n",
        "  elif op == \"/\":\n",
        "    if n2 == 0:     # pra previnir de alguém tentar dividir um número por zero (crasha o programa se dividir)\n",
        "     print(n1, op, n2, \"= inválido\\nError: não tem como dividir por 0 zé ruela\\n\") # print pra caso vc tente dividir por zero\n",
        "     continue\n",
        "     result = n1 / n2\n",
        "  else:\n",
        "    result = n1 / n2\n",
        "    continue\n",
        "\n",
        "  print(n1, op, n2, \"=\", result, \"\\n\") # resultado da operação\n",
        "\n",
        " except ValueError: # negocio pra não parar o programa caso vc digite uma letra na parte de número\n",
        "  print(\"Digite um número.\\n\")\n",
        "  continue"
      ]
    }
  ]
}