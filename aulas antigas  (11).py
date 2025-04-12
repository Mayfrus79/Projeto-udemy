import random

# Função para validar a entrada do usuário
def obter_numero_usuario():
    while True:
        try:
            numero = int(input("Digite um número entre 1 e 100: "))
            if 1 <= numero <= 100:
                return numero
            else:
                print("Por favor, digite um número dentro do intervalo de 1 a 100.")
        except ValueError:
            print("Valor inválido! Por favor, insira um número inteiro.")

# Função principal do jogo de adivinhação
def jogar_adivinhacao():
    numero_secreto = random.randint(1, 100)  # Número aleatório entre 1 e 100
    tentativas = 0
    acerto = False

    print("Bem-vindo ao Jogo de Adivinhação!")
    print("Tente adivinhar o número secreto entre 1 e 100.")

    while not acerto:
        numero_usuario = obter_numero_usuario()  # Pede o número ao usuário
        tentativas += 1

        if numero_usuario < numero_secreto:
            print("O número secreto é maior!")
        elif numero_usuario > numero_secreto:
            print("O número secreto é menor!")
        else:
            acerto = True
            print(f"Parabéns! Você acertou o número secreto em {tentativas} tentativas!")

    print("\n Agora, vamos ver o histórico das tentativas.")

    # Mostra as tentativas do jogador (para fins de exemplo, estou gerando aleatoriamente tentativas anteriores)
    print("Tentativas anteriores:")
    for i in range(1, tentativas + 1):
        tentativa = random.randint(1, 100)  # Tentativas aleatórias (isso pode ser modificado conforme desejado)
        print(f"Tentativa {i}: {tentativa}")

# Chama a função para rodar o jogo
if __name__ == "__main__":
    jogar_adivinhacao()
