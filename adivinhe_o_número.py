import random

print(
    'Adivinhe o número! (Aperte "Enter" com a caixa em branco para fechar o programa)\n'
'Coloque um número como o maximo e veja se você consegue adivinhar o número.\n')

while True:
 try:
  maximo = (input("Escolha um número maximo: "))
  if maximo == "":
   print("Obrigado por Jogar!")
   break
  while True:
   if maximo.isnumeric():
    break
   else:
    print("Digite um número.\n")
    break

  maximo = int(maximo)
  numero = random.randrange(maximo)
  #print(f"DEBUG: O número escolhido foi: {numero}")
  #tire ou coloque o # do print para ver a resposta antes de tentar. (estragando o jogo :( )
  tentativa = int(input(f"Digite um númedo de 0 a {maximo}: "))

  if tentativa == numero:
   print(f"Você Acertou! O número era {numero}\n")
  else:
   print(f"Você Errou! O número era {numero}\n")

 except:
  continue
