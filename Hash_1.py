""" Start the initial hash switch of the algorithm.
"""
from Hash_1_operators import Bitwise_Add_Mod2_3ops, Shift_Block, Rotate, Bitwise_Add_Mod2_2ops, Bitwise_Add_To_32


def Import_Block():
    """ Import the padded block. """
    file1 = open('block.txt', 'r')
    lines = file1.readlines()
    return lines


def Create_M_Blocks(input_string):
    """ Break the block into 16 32 bit sections. """
    chunks = []

    for i in range(0, len(input_string), 32):
        chunk = input_string[i:i + 32]
        chunks.append(chunk)

    return chunks


def W_Blocks(w_block):
    """ Prepare the message schedule. """
    """
    t starts with 16
    """
    t = 16
    for i in range(16, 18):  # 16 to 64
        part1 = Sigma_1(w_block[i - 2])
        part2 = w_block[i - 7]
        part3 = Sigma_0(w_block[i - 15])
        part4 = w_block[i - 16]
        inter_op1 = Bitwise_Add_To_32(part1, part2)
        inter_op2 = Bitwise_Add_To_32(part3, part4)
        final_sum = Bitwise_Add_Mod2_2ops(inter_op1, inter_op2)
        # w_block[i] = final_sum
        print("the final sum")
        print(final_sum)

    return w_block


def Sigma_0(block):
    """ Perform rotate and shift functions on the block. """
    block1 = Rotate(block, 7)
    block2 = Rotate(block, 18)
    block3 = Shift_Block(block, 10)
    final_block = Bitwise_Add_Mod2_3ops(block1, block2, block3)
    return final_block


def Sigma_1(block):
    """ Perform rotate and shift functions on the block. """
    block1 = Rotate(block, 17)
    block2 = Rotate(block, 19)
    block3 = Shift_Block(block, 10)
    final_block = Bitwise_Add_Mod2_3ops(block1, block2, block3)
    return final_block


# 32 Bit block creation
my_block = Import_Block()
string_block = str(my_block[0])
M_Block = Create_M_Blocks(string_block)
message_block = W_Blocks(M_Block)
# W16-63 creation and calculation

print(string_block)
print(M_Block)
