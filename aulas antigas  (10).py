lista_tel = []

while True:
    tel = input('Enter your number, [L]ist, [E]xit, [R]emove: ').strip()

    if tel.upper() == 'E':  # Sair
        print('You exited the list.')
        break

    elif tel.upper() == 'L':  # Listar
        if lista_tel:
            print(f'Here is your list: {lista_tel}')
        else:
            print('Your list is empty.')
        continue

    elif tel.upper() == 'R':  # Remover
        item = input('Enter the number to remove: ').strip()
        if item in lista_tel:
            lista_tel.remove(item)
            print(f'You removed {item}. Updated list: {lista_tel}')
        else:
            print(f'{item} is not in the list.')
        continue

    else:  # Adicionar
        if tel.isdigit():
            lista_tel.append(tel)
            print(f'{tel} was added to the list.')
        else:
            print('Please enter a valid number.')
