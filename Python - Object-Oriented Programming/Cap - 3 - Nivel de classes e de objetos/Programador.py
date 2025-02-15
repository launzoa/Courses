from datetime import datetime

class Developer:
    Limit = 3

    def __init__(self, name, date_age):
        self.name = name
        self.date_age = date_age
        self.skills = []
        self.age = 0
        
    def __str__(self):
        return f"Nome: {self.name}, Ano de nascimento: {self.date_age}"
    
    @classmethod
    def change_limit(cls, new_limit):
        cls.Limit = new_limit
        
    @staticmethod
    def year_now():
         year = datetime.today().year
         return year
    
    def age_in_years(self):
        self.age = Developer.year_now() - self.date_age #É apenas uma simples representação. Para uma abordagem mais séria, seria utilizado o dia e mês de nascimento...
        return self.age
    
    def developer_skills(self, skill):
        if(len(self.skills) < Developer.Limit):
            self.skills.append(skill)
        else:
            print("Limite de skills atingido. Impossível adicionar a linguagem " + skill + ". Aumente o limite!")
        
    def show_skills(self):
        print("As suas skills são:")
        for skill in self.skills:
            print(skill)

 
 