import math

class KeyGeneration:

    key = []

    def __init__(self):
        file = open(r"C:\\Users\\keyur\\Lecs\\Lab-AES\\key.txt","r")
        string = bytes(file.readline(),"utf-8")        
        key = []

        for i in range(0,4):
            temp_key = [string[4*(i)],string[4*(i+1)],string[4*(i+2)],string[4*(i+3)]]
            self.key.append(temp_key)

    def retKeys(self):
        return self.key
    


obj = KeyGeneration()
print(obj.retKeys())

pt = "Thats my Kung Fu".encode('utf-8')
sarray = []

for i in range(0,len(pt)):
               sarray.append(pt[i:i+1].hex())
print(sarray)


