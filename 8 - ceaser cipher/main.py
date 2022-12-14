from data import alphabet


def encode(shit):

    wor = input('what word do you want to encode')
    list_alphabet_number = []
    encodedword = ''

    for letter in wor:
        a = alphabet.index(letter)
        a += shit
        list_alphabet_number.append(a)

    for x in list_alphabet_number:
        encodedword += alphabet[x]
    print(encodedword)


def decode(shit):

    de = input('type the word')
    list_alphabet_number = []
    decodedword = ''

    for letter in de:
        a = alphabet.index(letter)
        a -= shit
        list_alphabet_number.append(a)

    for x in list_alphabet_number:
        decodedword += alphabet[x]
    print(decodedword)


while True:
    # logic game
    try:
        direction = input(' do you want decode oe encode .. ')
        shit = int(input('type the shit number'))

        if direction == 'encode':
            encode(shit)
        elif direction == 'decode':
            decode(shit)
        else:
            pass
    except:
        input('an error ocurred, try again')
        pass

