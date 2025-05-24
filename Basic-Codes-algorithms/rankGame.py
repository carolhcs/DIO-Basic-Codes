
rank = ""
Wins = int(input("Digite o número de vitórias do jogador: "))
Loses = int(input("Digite o número de derrotas do jogador: "))

def calcule_points(playerWins, playerLoses):
    return playerWins - playerLoses

def rank_game(playerWins, playerLoses):
    points = calcule_points(playerWins, playerLoses)
    if points < 11:
        rank = "Ferro"
    elif points < 21:
        rank = "Bronze"
    elif points < 51:
        rank = "Prata"
    elif points < 81:
        rank = "Ouro"
    elif points < 91:
        rank = "Diamante"
    elif points < 101:
        rank = "Lendário"
    else:
        rank = "Imortal"
    print(f"O Herói tem de saldo de {points} está no nível de {rank}")


rank_game(Wins, Loses)