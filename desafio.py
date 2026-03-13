from sqlalchemy import create_engine

from sqlalchemy import Column, Integer, String, Boolean

from sqlalchemy.orm import declarative_base

from sqlalchemy.orm import sessionmaker

Base = declarative_base() 

class Aluno(Base):
    __tablename__ = "alunos"

    id = Column(Integer, primary_key=True) 

    nome = Column(String(100)) 

    idade = Column(Integer)

    curso = Column(String(100)) 

    def __init__(self, nome, idade, curso):
        self.nome = nome
        self.idade = idade
        self.curso = curso


    def __repr__(self):
        return f"Produto ( id={self.id} - nome={self.nome} - idade={self.idade} - curso={self.curso})" 
    
engine = create_engine("sqlite:///alunos.db", echo=True) 
Base.metadata.create_all(engine) 
Session = sessionmaker(bind=engine)
session = Session()

aluno1 = Aluno("Alana", 17, "Medicina", True)
aluno2 = Aluno("Lucas", 29, "Informática", True)
aluno3 = Aluno("Luísa", 25, "Corte e costura", True)


session.add(aluno1)
session.add(aluno2)
session.add(aluno3)

session.commit()

    


        







    

