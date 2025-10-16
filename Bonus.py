from Lab007 import key, alphabet, encrypt_vigenere, decrypt_vigenere

choice = 0
et_list = []
while choice !=4:
    choice = int(input("Enter you choice\n1). Encrypt\n, 2). Decrypt\n, 3). Dump\n, 4). Exit\n>> "))
    if not (1 <= choice <= 4):
        print("Invalid choice")
        continue
    if choice == 1:
        messages = input('what is your message:')
        et_list.append(encrypt_vigenere(key, messages, alphabet))
    elif choice == 2:
        for ct in et_list:
            print(decrypt_vigenere(key, ct, alphabet))
    elif choice == 3:
        for ct in et_list:
            print(ct)

