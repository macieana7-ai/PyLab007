key = 'DAVINCI'
alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ '
#alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
alpha_len = len(alphabet)

def pretty_print(vsq: list):
    for i, row in enumerate (vsq):
        print(f'| {' | '.join(row)} |')
        if i == 0:
             suffix = '---|'*(alpha_len+1)
             print(f'|{suffix}')


def print_header():
    header = [' ']
    #print('|   |', end='')
    for a in alphabet:
        #print(f' {a} |', end='')
        header.append(a)
    #print()
    #suffix = '---|'*(alpha_len+1)
    #print(f'|{suffix}')

def print_row(a:int):
    row = []
    for c in range (alpha_len):
        row.append(alphabet[(c + a) % alpha_len])
        #print(f '{alphabet[(c + a)% alpha_len]} |', end="")
    #print()
    return row

def vigenere_sq():
    sq = []
    header = print_header()
    sq.append(header)
    for a in range(alpha_len):
        #print(f'| {alphabet[a]} |', end='')
        row = print_row(a)
        row.insert(0, [a])
        sq.append(row)
        #print(row)
    return sq

def letter_to_index(letter:str, alphabet:str) -> int:
    for i, c in enumerate(alphabet):
        if letter == c:
            #print(i, c)
            return i
    return -1

def index_to_letter(index:int, alphabet:str) -> str:
    if 0 <= index < alpha_len:
        return alphabet[index]
    return None

def encrypt_vigenere(key, plaintext, alphabet):
    cipher_text = []
    for i, pt in enumerate(plaintext):
        #print(i, pt, key[i%len(key)])
        cipher_text.append(vigenere_index(key[i%len(key)], pt, alphabet))
    return ''.join(cipher_text)

def vigenere_index(key_letter:str,plaintext_letter:str, alphabet:str):
    # C = (K + P) % AL
    ci = (letter_to_index(key_letter, alphabet) + letter_to_index(plaintext_letter, alphabet)) % alpha_len
    return index_to_letter(ci, alphabet)

def undo_vigenere_index(key_letter:str, cipher_letter:str, alphabet:str) -> str:
    #P= (C - K) % AL
    pi = (letter_to_index(cipher_letter, alphabet) - letter_to_index(key_letter, alphabet)) % alpha_len
    return index_to_letter(pi, alphabet)

def decrypt_vigenere(key, ciphertext, alphabet):
    plain_text = []
    for i, ct in enumerate(ciphertext):
        plain_text.append(undo_vigenere_index(key[i%len(key)], ct, alphabet))
    return ''.join(plain_text)

def main():
    # pretty_print(vigenere_sq())
    # print(letter_to_index('Z', alphabet))
    # print(index_to_letter('27', alphabet))

    plain_text = 'THE EAGLE HAS LANDED'
    # print(vigenere_index('D','T', alphabet))
    et = encrypt_vigenere(key, plain_text, alphabet)
    pt = decrypt_vigenere(key, et, alphabet)
    print(et, pt)

    # kl =len(key)
    # for i in range(20):
    #    print(i, i % kl, key[i % kl])


if __name__ == '__main__':
    main()