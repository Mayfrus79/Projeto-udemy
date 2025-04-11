
person = {
    'name': 'Maykon',
    'age': 30,
    'city': 'Ney York'}
print(person['name'])
print(person['age'])
person['email'] = 'alice@example.com.br'
person['age'] = 32
del person['city']
print('name' in person)
print('city' in person)
for key, value in person.items():
    print(f'{key}: {value}')

