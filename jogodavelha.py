def imprime_tabuleiro(tabuleiro):
    i = 0
    for espaco in range(len(tabuleiro)):
        print(tabuleiro[espaco], end= " ")
        i += 1
        if i == 1 or i == 2 or i == 4 or i == 5 or i == 7 or i == 8:
            print(" | ", end= " ")
        if i == 3 or i == 6 or i == 9:
            print("", end = " ")
        if espaco == 2 or espaco == 5:
            print(" ")

def verifica_tabuleiro(tabuleiro, jogador):
  #Checando se o jogador ganhou
  
  #Checando as linhas
    if tabuleiro[0] == jogador and tabuleiro[1] == jogador and tabuleiro[2] == jogador:
        if jogador == simbolo_jogador1:
            return 1
        else:
            return 2
    if tabuleiro[3] == jogador and tabuleiro[4] == jogador and tabuleiro[5] == jogador:
        if jogador == simbolo_jogador1:
            return 1
        else:
            return 2
    if tabuleiro[6] == jogador and tabuleiro[7] == jogador and tabuleiro[8] == jogador:
        if jogador == simbolo_jogador1:
            return 1
        else:
            return 2
  
  #Checando as colunas
    if tabuleiro[0] == jogador and tabuleiro[3] == jogador and tabuleiro[6] == jogador:
        if jogador == simbolo_jogador1:
            return 1
        else:
            return 2
    if tabuleiro[1] == jogador and tabuleiro[4] == jogador and tabuleiro[7] == jogador:
        if jogador == simbolo_jogador1:
            return 1
        else:
            return 2
    if tabuleiro[2] == jogador and tabuleiro[5] == jogador and tabuleiro[8] == jogador:
        if jogador == simbolo_jogador1:
            return 1
        else:
            return 2
  
  #Checando as diagonais
    if tabuleiro[0] == jogador and tabuleiro[4] == jogador and tabuleiro[8] == jogador:
        if jogador == simbolo_jogador1:
            return 1
        else:
            return 2
    if tabuleiro[2] == jogador and tabuleiro[4] == jogador and tabuleiro[6] == jogador:
        if jogador == simbolo_jogador1:
            return 1
        else:
            return 2
        
    return 0

def verifica_ganhador(vencedor):
    if vencedor == 1:
        print("\n\nParabéns Jogador 1, você ganhou!\n")
    elif vencedor == 2:
        print("\nParabéns Jogador 2, você ganhou!\n")
    else:
        print("\nDeu empate!\n")

def reiniciar_tabuleiro():
    global tabuleiro
    global turnos 
    tabuleiro = [" "] * 9
    turnos = 0
    return tabuleiro, turnos

def imprime_instrucoes():
    print("\n################### JOGO DA VELHA ###################")
    print("\nSiga as instruções abaixo\n")
    print("Você vai jogar contra uma máquina")
    print("Ganha quem conseguir uma sequência de X ou O, em linha ou na diagonal")
    print("Veja abaixo como funciona o tabuleiro\n")
    print("1 | 2 | 3")
    print("4 | 5 | 6")
    print("7 | 8 | 9")
    print("\nComo jogar?\n")
    print("escolha_jogador1 um número de 1 a 9 para marcar na tabela com seu símbolo escolhido")
    print("Veja um exemplo\n")
    print("Qual é a sua jogada? 5\n")
    print("1 | 2 | 3")
    print("4 | X | 6")
    print("7 | 8 | 9")
    print("\nEm seguida, a máquina jogará\n")
    print("1 | 2 | O")
    print("4 | X | 6")
    print("7 | 8 | 9\n")
    print("Vamos começar!")

