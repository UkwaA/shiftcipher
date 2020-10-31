from string import ascii_uppercase

class Shift:
    alph_num = {a:n for n,a in enumerate(ascii_uppercase)}
    num_alph = {n:a for n,a in enumerate(ascii_uppercase)}
    key = 0
    enc_msg = []
    plaintext = []

    def __init__(self):
        pass

    def encrypt(self, msg, key):
        self.key = key
        msg = msg.upper()
        for letter in msg:
            self.enc_msg.append(
                (self.alph_num[letter]+key)%26
                )

    def bruteforce(self):
        for num in range(1,26):
            temp_list = [(enc+num)%26 for enc in self.enc_msg]
            attempt = [self.num_alph[enc] for enc in temp_list]
            print(attempt)

    def decrypt(self):
        temp_list = [self.num_alph[(enc-self.key)%26] for enc in self.enc_msg]
        print(temp_list)
            
