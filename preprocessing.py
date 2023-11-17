"""
Andrew Pfeiffer
9/14/2023

The goal of this is to turn a string into a processed and read 512 bit long
binary string ready for SHA-256 hashing.

"""

#my_message = "RedBlockBlue"
my_message = "012100"


def Word_to_ascii(word):
    """ Turn a string into a string of ASCII values. """
    new_string = ''
    for i in word:
        if i.isalnum():
            j = ord(i)
            new_string += str(j) + " "

    return new_string


ascii_value = Word_to_ascii(my_message)


# print(ascii_value)


def ASCII_To_Binary(ascii_string):
    """ Convert 7-bit Ascii string into an 8-bit binary string. """
    my_chars = ascii_string.split()
    bin_string = ''
    for value in my_chars:
        new_int = int(value)
        new_binary = bin(new_int)

        # Remove the '0b' header
        new_binary = new_binary[2:]

        # Add a '0' to the start of every 7-bit number (7 -> 8-bit)
        bin_string += "0" + str(new_binary)

    return bin_string


def Padding(bin_string):
    """ Pad the number into a 512 bit (character) long string. """

    message_len = len(bin_string)
    message_len = bin(message_len)
    message_len = message_len[2:]

    # Ensure the message length pad is 8 char long
    while len(message_len) < 8:
        message_len = "0" + message_len

    # print("message len")
    # print(message_len)

    bin_string = bin_string + "1"
    pad_size = 512 - len(bin_string) - 64
    # print(pad_size)
    # FIXME make the message length dynamic at the end so 8 + 48 does not have to be done
    bin_string = bin_string + '0' * (pad_size + 48)
    bin_string = bin_string + '0' * len(message_len)

    bin_string = bin_string + str(message_len)

    return bin_string


def Export_Block_To_File(new_block):
    """ Store the block in the file. """

    # Define the file path (replace 'file.txt' with your file's path)
    file_path = 'block.txt'

    # Open the file in append mode ('a' for append)
    with open(file_path, 'w') as file:
        # Append the string to the file
        file.write(new_block)


result = ASCII_To_Binary(ascii_value)
Padded_Block = Padding(result)

# only binary message
# print(result)

# binary message with the padding
print("The padded block:")
print(Padded_Block)
Export_Block_To_File(Padded_Block)
