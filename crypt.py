from pyDes import *


yes = ['Y', 'Yes', 'yes', 'YES', 'y']
no = ['No', 'no', 'NO', 'n', 'N']


class DES(object):
    def __init__(self,  file, key):
        self.file = file
        self.key = key
        self.encryption = des(self.key, CBC, "\0\1\0\2\0\3\0\4", padmode=PAD_PKCS5)

    def des_encrypt(self):
        data = open(self.file, "rb")
        new_file = raw_input("Enter a file name for encrypted file: ")
        data2 = open(new_file, "wb")
        enc = self.encryption.encrypt(data.read())
        data2.write(enc)
        data.close()
        data2.close()
        print "Your file %s was encrypted to file named %s" % (self.file, new_file)


class DesDecrypt(object):
    def __init__(self, enc_file, key, dec_file):
        self.enc_file = enc_file
        self.key = key
        self.dec_file = dec_file
        self.decryption = des(self.key, CBC, "\0\1\0\2\0\3\0\4", padmode=PAD_PKCS5)

    def des_decrypt(self):
        enc_data = open(self.enc_file, "rb")
        dec_data = open(self.dec_file,"wb")
        enc_data_read = enc_data.read()
        s = self.decryption.decrypt(enc_data_read)
        dec_data.write(s)
        enc_data.close()
        dec_data.close()

y = raw_input("What do you want to do?\nEncrypt or Decrypt?\n(Enter \'E\' or \'D\') ")
if y == str("E"):
    file = raw_input("Enter a file name to encrypt: ")
    key = raw_input("Enter an 8 bit key (8 digits): ")
    x = DES(str(file), str(key))
    x.des_encrypt()
elif y == str("D"):
    enc_file = raw_input("Enter a file name to decrypt: ")
    dec_file = raw_input("Enter a file name for decrypted file: ")
    dec_key = raw_input("Enter an 8 bit key (8 digits): ")
    s = DesDecrypt(str(enc_file),str(dec_key),str(dec_file))
    s.des_decrypt()
else:
    pass