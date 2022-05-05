from hashlib import new


def reverse_words(text):
    list = text.split(" ")
    print(list)
    indice = 0
    revertir = lambda cadena: cadena[::-1]
    for palabra in list:
        palabra[indice] = revertir(palabra)
    print(list)

test = 'the lazy dog.'

reverse_words(test)