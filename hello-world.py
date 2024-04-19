coded_message = 'DrsCisCikxyDroBiwoCCkqoiDyiloiMYNONjicXPY,bcXKbOVgibRSaieKaiXYbiMYNON'
plain_message = 'this is another message to be CODED, UNFORTUNATELY THIS WAS NOT CODED'
alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ,'


def messageCoding(message, shift_lenght, coding=True):
    modified_message = ''
    for chr in message:
        if chr in alphabet:
            if coding:
                index = alphabet.find(chr) + shift_lenght
            else:
                index = alphabet.find(chr) - shift_lenght
            if index >= len(alphabet):
                index = index - len(alphabet)

            modified_message += alphabet[index]

        else:
            modified_message += chr

    else:
        return 'encoded message: {}'.format(modified_message)


print(messageCoding(coded_message, 10, coding=False))
