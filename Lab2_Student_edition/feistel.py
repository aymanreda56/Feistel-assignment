import math

class feistel:
    def __init__ (self, key, f_func, num_rounds):
        self.key = key
        self.f_func = f_func
        self.num_rounds = num_rounds

    
    
        
        
    
    def keyScheduler(self)->list:
        """
        This function reads the key from the class private data member
        it splits this big key into smaller subkeys
        We will assume that this function only splits the key into num_rounds subkeys
        
        hint1: bin(3) returns "0b00000000000000000000000000000011" as a string, you should remove the "0b" at the beginning
        hint2: int("011", 2) returns 3 as an integer 
        hint3: string.zfill(overall_length) fills the string with preceding zeros till it reaches the overall_length
        
        returns a list of those subkeys
        """
        #TODO : convert the key into a binary string
        
        
        #TODO : make a list of subkeys, their number is num_rounds
        #example: if key binary string is "1111000011110000" and num_rounds = 4, then split the key into 4 subkeys and construct the list ["1111", "0000", "1111", "0000"]
        #Dont forget to handle subkeys that are not divisible by the number of rounds. just pad the last remaining key with preceding zeros
        #ex: if the key string is "110011001" and num_rounds = 4, then pad the key with MSB zeros until it is divisible by num_rounds, so the key becomes "0110011001" and the subkeys are ["01", "10", "01", "10", "01"]
        
        
            
        
        # TODO : return this list
        pass
    
    
    
    def round(self, L_block:str, R_block:str, subkey:int) -> list:
        """
        Takes L, R and a subkey (resulting from the key scheduler)
        Applies F_function to R using the subkey --> H (an intermediate result)
        XORs H with L --> R_next
        Puts L_next as R
        
        returns [L_next , R_next] which is a list consisting of 2 bit-blocks
        """
        #TODO: apply the F_function, use the F_function passed to the class during initialization, F_function takes an integer not a string and the subkey
        # outputting intermediate result h
        
        
        
        #TODO: Xor h with L to be out R_next
        # you should convert R_next to a binary string of the same length as previous L and R blocks,
        # Xoring can truncate binary strings if there are zeros in the MSBs
        # Hint: use string.zfill(overall_length) to fill with MSB zeros till we reach overall_length
        
       
       
        #TODO: return the new [L_next, R_next], think of what L_next and R_next should be in a feistel network, make sure to return them in a list
        pass
        
        
        
        
    
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
        
        # TODO : deduce if the message is a binary string or anything else
        # if the message is an integer, then convert it to a binary string, if the message is a string, get the ascii of each letter, convert them to binary then concat the binary strings together to form a long binary string (hint: use ord() to get the unicode of a certain character)
        # if the message is already a binary string, do nothing and proceed to use this binary string
        
        
        
        # TODO pad the message binary string with MSB zeros to make sure it is splitable by half
        
            
        # TODO split the binary string into L_block and R_block
        
        
        # TODO generate list of subkeys using keyScheduler() function
        
        
        # TODO : check if we are decrypting, then reverse the subkey list
        
        
        
        # TODO perform num_rounds of rounds with the corresponding subkeys
        
            
            
            
        # TODO do the final swap, swap the final L_block with R_block
        
        
        # TODO return a concated binary string
        pass