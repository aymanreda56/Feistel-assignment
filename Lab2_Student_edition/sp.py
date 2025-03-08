import numpy as np
import math

"""

██████╗  ██████╗     ███╗   ██╗ ██████╗ ████████╗    ████████╗ ██████╗ ██╗   ██╗ ██████╗██╗  ██╗
██╔══██╗██╔═══██╗    ████╗  ██║██╔═══██╗╚══██╔══╝    ╚══██╔══╝██╔═══██╗██║   ██║██╔════╝██║  ██║
██║  ██║██║   ██║    ██╔██╗ ██║██║   ██║   ██║          ██║   ██║   ██║██║   ██║██║     ███████║
██║  ██║██║   ██║    ██║╚██╗██║██║   ██║   ██║          ██║   ██║   ██║██║   ██║██║     ██╔══██║
██████╔╝╚██████╔╝    ██║ ╚████║╚██████╔╝   ██║          ██║   ╚██████╔╝╚██████╔╝╚██████╗██║  ██║
╚═════╝  ╚═════╝     ╚═╝  ╚═══╝ ╚═════╝    ╚═╝          ╚═╝    ╚═════╝  ╚═════╝  ╚═════╝╚═╝  ╚═╝
                                                                                                
████████╗██╗  ██╗██╗███████╗     ██████╗ ██████╗ ██████╗ ███████╗                               
╚══██╔══╝██║  ██║██║██╔════╝    ██╔════╝██╔═══██╗██╔══██╗██╔════╝                               
   ██║   ███████║██║███████╗    ██║     ██║   ██║██║  ██║█████╗                                 
   ██║   ██╔══██║██║╚════██║    ██║     ██║   ██║██║  ██║██╔══╝                                 
   ██║   ██║  ██║██║███████║    ╚██████╗╚██████╔╝██████╔╝███████╗                               
   ╚═╝   ╚═╝  ╚═╝╚═╝╚══════╝     ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝                               
                                                                                                
                                                                                                

 ██████╗ ██████╗     ███████╗██╗   ██╗███████╗██████╗ ██╗   ██╗████████╗██╗  ██╗██╗███╗   ██╗ ██████╗ 
██╔═══██╗██╔══██╗    ██╔════╝██║   ██║██╔════╝██╔══██╗╚██╗ ██╔╝╚══██╔══╝██║  ██║██║████╗  ██║██╔════╝ 
██║   ██║██████╔╝    █████╗  ██║   ██║█████╗  ██████╔╝ ╚████╔╝    ██║   ███████║██║██╔██╗ ██║██║  ███╗
██║   ██║██╔══██╗    ██╔══╝  ╚██╗ ██╔╝██╔══╝  ██╔══██╗  ╚██╔╝     ██║   ██╔══██║██║██║╚██╗██║██║   ██║
╚██████╔╝██║  ██║    ███████╗ ╚████╔╝ ███████╗██║  ██║   ██║      ██║   ██║  ██║██║██║ ╚████║╚██████╔╝
 ╚═════╝ ╚═╝  ╚═╝    ╚══════╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝ 
                                                                                                      
██╗    ██╗██╗██╗     ██╗         ███████╗██╗  ██╗██████╗ ██╗      ██████╗ ██████╗ ███████╗            
██║    ██║██║██║     ██║         ██╔════╝╚██╗██╔╝██╔══██╗██║     ██╔═══██╗██╔══██╗██╔════╝            
██║ █╗ ██║██║██║     ██║         █████╗   ╚███╔╝ ██████╔╝██║     ██║   ██║██║  ██║█████╗              
██║███╗██║██║██║     ██║         ██╔══╝   ██╔██╗ ██╔═══╝ ██║     ██║   ██║██║  ██║██╔══╝              
╚███╔███╔╝██║███████╗███████╗    ███████╗██╔╝ ██╗██║     ███████╗╚██████╔╝██████╔╝███████╗            
 ╚══╝╚══╝ ╚═╝╚══════╝╚══════╝    ╚══════╝╚═╝  ╚═╝╚═╝     ╚══════╝ ╚═════╝ ╚═════╝ ╚══════╝            
"""

def fixed_s_box(value):
    """Fixed S-box (substitution step)"""
    s_box = {
        0x0: 0xE, 0x1: 0x4, 0x2: 0xD, 0x3: 0x1,
        0x4: 0x2, 0x5: 0xF, 0x6: 0xB, 0x7: 0x8,
        0x8: 0x3, 0x9: 0xA, 0xA: 0x6, 0xB: 0xC,
        0xC: 0x5, 0xD: 0x9, 0xE: 0x0, 0xF: 0x7
    }
    return s_box[value]

def fixed_p_box(value):
    """Fixed P-box (permutation step)"""
    perm = [2, 4, 1, 3, 0, 6, 5, 7]  # Example permutation
    binary = format(value, '08b')  # Convert to 8-bit binary
    permuted = ''.join(binary[perm[i]] for i in range(8))
    return int(permuted, 2)

def sp_network_one_block(block, rounds=4):
    """Fixed S-P network processing"""
    state = block
    for _ in range(rounds):
        substituted = (fixed_s_box((state >> 4) & 0xF) << 4) | fixed_s_box(state & 0xF)
        state = fixed_p_box(substituted)
    return state


def truncated_xor (bin_msg, key):
    bin_key = bin(key)
    if(len(bin_key) > len(bin_msg)):
        new_key = bin_key[len(bin_key) - len(bin_msg):]
    elif(len(bin_key) < len(bin_msg)):
        new_key = bin_key.zfill(len(bin_msg))
    else:
        new_key = bin_key
    
    xor = int(bin_msg, 2) ^ int(bin_key, 2)
    return bin(xor)[2:].zfill(len(bin_msg))

def SP_Network(message, key, rounds=4):
    """Process an arbitrary-length message split into 8-bit blocks"""
    binary_message = bin(message)[2:]
    binary_message = truncated_xor(binary_message, key)
    block_nums = len(binary_message) / 8
    if(block_nums - int(block_nums) != 0.0):
        block_nums = int(block_nums) + 1
    else: block_nums = int(block_nums)
    processed_blocks = []
    for block_idx in range(block_nums):
        if(block_idx == block_nums - 1):
            block = binary_message[block_idx*8:]
            block.zfill(8)
        else:
            block = binary_message[block_idx*8: (block_idx+1)*8]
    
        processed_block = sp_network_one_block(int(block, 2), rounds)
        processed_blocks.append(bin(processed_block)[2:].zfill(8))
    
    final_obj = "".join(processed_blocks)
    # print(f"DEBUG: {final_obj}")
    # print(f"DEBUG: {len(bin(message)[2:])}")
    if(len(final_obj) > len(bin(message)[2:])):
        final_obj = final_obj[len(final_obj) -len(bin(message)[2:])  :]
    elif(len(final_obj) < len(bin(message)[2:])):
        final_obj.zfill(len(bin(message)[2:]))
    assert (len(final_obj) == len(bin(message)[2:]))
    return final_obj

