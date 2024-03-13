print('*********************************')
print('Bem vindo, ao JOGO DE ADIVINHAÇÃO')
print('*********************************')

#Definindo o numero secreto
numeroSecreto = 38

#definindo o numero de tentativas
numerosTentativas = 3
rodada = 1

while(rodada <= numerosTentativas):

    print('tentativa' ,rodada, 'de', numerosTentativas)

#Recebendo o cute do jogador
    chuteString = input('Digite um número: ')
    
    chute = int(chuteString)

#Declaraçao as condicões
    if (numeroSecreto == chute):
        print('Você acertou!')
        break
    elif(chute>numeroSecreto):
        print('Você errou!! O número secreto é um número menor')
    else:
        print('Você errou!! O número secreto é um número maior')

    #numerosTentativas = numerosTentativas - 1
        rodada = rodada + 1
