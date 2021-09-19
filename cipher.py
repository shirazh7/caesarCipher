
# This is my Ceaser Cipher encryption program
# Written in python

def encryption():
    print("******** Encryption ********")

    msg = input("Enter message: ")
    key = int(input("Enter cipher key (0-25): "))

    encrypted_text = ""

    for i in range(len(msg)):
        if ord(msg[i]) == 32:  # ord() will give the ASCII of the space, which is 32
            # chr() will convert the ASCII back to characters
            encrypted_text += chr(ord(msg[i]))

        elif ord(msg[i]) + key > 122:  # after the Uppercase letters Lowercase end at 122
            # subtracting to get a lower integer then adding 96
            temp = (ord(msg[i]) + key) - 122
            encrypted_text += chr(96+temp)

        elif (ord(msg[i]) + key > 90) and (ord(msg[i]) <= 96):
            temp = ord(msg[i]) + key - 90
            encrypted_text += chr(64+temp)

        else:
            encrypted_text += chr(ord(msg[i]) + key)
    print("Your Encrypted Message is: " + encrypted_text)
    main()


def decryption():
    print("******** Decryption ********")

    encypt_msg = input("Enter message: ")
    decrypt_key = int(input("Enter cipher key (0-25): "))
    decrpted_message = ""

    for i in range(len(encypt_msg)):
        if ord(encypt_msg[i]) == 32:
            decrpted_message += chr(ord(encypt_msg[i]))

        elif ((ord(encypt_msg[i]) - decrypt_key) < 97) and ((ord(encypt_msg[i]) - decrypt_key) > 90):
            # subtract the key from ASCII and add 26
            temp = ord(encypt_msg[i])-decrypt_key+26
            decrpted_message += chr(temp)

        elif (ord(encypt_msg[i]) - decrypt_key) < 65:
            temp = (ord(encypt_msg[i]) - decrypt_key) - 26
            decrpted_message += chr(temp)

        else:
            decrpted_message += chr(ord(encypt_msg[i]) - decrypt_key)

    print("Your Decrypted Message is: " + decrpted_message)
    main()


def main():
    choice = int(input("1. Encryption\n2. Decrepytion\n3. Quit3\n Pick: "))

    if choice == 1:
        encryption()
    elif choice == 2:
        decryption()
    elif choice == 3:
        quit
    else:
        print("Invalid Input ")
        main()


main()
