
def guess_the_number():
    number_to_guess = 7  # Corrigido o nome da variável
    while True:
        guess = int(input('Guess the number between 1-10 (Type 0 to quit): '))  # Corrigido o texto
        if guess == 0:
            print('Goodbye!')
            break
        if guess == number_to_guess:
            print('You guessed it!')
            break  # Sai do loop ao acertar o número
        else:
            print('Try again!')

# Chamar a função corretamente
game_of_guess = guess_the_number
game_of_guess()