def escolher_simbolo():
    global simbolo_jogador2 
    global simbolo_jogador1
    simbolo_jogador1 = " "
    simbolo_jogador2 = " "
    simbolo = " "
    while simbolo != "X" and simbolo !=  "O":
        print("\nVocê quer ser X ou O? ")
        simbolo = input().upper()
        if simbolo == "X":
            simbolo_jogador1 = "X"
            simbolo_jogador2 = "O"
        elif simbolo == "O":
            simbolo_jogador2 = "X"
            simbolo_jogador1 = "O"
        else:
            print("Comando inválido. Tente X ou O.")
    return simbolo_jogador1, simbolo_jogador2

turnos = 0
tabuleiro = [" "] * 9
jogando = True
vencedor = 0
pontuacao_jogador1 = 0
pontuacao_jogador2 = 0

imprime_instrucoes()

escolher_simbolo()

while jogando:

    print("\nÉ a vez do jogador 1")
    escolha_jogador1 = int(input("\n\nQual é a sua jogada? "))
    while tabuleiro[escolha_jogador1-1] != " " or escolha_jogador1 > 9 :
        print("Espaço já preenchido. Tente outra jogada!")
        escolha_jogador1 = int(input("Qual é a sua jogada? "))
    print("\n################### PARTIDA ###################\n")
    tabuleiro[escolha_jogador1-1] = simbolo_jogador1
    turnos += 1

    #Função para retornar um valor que resultará na vitória do jogador ou da máquina
    
    vencedor = verifica_tabuleiro(tabuleiro, simbolo_jogador1)
    imprime_tabuleiro(tabuleiro)
    
    #Se for 1, entrará na condição e quebrará o laço while, dando a vitória pro jogador
    if vencedor != 0:
        verifica_ganhador(vencedor)
        pontuacao_jogador1 += 1
        print("\nDesejar continuar jogando? (1 pra Sim ou 0 pra não)")
        continuar_jogando = int(input())
        if continuar_jogando == 1:
            reiniciar_tabuleiro()
            escolher_simbolo()
        elif continuar_jogando == 0:
            print("\nEncerrando jogo...")
            break

    if turnos == 9:
        verifica_ganhador(vencedor)
        imprime_tabuleiro(tabuleiro)
        print("\nDesejar continuar jogando? (1 pra Sim ou 0 pra não)")
        continuar_jogando = int(input())
        if continuar_jogando == 1:
            reiniciar_tabuleiro()
            escolher_simbolo()
        elif continuar_jogando == 0:
            print("\nEncerrando jogo...")
            break

    print("\nÉ a vez do jogador 2")
    escolha_jogador2 = int(input("\n\nQual é a sua jogada? "))
    while tabuleiro[escolha_jogador2 - 1] != " ":
        escolha_jogador2 = int(input("\n\nQual é a sua jogada? "))
    print("\n################### PARTIDA ###################\n")
    tabuleiro[escolha_jogador2-1] = simbolo_jogador2
    
    turnos += 1

    vencedor = verifica_tabuleiro(tabuleiro, simbolo_jogador2)
    imprime_tabuleiro(tabuleiro)

    #Se for 2, entrará na condição e quebrará o laço while, dando a vitória pra máquina
    if vencedor != 0:
        verifica_ganhador(vencedor)
        pontuacao_jogador2 += 1
        print("\nDesejar continuar jogando? (1 pra Sim ou 0 pra não)")
        continuar_jogando = int(input())
        if continuar_jogando == 1:
            reiniciar_tabuleiro()
            escolher_simbolo()
        elif continuar_jogando == 0:
            print("\nEncerrando jogo...")
            break

    if turnos == 9:
        verifica_ganhador(vencedor)
        print("\nDesejar continuar jogando? (1 pra Sim ou 0 pra não)")
        continuar_jogando = int(input())
        if continuar_jogando == 1:
            reiniciar_tabuleiro()
            escolher_simbolo()
        elif continuar_jogando == 0:
            print("\nEncerrando jogo...")
            break


print(f"\nPontuação do jogador 1: {pontuacao_jogador1}\nPontuação do jogador 2: {pontuacao_jogador2}")


    



    