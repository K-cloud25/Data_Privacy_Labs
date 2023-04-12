import math

class KeyGeneration:

    key = []

    def __init__(self):
        file = open(r"C:\\Users\\keyur\\Lecs\\Lab-AES\\key.txt","r")
        string = bytes(file.readline(),"utf-8")        
        key = []
        print(len(string))
        for i in range(0,4):
            temp_key = [string[4*i],string[4*i+1],string[4*i+2],string[4*i+3]]
            self.key.append(temp_key)

        for i in range(4,44):
            temp = key[i -1]

    def retKeys(self):
        return self.key
    


obj = KeyGeneration()
print(obj.retKeys())