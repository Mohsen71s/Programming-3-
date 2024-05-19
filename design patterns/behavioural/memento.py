# this is example for memento design pattern

class Memento:
    def __init__(self,file,content):
        self.file=file
        self.content=content

class X:
    def __init__(self,file):
        self.file=file
        self.content=""
    
    def write(self,text):
        self.content+=text
    
    def save(self):
        return Memento(self.file,self.content)
    
    def undo(self,mem):
        self.file=mem.file
        self.content=mem.content
class Y:
    def save(self,x):
        self.mem=x.save()
    def undo(self,x):
        x.undo(self.mem)
    
    
if __name__=='__main__':
    y=Y()
    
    x=X("x")
    x.write("ayhaga")
    print(x.content)
    y.save(x)
    x.write("Y")
    print(x.content)
    y.undo(x)
    print(x.content)