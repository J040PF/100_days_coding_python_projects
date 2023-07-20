import random

senha = []
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


senha_letters = int(input('how many letters would you like ?'))
senha_numbers = int(input('how many numbers would you like ?'))
senha_symbols = int(input('how many symbols would you like ?'))

for x in range(1, senha_letters + 1):
    senha.append(random.choice(letters))

for x in range(1, senha_numbers + 1):
    senha.append(random.choice(numbers))

for x in range(1, senha_symbols + 1):
    senha.append(random.choice(symbols))


random.shuffle(senha)

print(f'Your password is : {"".join(senha)}')