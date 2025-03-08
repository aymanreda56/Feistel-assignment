import math

class feistel:
    def __init__ (self, key, f_func, num_rounds):
        self.key = key
        self.f_func = f_func
        self.num_rounds = num_rounds

    
    def round(self, L_block, R_block, subkey) -> list:
        """
        Takes L, R and a subkey (resulting from the key scheduler)
        Applies F_function to R using the subkey --> H (an intermediate result)
        XORs H with L --> R_next
        Puts L_next as R
        
        returns [L_next , R_next] which is a list consisting of 2 bit-blocks
        """
        #TODO 1: apply the F_function, use the F_function passed to the class during initialization, F_function takes an integer not a string and the subkey
        # outputting intermediate result h
        h = self.f_func(int(R_block, 2), subkey)
        
        
        #TODO 2: Xor h with L to be out R_next
        # you should convert R_next to a binary string of the same length as previous L and R blocks,
        # Xoring can truncate binary strings if there are zeros in the MSBs
        # Hint: use string.zfill(overall_length) to fill with MSB zeros till we reach overall_length
        R_next = int(h,2) ^ int(L_block, 2)                #bitwise Xor in python is written with ^
        R_next = bin(R_next)[2:].zfill(len(L_block))       #converting R_next to a binary string and padding with preceding zeros
       
       
        #TODO 3: return [R_block, R_next] as the new [L, R], make sure to return them in a list
        return [R_block, R_next]
        
        
    
    def keyScheduler(self)->list:
        """
        This function reads the key from the class private data member
        it splits this big key into smaller subkeys
        We will assume that this function only splits the key into num_rounds subkeys
        
        hint1: bin(3) returns "0b00000000000000000000000000000011" as a string, you should remove the "0b" at the beginning
        hint2: int("011", 2) returns 3 as an integer 
        
        returns a list of those subkeys
        """
        #TODO : convert the key into a binary string
        key_string = bin(self.key)[2:]
        
        #TODO : make a list of subkeys, their number is num_rounds
        #example: if key binary string is "1111000011110000" and num_rounds = 4, then split the key into 4 subkeys and construct the list ["1111", "0000", "1111", "0000"]
        subkeys_list = []
        subkey_size = len(key_string) / self.num_rounds
        while(subkey_size - math.floor(subkey_size) != 0.0):
            key_string = '0' + key_string
            subkey_size = len(key_string) / self.num_rounds

        subkey_size = int(subkey_size)
        for i in range(self.num_rounds):
            subkey= key_string[i*subkey_size: (i+1)*subkey_size]
            subkey = int(subkey, 2)
            subkeys_list.append(subkey)
            
        
        # TODO : return this list
        return subkeys_list
        
        
        
        
    
    def feistel_network(self, message, encrypt_flag:bool):
        """
        First try to deduce if the message is a binary string or a normal message
        This function does the following:
        1) Pads the input message block with preceding 0s to ensure it is splitable by half
        2) Splits the block into L_block and R_block where L_block is the most significant half, and the R_block is the least significant half
        3) generates subkeys using the keySchedule() function
        3.1) if the encrypt_flag is 0 meaning we want to decrypt, then reverse the subkeys list
        4) Does num_rounds of rounds using the corresponding subkey
            if num_rounds == 16, then keySchedule() will return 16 subkeys
            and do 16 rounds with each i-th round using the i-th subkey
        5) Do a final swap, swap L_block with R_block
        6) Concat both blocks and return a binary string
        """
        assert(message)
        
        # TODO : deduce if the message is a binary string or an integer
        # if the message is an integer, then convert it to a binary string
        # if the message is already a binary string, do nothing
        if type(message) == str and all(c in '01' for c in message):
            binary_msg = message
        else:
            binary_msg = bin(message)[2:]
        
        
        # TODO pad the message binary string with MSB zeros to make sure it is splitable by half
        mid = len(binary_msg) // 2
        while(mid % 2 != 0):
            binary_msg = '0' + binary_msg
            mid = len(binary_msg) // 2
            
        # TODO split the binary string into L_block and R_block
        L_block, R_block = binary_msg[:mid], binary_msg[mid:]
        
        # TODO generate list of subkeys using keyScheduler() function
        subkeys = self.keyScheduler()
        
        # TODO : check if we are decrypting, then reverse the subkey list
        if(not encrypt_flag): subkeys.reverse()
        
        
        # TODO perform num_rounds of rounds with the corresponding subkeys
        for round_idx in range (self.num_rounds):
            subkey = subkeys[round_idx]
            L_block, R_block = self.round(L_block=L_block, R_block=R_block, subkey=subkey)
            
            
            
        # TODO do the final swap, swap the final L_block with R_block
        L_block, R_block = R_block, L_block         #final swapping
        
        # TODO return a concated binary string
        return L_block + R_block