print('*********************************')
print('Bem vindo, ao JOGO DE ADIVINHAÇÃO')
print('*********************************')

#Definindo o numero secreto
numeroSecreto = 38

#definindo o numero de tentativas
numerosTentativas = 3

while(numerosTentativas > 0):
    print('ok')

#Recebendo o cute do jogador
    chuteString = input('Digite um número: ')
    print('Você digitou o número', chuteString)
    chute = int(chuteString)

#Declaraçao as condicões
    if numeroSecreto == chute:
        print('Você acertou!')
    elif(chute>numeroSecreto):
        print('Você errou!! O número secreto é um número menor')
    else:
        print('Você errou!! O número secreto é um número maior')
