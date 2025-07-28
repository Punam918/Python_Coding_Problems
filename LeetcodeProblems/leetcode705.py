''' Design Hashsets'''
#Brute Force
class MyHashSet:
    def __init__(self):
        self.data = []

    def add(self,key:int) -> None:
        if key not in self.data:
            self.data.append(key)

    def remove(self,key:int) -> None:
        if key in self.data:
            self.data.remove(key)
    def contains(self,key:int)->bool:
        return key in self.data
    
''' TC = o(n) for each function call and SC = o(n)'''

''' Boolean Array'''
class MyHastSet:
    def __init__(self):
        self.data = [False]*10000001
    
    def add(self,key:int) -> None:
        self.data[key] = True 

    def remove(self,key:int) -> None:
        self.data[key] = False 
    
    def contains(self,key:int) ->bool:
        return self.data[key]
'''Tc = o(1) for each function call and SC = o(1000000)''' 