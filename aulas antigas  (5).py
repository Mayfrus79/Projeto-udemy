while True:
    username = input('Digite seu nome completo: ')
    if len(username) > 12:
        print('Username não pode conter mais do que 12 characteres!')
        continue

    elif ' ' in username:
        print('Username não pode conter espaços!')
        continue

    elif any(char.isdigit() for char in username):
        continue

    print('Username Válido!')


    