coded_message = 'ghfrglqj wklv phvvdjh grhv qhhg d olwwoh sdwlhqfh dqg d olwwoh elw ri lpdjlqdwlrq, l glg qrw xvh fdslwdo ohwwhuv lq rughu wr dyrlg lqfuhdvlqj wkh frpsohalwb'
another_message = "\\ this is ANOTHER MESSAGE, PLEASE__CODE, is  coded, \"let's\" say XYLOPHONE xylophone, 200$"


alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFHIJKLMNOPQRSTUVWXYZ0123456789 ,\'_$"\\'


def messageCoding(message, shift_position, coding=1):
    modified_message = ''
    for chr in message:
        if chr in alphabet:
            if coding:
                index = alphabet.find(chr) + shift_position
            else:
                index = alphabet.find(chr) - shift_position

            if index >= len(alphabet):
                index = index - len(alphabet)
            modified_message += alphabet[index]
        else:
            modified_message += chr
    else:
        return modified_message


print(messageCoding(another_message, 3, True))
