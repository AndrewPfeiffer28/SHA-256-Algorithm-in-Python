"""
This contains the basic rotate, shift and addition functions for hash operation 1
"""


def Bitwise_Add_Mod2_3ops(block1, block2, block3):
    """ Add three binary numbers together. """
    # our final block that will be reversed before returning
    sum_block = ''

    for i in range(len(block1) - 1, -1, -1):
        current_op = ''
        current_op += block1[i]
        current_op += block2[i]
        current_op += block3[i]

        # Bitwise addition of 3 numbers with all cases in the column
        if current_op == '000':
            sum_block += '0'
            print("0 part")
        elif current_op == '010' or current_op == '100' or current_op == '001':
            sum_block += '1'
            print("1 part")
        elif current_op == '110' or current_op == '101' or current_op == '011':
            sum_block += '0'
            print("2 part")
        elif current_op == '111':
            sum_block += '1'
            print("3 part")

    sum_block = sum_block[::-1]
    return sum_block


def Rotate(block, shift_amount):
    """ Rotate the block x number of times. """
    # Ensure the shift_amount is within the string length
    shift_amount %= len(block)

    # Split the string into two parts: characters to shift and remaining characters
    chars_to_shift = block[-shift_amount:]
    remaining_chars = block[:-shift_amount]

    # Concatenate the two parts in the shifted order
    shifted_string = chars_to_shift + remaining_chars
    return block


def Shift_Block(input_string, shift_size):
    """
    Shift characters in a string to the left by 3 '0's.
    """
    shift_string = '0' * shift_size
    input_string = input_string[:0] + shift_string + input_string[shift_size - 1:]
    return input_string


def Bitwise_Add_Mod2_2ops(block1, block2):
    """ Add two binary numbers together with carry-in. """
    # Our final block that will be reversed before returning
    sum_block = ''

    for i in range(len(block1) - 1, -1, -1):
        current_op = ''
        current_op += block1[i]
        current_op += block2[i]

        # Bitwise addition of 3 numbers with all cases in the column
        if current_op == '00':
            sum_block += '0'
        elif current_op == '01' or current_op == '10':
            sum_block += '1'
        elif current_op == '11':
            sum_block += '0'  # Carry-out, not '1'

    sum_block = sum_block[::-1]
    return sum_block


def Bitwise_Add_To_32(string1, string2):
    """ Add two binary numbers using mod 2**32. """
    # Convert binary strings to integers
    int_value1 = int(string1, 2)
    int_value2 = int(string2, 2)

    # Perform modulo 2 to the 32nd power
    result = (int_value1 + int_value2) % (2 ** 32)

    # Convert the result back to a binary string
    result_binary_string = bin(result)[2:]

    return result_binary_string

