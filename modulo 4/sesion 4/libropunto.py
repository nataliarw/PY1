class Libro: 
    
    def __init__(self, autor, titulo):
        self.autor = autor 
        self.titulo = titulo 
    def __init__(self, autor=None, titulo=None, publicado=None): 
        self.autor = autor 
        self.titulo = titulo 
        self.publicado = publicado 
       
        
    
libro_1 = Libro('Dan Brown','Infierno') 
libro_2 = Libro('Dan Brown', 'El Codigo Da Vinci', '2003') 
print(libro_1.__dict__) 

print('================================') 
print(libro_2.__dict__) 

print('================================') 











