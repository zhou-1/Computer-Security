import random
import _json

def freq_count(nameIn1, nameOut1):
    freq = {}
    toDecode1 = bytearray()
    with open(nameIn1, "rb") as inFile1, open(nameOut1, "w") as outFile:
        for length in range(2,150,1):
            freq.clear()
            for line1 in inFile1:
                for x1 in line1:
                    toDecode1.append(x1)
            for i in range(length,len(toDecode1),1):
                if toDecode1[i] == toDecode1[i-length]:
                    #freq[chr(toDecode1[i])] += 1
                    if freq.get(chr(toDecode1[i])):
                        freq[chr(toDecode1[i])] += 1
                    else:
                        freq[chr(toDecode1[i])] = 1
            print(freq)
            maxOcc = 0
            for m, n in freq.items():
                #print(n)
                if maxOcc < n:
                    maxOcc = n
            outFile.write(str(length) + ':' + str(maxOcc) + '\n')
        inFile1.close()
        outFile.close()

freq_count("challenge4.txt","4_output.txt")

password = "Boulderdash"

def decipher(nameIn, nameOut):
    toDecode = bytearray()
    result = bytearray()
    with open(nameIn, "rb") as inFile, open(nameOut, "wb") as outFile:
        for line in inFile:
            for x in line:
                toDecode.append(x)
                #print(x)
        for i in range(len(toDecode)):
            result.append(toDecode[i] ^ ord(password[i%len(password)]))
            print(result[i])
        outFile.write(result)

#decipher("challenge1.txt","1_output.txt")