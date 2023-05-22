import numpy as np
from elgamal import ElGamal

if __name__ == '__main__':
    print('1. Encrypt')
    print('2. Decrypt')
    mode = int(input('mode: '))
    key = int(input('key (bilangan prima): '))
    filename = input('nama file yang akan dienkripsi/didekripsi (berada dalam folder test): ')
    filenameoutput = input('nama file output: ')
    if mode == 1:
        # Read file
        f = np.fromfile(f'test/{filename}',dtype=np.uint8)
        listByte = f.tolist()

        # Hardcode elgamal parameter to 16 bit ciphertext
        elgamal = ElGamal(key,32749)

        # Ecnrypt
        ciphertext = []
        for i in range(len(listByte)):
            a,num = elgamal.encrypt(listByte[i])
            if i == 0:
                print(listByte[i],num)
            ciphertext.append(a & 0xFF)
            a >>= 8
            ciphertext.append(a & 0xFF)
            ciphertext.append(num & 0xFF)
            num >>= 8
            ciphertext.append(num & 0xFF)

        # Write file
        byteArr = bytearray(ciphertext)
        newFile = open(f'test/{filenameoutput}','wb')
        newFile.write(byteArr)
        newFile.close()

    elif mode == 2:
        # Read file
        f = np.fromfile(f'test/{filename}',dtype=np.uint8)
        listByte = f.tolist()

        # Hardcode elgamal decrypt parameter
        elgamal = ElGamal(key,32749)

        # Decrypt
        plaintext = []
        for i in range(0,len(listByte),4):
            a = listByte[i] | (listByte[i+1] << 8)
            num = listByte[i+2] | (listByte[i+3] << 8)
            plaintext.append(elgamal.decrypt(a,num))

        try:
            byteArr = bytearray(plaintext)
            newFile = open(f'test/{filenameoutput}','wb')
            newFile.write(byteArr)
            newFile.close()
        except:
            print("Key is not valid")