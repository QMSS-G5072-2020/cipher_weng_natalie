def cipher(text, shift, encrypt=True):
    """
    The cipher() function encrypts and decrypts text strings.

    Parameters:
    ===========================================================
    text: string ('example')
    shift: integer value (2,3,4)
    encrypt: True or False (default is True)

    Outputs:
    ===========================================================
    string

    Examples:
    ===========================================================
    >> cipher('example', 1)
    'fybnqmf'

    >> cipher('fybnqmf', -1, encrypt=False)
    'example'

    """
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text