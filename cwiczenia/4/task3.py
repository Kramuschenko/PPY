def caesar_cipher(message, klucz, alphabet='abcdefghijklmnopqrstuvwxyz'):
    message = message.lower()
    alphabet = alphabet.lower()
    klucz = klucz % len(alphabet)
    result = ""
    for litera in message:
        if litera in alphabet:
            literaIndex = alphabet.index(litera)
            resultIndex = (literaIndex + klucz) % len(alphabet)
            result += alphabet[resultIndex]
        else:
            result += litera

    return result

print(caesar_cipher('test message', 20))