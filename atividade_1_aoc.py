# Nome: Daniel Fortunato de Castro
# RA: 2920482021036

# Arquitetura e Organização de Computadores
# Atividade 1 - Conversor de base numérica
# Binário, Decimal e Hexadecimal

print('''ÍNDICE DE CONVERSÃO:
[1] converter número DECIMAL
[2] converter número BINÁRIO
[3] converter número HEXADECIMAL''')

conversao = int(input("Selecione o tipo do valor: "))

# Decimal
if (conversao == 1):
    valor = int(input("Digite o valor: "))
    BIN = bin(valor)
    HEX = hex(valor)
    print("DEC: %i" % valor)
    print("BIN: %s" % BIN[2:])
    print("HEX: %s" % HEX[2:])
        
# Binário
elif (conversao == 2):

    valor = input("Digite o valor: ")

    L = []
    DEC = 0
    p = 0

    for i in valor:
        L.insert(0, int(i))

    for x in L:
        DEC = DEC+(x * 2**p)
        p += 1

    BIN = bin(DEC)
    HEX = hex(DEC)

    print("DEC: %i" % DEC)
    print("BIN: %s" % BIN[2:])
    print("HEX: %s" % HEX[2:])

# Hexadecimal
elif (conversao == 3):

    valor = input("Digite o valor: ")

    L = []
    DEC = 0
    p = 0

    for i in valor:

        if i == 'a':
            i = 10
        elif i == 'b':
            i = 11
        elif i == 'c':
            i = 12
        elif i == 'd':
            i = 13
        elif i == 'e':
            i = 14
        elif i == 'f':
            i = 15
        L.insert(0, int(i))

    for x in L:
        DEC = DEC+(x * 16**p)
        p += 1

    BIN = bin(DEC)
    HEX = hex(DEC)

    print("DEC: %i" % DEC)
    print("BIN: %s" % BIN[2:])
    print("HEX: %s" % HEX[2:])

else: print("Valor inválido!")