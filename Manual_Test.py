def ASCII_To_Binary(ascii_string):
    """ Convert Ascii string into a binary string. """
    my_chars = ascii_string.split()
    bin_string = ''
    for value in my_chars:
        new_int = int(value)
        new_binary = bin(new_int)
        # removes the '0b' from the start of each binary
        new_binary = new_binary[2:]
        bin_string += "0" + str(new_binary)

    return bin_string


def Word_to_ascii(word):
    """ Turn a string into a string of ASCII values. """
    new_string = ''
    for i in word:
        if i.isalnum():
            j = ord(i)
            new_string += str(j) + " "

    return new_string


print("Testing an input using TAB and whitespace with ascii inputs")
word = str(input())
result = ASCII_To_Binary(word)
print(result)
""""""
