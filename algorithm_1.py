
def dec_method(encrypted_text : str):

    decrypted_text = ''

    for char in encrypted_text:

        char_aski = ord(char) // 11 
        char_decrypted = chr(char_aski)
        decrypted_text += char_decrypted

    return decrypted_text


def enc_method(text : str):

    encrypted_text = ''

    for char in text:

        char_aski = ord(char) * 11
        char_encrypted = chr(char_aski)
        encrypted_text += char_encrypted

    return encrypted_text