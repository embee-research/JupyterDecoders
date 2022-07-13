#Decoder for the AES-style Jupyter persistence mechanism. 

import os,sys,base64,argparse
from Crypto.Cipher import AES


parser = argparse.ArgumentParser()
parser.add_argument("--file", type=str,required=False)
parser.add_argument("--key",type=str,required=False)
parser.add_argument('--save', type=str, required=False, default="jupyter.bin")
args = parser.parse_args()

#Exit if no arguments are present
if not (args.file or args.key):
    print("Please enter a key and a file, using --file <filename> --key <b64key>")
    sys.exit(1)

#Read files
f = open(args.file)
data = f.read()
f.close()

#Assumes input data is base64 encoded
key = base64.b64decode(args.key)
s1 = base64.b64decode(data)

#Takes first 16 bytes of decoded input as the AES IV
IV = s1[0:16]
enc = s1[16:]

#Use AES library to decrypt the data using provided key
cipher = AES.new(key, AES.MODE_CBC, iv=IV)
plain = cipher.decrypt(enc)

#Save results to a file
print(plain[0:10])
print("Saving {} bytes to file {}: ".format(len(plain),str(args.save)))
f = open(args.save, "wb")
f.write(plain)
f.close()


