# Instalar o sqlalchemy
# pip install sqlalchemy

# Importar a biblioteca responsável por criar a conexão com banco
from sqlalchemy import create_engine

# Importa os tipos de dados das colunas do banco
from sqlalchemy import Column, Integer, String, Float, Boolean

# Importa a classe base usada para criar os modelos orm
from sqlalchemy.orm import declarative_base

# Importa a ferramenta para criar sessões no banco
from sqlalchemy.orm import sessionmaker


# Criar a classe base do orm
Base = declarative_base() 

# Classe = Tabela no banco
# Atributo = Coluna
# Objeto = Linha da tabela


# Classe Produto representando a tabela do banco
class Produto(Base):
    #nome da tabela
    __tablename__ = "produtos"

    # criar coluna
    id = Column(Integer, primary_key=True) 

    # coluna do nome
    nome = Column(String(100)) 

    # coluna de preço
    preco = Column(Float) 

    estoque = Column(Integer)

    ativo = Column(Boolean)

    # método construtor
    def __init__(self, nome, preco, estoque, ativo):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque
        self.ativo = ativo

    # Função para exibir os valores
    def __repr__(self):
        return f"Produto ( id={self.id} - nome={self.nome} - preco={self.preco} - estoque={self.estoque} -ativo={self.ativo})" 
    
#Criar a conexão
# log do banco de daods para ativar = echo=True
engine = create_engine("sqlite:///estoque.db", echo=True) 

#Criar as tabelas - se ainda não existirem
Base.metadata.create_all(engine) 


#Criar uma fábrica de sessões
Session = sessionmaker(bind=engine)

#Criar um carrinho (sessão ativa no banco)
session = Session()


#CRIAR - Cadastrar
#Como criar um objeto
produto4 = Produto("Celular", 1500, 70, True)


session.add(produto4)

#Salvar no banco
session.commit()

# Buscar produtos - listar
produtos = session.query(Produto).all()

for produto in produtos:
    print(produto)







                      




