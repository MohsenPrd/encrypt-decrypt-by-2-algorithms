import algorithm_1
import algorithm_2



while True:

    input_text = input('enter the text to encrypt: ')

    enc_algorithm = input('which algorithm to use?: ( 1 or 2 ) ')

    while enc_algorithm != '1' and enc_algorithm != '2':

        enc_algorithm = input('Invalid!! which algorithm to use?: ( 1 or 2 ) ')





    encrypted_text = ''

    if enc_algorithm == '1':

        encrypted_text = algorithm_1.enc_method(input_text)

    else:

        encrypted_text = algorithm_2.enc_method(input_text)


    print('\nthe encrypted text is: ' + encrypted_text+'\n')





    dec_algorithm = input('which algorithm to use for decryption? ( 1 or 2 ) ')

    while dec_algorithm != '1' and dec_algorithm != '2':

        dec_algorithm = input('Invalid!! which algorithm to use?: ( 1 or 2 ) ')


    decrypted_text = ''

    if dec_algorithm == '1':

        decrypted_text = algorithm_1.dec_method(encrypted_text)

    else:

        decrypted_text = algorithm_2.dec_method(encrypted_text)






    if dec_algorithm == enc_algorithm:

        print('\n---the decrypted text is: ' + decrypted_text+'\n')

    else:

        print('\n---you chose wrong decryption algorithm\n')
