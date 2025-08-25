print('Contator de Letras e Vogais.\n(Aperte "Enter" com a caixa em branco para fechar o programa)\n')

while True:
  palavra = input("Digite uma palavra: ")
  if palavra == "":
    print("Obrigado por utilizar meu código!")
    break
  cvogais = 0
  cconsoantes = 0

  for vogais in palavra:
    if vogais.lower() in "aeiou":
     cvogais += 1

  for consoantes in palavra:
    if consoantes.lower() in "bcdfghjklmnpqrstvwxyz":
     cconsoantes += 1

  cletras = cvogais + cconsoantes

  print(f"Essa palavra tem {cletras} letras, {cvogais} vogais e {cconsoantes} consoantes\n")
  continue
