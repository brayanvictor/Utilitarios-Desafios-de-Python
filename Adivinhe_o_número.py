{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyO9yFgfcV8CjRLY4KFy9QO0"
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
        "id": "YW1DgYVCVeDG"
      },
      "outputs": [],
      "source": [
        "import random\n",
        "\n",
        "print(\n",
        "    'Adivinhe o número! (Aperte \"Enter\" com a caixa em branco para fechar o programa)\\n'\n",
        "'Coloque um número como o maximo e veja se você consegue adivinhar o número.\\n')\n",
        "\n",
        "while True:\n",
        " try:\n",
        "  maximo = (input(\"Escolha um número maximo: \"))\n",
        "  if maximo == \"\":\n",
        "   print(\"Obrigado por Jogar!\")\n",
        "   break\n",
        "  while True:\n",
        "   if maximo.isnumeric():\n",
        "    break\n",
        "   else:\n",
        "    print(\"Digite um número.\\n\")\n",
        "    break\n",
        "\n",
        "  maximo = int(maximo)\n",
        "  numero = random.randrange(maximo)\n",
        "  #print(f\"DEBUG: O número escolhido foi: {numero}\")\n",
        "  #tire ou coloque o # do print para ver a resposta antes de tentar. (estragando o jogo :( )\n",
        "  tentativa = int(input(f\"Digite um númedo de 0 a {maximo}: \"))\n",
        "\n",
        "  if tentativa == numero:\n",
        "   print(f\"Você Acertou! O número era {numero}\\n\")\n",
        "  else:\n",
        "   print(f\"Você Errou! O número era {numero}\\n\")\n",
        "\n",
        " except:\n",
        "  continue"
      ]
    }
  ]
}