#  Dada uma string, encontrar o comprimento da maior substring sem caracteres repetidos.

letra = input("Digite um conjunto de letras\n").upper()

conjunto = ''
maior_conjunto = ''

for i in range(len(letra)):
    if not (letra[i] in conjunto):
        conjunto += letra[i]
    else:
        if (len(conjunto) > len(maior_conjunto)):
            maior_conjunto = conjunto

        conjunto = letra[i]

print(f"\nResposta: {maior_conjunto}, de tamanho {len(maior_conjunto)}")