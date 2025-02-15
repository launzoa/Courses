class SampleClass:
    
    X = 0 #Para a classe temos três possíveis chamadas para X global.
    
    def __init__(self):
        self.Y = 10
    
    def __str__(self):
        return f"X: {self.__class__.X}, Y: {self.Y}" 
    
    def change_values(self, x, y):
        self.__class__.X = x #Chamando o método de class, self.__class__.X Permite acessar atributos de classe a partir de métodos de instância.
        self.Y = y
        return (x, y)
    @classmethod
    def change_x(cls, new_x):
        cls.X = new_x #Utilizando o cls, que é como a instrução self, porém, para métodos da classe. cls.Y não funcionaria, por exemplo, afinal, ele é uma instância. Mais flexível e orientado a objetos
        return cls.X
        
    @staticmethod
    def show(y):
        print(f"X: {SampleClass.X}, Y: {y}") #Último exemplo, uma outra forma de chamar é pelo próprio nome da classe. Não é tão flexível. Se o nome da classe mudar, você precisará atualizar todas as referências a SampleClass.X.
        
