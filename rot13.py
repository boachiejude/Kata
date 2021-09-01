def rot13(string):
    alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] * 5
    cipher = ''
    for alphabet in string:
        if alphabet.lower() not in alphabet_list:
            cipher += alphabet
            continue
        elif alphabet.isupper():
            cipher += (alphabet_list[alphabet_list.index(alphabet.lower()) + 13]).upper()
            continue
        cipher += alphabet_list[alphabet_list.index(alphabet.lower()) + 13]
    return cipher