from collections import defaultdict

def TrieDefaultDict():
    return Trie()

class Trie:
    def __init__(self,starter={}):
        self.items = defaultdict(TrieDefaultDict)
        self.value = None
        for k,v in starter.items():
            items = k.split(' ')
            self.insert(items,v)
    
    def insert(self,items:list[str],value):
        if items==[]:
            self.value=value
        else:
            self.items[items[0]].insert(items[1:],value)
    
    def search(self,items:list[str]):
        if items==[] or items[0] not in self.items:
            return (0, self.value)
        else:
            (consumed, ans) = self.items[items[0]].search(items[1:])
            
            if ans == None:
                return (0, self.value)
            else:
                return (consumed + 1, ans)