from collections import defaultdict

def TrieDefaultDict():
    return Trie()

class Trie:
    def __init__(self,defaultValue=0,starters=[]):
        self.items = defaultdict(TrieDefaultDict)
        self.value = defaultValue
        for dict in starters:
            for k,v in dict.items():
                items = k.split(' ')
                self.insert(items,v)
                
    
    def insert(self,items:list[str],value):
        if items==[]:
            self.value=value
        else:
            self.items[items[0]].insert(items[1:],value)
    
    def search(self,items:list[str]):
        if items==[]:
            return self.value
        else:
            return self.items[items[0]].search(items[1:])