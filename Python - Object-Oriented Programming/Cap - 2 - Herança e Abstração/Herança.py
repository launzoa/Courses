class A:
    def __init__(self):
        self.X = 10
    
    
class B(A):
    def __init__(self):
        super().__init__()
        self.Y = 20


class C(A):
    def __init__(self, Z = 0):
        super().__init__()
        self.Y = 30
        
        
class D(B,C):
    def __init__(self):
        super().__init__()
        
    
    
